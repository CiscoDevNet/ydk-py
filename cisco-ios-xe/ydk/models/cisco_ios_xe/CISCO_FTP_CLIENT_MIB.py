""" CISCO_FTP_CLIENT_MIB 

The MIB module for invoking Internet File Transfer Protocol
(FTP) operations for network management purposes.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOFTPCLIENTMIB(Entity):
    """
    
    
    .. attribute:: cfcrequest
    
    	
    	**type**\:  :py:class:`CfcRequest <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequest>`
    
    	**config**\: False
    
    .. attribute:: cfcrequesttable
    
    	A table of FTP client requests
    	**type**\:  :py:class:`CfcRequestTable <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-FTP-CLIENT-MIB'
    _revision = '2006-03-31'

    def __init__(self):
        super(CISCOFTPCLIENTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-FTP-CLIENT-MIB"
        self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cfcRequest", ("cfcrequest", CISCOFTPCLIENTMIB.CfcRequest)), ("cfcRequestTable", ("cfcrequesttable", CISCOFTPCLIENTMIB.CfcRequestTable))])
        self._leafs = OrderedDict()

        self.cfcrequest = CISCOFTPCLIENTMIB.CfcRequest()
        self.cfcrequest.parent = self
        self._children_name_map["cfcrequest"] = "cfcRequest"

        self.cfcrequesttable = CISCOFTPCLIENTMIB.CfcRequestTable()
        self.cfcrequesttable.parent = self
        self._children_name_map["cfcrequesttable"] = "cfcRequestTable"
        self._segment_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOFTPCLIENTMIB, [], name, value)


    class CfcRequest(Entity):
        """
        
        
        .. attribute:: cfcrequestmaximum
        
        	The maximum number of requests this system can hold in cfcRequestTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  When an attempt is made to create a new entry but the table is full, the oldest completed entry is bumped out and cfcRequestsBumped is incremented.  Changing this number does not disturb existing requests that are not completed and bumps completed requests as necessary
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cfcrequests
        
        	The current number of requests in cfcRequestTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cfcrequestshigh
        
        	The highest number of requests in cfcRequestTable since this system was last initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cfcrequestsbumped
        
        	The number of requests in cfcRequestTable that were bumped out to make room for a new request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CISCOFTPCLIENTMIB.CfcRequest, self).__init__()

            self.yang_name = "cfcRequest"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cfcrequestmaximum', (YLeaf(YType.uint32, 'cfcRequestMaximum'), ['int'])),
                ('cfcrequests', (YLeaf(YType.uint32, 'cfcRequests'), ['int'])),
                ('cfcrequestshigh', (YLeaf(YType.uint32, 'cfcRequestsHigh'), ['int'])),
                ('cfcrequestsbumped', (YLeaf(YType.uint32, 'cfcRequestsBumped'), ['int'])),
            ])
            self.cfcrequestmaximum = None
            self.cfcrequests = None
            self.cfcrequestshigh = None
            self.cfcrequestsbumped = None
            self._segment_path = lambda: "cfcRequest"
            self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFTPCLIENTMIB.CfcRequest, ['cfcrequestmaximum', 'cfcrequests', 'cfcrequestshigh', 'cfcrequestsbumped'], name, value)



    class CfcRequestTable(Entity):
        """
        A table of FTP client requests.
        
        .. attribute:: cfcrequestentry
        
        	Information about an FTP client request.  Management applications use cfcRequestEntryStatus to control entry modification, creation, and deletion.  Setting cfcRequestEntryStatus to 'active' from any state including 'active' causes the operation to be started.  The entry may be modified only when cfcRequestOperationState is 'stopped'.  The value of cfcRequestEntryStatus may be set to 'destroy' at any time.  Doing so will abort a running request.  Entries may not be created without explicitly setting cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'
        	**type**\: list of  		 :py:class:`CfcRequestEntry <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            super(CISCOFTPCLIENTMIB.CfcRequestTable, self).__init__()

            self.yang_name = "cfcRequestTable"
            self.yang_parent_name = "CISCO-FTP-CLIENT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cfcRequestEntry", ("cfcrequestentry", CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry))])
            self._leafs = OrderedDict()

            self.cfcrequestentry = YList(self)
            self._segment_path = lambda: "cfcRequestTable"
            self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFTPCLIENTMIB.CfcRequestTable, [], name, value)


        class CfcRequestEntry(Entity):
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
            
            .. attribute:: cfcrequestindex  (key)
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cfcrequestoperation
            
            	The FTP operation to be performed
            	**type**\:  :py:class:`CfcRequestOperation <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperation>`
            
            	**config**\: False
            
            .. attribute:: cfcrequestlocalfile
            
            	The local file on which the operation is to be performed
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cfcrequestremotefile
            
            	The remote file on which the operation is to be performed
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cfcrequestserver
            
            	The domain name or IP address of the FTP server to use
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cfcrequestuser
            
            	The user name to use at the FTP server
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: cfcrequestpassword
            
            	The password to use at the FTP server.  When read this object always returns a zero\-length string
            	**type**\: str
            
            	**length:** 0..16
            
            	**config**\: False
            
            .. attribute:: cfcrequestresult
            
            	The result of the FTP operation
            	**type**\:  :py:class:`CfcRequestResult <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestResult>`
            
            	**config**\: False
            
            .. attribute:: cfcrequestcompletiontime
            
            	The value of sysUpTime when the operation completed.  For an incomplete operation this value is zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cfcrequeststop
            
            	The action control to stop a running request.  Setting this to 'stop' will begin the process of stopping the request.  Setting it to 'ready' or setting it to 'stop' more than once have no effect.  When read this object always returns ready
            	**type**\:  :py:class:`CfcRequestStop <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestStop>`
            
            	**config**\: False
            
            .. attribute:: cfcrequestoperationstate
            
            	The operational state of the file transfer.  To short\-terminate the transfer set cfcRequestStop to 'stop'
            	**type**\:  :py:class:`CfcRequestOperationState <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperationState>`
            
            	**config**\: False
            
            .. attribute:: cfcrequestentrystatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cfcRequestEntry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-FTP-CLIENT-MIB'
            _revision = '2006-03-31'

            def __init__(self):
                super(CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry, self).__init__()

                self.yang_name = "cfcRequestEntry"
                self.yang_parent_name = "cfcRequestTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cfcrequestindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cfcrequestindex', (YLeaf(YType.uint32, 'cfcRequestIndex'), ['int'])),
                    ('cfcrequestoperation', (YLeaf(YType.enumeration, 'cfcRequestOperation'), [('ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB', 'CfcRequestTable.CfcRequestEntry.CfcRequestOperation')])),
                    ('cfcrequestlocalfile', (YLeaf(YType.str, 'cfcRequestLocalFile'), ['str'])),
                    ('cfcrequestremotefile', (YLeaf(YType.str, 'cfcRequestRemoteFile'), ['str'])),
                    ('cfcrequestserver', (YLeaf(YType.str, 'cfcRequestServer'), ['str'])),
                    ('cfcrequestuser', (YLeaf(YType.str, 'cfcRequestUser'), ['str'])),
                    ('cfcrequestpassword', (YLeaf(YType.str, 'cfcRequestPassword'), ['str'])),
                    ('cfcrequestresult', (YLeaf(YType.enumeration, 'cfcRequestResult'), [('ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB', 'CfcRequestTable.CfcRequestEntry.CfcRequestResult')])),
                    ('cfcrequestcompletiontime', (YLeaf(YType.uint32, 'cfcRequestCompletionTime'), ['int'])),
                    ('cfcrequeststop', (YLeaf(YType.enumeration, 'cfcRequestStop'), [('ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB', 'CfcRequestTable.CfcRequestEntry.CfcRequestStop')])),
                    ('cfcrequestoperationstate', (YLeaf(YType.enumeration, 'cfcRequestOperationState'), [('ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB', 'CISCOFTPCLIENTMIB', 'CfcRequestTable.CfcRequestEntry.CfcRequestOperationState')])),
                    ('cfcrequestentrystatus', (YLeaf(YType.enumeration, 'cfcRequestEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cfcrequestindex = None
                self.cfcrequestoperation = None
                self.cfcrequestlocalfile = None
                self.cfcrequestremotefile = None
                self.cfcrequestserver = None
                self.cfcrequestuser = None
                self.cfcrequestpassword = None
                self.cfcrequestresult = None
                self.cfcrequestcompletiontime = None
                self.cfcrequeststop = None
                self.cfcrequestoperationstate = None
                self.cfcrequestentrystatus = None
                self._segment_path = lambda: "cfcRequestEntry" + "[cfcRequestIndex='" + str(self.cfcrequestindex) + "']"
                self._absolute_path = lambda: "CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/cfcRequestTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry, ['cfcrequestindex', 'cfcrequestoperation', 'cfcrequestlocalfile', 'cfcrequestremotefile', 'cfcrequestserver', 'cfcrequestuser', 'cfcrequestpassword', 'cfcrequestresult', 'cfcrequestcompletiontime', 'cfcrequeststop', 'cfcrequestoperationstate', 'cfcrequestentrystatus'], name, value)

            class CfcRequestOperation(Enum):
                """
                CfcRequestOperation (Enum Class)

                The FTP operation to be performed.

                .. data:: putBinary = 1

                .. data:: putASCII = 2

                """

                putBinary = Enum.YLeaf(1, "putBinary")

                putASCII = Enum.YLeaf(2, "putASCII")


            class CfcRequestOperationState(Enum):
                """
                CfcRequestOperationState (Enum Class)

                The operational state of the file transfer.  To short\-terminate

                the transfer set cfcRequestStop to 'stop'.

                .. data:: running = 1

                .. data:: stopping = 2

                .. data:: stopped = 3

                """

                running = Enum.YLeaf(1, "running")

                stopping = Enum.YLeaf(2, "stopping")

                stopped = Enum.YLeaf(3, "stopped")


            class CfcRequestResult(Enum):
                """
                CfcRequestResult (Enum Class)

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


            class CfcRequestStop(Enum):
                """
                CfcRequestStop (Enum Class)

                The action control to stop a running request.  Setting this to

                'stop' will begin the process of stopping the request.  Setting

                it to 'ready' or setting it to 'stop' more than once have no

                effect.  When read this object always returns ready.

                .. data:: ready = 1

                .. data:: stop = 2

                """

                ready = Enum.YLeaf(1, "ready")

                stop = Enum.YLeaf(2, "stop")




    def clone_ptr(self):
        self._top_entity = CISCOFTPCLIENTMIB()
        return self._top_entity



