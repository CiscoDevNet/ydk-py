""" CISCO_FTP_CLIENT_MIB 

The MIB module for invoking Internet File Transfer Protocol
(FTP) operations for network management purposes.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoFtpClientMib(Entity):
    """
    
    
    .. attribute:: cfcrequest
    
    	
    	**type**\:   :py:class:`Cfcrequest <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequest>`
    
    .. attribute:: cfcrequesttable
    
    	A table of FTP client requests
    	**type**\:   :py:class:`Cfcrequesttable <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable>`
    
    

    """

    _prefix = 'CISCO-FTP-CLIENT-MIB'
    _revision = '2006-03-31'

    def __init__(self):
        super(CiscoFtpClientMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-FTP-CLIENT-MIB"
        self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"

        self.cfcrequest = CiscoFtpClientMib.Cfcrequest()
        self.cfcrequest.parent = self
        self._children_name_map["cfcrequest"] = "cfcRequest"
        self._children_yang_names.add("cfcRequest")

        self.cfcrequesttable = CiscoFtpClientMib.Cfcrequesttable()
        self.cfcrequesttable.parent = self
        self._children_name_map["cfcrequesttable"] = "cfcRequestTable"
        self._children_yang_names.add("cfcRequestTable")


    class Cfcrequest(Entity):
        """
        
        
        .. attribute:: cfcrequestmaximum
        
        	The maximum number of requests this system can hold in cfcRequestTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  When an attempt is made to create a new entry but the table is full, the oldest completed entry is bumped out and cfcRequestsBumped is incremented.  Changing this number does not disturb existing requests that are not completed and bumps completed requests as necessary
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequests
        
        	The current number of requests in cfcRequestTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestsbumped
        
        	The number of requests in cfcRequestTable that were bumped out to make room for a new request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestshigh
        
        	The highest number of requests in cfcRequestTable since this system was last initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CiscoFtpClientMib.Cfcrequest, self).__init__()

            self.yang_name = "cfcRequest"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"

            self.cfcrequestmaximum = YLeaf(YType.uint32, "cfcRequestMaximum")

            self.cfcrequests = YLeaf(YType.uint32, "cfcRequests")

            self.cfcrequestsbumped = YLeaf(YType.uint32, "cfcRequestsBumped")

            self.cfcrequestshigh = YLeaf(YType.uint32, "cfcRequestsHigh")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cfcrequestmaximum",
                            "cfcrequests",
                            "cfcrequestsbumped",
                            "cfcrequestshigh") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoFtpClientMib.Cfcrequest, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFtpClientMib.Cfcrequest, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cfcrequestmaximum.is_set or
                self.cfcrequests.is_set or
                self.cfcrequestsbumped.is_set or
                self.cfcrequestshigh.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cfcrequestmaximum.yfilter != YFilter.not_set or
                self.cfcrequests.yfilter != YFilter.not_set or
                self.cfcrequestsbumped.yfilter != YFilter.not_set or
                self.cfcrequestshigh.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cfcRequest" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cfcrequestmaximum.is_set or self.cfcrequestmaximum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cfcrequestmaximum.get_name_leafdata())
            if (self.cfcrequests.is_set or self.cfcrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cfcrequests.get_name_leafdata())
            if (self.cfcrequestsbumped.is_set or self.cfcrequestsbumped.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cfcrequestsbumped.get_name_leafdata())
            if (self.cfcrequestshigh.is_set or self.cfcrequestshigh.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cfcrequestshigh.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cfcRequestMaximum" or name == "cfcRequests" or name == "cfcRequestsBumped" or name == "cfcRequestsHigh"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cfcRequestMaximum"):
                self.cfcrequestmaximum = value
                self.cfcrequestmaximum.value_namespace = name_space
                self.cfcrequestmaximum.value_namespace_prefix = name_space_prefix
            if(value_path == "cfcRequests"):
                self.cfcrequests = value
                self.cfcrequests.value_namespace = name_space
                self.cfcrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "cfcRequestsBumped"):
                self.cfcrequestsbumped = value
                self.cfcrequestsbumped.value_namespace = name_space
                self.cfcrequestsbumped.value_namespace_prefix = name_space_prefix
            if(value_path == "cfcRequestsHigh"):
                self.cfcrequestshigh = value
                self.cfcrequestshigh.value_namespace = name_space
                self.cfcrequestshigh.value_namespace_prefix = name_space_prefix


    class Cfcrequesttable(Entity):
        """
        A table of FTP client requests.
        
        .. attribute:: cfcrequestentry
        
        	Information about an FTP client request.  Management applications use cfcRequestEntryStatus to control entry modification, creation, and deletion.  Setting cfcRequestEntryStatus to 'active' from any state including 'active' causes the operation to be started.  The entry may be modified only when cfcRequestOperationState is 'stopped'.  The value of cfcRequestEntryStatus may be set to 'destroy' at any time.  Doing so will abort a running request.  Entries may not be created without explicitly setting cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'
        	**type**\: list of    :py:class:`Cfcrequestentry <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry>`
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CiscoFtpClientMib.Cfcrequesttable, self).__init__()

            self.yang_name = "cfcRequestTable"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"

            self.cfcrequestentry = YList(self)

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
                        super(CiscoFtpClientMib.Cfcrequesttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFtpClientMib.Cfcrequesttable, self).__setattr__(name, value)


        class Cfcrequestentry(Entity):
            """
            Information about an FTP client request.  Management applications
            use cfcRequestEntryStatus to control entry modification, creation,
            and deletion.
            
            Setting cfcRequestEntryStatus to 'active' from any state including
            'active' causes the operation to be started.
            
            The entry may be modified only when cfcRequestOperationState is
            'stopped'.
            
            The value of cfcRequestEntryStatus may be set to 'destroy' at any
            time.  Doing so will abort a running request.
            
            Entries may not be created without explicitly setting
            cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'.
            
            .. attribute:: cfcrequestindex  <key>
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cfcrequestcompletiontime
            
            	The value of sysUpTime when the operation completed.  For an incomplete operation this value is zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfcrequestentrystatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cfcRequestEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cfcrequestlocalfile
            
            	The local file on which the operation is to be performed
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cfcrequestoperation
            
            	The FTP operation to be performed
            	**type**\:   :py:class:`Cfcrequestoperation <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.Cfcrequestoperation>`
            
            .. attribute:: cfcrequestoperationstate
            
            	The operational state of the file transfer.  To short\-terminate the transfer set cfcRequestStop to 'stop'
            	**type**\:   :py:class:`Cfcrequestoperationstate <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.Cfcrequestoperationstate>`
            
            .. attribute:: cfcrequestpassword
            
            	The password to use at the FTP server.  When read this object always returns a zero\-length string
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: cfcrequestremotefile
            
            	The remote file on which the operation is to be performed
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cfcrequestresult
            
            	The result of the FTP operation
            	**type**\:   :py:class:`Cfcrequestresult <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.Cfcrequestresult>`
            
            .. attribute:: cfcrequestserver
            
            	The domain name or IP address of the FTP server to use
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cfcrequeststop
            
            	The action control to stop a running request.  Setting this to 'stop' will begin the process of stopping the request.  Setting it to 'ready' or setting it to 'stop' more than once have no effect.  When read this object always returns ready
            	**type**\:   :py:class:`Cfcrequeststop <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.Cfcrequeststop>`
            
            .. attribute:: cfcrequestuser
            
            	The user name to use at the FTP server
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'CISCO-FTP-CLIENT-MIB'
            _revision = '2006-03-31'

            def __init__(self):
                super(CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry, self).__init__()

                self.yang_name = "cfcRequestEntry"
                self.yang_parent_name = "cfcRequestTable"

                self.cfcrequestindex = YLeaf(YType.uint32, "cfcRequestIndex")

                self.cfcrequestcompletiontime = YLeaf(YType.uint32, "cfcRequestCompletionTime")

                self.cfcrequestentrystatus = YLeaf(YType.enumeration, "cfcRequestEntryStatus")

                self.cfcrequestlocalfile = YLeaf(YType.str, "cfcRequestLocalFile")

                self.cfcrequestoperation = YLeaf(YType.enumeration, "cfcRequestOperation")

                self.cfcrequestoperationstate = YLeaf(YType.enumeration, "cfcRequestOperationState")

                self.cfcrequestpassword = YLeaf(YType.str, "cfcRequestPassword")

                self.cfcrequestremotefile = YLeaf(YType.str, "cfcRequestRemoteFile")

                self.cfcrequestresult = YLeaf(YType.enumeration, "cfcRequestResult")

                self.cfcrequestserver = YLeaf(YType.str, "cfcRequestServer")

                self.cfcrequeststop = YLeaf(YType.enumeration, "cfcRequestStop")

                self.cfcrequestuser = YLeaf(YType.str, "cfcRequestUser")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cfcrequestindex",
                                "cfcrequestcompletiontime",
                                "cfcrequestentrystatus",
                                "cfcrequestlocalfile",
                                "cfcrequestoperation",
                                "cfcrequestoperationstate",
                                "cfcrequestpassword",
                                "cfcrequestremotefile",
                                "cfcrequestresult",
                                "cfcrequestserver",
                                "cfcrequeststop",
                                "cfcrequestuser") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry, self).__setattr__(name, value)

            class Cfcrequestoperation(Enum):
                """
                Cfcrequestoperation

                The FTP operation to be performed.

                .. data:: putBinary = 1

                .. data:: putASCII = 2

                """

                putBinary = Enum.YLeaf(1, "putBinary")

                putASCII = Enum.YLeaf(2, "putASCII")


            class Cfcrequestoperationstate(Enum):
                """
                Cfcrequestoperationstate

                The operational state of the file transfer.  To short\-terminate

                the transfer set cfcRequestStop to 'stop'.

                .. data:: running = 1

                .. data:: stopping = 2

                .. data:: stopped = 3

                """

                running = Enum.YLeaf(1, "running")

                stopping = Enum.YLeaf(2, "stopping")

                stopped = Enum.YLeaf(3, "stopped")


            class Cfcrequestresult(Enum):
                """
                Cfcrequestresult

                The result of the FTP operation.

                .. data:: pending = 1

                .. data:: success = 2

                .. data:: aborted = 3

                .. data:: fileOpenFailLocal = 4

                .. data:: fileOpenFailRemote = 5

                .. data:: badDomainName = 6

                .. data:: unreachableIpAddress = 7

                .. data:: linkFailed = 8

                .. data:: fileReadFailed = 9

                .. data:: fileWriteFailed = 10

                """

                pending = Enum.YLeaf(1, "pending")

                success = Enum.YLeaf(2, "success")

                aborted = Enum.YLeaf(3, "aborted")

                fileOpenFailLocal = Enum.YLeaf(4, "fileOpenFailLocal")

                fileOpenFailRemote = Enum.YLeaf(5, "fileOpenFailRemote")

                badDomainName = Enum.YLeaf(6, "badDomainName")

                unreachableIpAddress = Enum.YLeaf(7, "unreachableIpAddress")

                linkFailed = Enum.YLeaf(8, "linkFailed")

                fileReadFailed = Enum.YLeaf(9, "fileReadFailed")

                fileWriteFailed = Enum.YLeaf(10, "fileWriteFailed")


            class Cfcrequeststop(Enum):
                """
                Cfcrequeststop

                The action control to stop a running request.  Setting this to

                'stop' will begin the process of stopping the request.  Setting

                it to 'ready' or setting it to 'stop' more than once have no

                effect.  When read this object always returns ready.

                .. data:: ready = 1

                .. data:: stop = 2

                """

                ready = Enum.YLeaf(1, "ready")

                stop = Enum.YLeaf(2, "stop")


            def has_data(self):
                return (
                    self.cfcrequestindex.is_set or
                    self.cfcrequestcompletiontime.is_set or
                    self.cfcrequestentrystatus.is_set or
                    self.cfcrequestlocalfile.is_set or
                    self.cfcrequestoperation.is_set or
                    self.cfcrequestoperationstate.is_set or
                    self.cfcrequestpassword.is_set or
                    self.cfcrequestremotefile.is_set or
                    self.cfcrequestresult.is_set or
                    self.cfcrequestserver.is_set or
                    self.cfcrequeststop.is_set or
                    self.cfcrequestuser.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cfcrequestindex.yfilter != YFilter.not_set or
                    self.cfcrequestcompletiontime.yfilter != YFilter.not_set or
                    self.cfcrequestentrystatus.yfilter != YFilter.not_set or
                    self.cfcrequestlocalfile.yfilter != YFilter.not_set or
                    self.cfcrequestoperation.yfilter != YFilter.not_set or
                    self.cfcrequestoperationstate.yfilter != YFilter.not_set or
                    self.cfcrequestpassword.yfilter != YFilter.not_set or
                    self.cfcrequestremotefile.yfilter != YFilter.not_set or
                    self.cfcrequestresult.yfilter != YFilter.not_set or
                    self.cfcrequestserver.yfilter != YFilter.not_set or
                    self.cfcrequeststop.yfilter != YFilter.not_set or
                    self.cfcrequestuser.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cfcRequestEntry" + "[cfcRequestIndex='" + self.cfcrequestindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/cfcRequestTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cfcrequestindex.is_set or self.cfcrequestindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestindex.get_name_leafdata())
                if (self.cfcrequestcompletiontime.is_set or self.cfcrequestcompletiontime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestcompletiontime.get_name_leafdata())
                if (self.cfcrequestentrystatus.is_set or self.cfcrequestentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestentrystatus.get_name_leafdata())
                if (self.cfcrequestlocalfile.is_set or self.cfcrequestlocalfile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestlocalfile.get_name_leafdata())
                if (self.cfcrequestoperation.is_set or self.cfcrequestoperation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestoperation.get_name_leafdata())
                if (self.cfcrequestoperationstate.is_set or self.cfcrequestoperationstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestoperationstate.get_name_leafdata())
                if (self.cfcrequestpassword.is_set or self.cfcrequestpassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestpassword.get_name_leafdata())
                if (self.cfcrequestremotefile.is_set or self.cfcrequestremotefile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestremotefile.get_name_leafdata())
                if (self.cfcrequestresult.is_set or self.cfcrequestresult.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestresult.get_name_leafdata())
                if (self.cfcrequestserver.is_set or self.cfcrequestserver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestserver.get_name_leafdata())
                if (self.cfcrequeststop.is_set or self.cfcrequeststop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequeststop.get_name_leafdata())
                if (self.cfcrequestuser.is_set or self.cfcrequestuser.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cfcrequestuser.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cfcRequestIndex" or name == "cfcRequestCompletionTime" or name == "cfcRequestEntryStatus" or name == "cfcRequestLocalFile" or name == "cfcRequestOperation" or name == "cfcRequestOperationState" or name == "cfcRequestPassword" or name == "cfcRequestRemoteFile" or name == "cfcRequestResult" or name == "cfcRequestServer" or name == "cfcRequestStop" or name == "cfcRequestUser"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cfcRequestIndex"):
                    self.cfcrequestindex = value
                    self.cfcrequestindex.value_namespace = name_space
                    self.cfcrequestindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestCompletionTime"):
                    self.cfcrequestcompletiontime = value
                    self.cfcrequestcompletiontime.value_namespace = name_space
                    self.cfcrequestcompletiontime.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestEntryStatus"):
                    self.cfcrequestentrystatus = value
                    self.cfcrequestentrystatus.value_namespace = name_space
                    self.cfcrequestentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestLocalFile"):
                    self.cfcrequestlocalfile = value
                    self.cfcrequestlocalfile.value_namespace = name_space
                    self.cfcrequestlocalfile.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestOperation"):
                    self.cfcrequestoperation = value
                    self.cfcrequestoperation.value_namespace = name_space
                    self.cfcrequestoperation.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestOperationState"):
                    self.cfcrequestoperationstate = value
                    self.cfcrequestoperationstate.value_namespace = name_space
                    self.cfcrequestoperationstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestPassword"):
                    self.cfcrequestpassword = value
                    self.cfcrequestpassword.value_namespace = name_space
                    self.cfcrequestpassword.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestRemoteFile"):
                    self.cfcrequestremotefile = value
                    self.cfcrequestremotefile.value_namespace = name_space
                    self.cfcrequestremotefile.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestResult"):
                    self.cfcrequestresult = value
                    self.cfcrequestresult.value_namespace = name_space
                    self.cfcrequestresult.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestServer"):
                    self.cfcrequestserver = value
                    self.cfcrequestserver.value_namespace = name_space
                    self.cfcrequestserver.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestStop"):
                    self.cfcrequeststop = value
                    self.cfcrequeststop.value_namespace = name_space
                    self.cfcrequeststop.value_namespace_prefix = name_space_prefix
                if(value_path == "cfcRequestUser"):
                    self.cfcrequestuser = value
                    self.cfcrequestuser.value_namespace = name_space
                    self.cfcrequestuser.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cfcrequestentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cfcrequestentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cfcRequestTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cfcRequestEntry"):
                for c in self.cfcrequestentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cfcrequestentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cfcRequestEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cfcrequest is not None and self.cfcrequest.has_data()) or
            (self.cfcrequesttable is not None and self.cfcrequesttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cfcrequest is not None and self.cfcrequest.has_operation()) or
            (self.cfcrequesttable is not None and self.cfcrequesttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB" + path_buffer

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

        if (child_yang_name == "cfcRequest"):
            if (self.cfcrequest is None):
                self.cfcrequest = CiscoFtpClientMib.Cfcrequest()
                self.cfcrequest.parent = self
                self._children_name_map["cfcrequest"] = "cfcRequest"
            return self.cfcrequest

        if (child_yang_name == "cfcRequestTable"):
            if (self.cfcrequesttable is None):
                self.cfcrequesttable = CiscoFtpClientMib.Cfcrequesttable()
                self.cfcrequesttable.parent = self
                self._children_name_map["cfcrequesttable"] = "cfcRequestTable"
            return self.cfcrequesttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cfcRequest" or name == "cfcRequestTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoFtpClientMib()
        return self._top_entity

