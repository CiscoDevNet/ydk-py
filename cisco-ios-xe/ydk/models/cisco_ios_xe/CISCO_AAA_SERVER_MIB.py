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
    
    	
    	**type**\:  :py:class:`Casconfig <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.Casconfig>`
    
    .. attribute:: casconfigtable
    
    	This table shows current configurations for each AAA server, allows existing servers to	be removed and new ones to be created
    	**type**\:  :py:class:`Casconfigtable <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.Casconfigtable>`
    
    

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
        self._child_container_classes = OrderedDict([("casConfig", ("casconfig", CISCOAAASERVERMIB.Casconfig)), ("casConfigTable", ("casconfigtable", CISCOAAASERVERMIB.Casconfigtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.casconfig = CISCOAAASERVERMIB.Casconfig()
        self.casconfig.parent = self
        self._children_name_map["casconfig"] = "casConfig"
        self._children_yang_names.add("casConfig")

        self.casconfigtable = CISCOAAASERVERMIB.Casconfigtable()
        self.casconfigtable.parent = self
        self._children_name_map["casconfigtable"] = "casConfigTable"
        self._children_yang_names.add("casConfigTable")
        self._segment_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB"


    class Casconfig(Entity):
        """
        
        
        .. attribute:: casserverstatechangeenable
        
        	This variable controls the	generation of casServerStateChange notification.  When this variable	is true(1), generation of casServerStateChange notifications	is enabled. When this variable	is false(2), generation	of casServerStateChange notifications	is disabled.  The default value is false(2)
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CISCOAAASERVERMIB.Casconfig, self).__init__()

            self.yang_name = "casConfig"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('casserverstatechangeenable', YLeaf(YType.boolean, 'casServerStateChangeEnable')),
            ])
            self.casserverstatechangeenable = None
            self._segment_path = lambda: "casConfig"
            self._absolute_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASERVERMIB.Casconfig, ['casserverstatechangeenable'], name, value)


    class Casconfigtable(Entity):
        """
        This table shows current configurations for each
        AAA server, allows existing servers to	be removed
        and new ones to be created.
        
        .. attribute:: casconfigentry
        
        	An	AAA server configuration identified by its protocol and its index.  An	entry is created/removed when a	server is defined or	undefined with IOS configuration commands via CLI or by issuing appropriate sets	to this	table using snmp.  A management station wishing to create an entry should first generate a random number to be used as the index to	this sparse table.  The	station	should then create the associated	instance of the	row status and row index objects. It	must also, either in the same or in successive PDUs, create an instance	of casAddress where casAddress is the IP	address	of the server to be added.  It	should also modify the default values for casAuthenPort, casAcctPort if the	defaults are not appropriate.  If	casKey is a zero\-length	string or is not explicitly set, then the global key will be used.	Otherwise, this	value is	used as	the key	for this server	instance.  Once the appropriate instance of all the configuration objects have been created,	either by an explicit SNMP set request or	by default, the	row status should be set to active(1) to initiate the request.  After the AAA server is made active, the entry can	not be modified \-	the only allowed operation after this is to destroy the entry by setting casConfigRowStatus to	destroy(6).  casPriority is automatically assigned once	the entry is made active and reflects the relative priority of the defined server with respect to already configured servers. Newly\-created servers will	be assigned the	lowest priority. To	reassign server	priorities to existing server entries, it	may be necessary to destroy and	recreate entries in order of	priority.  Entries in	this table with	casConfigRowStatus equal to active(1) remain in the table until destroyed.  Entries in	this table with	casConfigRowStatus equal to values other than active(1) will be destroyed after timeout (5	minutes).  If	a server address being created via SNMP	exists already in	another	active casConfigEntry, then a newly created row can not be	made active until the original row with	the with the same server address value	is destroyed.  Upon reload, casIndex values may be changed, but the priorities	that were saved	before reload will be retained, with lowest priority number corresponding to the higher priority servers
        	**type**\: list of  		 :py:class:`Casconfigentry <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.Casconfigtable.Casconfigentry>`
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CISCOAAASERVERMIB.Casconfigtable, self).__init__()

            self.yang_name = "casConfigTable"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("casConfigEntry", ("casconfigentry", CISCOAAASERVERMIB.Casconfigtable.Casconfigentry))])
            self._leafs = OrderedDict()

            self.casconfigentry = YList(self)
            self._segment_path = lambda: "casConfigTable"
            self._absolute_path = lambda: "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOAAASERVERMIB.Casconfigtable, [], name, value)


        class Casconfigentry(Entity):
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
            
            .. attribute:: casindex  (key)
            
            	A management station wishing to initiate a	new AAA	server configuration should use a	random value for this object when creating an instance of casConfigEntry.  The RowStatus semantics of	the casConfigRowStatus object will prevent access conflicts.  If	the randomly chosen casIndex value for row creation is	already	in use by an existing entry, snmp set to the casIndex value will fail
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: casaddress
            
            	The IP address of the server
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: casauthenport
            
            	UDP/TCP port used for authentication in the configuration  For TACACS+, this object should be	explictly set.  Default value is the IOS default for radius\: 1645
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: casacctport
            
            	UDP/TCP port used for accounting service in the configuration  For TACACS+, the value of casAcctPort is ignored. casAuthenPort will	be used	instead.  Default value is the IOS default for radius\: 1646
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: caskey
            
            	The server key	to be used with	this server.  Retrieving the	value of this object via SNMP will return	an empty string	for security reasons
            	**type**\: str
            
            .. attribute:: caspriority
            
            	A number that indicates the priority of the server	in this entry.  Lower	numbers	indicate higher	priority
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: casconfigrowstatus
            
            	The status of this table entry.  Once the entry status	is set to	active,	the associated entry cannot be modified except	destroyed by setting this object to destroy(6)
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: casauthenrequests
            
            	The number	of authentication requests sent	to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenrequesttimeouts
            
            	The number	of authentication requests which have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenunexpectedresponses
            
            	The number	of unexpected authentication responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenservererrorresponses
            
            	The number	of server ERROR	authentication responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authentication operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenincorrectresponses
            
            	The number	of authentication responses which could	not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenresponsetime
            
            	Average response time for authentication requests sent to	this server, excluding timeouts, since system re\-initialization
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: casauthentransactionsuccesses
            
            	The number	of authentication transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authentication pass	or fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthentransactionfailures
            
            	The number	of authentication transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorrequests
            
            	The number	of authorization requests sent to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorrequesttimeouts
            
            	The number	of authorization requests which	have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorunexpectedresponses
            
            	The number	of unexpected authorization responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorservererrorresponses
            
            	The number	of server ERROR	authorization responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authorization operation.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorincorrectresponses
            
            	The number	of authorization responses which could not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorresponsetime
            
            	Average response time for authorization requests sent to	this server, excluding timeouts, since system re\-initialization.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: casauthortransactionsuccesses
            
            	The number	of authorization transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authorization pass or fail.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthortransactionfailures
            
            	The number	of authorization transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctrequests
            
            	The number	of accounting requests sent to this server since system re\-initialization.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctrequesttimeouts
            
            	The number	of accounting requests which have timed out since system re\-initialization.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctunexpectedresponses
            
            	The number	of unexpected accounting responses received from this server since system re\-initialization.  An	example	is a delayed response to a request which had already timed out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctservererrorresponses
            
            	The number	of server ERROR	accounting responses received from this server since system re\-initialization.  These are responses indicating that the server itself has identified an error with its accounting operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctincorrectresponses
            
            	The number	of accounting responses	which could not be	processed since	system re\-initialization.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctresponsetime
            
            	Average response time for accounting requests sent to	this server,, since system re\-initialization excluding timeouts
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: casaccttransactionsuccesses
            
            	The number	of accounting transactions with	this server which succeeded since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an accounting pass or fail
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casaccttransactionfailures
            
            	The number	of accounting transactions with	this server which failed since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: casstate
            
            	Current state of this server.  up(1)	 \- Server responding to	requests  dead(2) \- Server failed to respond  A server is marked	dead if	it does	not respond after maximum retransmissions.  A server is marked	up again either	after a	waiting period or if some response	is received from it.  The initial value of casState is 'up(1)' at system re\-initialization.	This will only transistion to 'dead(2)' if	an attempt to communicate fails
            	**type**\:  :py:class:`Casstate <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CISCOAAASERVERMIB.Casconfigtable.Casconfigentry.Casstate>`
            
            .. attribute:: cascurrentstateduration
            
            	This object provides the elapsed time the server has been in its current state as shown	in casState
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: caspreviousstateduration
            
            	This object provides the elapsed time the server was been in its previous state	prior to the most recent transistion of casState.  This value	is zero	if the server has not changed state
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: castotaldeadtime
            
            	The total elapsed time this server's casState has had the value 'dead(2)' since system re\-initialization
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: casdeadcount
            
            	The number	of times this server's casState	has transitioned to 'dead(2)' since system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-AAA-SERVER-MIB'
            _revision = '2003-11-17'

            def __init__(self):
                super(CISCOAAASERVERMIB.Casconfigtable.Casconfigentry, self).__init__()

                self.yang_name = "casConfigEntry"
                self.yang_parent_name = "casConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['casprotocol','casindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('casprotocol', YLeaf(YType.enumeration, 'casProtocol')),
                    ('casindex', YLeaf(YType.uint32, 'casIndex')),
                    ('casaddress', YLeaf(YType.str, 'casAddress')),
                    ('casauthenport', YLeaf(YType.int32, 'casAuthenPort')),
                    ('casacctport', YLeaf(YType.int32, 'casAcctPort')),
                    ('caskey', YLeaf(YType.str, 'casKey')),
                    ('caspriority', YLeaf(YType.uint32, 'casPriority')),
                    ('casconfigrowstatus', YLeaf(YType.enumeration, 'casConfigRowStatus')),
                    ('casauthenrequests', YLeaf(YType.uint32, 'casAuthenRequests')),
                    ('casauthenrequesttimeouts', YLeaf(YType.uint32, 'casAuthenRequestTimeouts')),
                    ('casauthenunexpectedresponses', YLeaf(YType.uint32, 'casAuthenUnexpectedResponses')),
                    ('casauthenservererrorresponses', YLeaf(YType.uint32, 'casAuthenServerErrorResponses')),
                    ('casauthenincorrectresponses', YLeaf(YType.uint32, 'casAuthenIncorrectResponses')),
                    ('casauthenresponsetime', YLeaf(YType.int32, 'casAuthenResponseTime')),
                    ('casauthentransactionsuccesses', YLeaf(YType.uint32, 'casAuthenTransactionSuccesses')),
                    ('casauthentransactionfailures', YLeaf(YType.uint32, 'casAuthenTransactionFailures')),
                    ('casauthorrequests', YLeaf(YType.uint32, 'casAuthorRequests')),
                    ('casauthorrequesttimeouts', YLeaf(YType.uint32, 'casAuthorRequestTimeouts')),
                    ('casauthorunexpectedresponses', YLeaf(YType.uint32, 'casAuthorUnexpectedResponses')),
                    ('casauthorservererrorresponses', YLeaf(YType.uint32, 'casAuthorServerErrorResponses')),
                    ('casauthorincorrectresponses', YLeaf(YType.uint32, 'casAuthorIncorrectResponses')),
                    ('casauthorresponsetime', YLeaf(YType.int32, 'casAuthorResponseTime')),
                    ('casauthortransactionsuccesses', YLeaf(YType.uint32, 'casAuthorTransactionSuccesses')),
                    ('casauthortransactionfailures', YLeaf(YType.uint32, 'casAuthorTransactionFailures')),
                    ('casacctrequests', YLeaf(YType.uint32, 'casAcctRequests')),
                    ('casacctrequesttimeouts', YLeaf(YType.uint32, 'casAcctRequestTimeouts')),
                    ('casacctunexpectedresponses', YLeaf(YType.uint32, 'casAcctUnexpectedResponses')),
                    ('casacctservererrorresponses', YLeaf(YType.uint32, 'casAcctServerErrorResponses')),
                    ('casacctincorrectresponses', YLeaf(YType.uint32, 'casAcctIncorrectResponses')),
                    ('casacctresponsetime', YLeaf(YType.int32, 'casAcctResponseTime')),
                    ('casaccttransactionsuccesses', YLeaf(YType.uint32, 'casAcctTransactionSuccesses')),
                    ('casaccttransactionfailures', YLeaf(YType.uint32, 'casAcctTransactionFailures')),
                    ('casstate', YLeaf(YType.enumeration, 'casState')),
                    ('cascurrentstateduration', YLeaf(YType.int32, 'casCurrentStateDuration')),
                    ('caspreviousstateduration', YLeaf(YType.int32, 'casPreviousStateDuration')),
                    ('castotaldeadtime', YLeaf(YType.int32, 'casTotalDeadTime')),
                    ('casdeadcount', YLeaf(YType.uint32, 'casDeadCount')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOAAASERVERMIB.Casconfigtable.Casconfigentry, ['casprotocol', 'casindex', 'casaddress', 'casauthenport', 'casacctport', 'caskey', 'caspriority', 'casconfigrowstatus', 'casauthenrequests', 'casauthenrequesttimeouts', 'casauthenunexpectedresponses', 'casauthenservererrorresponses', 'casauthenincorrectresponses', 'casauthenresponsetime', 'casauthentransactionsuccesses', 'casauthentransactionfailures', 'casauthorrequests', 'casauthorrequesttimeouts', 'casauthorunexpectedresponses', 'casauthorservererrorresponses', 'casauthorincorrectresponses', 'casauthorresponsetime', 'casauthortransactionsuccesses', 'casauthortransactionfailures', 'casacctrequests', 'casacctrequesttimeouts', 'casacctunexpectedresponses', 'casacctservererrorresponses', 'casacctincorrectresponses', 'casacctresponsetime', 'casaccttransactionsuccesses', 'casaccttransactionfailures', 'casstate', 'cascurrentstateduration', 'caspreviousstateduration', 'castotaldeadtime', 'casdeadcount'], name, value)

            class Casstate(Enum):
                """
                Casstate (Enum Class)

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

