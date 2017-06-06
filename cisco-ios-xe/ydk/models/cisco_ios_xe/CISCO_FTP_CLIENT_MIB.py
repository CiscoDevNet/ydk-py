""" CISCO_FTP_CLIENT_MIB 

The MIB module for invoking Internet File Transfer Protocol
(FTP) operations for network management purposes.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoFtpClientMib(object):
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
        self.cfcrequest = CiscoFtpClientMib.Cfcrequest()
        self.cfcrequest.parent = self
        self.cfcrequesttable = CiscoFtpClientMib.Cfcrequesttable()
        self.cfcrequesttable.parent = self


    class Cfcrequest(object):
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
            if self.cfcrequestmaximum is not None:
                return True

            if self.cfcrequests is not None:
                return True

            if self.cfcrequestsbumped is not None:
                return True

            if self.cfcrequestshigh is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
            return meta._meta_table['CiscoFtpClientMib.Cfcrequest']['meta_info']


    class Cfcrequesttable(object):
        """
        A table of FTP client requests.
        
        .. attribute:: cfcrequestentry
        
        	Information about an FTP client request.  Management applications use cfcRequestEntryStatus to control entry modification, creation, and deletion.  Setting cfcRequestEntryStatus to 'active' from any state including 'active' causes the operation to be started.  The entry may be modified only when cfcRequestOperationState is 'stopped'.  The value of cfcRequestEntryStatus may be set to 'destroy' at any time.  Doing so will abort a running request.  Entries may not be created without explicitly setting cfcRequestEntryStatus to either 'createAndGo' or 'createAndWait'
        	**type**\: list of    :py:class:`Cfcrequestentry <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry>`
        
        

        """

        _prefix = 'CISCO-FTP-CLIENT-MIB'
        _revision = '2006-03-31'

        def __init__(self):
            self.parent = None
            self.cfcrequestentry = YList()
            self.cfcrequestentry.parent = self
            self.cfcrequestentry.name = 'cfcrequestentry'


        class Cfcrequestentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: cfcrequestlocalfile
            
            	The local file on which the operation is to be performed
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cfcrequestoperation
            
            	The FTP operation to be performed
            	**type**\:   :py:class:`CfcrequestoperationEnum <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationEnum>`
            
            .. attribute:: cfcrequestoperationstate
            
            	The operational state of the file transfer.  To short\-terminate the transfer set cfcRequestStop to 'stop'
            	**type**\:   :py:class:`CfcrequestoperationstateEnum <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationstateEnum>`
            
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
            	**type**\:   :py:class:`CfcrequestresultEnum <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestresultEnum>`
            
            .. attribute:: cfcrequestserver
            
            	The domain name or IP address of the FTP server to use
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cfcrequeststop
            
            	The action control to stop a running request.  Setting this to 'stop' will begin the process of stopping the request.  Setting it to 'ready' or setting it to 'stop' more than once have no effect.  When read this object always returns ready
            	**type**\:   :py:class:`CfcrequeststopEnum <ydk.models.cisco_ios_xe.CISCO_FTP_CLIENT_MIB.CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequeststopEnum>`
            
            .. attribute:: cfcrequestuser
            
            	The user name to use at the FTP server
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'CISCO-FTP-CLIENT-MIB'
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

            class CfcrequestoperationEnum(Enum):
                """
                CfcrequestoperationEnum

                The FTP operation to be performed.

                .. data:: putBinary = 1

                .. data:: putASCII = 2

                """

                putBinary = 1

                putASCII = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationEnum']


            class CfcrequestoperationstateEnum(Enum):
                """
                CfcrequestoperationstateEnum

                The operational state of the file transfer.  To short\-terminate

                the transfer set cfcRequestStop to 'stop'.

                .. data:: running = 1

                .. data:: stopping = 2

                .. data:: stopped = 3

                """

                running = 1

                stopping = 2

                stopped = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestoperationstateEnum']


            class CfcrequestresultEnum(Enum):
                """
                CfcrequestresultEnum

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

                pending = 1

                success = 2

                aborted = 3

                fileOpenFailLocal = 4

                fileOpenFailRemote = 5

                badDomainName = 6

                unreachableIpAddress = 7

                linkFailed = 8

                fileReadFailed = 9

                fileWriteFailed = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequestresultEnum']


            class CfcrequeststopEnum(Enum):
                """
                CfcrequeststopEnum

                The action control to stop a running request.  Setting this to

                'stop' will begin the process of stopping the request.  Setting

                it to 'ready' or setting it to 'stop' more than once have no

                effect.  When read this object always returns ready.

                .. data:: ready = 1

                .. data:: stop = 2

                """

                ready = 1

                stop = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
                    return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry.CfcrequeststopEnum']


            @property
            def _common_path(self):
                if self.cfcrequestindex is None:
                    raise YPYModelError('Key property cfcrequestindex is None')

                return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/CISCO-FTP-CLIENT-MIB:cfcRequestTable/CISCO-FTP-CLIENT-MIB:cfcRequestEntry[CISCO-FTP-CLIENT-MIB:cfcRequestIndex = ' + str(self.cfcrequestindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
                return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable.Cfcrequestentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB/CISCO-FTP-CLIENT-MIB:cfcRequestTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cfcrequestentry is not None:
                for child_ref in self.cfcrequestentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
            return meta._meta_table['CiscoFtpClientMib.Cfcrequesttable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-FTP-CLIENT-MIB:CISCO-FTP-CLIENT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cfcrequest is not None and self.cfcrequest._has_data():
            return True

        if self.cfcrequesttable is not None and self.cfcrequesttable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_FTP_CLIENT_MIB as meta
        return meta._meta_table['CiscoFtpClientMib']['meta_info']


