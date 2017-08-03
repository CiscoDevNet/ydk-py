""" CISCO_AAA_SERVER_MIB 

The MIB module	for monitoring communications and status
of AAA	Server operation

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscoaaaprotocol(Enum):
    """
    Ciscoaaaprotocol

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



class CiscoAaaServerMib(Entity):
    """
    
    
    .. attribute:: casconfig
    
    	
    	**type**\:   :py:class:`Casconfig <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CiscoAaaServerMib.Casconfig>`
    
    .. attribute:: casconfigtable
    
    	This table shows current configurations for each AAA server, allows existing servers to	be removed and new ones to be created
    	**type**\:   :py:class:`Casconfigtable <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CiscoAaaServerMib.Casconfigtable>`
    
    

    """

    _prefix = 'CISCO-AAA-SERVER-MIB'
    _revision = '2003-11-17'

    def __init__(self):
        super(CiscoAaaServerMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-AAA-SERVER-MIB"
        self.yang_parent_name = "CISCO-AAA-SERVER-MIB"

        self.casconfig = CiscoAaaServerMib.Casconfig()
        self.casconfig.parent = self
        self._children_name_map["casconfig"] = "casConfig"
        self._children_yang_names.add("casConfig")

        self.casconfigtable = CiscoAaaServerMib.Casconfigtable()
        self.casconfigtable.parent = self
        self._children_name_map["casconfigtable"] = "casConfigTable"
        self._children_yang_names.add("casConfigTable")


    class Casconfig(Entity):
        """
        
        
        .. attribute:: casserverstatechangeenable
        
        	This variable controls the	generation of casServerStateChange notification.  When this variable	is true(1), generation of casServerStateChange notifications	is enabled. When this variable	is false(2), generation	of casServerStateChange notifications	is disabled.  The default value is false(2)
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CiscoAaaServerMib.Casconfig, self).__init__()

            self.yang_name = "casConfig"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"

            self.casserverstatechangeenable = YLeaf(YType.boolean, "casServerStateChangeEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("casserverstatechangeenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoAaaServerMib.Casconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAaaServerMib.Casconfig, self).__setattr__(name, value)

        def has_data(self):
            return self.casserverstatechangeenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.casserverstatechangeenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "casConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.casserverstatechangeenable.is_set or self.casserverstatechangeenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.casserverstatechangeenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "casServerStateChangeEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "casServerStateChangeEnable"):
                self.casserverstatechangeenable = value
                self.casserverstatechangeenable.value_namespace = name_space
                self.casserverstatechangeenable.value_namespace_prefix = name_space_prefix


    class Casconfigtable(Entity):
        """
        This table shows current configurations for each
        AAA server, allows existing servers to	be removed
        and new ones to be created.
        
        .. attribute:: casconfigentry
        
        	An	AAA server configuration identified by its protocol and its index.  An	entry is created/removed when a	server is defined or	undefined with IOS configuration commands via CLI or by issuing appropriate sets	to this	table using snmp.  A management station wishing to create an entry should first generate a random number to be used as the index to	this sparse table.  The	station	should then create the associated	instance of the	row status and row index objects. It	must also, either in the same or in successive PDUs, create an instance	of casAddress where casAddress is the IP	address	of the server to be added.  It	should also modify the default values for casAuthenPort, casAcctPort if the	defaults are not appropriate.  If	casKey is a zero\-length	string or is not explicitly set, then the global key will be used.	Otherwise, this	value is	used as	the key	for this server	instance.  Once the appropriate instance of all the configuration objects have been created,	either by an explicit SNMP set request or	by default, the	row status should be set to active(1) to initiate the request.  After the AAA server is made active, the entry can	not be modified \-	the only allowed operation after this is to destroy the entry by setting casConfigRowStatus to	destroy(6).  casPriority is automatically assigned once	the entry is made active and reflects the relative priority of the defined server with respect to already configured servers. Newly\-created servers will	be assigned the	lowest priority. To	reassign server	priorities to existing server entries, it	may be necessary to destroy and	recreate entries in order of	priority.  Entries in	this table with	casConfigRowStatus equal to active(1) remain in the table until destroyed.  Entries in	this table with	casConfigRowStatus equal to values other than active(1) will be destroyed after timeout (5	minutes).  If	a server address being created via SNMP	exists already in	another	active casConfigEntry, then a newly created row can not be	made active until the original row with	the with the same server address value	is destroyed.  Upon reload, casIndex values may be changed, but the priorities	that were saved	before reload will be retained, with lowest priority number corresponding to the higher priority servers
        	**type**\: list of    :py:class:`Casconfigentry <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CiscoAaaServerMib.Casconfigtable.Casconfigentry>`
        
        

        """

        _prefix = 'CISCO-AAA-SERVER-MIB'
        _revision = '2003-11-17'

        def __init__(self):
            super(CiscoAaaServerMib.Casconfigtable, self).__init__()

            self.yang_name = "casConfigTable"
            self.yang_parent_name = "CISCO-AAA-SERVER-MIB"

            self.casconfigentry = YList(self)

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
                        super(CiscoAaaServerMib.Casconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAaaServerMib.Casconfigtable, self).__setattr__(name, value)


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
            
            .. attribute:: casprotocol  <key>
            
            	The variable denotes the protocol used by the managed device with the AAA server corresponding to  this entry in the table
            	**type**\:   :py:class:`Ciscoaaaprotocol <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.Ciscoaaaprotocol>`
            
            .. attribute:: casindex  <key>
            
            	A management station wishing to initiate a	new AAA	server configuration should use a	random value for this object when creating an instance of casConfigEntry.  The RowStatus semantics of	the casConfigRowStatus object will prevent access conflicts.  If	the randomly chosen casIndex value for row creation is	already	in use by an existing entry, snmp set to the casIndex value will fail
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: casacctincorrectresponses
            
            	The number	of accounting responses	which could not be	processed since	system re\-initialization.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctport
            
            	UDP/TCP port used for accounting service in the configuration  For TACACS+, the value of casAcctPort is ignored. casAuthenPort will	be used	instead.  Default value is the IOS default for radius\: 1646
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: casacctrequests
            
            	The number	of accounting requests sent to this server since system re\-initialization.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctrequesttimeouts
            
            	The number	of accounting requests which have timed out since system re\-initialization.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctresponsetime
            
            	Average response time for accounting requests sent to	this server,, since system re\-initialization excluding timeouts
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: casacctservererrorresponses
            
            	The number	of server ERROR	accounting responses received from this server since system re\-initialization.  These are responses indicating that the server itself has identified an error with its accounting operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casaccttransactionfailures
            
            	The number	of accounting transactions with	this server which failed since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casaccttransactionsuccesses
            
            	The number	of accounting transactions with	this server which succeeded since system re\-initialization.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an accounting pass or fail
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casacctunexpectedresponses
            
            	The number	of unexpected accounting responses received from this server since system re\-initialization.  An	example	is a delayed response to a request which had already timed out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casaddress
            
            	The IP address of the server
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: casauthenincorrectresponses
            
            	The number	of authentication responses which could	not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenport
            
            	UDP/TCP port used for authentication in the configuration  For TACACS+, this object should be	explictly set.  Default value is the IOS default for radius\: 1645
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: casauthenrequests
            
            	The number	of authentication requests sent	to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenrequesttimeouts
            
            	The number	of authentication requests which have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenresponsetime
            
            	Average response time for authentication requests sent to	this server, excluding timeouts, since system re\-initialization
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: casauthenservererrorresponses
            
            	The number	of server ERROR	authentication responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authentication operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthentransactionfailures
            
            	The number	of authentication transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthentransactionsuccesses
            
            	The number	of authentication transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authentication pass	or fail
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthenunexpectedresponses
            
            	The number	of unexpected authentication responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorincorrectresponses
            
            	The number	of authorization responses which could not be	processed since	it is made active.  Reasons include inability to decrypt the response, invalid fields, or	the response is	not valid based	on the request.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorrequests
            
            	The number	of authorization requests sent to this server since it is made active.  Retransmissions due to request timeouts are counted as	distinct requests.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorrequesttimeouts
            
            	The number	of authorization requests which	have timed out since it	is made	active.  A timeout results in a retransmission of the request If	the maximum number of attempts has been	reached, no	further	retransmissions	will be	attempted.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorresponsetime
            
            	Average response time for authorization requests sent to	this server, excluding timeouts, since system re\-initialization.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: casauthorservererrorresponses
            
            	The number	of server ERROR	authorization responses received from this	server since it	is made	active.  These are responses indicating that the server itself has identified an error with its authorization operation.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthortransactionfailures
            
            	The number	of authorization transactions with this server which failed since it is made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction failure occurs if maximum resends have been met or the server aborts the transaction.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthortransactionsuccesses
            
            	The number	of authorization transactions with this server which succeeded since it is	made active.  A transaction may include multiple	request retransmissions if	timeouts occur.  A transaction is successful if the	server responds with either an authorization pass or fail.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casauthorunexpectedresponses
            
            	The number	of unexpected authorization responses received from this server since it is made active.  An	example	is a delayed response to a request which had already timed out.  This object is not	instantiated for protocols which do not support a distinct authorization function
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casconfigrowstatus
            
            	The status of this table entry.  Once the entry status	is set to	active,	the associated entry cannot be modified except	destroyed by setting this object to destroy(6)
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cascurrentstateduration
            
            	This object provides the elapsed time the server has been in its current state as shown	in casState
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: casdeadcount
            
            	The number	of times this server's casState	has transitioned to 'dead(2)' since system re\-initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: caskey
            
            	The server key	to be used with	this server.  Retrieving the	value of this object via SNMP will return	an empty string	for security reasons
            	**type**\:  str
            
            .. attribute:: caspreviousstateduration
            
            	This object provides the elapsed time the server was been in its previous state	prior to the most recent transistion of casState.  This value	is zero	if the server has not changed state
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: caspriority
            
            	A number that indicates the priority of the server	in this entry.  Lower	numbers	indicate higher	priority
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: casstate
            
            	Current state of this server.  up(1)	 \- Server responding to	requests  dead(2) \- Server failed to respond  A server is marked	dead if	it does	not respond after maximum retransmissions.  A server is marked	up again either	after a	waiting period or if some response	is received from it.  The initial value of casState is 'up(1)' at system re\-initialization.	This will only transistion to 'dead(2)' if	an attempt to communicate fails
            	**type**\:   :py:class:`Casstate <ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB.CiscoAaaServerMib.Casconfigtable.Casconfigentry.Casstate>`
            
            .. attribute:: castotaldeadtime
            
            	The total elapsed time this server's casState has had the value 'dead(2)' since system re\-initialization
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-AAA-SERVER-MIB'
            _revision = '2003-11-17'

            def __init__(self):
                super(CiscoAaaServerMib.Casconfigtable.Casconfigentry, self).__init__()

                self.yang_name = "casConfigEntry"
                self.yang_parent_name = "casConfigTable"

                self.casprotocol = YLeaf(YType.enumeration, "casProtocol")

                self.casindex = YLeaf(YType.uint32, "casIndex")

                self.casacctincorrectresponses = YLeaf(YType.uint32, "casAcctIncorrectResponses")

                self.casacctport = YLeaf(YType.int32, "casAcctPort")

                self.casacctrequests = YLeaf(YType.uint32, "casAcctRequests")

                self.casacctrequesttimeouts = YLeaf(YType.uint32, "casAcctRequestTimeouts")

                self.casacctresponsetime = YLeaf(YType.int32, "casAcctResponseTime")

                self.casacctservererrorresponses = YLeaf(YType.uint32, "casAcctServerErrorResponses")

                self.casaccttransactionfailures = YLeaf(YType.uint32, "casAcctTransactionFailures")

                self.casaccttransactionsuccesses = YLeaf(YType.uint32, "casAcctTransactionSuccesses")

                self.casacctunexpectedresponses = YLeaf(YType.uint32, "casAcctUnexpectedResponses")

                self.casaddress = YLeaf(YType.str, "casAddress")

                self.casauthenincorrectresponses = YLeaf(YType.uint32, "casAuthenIncorrectResponses")

                self.casauthenport = YLeaf(YType.int32, "casAuthenPort")

                self.casauthenrequests = YLeaf(YType.uint32, "casAuthenRequests")

                self.casauthenrequesttimeouts = YLeaf(YType.uint32, "casAuthenRequestTimeouts")

                self.casauthenresponsetime = YLeaf(YType.int32, "casAuthenResponseTime")

                self.casauthenservererrorresponses = YLeaf(YType.uint32, "casAuthenServerErrorResponses")

                self.casauthentransactionfailures = YLeaf(YType.uint32, "casAuthenTransactionFailures")

                self.casauthentransactionsuccesses = YLeaf(YType.uint32, "casAuthenTransactionSuccesses")

                self.casauthenunexpectedresponses = YLeaf(YType.uint32, "casAuthenUnexpectedResponses")

                self.casauthorincorrectresponses = YLeaf(YType.uint32, "casAuthorIncorrectResponses")

                self.casauthorrequests = YLeaf(YType.uint32, "casAuthorRequests")

                self.casauthorrequesttimeouts = YLeaf(YType.uint32, "casAuthorRequestTimeouts")

                self.casauthorresponsetime = YLeaf(YType.int32, "casAuthorResponseTime")

                self.casauthorservererrorresponses = YLeaf(YType.uint32, "casAuthorServerErrorResponses")

                self.casauthortransactionfailures = YLeaf(YType.uint32, "casAuthorTransactionFailures")

                self.casauthortransactionsuccesses = YLeaf(YType.uint32, "casAuthorTransactionSuccesses")

                self.casauthorunexpectedresponses = YLeaf(YType.uint32, "casAuthorUnexpectedResponses")

                self.casconfigrowstatus = YLeaf(YType.enumeration, "casConfigRowStatus")

                self.cascurrentstateduration = YLeaf(YType.int32, "casCurrentStateDuration")

                self.casdeadcount = YLeaf(YType.uint32, "casDeadCount")

                self.caskey = YLeaf(YType.str, "casKey")

                self.caspreviousstateduration = YLeaf(YType.int32, "casPreviousStateDuration")

                self.caspriority = YLeaf(YType.uint32, "casPriority")

                self.casstate = YLeaf(YType.enumeration, "casState")

                self.castotaldeadtime = YLeaf(YType.int32, "casTotalDeadTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("casprotocol",
                                "casindex",
                                "casacctincorrectresponses",
                                "casacctport",
                                "casacctrequests",
                                "casacctrequesttimeouts",
                                "casacctresponsetime",
                                "casacctservererrorresponses",
                                "casaccttransactionfailures",
                                "casaccttransactionsuccesses",
                                "casacctunexpectedresponses",
                                "casaddress",
                                "casauthenincorrectresponses",
                                "casauthenport",
                                "casauthenrequests",
                                "casauthenrequesttimeouts",
                                "casauthenresponsetime",
                                "casauthenservererrorresponses",
                                "casauthentransactionfailures",
                                "casauthentransactionsuccesses",
                                "casauthenunexpectedresponses",
                                "casauthorincorrectresponses",
                                "casauthorrequests",
                                "casauthorrequesttimeouts",
                                "casauthorresponsetime",
                                "casauthorservererrorresponses",
                                "casauthortransactionfailures",
                                "casauthortransactionsuccesses",
                                "casauthorunexpectedresponses",
                                "casconfigrowstatus",
                                "cascurrentstateduration",
                                "casdeadcount",
                                "caskey",
                                "caspreviousstateduration",
                                "caspriority",
                                "casstate",
                                "castotaldeadtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAaaServerMib.Casconfigtable.Casconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAaaServerMib.Casconfigtable.Casconfigentry, self).__setattr__(name, value)

            class Casstate(Enum):
                """
                Casstate

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


            def has_data(self):
                return (
                    self.casprotocol.is_set or
                    self.casindex.is_set or
                    self.casacctincorrectresponses.is_set or
                    self.casacctport.is_set or
                    self.casacctrequests.is_set or
                    self.casacctrequesttimeouts.is_set or
                    self.casacctresponsetime.is_set or
                    self.casacctservererrorresponses.is_set or
                    self.casaccttransactionfailures.is_set or
                    self.casaccttransactionsuccesses.is_set or
                    self.casacctunexpectedresponses.is_set or
                    self.casaddress.is_set or
                    self.casauthenincorrectresponses.is_set or
                    self.casauthenport.is_set or
                    self.casauthenrequests.is_set or
                    self.casauthenrequesttimeouts.is_set or
                    self.casauthenresponsetime.is_set or
                    self.casauthenservererrorresponses.is_set or
                    self.casauthentransactionfailures.is_set or
                    self.casauthentransactionsuccesses.is_set or
                    self.casauthenunexpectedresponses.is_set or
                    self.casauthorincorrectresponses.is_set or
                    self.casauthorrequests.is_set or
                    self.casauthorrequesttimeouts.is_set or
                    self.casauthorresponsetime.is_set or
                    self.casauthorservererrorresponses.is_set or
                    self.casauthortransactionfailures.is_set or
                    self.casauthortransactionsuccesses.is_set or
                    self.casauthorunexpectedresponses.is_set or
                    self.casconfigrowstatus.is_set or
                    self.cascurrentstateduration.is_set or
                    self.casdeadcount.is_set or
                    self.caskey.is_set or
                    self.caspreviousstateduration.is_set or
                    self.caspriority.is_set or
                    self.casstate.is_set or
                    self.castotaldeadtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.casprotocol.yfilter != YFilter.not_set or
                    self.casindex.yfilter != YFilter.not_set or
                    self.casacctincorrectresponses.yfilter != YFilter.not_set or
                    self.casacctport.yfilter != YFilter.not_set or
                    self.casacctrequests.yfilter != YFilter.not_set or
                    self.casacctrequesttimeouts.yfilter != YFilter.not_set or
                    self.casacctresponsetime.yfilter != YFilter.not_set or
                    self.casacctservererrorresponses.yfilter != YFilter.not_set or
                    self.casaccttransactionfailures.yfilter != YFilter.not_set or
                    self.casaccttransactionsuccesses.yfilter != YFilter.not_set or
                    self.casacctunexpectedresponses.yfilter != YFilter.not_set or
                    self.casaddress.yfilter != YFilter.not_set or
                    self.casauthenincorrectresponses.yfilter != YFilter.not_set or
                    self.casauthenport.yfilter != YFilter.not_set or
                    self.casauthenrequests.yfilter != YFilter.not_set or
                    self.casauthenrequesttimeouts.yfilter != YFilter.not_set or
                    self.casauthenresponsetime.yfilter != YFilter.not_set or
                    self.casauthenservererrorresponses.yfilter != YFilter.not_set or
                    self.casauthentransactionfailures.yfilter != YFilter.not_set or
                    self.casauthentransactionsuccesses.yfilter != YFilter.not_set or
                    self.casauthenunexpectedresponses.yfilter != YFilter.not_set or
                    self.casauthorincorrectresponses.yfilter != YFilter.not_set or
                    self.casauthorrequests.yfilter != YFilter.not_set or
                    self.casauthorrequesttimeouts.yfilter != YFilter.not_set or
                    self.casauthorresponsetime.yfilter != YFilter.not_set or
                    self.casauthorservererrorresponses.yfilter != YFilter.not_set or
                    self.casauthortransactionfailures.yfilter != YFilter.not_set or
                    self.casauthortransactionsuccesses.yfilter != YFilter.not_set or
                    self.casauthorunexpectedresponses.yfilter != YFilter.not_set or
                    self.casconfigrowstatus.yfilter != YFilter.not_set or
                    self.cascurrentstateduration.yfilter != YFilter.not_set or
                    self.casdeadcount.yfilter != YFilter.not_set or
                    self.caskey.yfilter != YFilter.not_set or
                    self.caspreviousstateduration.yfilter != YFilter.not_set or
                    self.caspriority.yfilter != YFilter.not_set or
                    self.casstate.yfilter != YFilter.not_set or
                    self.castotaldeadtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "casConfigEntry" + "[casProtocol='" + self.casprotocol.get() + "']" + "[casIndex='" + self.casindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/casConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.casprotocol.is_set or self.casprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casprotocol.get_name_leafdata())
                if (self.casindex.is_set or self.casindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casindex.get_name_leafdata())
                if (self.casacctincorrectresponses.is_set or self.casacctincorrectresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctincorrectresponses.get_name_leafdata())
                if (self.casacctport.is_set or self.casacctport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctport.get_name_leafdata())
                if (self.casacctrequests.is_set or self.casacctrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctrequests.get_name_leafdata())
                if (self.casacctrequesttimeouts.is_set or self.casacctrequesttimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctrequesttimeouts.get_name_leafdata())
                if (self.casacctresponsetime.is_set or self.casacctresponsetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctresponsetime.get_name_leafdata())
                if (self.casacctservererrorresponses.is_set or self.casacctservererrorresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctservererrorresponses.get_name_leafdata())
                if (self.casaccttransactionfailures.is_set or self.casaccttransactionfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casaccttransactionfailures.get_name_leafdata())
                if (self.casaccttransactionsuccesses.is_set or self.casaccttransactionsuccesses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casaccttransactionsuccesses.get_name_leafdata())
                if (self.casacctunexpectedresponses.is_set or self.casacctunexpectedresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casacctunexpectedresponses.get_name_leafdata())
                if (self.casaddress.is_set or self.casaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casaddress.get_name_leafdata())
                if (self.casauthenincorrectresponses.is_set or self.casauthenincorrectresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenincorrectresponses.get_name_leafdata())
                if (self.casauthenport.is_set or self.casauthenport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenport.get_name_leafdata())
                if (self.casauthenrequests.is_set or self.casauthenrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenrequests.get_name_leafdata())
                if (self.casauthenrequesttimeouts.is_set or self.casauthenrequesttimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenrequesttimeouts.get_name_leafdata())
                if (self.casauthenresponsetime.is_set or self.casauthenresponsetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenresponsetime.get_name_leafdata())
                if (self.casauthenservererrorresponses.is_set or self.casauthenservererrorresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenservererrorresponses.get_name_leafdata())
                if (self.casauthentransactionfailures.is_set or self.casauthentransactionfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthentransactionfailures.get_name_leafdata())
                if (self.casauthentransactionsuccesses.is_set or self.casauthentransactionsuccesses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthentransactionsuccesses.get_name_leafdata())
                if (self.casauthenunexpectedresponses.is_set or self.casauthenunexpectedresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthenunexpectedresponses.get_name_leafdata())
                if (self.casauthorincorrectresponses.is_set or self.casauthorincorrectresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorincorrectresponses.get_name_leafdata())
                if (self.casauthorrequests.is_set or self.casauthorrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorrequests.get_name_leafdata())
                if (self.casauthorrequesttimeouts.is_set or self.casauthorrequesttimeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorrequesttimeouts.get_name_leafdata())
                if (self.casauthorresponsetime.is_set or self.casauthorresponsetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorresponsetime.get_name_leafdata())
                if (self.casauthorservererrorresponses.is_set or self.casauthorservererrorresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorservererrorresponses.get_name_leafdata())
                if (self.casauthortransactionfailures.is_set or self.casauthortransactionfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthortransactionfailures.get_name_leafdata())
                if (self.casauthortransactionsuccesses.is_set or self.casauthortransactionsuccesses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthortransactionsuccesses.get_name_leafdata())
                if (self.casauthorunexpectedresponses.is_set or self.casauthorunexpectedresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casauthorunexpectedresponses.get_name_leafdata())
                if (self.casconfigrowstatus.is_set or self.casconfigrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casconfigrowstatus.get_name_leafdata())
                if (self.cascurrentstateduration.is_set or self.cascurrentstateduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cascurrentstateduration.get_name_leafdata())
                if (self.casdeadcount.is_set or self.casdeadcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casdeadcount.get_name_leafdata())
                if (self.caskey.is_set or self.caskey.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caskey.get_name_leafdata())
                if (self.caspreviousstateduration.is_set or self.caspreviousstateduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caspreviousstateduration.get_name_leafdata())
                if (self.caspriority.is_set or self.caspriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.caspriority.get_name_leafdata())
                if (self.casstate.is_set or self.casstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casstate.get_name_leafdata())
                if (self.castotaldeadtime.is_set or self.castotaldeadtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.castotaldeadtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "casProtocol" or name == "casIndex" or name == "casAcctIncorrectResponses" or name == "casAcctPort" or name == "casAcctRequests" or name == "casAcctRequestTimeouts" or name == "casAcctResponseTime" or name == "casAcctServerErrorResponses" or name == "casAcctTransactionFailures" or name == "casAcctTransactionSuccesses" or name == "casAcctUnexpectedResponses" or name == "casAddress" or name == "casAuthenIncorrectResponses" or name == "casAuthenPort" or name == "casAuthenRequests" or name == "casAuthenRequestTimeouts" or name == "casAuthenResponseTime" or name == "casAuthenServerErrorResponses" or name == "casAuthenTransactionFailures" or name == "casAuthenTransactionSuccesses" or name == "casAuthenUnexpectedResponses" or name == "casAuthorIncorrectResponses" or name == "casAuthorRequests" or name == "casAuthorRequestTimeouts" or name == "casAuthorResponseTime" or name == "casAuthorServerErrorResponses" or name == "casAuthorTransactionFailures" or name == "casAuthorTransactionSuccesses" or name == "casAuthorUnexpectedResponses" or name == "casConfigRowStatus" or name == "casCurrentStateDuration" or name == "casDeadCount" or name == "casKey" or name == "casPreviousStateDuration" or name == "casPriority" or name == "casState" or name == "casTotalDeadTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "casProtocol"):
                    self.casprotocol = value
                    self.casprotocol.value_namespace = name_space
                    self.casprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "casIndex"):
                    self.casindex = value
                    self.casindex.value_namespace = name_space
                    self.casindex.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctIncorrectResponses"):
                    self.casacctincorrectresponses = value
                    self.casacctincorrectresponses.value_namespace = name_space
                    self.casacctincorrectresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctPort"):
                    self.casacctport = value
                    self.casacctport.value_namespace = name_space
                    self.casacctport.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctRequests"):
                    self.casacctrequests = value
                    self.casacctrequests.value_namespace = name_space
                    self.casacctrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctRequestTimeouts"):
                    self.casacctrequesttimeouts = value
                    self.casacctrequesttimeouts.value_namespace = name_space
                    self.casacctrequesttimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctResponseTime"):
                    self.casacctresponsetime = value
                    self.casacctresponsetime.value_namespace = name_space
                    self.casacctresponsetime.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctServerErrorResponses"):
                    self.casacctservererrorresponses = value
                    self.casacctservererrorresponses.value_namespace = name_space
                    self.casacctservererrorresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctTransactionFailures"):
                    self.casaccttransactionfailures = value
                    self.casaccttransactionfailures.value_namespace = name_space
                    self.casaccttransactionfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctTransactionSuccesses"):
                    self.casaccttransactionsuccesses = value
                    self.casaccttransactionsuccesses.value_namespace = name_space
                    self.casaccttransactionsuccesses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAcctUnexpectedResponses"):
                    self.casacctunexpectedresponses = value
                    self.casacctunexpectedresponses.value_namespace = name_space
                    self.casacctunexpectedresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAddress"):
                    self.casaddress = value
                    self.casaddress.value_namespace = name_space
                    self.casaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenIncorrectResponses"):
                    self.casauthenincorrectresponses = value
                    self.casauthenincorrectresponses.value_namespace = name_space
                    self.casauthenincorrectresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenPort"):
                    self.casauthenport = value
                    self.casauthenport.value_namespace = name_space
                    self.casauthenport.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenRequests"):
                    self.casauthenrequests = value
                    self.casauthenrequests.value_namespace = name_space
                    self.casauthenrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenRequestTimeouts"):
                    self.casauthenrequesttimeouts = value
                    self.casauthenrequesttimeouts.value_namespace = name_space
                    self.casauthenrequesttimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenResponseTime"):
                    self.casauthenresponsetime = value
                    self.casauthenresponsetime.value_namespace = name_space
                    self.casauthenresponsetime.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenServerErrorResponses"):
                    self.casauthenservererrorresponses = value
                    self.casauthenservererrorresponses.value_namespace = name_space
                    self.casauthenservererrorresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenTransactionFailures"):
                    self.casauthentransactionfailures = value
                    self.casauthentransactionfailures.value_namespace = name_space
                    self.casauthentransactionfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenTransactionSuccesses"):
                    self.casauthentransactionsuccesses = value
                    self.casauthentransactionsuccesses.value_namespace = name_space
                    self.casauthentransactionsuccesses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthenUnexpectedResponses"):
                    self.casauthenunexpectedresponses = value
                    self.casauthenunexpectedresponses.value_namespace = name_space
                    self.casauthenunexpectedresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorIncorrectResponses"):
                    self.casauthorincorrectresponses = value
                    self.casauthorincorrectresponses.value_namespace = name_space
                    self.casauthorincorrectresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorRequests"):
                    self.casauthorrequests = value
                    self.casauthorrequests.value_namespace = name_space
                    self.casauthorrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorRequestTimeouts"):
                    self.casauthorrequesttimeouts = value
                    self.casauthorrequesttimeouts.value_namespace = name_space
                    self.casauthorrequesttimeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorResponseTime"):
                    self.casauthorresponsetime = value
                    self.casauthorresponsetime.value_namespace = name_space
                    self.casauthorresponsetime.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorServerErrorResponses"):
                    self.casauthorservererrorresponses = value
                    self.casauthorservererrorresponses.value_namespace = name_space
                    self.casauthorservererrorresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorTransactionFailures"):
                    self.casauthortransactionfailures = value
                    self.casauthortransactionfailures.value_namespace = name_space
                    self.casauthortransactionfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorTransactionSuccesses"):
                    self.casauthortransactionsuccesses = value
                    self.casauthortransactionsuccesses.value_namespace = name_space
                    self.casauthortransactionsuccesses.value_namespace_prefix = name_space_prefix
                if(value_path == "casAuthorUnexpectedResponses"):
                    self.casauthorunexpectedresponses = value
                    self.casauthorunexpectedresponses.value_namespace = name_space
                    self.casauthorunexpectedresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "casConfigRowStatus"):
                    self.casconfigrowstatus = value
                    self.casconfigrowstatus.value_namespace = name_space
                    self.casconfigrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "casCurrentStateDuration"):
                    self.cascurrentstateduration = value
                    self.cascurrentstateduration.value_namespace = name_space
                    self.cascurrentstateduration.value_namespace_prefix = name_space_prefix
                if(value_path == "casDeadCount"):
                    self.casdeadcount = value
                    self.casdeadcount.value_namespace = name_space
                    self.casdeadcount.value_namespace_prefix = name_space_prefix
                if(value_path == "casKey"):
                    self.caskey = value
                    self.caskey.value_namespace = name_space
                    self.caskey.value_namespace_prefix = name_space_prefix
                if(value_path == "casPreviousStateDuration"):
                    self.caspreviousstateduration = value
                    self.caspreviousstateduration.value_namespace = name_space
                    self.caspreviousstateduration.value_namespace_prefix = name_space_prefix
                if(value_path == "casPriority"):
                    self.caspriority = value
                    self.caspriority.value_namespace = name_space
                    self.caspriority.value_namespace_prefix = name_space_prefix
                if(value_path == "casState"):
                    self.casstate = value
                    self.casstate.value_namespace = name_space
                    self.casstate.value_namespace_prefix = name_space_prefix
                if(value_path == "casTotalDeadTime"):
                    self.castotaldeadtime = value
                    self.castotaldeadtime.value_namespace = name_space
                    self.castotaldeadtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.casconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.casconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "casConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "casConfigEntry"):
                for c in self.casconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAaaServerMib.Casconfigtable.Casconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.casconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "casConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.casconfig is not None and self.casconfig.has_data()) or
            (self.casconfigtable is not None and self.casconfigtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.casconfig is not None and self.casconfig.has_operation()) or
            (self.casconfigtable is not None and self.casconfigtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-AAA-SERVER-MIB:CISCO-AAA-SERVER-MIB" + path_buffer

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

        if (child_yang_name == "casConfig"):
            if (self.casconfig is None):
                self.casconfig = CiscoAaaServerMib.Casconfig()
                self.casconfig.parent = self
                self._children_name_map["casconfig"] = "casConfig"
            return self.casconfig

        if (child_yang_name == "casConfigTable"):
            if (self.casconfigtable is None):
                self.casconfigtable = CiscoAaaServerMib.Casconfigtable()
                self.casconfigtable.parent = self
                self._children_name_map["casconfigtable"] = "casConfigTable"
            return self.casconfigtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "casConfig" or name == "casConfigTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoAaaServerMib()
        return self._top_entity

