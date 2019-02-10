""" CISCO_AAA_SERVER_MIB 

The MIB module	for monitoring communications and status
of AAA	Server operation

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoAAAProtocol(Enum):
    """
    CiscoAAAProtocol (Enum Class)

    Protocol used with this server.

    tacacsplus(1) \- TACACS+

    radius(2)   \- RADIUS

    ldap(3)     \-   Light Weight Directory Protocol

    kerberos(4) \-   Kerberos

    ntlm(5)     \-   Authentication/Authorization using

    		 NT Domain

    sdi(6)      \-   Authentication/Authorization using

    		 Secure ID

    other(7)    \-   Other protocols

    .. data:: tacacsplus = 1

    .. data:: radius = 2

    .. data:: ldap = 3

    .. data:: kerberos = 4

    .. data:: ntlm = 5

    .. data:: sdi = 6

    .. data:: other = 7

    """

    tacacsplus = Enum.YLeaf(1, "tacacsplus")

    radius = Enum.YLeaf(2, "radius")

    ldap = Enum.YLeaf(3, "ldap")

    kerberos = Enum.YLeaf(4, "kerberos")

    ntlm = Enum.YLeaf(5, "ntlm")

    sdi = Enum.YLeaf(6, "sdi")

    other = Enum.YLeaf(7, "other")



class CISCOAAASERVERMIB(Entity):
    """
    
    
    .. attribute:: casconfig
    
    	
    	**type**\:  :py:class:`CasConfig <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.CasConfig>`
    
    	**config**\: False
    
    .. attribute:: casconfigtable
    
    	This table shows current configurations for each AAA server, allows existing servers to	be removed and new ones to be created
    	**type**\:  :py:class:`CasConfigTable <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.CasConfigTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-AAA-SERVER-MIB'
    _revision = '2003-11-17'

    def __init__(self):
        super(CISCOAAASERVERMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-AAA-SERVER-MIB"
        self.yang_parent_name = "CISCO-AAA-SERVER-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("casConfig", ("casconfig", CISCOAAASERVERMIB.CasConfig)), ("casConfigTable", ("casconfigtable", CISCOAAASERVERMIB.CasConfigTable))])
        self._leafs = OrderedDict()

        self.casconfig = CISCOAAASERVERMIB.CasConfig()
        self.casconfig.parent = self
        self._children_name_map["casconfig"] = "casConfig"

        self.casconfigtable = CISCOAAASERVERMIB.CasConfigTable()
        self.casconfigtable.parent = self
        self._children_name_map["casconfigtable"] = "casConfigTable"
        self._segment_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOAAASERVERMIB, [], name, value)


    class CasConfig(Entity):
        """
        
        
        .. attribute:: casserverstatechangeenable
        
        	This variable controls the	generation of casServerStateChange notification.  When this variable	is true(1), generation of casServerStateChange notifications	is enabled. When this variable	is false(2), generation	of casServerStateChange notifications	is disabled.  The default value is false(2)
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CISCOAAASERVERMIB.CasConfig, self).__init__()

            self.yang_name = "casConfig"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('casserverstatechangeenable', (YLeaf(YType.boolean, 'casServerStateChangeEnable'), ['bool'])),
            ])
            self.casserverstatechangeenable = None
            self._segment_path = lambda: "casConfig"
            self._absolute_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASERVERMIB.CasConfig, ['casserverstatechangeenable'], name, value)



    class CasConfigTable(Entity):
        """
        This table shows current configurations for each
        AAA server, allows existing servers to	be removed
        and new ones to be created.
        
        .. attribute:: casconfigentry
        
        	An	AAA server configuration identified by its protocol and its index.  An	entry is created/removed when a	server is defined or	undefined with IOS configuration commands via CLI or by issuing appropriate sets	to this	table using snmp.  A management station wishing to create an entry should first generate a random number to be used as the index to	this sparse table.  The	station	should then create the associated	instance of the	row status and row index objects. It	must also, either in the same or in successive PDUs, create an instance	of casAddress where casAddress is the IP	address	of the server to be added.  It	should also modify the default values for casAuthenPort, casAcctPort if the	defaults are not appropriate.  If	casKey is a zero\-length	string or is not explicitly set, then the global key will be used.	Otherwise, this	value is	used as	the key	for this server	instance.  Once the appropriate instance of all the configuration objects have been created,	either by an explicit SNMP set request or	by default, the	row status should be set to active(1) to initiate the request.  After the AAA server is made active, the entry can	not be modified \-	the only allowed operation after this is to destroy the entry by setting casConfigRowStatus to	destroy(6).  casPriority is automatically assigned once	the entry is made active and reflects the relative priority of the defined server with respect to already configured servers. Newly\-created servers will	be assigned the	lowest priority. To	reassign server	priorities to existing server entries, it	may be necessary to destroy and	recreate entries in order of	priority.  Entries in	this table with	casConfigRowStatus equal to active(1) remain in the table until destroyed.  Entries in	this table with	casConfigRowStatus equal to values other than active(1) will be destroyed after timeout (5	minutes).  If	a server address being created via SNMP	exists already in	another	active casConfigEntry, then a newly created row can not be	made active until the original row with	the with the same server address value	is destroyed.  Upon reload, casIndex values may be changed, but the priorities	that were saved	before reload will be retained, with lowest priority number corresponding to the higher priority servers
        	**type**\: list of  		 :py:class:`CasConfigEntry <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.CasConfigTable.CasConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CISCOAAASERVERMIB.CasConfigTable, self).__init__()

            self.yang_name = "casConfigTable"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("casConfigEntry", ("casconfigentry", CISCOAAASERVERMIB.CasConfigTable.CasConfigEntry))])
            self._leafs = OrderedDict()

            self.casconfigentry = YList(self)
            self._segment_path = lambda: "casConfigTable"
            self._absolute_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASERVERMIB.CasConfigTable, [], name, value)


        class CasConfigEntry(Entity):
            """
            An	AAA server configuration identified by its protocol
            and its index.
            
            An	entry is created/removed when a	server is defined
            or	undefined with IOS configuration commands via
            CLI or by issuing appropriate sets	to this	table
            using snmp.
            
            A management station wishing to create an entry should
            first generate a random number to be used as the index
            to	this sparse table.  The	station	should then create the
            associated	instance of the	row status and row index objects.
            It	must also, either in the same or in successive PDUs,
            create an instance	of casAddress where casAddress is the
            IP	address	of the server to be added.
            
            It	should also modify the default values for casAuthenPort,
            casAcctPort if the	defaults are not appropriate.
            
            If	casKey is a zero\-length	string or is not explicitly set,
            then the global key will be used.	Otherwise, this	value
            is	used as	the key	for this server	instance.
            
            Once the appropriate instance of all the configuration
            objects have been created,	either by an explicit SNMP set
            request or	by default, the	row status should be set to
            active(1) to initiate the request.
            
            After the AAA server is made active, the entry can	not be
            modified \-	the only allowed operation after this is to
            destroy the entry by setting casConfigRowStatus to	destroy(6).
            
            casPriority is automatically assigned once	the entry is
            made active and reflects the relative priority of the
            defined server with respect to already configured servers.
            Newly\-created servers will	be assigned the	lowest priority.
            To	reassign server	priorities to existing server entries,
            it	may be necessary to destroy and	recreate entries in order
            of	priority.
            
            Entries in	this table with	casConfigRowStatus equal to
            active(1) remain in the table until destroyed.
            
            Entries in	this table with	casConfigRowStatus equal to
            values other than active(1) will be destroyed after timeout
            (5	minutes).
            
            If	a server address being created via SNMP	exists already
            in	another	active casConfigEntry, then a newly created row
            can not be	made active until the original row with	the
            with the same server address value	is destroyed.
            
            Upon reload, casIndex values may be changed, but the
            priorities	that were saved	before reload will be retained,
            with lowest priority number corresponding to the higher
            priority servers.
            
            .. attribute:: casprotocol  (key)
            
            	The variable denotes the protocol used by the managed device with the AAA server corresponding to  this entry in the table
            	**type**\:  :py:class:`CiscoAAAProtocol <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CiscoAAAProtocol>`
            
            	**config**\: False
            
            .. attribute:: casindex  (key)
            
            	A management station wishing to initiate a	new AAA	server configuration should use a	random value for this object when creating an instance of casConfigEntry.  The RowStatus semantics of	the casConfigRowStatus object will prevent access conflicts.  If	the randomly chosen casIndex value for row creation is	already	in use by an existing entry, snmp set to the casIndex value will fail
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: casaddress
            
            	The IP address of the server
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: casauthenport
            
            	UDP/TCP port used for authentication in the configuration  For TACACS+, this object should be	explictly set.  Default value is the IOS default for radius\: 1645
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: casacctport
            
            	UDP/TCP port used for accounting service in the configuration  For TACACS+, the value of casAcctPort is ignored. casAuthenPort will	be used	instead.  Default value is the IOS default for radius\: 1646
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: caskey
            
            	The server key	to be used with	this server.  Retrieving the	value of this object via SNMP will return	an empty string	for security reasons
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: caspriority
            
            	A number that indicates the priority of the server	in this entry.  Lower	numbers	indicate higher	priority
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: casconfigrowstatus
            
            	The status of this table entry.  Once the entry status	is set to	active,	the associated entry cannot be modified except	destroyed by setting this object to destroy(6)
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: casauthenrequests
            
            	The number	of authentication requests sent	to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthenrequesttimeouts
            
            	The number	of authentication requests which have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthenunexpectedresponses
            
            	The number	of unexpected authentication responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthenservererrorresponses
            
            	The number	of server ERROR	authentication responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authentication operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthenincorrectresponses
            
            	The number	of authentication responses which could	not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthenresponsetime
            
            	Average response time for authentication requests sent to	this server, excluding timeouts, since system re\-initialization
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: casauthentransactionsuccesses
            
            	The number	of authentication transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authentication pass	or fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthentransactionfailures
            
            	The number	of authentication transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorrequests
            
            	The number	of authorization requests sent to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorrequesttimeouts
            
            	The number	of authorization requests which	have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorunexpectedresponses
            
            	The number	of unexpected authorization responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorservererrorresponses
            
            	The number	of server ERROR	authorization responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authorization operation.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorincorrectresponses
            
            	The number	of authorization responses which could not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthorresponsetime
            
            	Average response time for authorization requests sent to	this server, excluding timeouts, since system re\-initialization.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: casauthortransactionsuccesses
            
            	The number	of authorization transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authorization pass or fail.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casauthortransactionfailures
            
            	The number	of authorization transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctrequests
            
            	The number	of accounting requests sent to this server since system re\-initialization.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctrequesttimeouts
            
            	The number	of accounting requests which have timed out since system re\-initialization.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctunexpectedresponses
            
            	The number	of unexpected accounting responses received from this server since system re\-initialization.  An	example	is a delayed response to a request which had already timed out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctservererrorresponses
            
            	The number	of server ERROR	accounting responses received from this server since system re\-initialization.  These are responses indicating that the server itself has identified an error with its accounting operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctincorrectresponses
            
            	The number	of accounting responses	which could not be	processed since	system re\-initialization.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casacctresponsetime
            
            	Average response time for accounting requests sent to	this server,, since system re\-initialization excluding timeouts
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: casaccttransactionsuccesses
            
            	The number	of accounting transactions with	this server which succeeded since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an accounting pass or fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casaccttransactionfailures
            
            	The number	of accounting transactions with	this server which failed since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: casstate
            
            	Current state of this server.  up(1)	 \- Server responding to	requests  dead(2) \- Server failed to respond  A server is marked	dead if	it does	not respond after maximum retransmissions.  A server is marked	up again either	after a	waiting period or if some response	is received from it.  The initial value of casState is 'up(1)' at system re\-initialization.	This will only transistion to 'dead(2)' if	an attempt to communicate fails
            	**type**\:  :py:class:`CasState <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.CasConfigTable.CasConfigEntry.CasState>`
            
            	**config**\: False
            
            .. attribute:: cascurrentstateduration
            
            	This object provides the elapsed time the server has been in its current state as shown	in casState
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: caspreviousstateduration
            
            	This object provides the elapsed time the server was been in its previous state	prior to the most recent transistion of casState.  This value	is zero	if the server has not changed state
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: castotaldeadtime
            
            	The total elapsed time this server's casState has had the value 'dead(2)' since system re\-initialization
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: casdeadcount
            
            	The number	of times this server's casState	has transitioned to 'dead(2)' since system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-AAA-SERVER-MIB'
            _revision = '2003-11-17'

            def __init__(self):
                super(CISCOAAASERVERMIB.CasConfigTable.CasConfigEntry, self).__init__()

                self.yang_name = "casConfigEntry"
                self.yang_parent_name = "casConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['casprotocol','casindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('casprotocol', (YLeaf(YType.enumeration, 'casProtocol'), [('ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoAAAProtocol', '')])),
                    ('casindex', (YLeaf(YType.uint32, 'casIndex'), ['int'])),
                    ('casaddress', (YLeaf(YType.str, 'casAddress'), ['str'])),
                    ('casauthenport', (YLeaf(YType.int32, 'casAuthenPort'), ['int'])),
                    ('casacctport', (YLeaf(YType.int32, 'casAcctPort'), ['int'])),
                    ('caskey', (YLeaf(YType.str, 'casKey'), ['str'])),
                    ('caspriority', (YLeaf(YType.uint32, 'casPriority'), ['int'])),
                    ('casconfigrowstatus', (YLeaf(YType.enumeration, 'casConfigRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('casauthenrequests', (YLeaf(YType.uint32, 'casAuthenRequests'), ['int'])),
                    ('casauthenrequesttimeouts', (YLeaf(YType.uint32, 'casAuthenRequestTimeouts'), ['int'])),
                    ('casauthenunexpectedresponses', (YLeaf(YType.uint32, 'casAuthenUnexpectedResponses'), ['int'])),
                    ('casauthenservererrorresponses', (YLeaf(YType.uint32, 'casAuthenServerErrorResponses'), ['int'])),
                    ('casauthenincorrectresponses', (YLeaf(YType.uint32, 'casAuthenIncorrectResponses'), ['int'])),
                    ('casauthenresponsetime', (YLeaf(YType.int32, 'casAuthenResponseTime'), ['int'])),
                    ('casauthentransactionsuccesses', (YLeaf(YType.uint32, 'casAuthenTransactionSuccesses'), ['int'])),
                    ('casauthentransactionfailures', (YLeaf(YType.uint32, 'casAuthenTransactionFailures'), ['int'])),
                    ('casauthorrequests', (YLeaf(YType.uint32, 'casAuthorRequests'), ['int'])),
                    ('casauthorrequesttimeouts', (YLeaf(YType.uint32, 'casAuthorRequestTimeouts'), ['int'])),
                    ('casauthorunexpectedresponses', (YLeaf(YType.uint32, 'casAuthorUnexpectedResponses'), ['int'])),
                    ('casauthorservererrorresponses', (YLeaf(YType.uint32, 'casAuthorServerErrorResponses'), ['int'])),
                    ('casauthorincorrectresponses', (YLeaf(YType.uint32, 'casAuthorIncorrectResponses'), ['int'])),
                    ('casauthorresponsetime', (YLeaf(YType.int32, 'casAuthorResponseTime'), ['int'])),
                    ('casauthortransactionsuccesses', (YLeaf(YType.uint32, 'casAuthorTransactionSuccesses'), ['int'])),
                    ('casauthortransactionfailures', (YLeaf(YType.uint32, 'casAuthorTransactionFailures'), ['int'])),
                    ('casacctrequests', (YLeaf(YType.uint32, 'casAcctRequests'), ['int'])),
                    ('casacctrequesttimeouts', (YLeaf(YType.uint32, 'casAcctRequestTimeouts'), ['int'])),
                    ('casacctunexpectedresponses', (YLeaf(YType.uint32, 'casAcctUnexpectedResponses'), ['int'])),
                    ('casacctservererrorresponses', (YLeaf(YType.uint32, 'casAcctServerErrorResponses'), ['int'])),
                    ('casacctincorrectresponses', (YLeaf(YType.uint32, 'casAcctIncorrectResponses'), ['int'])),
                    ('casacctresponsetime', (YLeaf(YType.int32, 'casAcctResponseTime'), ['int'])),
                    ('casaccttransactionsuccesses', (YLeaf(YType.uint32, 'casAcctTransactionSuccesses'), ['int'])),
                    ('casaccttransactionfailures', (YLeaf(YType.uint32, 'casAcctTransactionFailures'), ['int'])),
                    ('casstate', (YLeaf(YType.enumeration, 'casState'), [('ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CISCOAAASERVERMIB', 'CasConfigTable.CasConfigEntry.CasState')])),
                    ('cascurrentstateduration', (YLeaf(YType.int32, 'casCurrentStateDuration'), ['int'])),
                    ('caspreviousstateduration', (YLeaf(YType.int32, 'casPreviousStateDuration'), ['int'])),
                    ('castotaldeadtime', (YLeaf(YType.int32, 'casTotalDeadTime'), ['int'])),
                    ('casdeadcount', (YLeaf(YType.uint32, 'casDeadCount'), ['int'])),
                ])
                self.casprotocol = None
                self.casindex = None
                self.casaddress = None
                self.casauthenport = None
                self.casacctport = None
                self.caskey = None
                self.caspriority = None
                self.casconfigrowstatus = None
                self.casauthenrequests = None
                self.casauthenrequesttimeouts = None
                self.casauthenunexpectedresponses = None
                self.casauthenservererrorresponses = None
                self.casauthenincorrectresponses = None
                self.casauthenresponsetime = None
                self.casauthentransactionsuccesses = None
                self.casauthentransactionfailures = None
                self.casauthorrequests = None
                self.casauthorrequesttimeouts = None
                self.casauthorunexpectedresponses = None
                self.casauthorservererrorresponses = None
                self.casauthorincorrectresponses = None
                self.casauthorresponsetime = None
                self.casauthortransactionsuccesses = None
                self.casauthortransactionfailures = None
                self.casacctrequests = None
                self.casacctrequesttimeouts = None
                self.casacctunexpectedresponses = None
                self.casacctservererrorresponses = None
                self.casacctincorrectresponses = None
                self.casacctresponsetime = None
                self.casaccttransactionsuccesses = None
                self.casaccttransactionfailures = None
                self.casstate = None
                self.cascurrentstateduration = None
                self.caspreviousstateduration = None
                self.castotaldeadtime = None
                self.casdeadcount = None
                self._segment_path = lambda: "casConfigEntry" + "[casProtocol='" + str(self.casprotocol) + "']" + "[casIndex='" + str(self.casindex) + "']"
                self._absolute_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/casConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOAAASERVERMIB.CasConfigTable.CasConfigEntry, ['casprotocol', 'casindex', 'casaddress', 'casauthenport', 'casacctport', 'caskey', 'caspriority', 'casconfigrowstatus', 'casauthenrequests', 'casauthenrequesttimeouts', 'casauthenunexpectedresponses', 'casauthenservererrorresponses', 'casauthenincorrectresponses', 'casauthenresponsetime', 'casauthentransactionsuccesses', 'casauthentransactionfailures', 'casauthorrequests', 'casauthorrequesttimeouts', 'casauthorunexpectedresponses', 'casauthorservererrorresponses', 'casauthorincorrectresponses', 'casauthorresponsetime', 'casauthortransactionsuccesses', 'casauthortransactionfailures', 'casacctrequests', 'casacctrequesttimeouts', 'casacctunexpectedresponses', 'casacctservererrorresponses', 'casacctincorrectresponses', 'casacctresponsetime', 'casaccttransactionsuccesses', 'casaccttransactionfailures', 'casstate', 'cascurrentstateduration', 'caspreviousstateduration', 'castotaldeadtime', 'casdeadcount'], name, value)

            class CasState(Enum):
                """
                CasState (Enum Class)

                Current state of this server.

                up(1)	 \- Server responding to	requests

                dead(2) \- Server failed to respond

                A server is marked	dead if	it does	not respond after

                maximum retransmissions.

                A server is marked	up again either	after a	waiting

                period or if some response	is received from it.

                The initial value of casState is 'up(1)' at system

                re\-initialization.	This will only transistion to 'dead(2)'

                if	an attempt to communicate fails.

                .. data:: up = 1

                .. data:: dead = 2

                """

                up = Enum.YLeaf(1, "up")

                dead = Enum.YLeaf(2, "dead")




    def clone_ptr(self):
        self._top_entity = CISCOAAASERVERMIB()
        return self._top_entity



