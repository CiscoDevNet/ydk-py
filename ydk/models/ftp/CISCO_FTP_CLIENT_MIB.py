""" CISCO_FTP_CLIENT_MIB 

The MIB module for invoking Internet File Transfer Protocol
(FTP) operations for network management purposes.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOFTPCLIENTMIB(object):
    """
    
    
    .. attribute:: cfcrequest
    
    	
    	**type**\: :py:class:`CfcRequest <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequest>`
    
    .. attribute:: cfcrequesttable
    
    	A table of FTP client requests
    	**type**\: :py:class:`CfcRequestTable <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable>`
    
    

    """

    _prefix = 'cisco-ftp'
    _revision = '2006-03-31'

    def __init__(self):
        self.cfcrequest = CISCOFTPCLIENTMIB.CfcRequest()
        self.cfcrequest.parent = self
        self.cfcrequesttable = CISCOFTPCLIENTMIB.CfcRequestTable()
        self.cfcrequesttable.parent = self


    class CfcRequest(object):
        """
        
        
        .. attribute:: cfcrequestmaximum
        
        	The maximum number of requests this system can hold in cfcRequestTable.  A value of 0 indicates no configured limit.  This object may be read\-only on some systems.  When an attempt is made to create a new entry but the table is full, the oldest completed entry is bumped out and cfcRequestsBumped is incremented.  Changing this number does not disturb existing requests that are not completed and bumps completed requests as necessary
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequests
        
        	The current number of requests in cfcRequestTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestsbumped
        
        	The number of requests in cfcRequestTable that were bumped out to make room for a new request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cfcrequestshigh
        
        	The highest number of requests in cfcRequestTable since this system was last initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ftp'
        _revision = '2006-03-31'

        def __init__(self):
            self.parent = None
            self.cfcrequestmaximum = None
            self.cfcrequests = None
            self.cfcrequestsbumped = None
            self.cfcrequestshigh = None

        @property
        def _common_path(self):

            return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/CISCO-FTP-CLIENT-MIB:cfcRequest'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfcrequestmaximum is not None:
                return True

            if self.cfcrequests is not None:
                return True

            if self.cfcrequestsbumped is not None:
                return True

            if self.cfcrequestshigh is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
            return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequest']['meta_info']


    class CfcRequestTable(object):
        """
        A table of FTP client requests.
        
        .. attribute:: cfcrequestentry
        
        	Information about an FTP client request.  Management applications use cfcRequestEntryStatus to control entry modification, creation, and deletion.  Setting cfcRequestEntryStatus to 'active' from any state including 'active' causes the operation to be started.  The entry may be modified only when cfcRequestOperationState is 'stopped'.  The value of cfcRequestEntryStatus may be set to 'destroy' at any time.  Doing so will abort a running request.  Entries may not be created without explicitly setting cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'
        	**type**\: list of :py:class:`CfcRequestEntry <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry>`
        
        

        """

        _prefix = 'cisco-ftp'
        _revision = '2006-03-31'

        def __init__(self):
            self.parent = None
            self.cfcrequestentry = YList()
            self.cfcrequestentry.parent = self
            self.cfcrequestentry.name = 'cfcrequestentry'


        class CfcRequestEntry(object):
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
            
            .. attribute:: cfcrequestindex
            
            	An arbitrary integer to uniquely identify this entry.  To create an entry a management application should pick a random number
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cfcrequestcompletiontime
            
            	The value of sysUpTime when the operation completed.  For an incomplete operation this value is zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cfcrequestentrystatus
            
            	The control that allows modification, creation, and deletion of entries.  For detailed rules see the DESCRIPTION for cfcRequestEntry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cfcrequestlocalfile
            
            	The local file on which the operation is to be performed
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cfcrequestoperation
            
            	The FTP operation to be performed
            	**type**\: :py:class:`CfcRequestOperation_Enum <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperation_Enum>`
            
            .. attribute:: cfcrequestoperationstate
            
            	The operational state of the file transfer.  To short\-terminate the transfer set cfcRequestStop to 'stop'
            	**type**\: :py:class:`CfcRequestOperationState_Enum <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperationState_Enum>`
            
            .. attribute:: cfcrequestpassword
            
            	The password to use at the FTP server.  When read this object always returns a zero\-length string
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cfcrequestremotefile
            
            	The remote file on which the operation is to be performed
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cfcrequestresult
            
            	The result of the FTP operation
            	**type**\: :py:class:`CfcRequestResult_Enum <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestResult_Enum>`
            
            .. attribute:: cfcrequestserver
            
            	The domain name or IP address of the FTP server to use
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cfcrequeststop
            
            	The action control to stop a running request.  Setting this to 'stop' will begin the process of stopping the request.  Setting it to 'ready' or setting it to 'stop' more than once have no effect.  When read this object always returns ready
            	**type**\: :py:class:`CfcRequestStop_Enum <ydk.models.ftp.CISCO_FTP_CLIENT_MIB.CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestStop_Enum>`
            
            .. attribute:: cfcrequestuser
            
            	The user name to use at the FTP server
            	**type**\: str
            
            	**range:** 1..32
            
            

            """

            _prefix = 'cisco-ftp'
            _revision = '2006-03-31'

            def __init__(self):
                self.parent = None
                self.cfcrequestindex = None
                self.cfcrequestcompletiontime = None
                self.cfcrequestentrystatus = None
                self.cfcrequestlocalfile = None
                self.cfcrequestoperation = None
                self.cfcrequestoperationstate = None
                self.cfcrequestpassword = None
                self.cfcrequestremotefile = None
                self.cfcrequestresult = None
                self.cfcrequestserver = None
                self.cfcrequeststop = None
                self.cfcrequestuser = None

            class CfcRequestOperationState_Enum(Enum):
                """
                CfcRequestOperationState_Enum

                The operational state of the file transfer.  To short\-terminate
                the transfer set cfcRequestStop to 'stop'.

                """

                RUNNING = 1

                STOPPING = 2

                STOPPED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperationState_Enum']


            class CfcRequestOperation_Enum(Enum):
                """
                CfcRequestOperation_Enum

                The FTP operation to be performed.

                """

                PUTBINARY = 1

                PUTASCII = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestOperation_Enum']


            class CfcRequestResult_Enum(Enum):
                """
                CfcRequestResult_Enum

                The result of the FTP operation.

                """

                PENDING = 1

                SUCCESS = 2

                ABORTED = 3

                FILEOPENFAILLOCAL = 4

                FILEOPENFAILREMOTE = 5

                BADDOMAINNAME = 6

                UNREACHABLEIPADDRESS = 7

                LINKFAILED = 8

                FILEREADFAILED = 9

                FILEWRITEFAILED = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestResult_Enum']


            class CfcRequestStop_Enum(Enum):
                """
                CfcRequestStop_Enum

                The action control to stop a running request.  Setting this to
                'stop' will begin the process of stopping the request.  Setting
                it to 'ready' or setting it to 'stop' more than once have no
                effect.  When read this object always returns ready.

                """

                READY = 1

                STOP = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry.CfcRequestStop_Enum']


            @property
            def _common_path(self):
                if self.cfcrequestindex is None:
                    raise YPYDataValidationError('Key property cfcrequestindex is None')

                return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/CISCO-FTP-CLIENT-MIB:cfcRequestTable/CISCO-FTP-CLIENT-MIB:cfcRequestEntry[CISCO-FTP-CLIENT-MIB:cfcRequestIndex = ' + str(self.cfcrequestindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cfcrequestindex is not None:
                    return True

                if self.cfcrequestcompletiontime is not None:
                    return True

                if self.cfcrequestentrystatus is not None:
                    return True

                if self.cfcrequestlocalfile is not None:
                    return True

                if self.cfcrequestoperation is not None:
                    return True

                if self.cfcrequestoperationstate is not None:
                    return True

                if self.cfcrequestpassword is not None:
                    return True

                if self.cfcrequestremotefile is not None:
                    return True

                if self.cfcrequestresult is not None:
                    return True

                if self.cfcrequestserver is not None:
                    return True

                if self.cfcrequeststop is not None:
                    return True

                if self.cfcrequestuser is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
                return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable.CfcRequestEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/CISCO-FTP-CLIENT-MIB:cfcRequestTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cfcrequestentry is not None:
                for child_ref in self.cfcrequestentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
            return meta._meta_table['CISCOFTPCLIENTMIB.CfcRequestTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cfcrequest is not None and self.cfcrequest._has_data():
            return True

        if self.cfcrequest is not None and self.cfcrequest.is_presence():
            return True

        if self.cfcrequesttable is not None and self.cfcrequesttable._has_data():
            return True

        if self.cfcrequesttable is not None and self.cfcrequesttable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ftp._meta import _CISCO_FTP_CLIENT_MIB as meta
        return meta._meta_table['CISCOFTPCLIENTMIB']['meta_info']


