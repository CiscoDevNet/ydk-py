""" INT_SERV_MIB 

The MIB module to describe the Integrated Services
Protocol

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class QosserviceEnum(Enum):
    """
    QosserviceEnum

    The class of service in use by a flow.

    .. data:: bestEffort = 1

    .. data:: guaranteedDelay = 2

    .. data:: controlledLoad = 5

    """

    bestEffort = 1

    guaranteedDelay = 2

    controlledLoad = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
        return meta._meta_table['QosserviceEnum']



class IntServMib(object):
    """
    
    
    .. attribute:: intsrvflowtable
    
    	Information describing the reserved flows  us\- ing the system's interfaces
    	**type**\:   :py:class:`Intsrvflowtable <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvflowtable>`
    
    .. attribute:: intsrvgenobjects
    
    	
    	**type**\:   :py:class:`Intsrvgenobjects <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvgenobjects>`
    
    .. attribute:: intsrvifattribtable
    
    	The reservable attributes of the system's  in\- terfaces
    	**type**\:   :py:class:`Intsrvifattribtable <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvifattribtable>`
    
    

    """

    _prefix = 'INT-SERV-MIB'
    _revision = '1997-10-03'

    def __init__(self):
        self.intsrvflowtable = IntServMib.Intsrvflowtable()
        self.intsrvflowtable.parent = self
        self.intsrvgenobjects = IntServMib.Intsrvgenobjects()
        self.intsrvgenobjects.parent = self
        self.intsrvifattribtable = IntServMib.Intsrvifattribtable()
        self.intsrvifattribtable.parent = self


    class Intsrvgenobjects(object):
        """
        
        
        .. attribute:: intsrvflownewindex
        
        	This  object  is  used  to  assign  values  to intSrvFlowNumber  as described in 'Textual Con\- ventions  for  SNMPv2'.   The  network  manager reads  the  object,  and  then writes the value back in the SET that creates a new instance  of intSrvFlowEntry.   If  the  SET  fails with the code 'inconsistentValue', then the process must be  repeated; If the SET succeeds, then the ob\- ject is incremented, and the  new  instance  is created according to the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            self.parent = None
            self.intsrvflownewindex = None

        @property
        def _common_path(self):

            return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvGenObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.intsrvflownewindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
            return meta._meta_table['IntServMib.Intsrvgenobjects']['meta_info']


    class Intsrvifattribtable(object):
        """
        The reservable attributes of the system's  in\-
        terfaces.
        
        .. attribute:: intsrvifattribentry
        
        	The reservable attributes of  a  given  inter\- face
        	**type**\: list of    :py:class:`Intsrvifattribentry <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvifattribtable.Intsrvifattribentry>`
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            self.parent = None
            self.intsrvifattribentry = YList()
            self.intsrvifattribentry.parent = self
            self.intsrvifattribentry.name = 'intsrvifattribentry'


        class Intsrvifattribentry(object):
            """
            The reservable attributes of  a  given  inter\-
            face.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: intsrvifattriballocatedbits
            
            	The number of bits/second currently  allocated to reserved sessions on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattriballocatedbuffer
            
            	The amount of buffer space  required  to  hold the simultaneous burst of all reserved flows on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: intsrvifattribflows
            
            	The number of reserved flows currently  active on  this  interface.  A flow can be created ei\- ther from a reservation protocol (such as  RSVP or ST\-II) or via configuration information
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvifattribmaxallocatedbits
            
            	The maximum number of bits/second that may  be allocated  to  reserved  sessions on the inter\- face
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattribpropagationdelay
            
            	The amount of propagation delay that this  in\- terface  introduces  in addition to that intro\- diced by bit propagation delays
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: intsrvifattribstatus
            
            	'active' on interfaces that are configured for RSVP
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'INT-SERV-MIB'
            _revision = '1997-10-03'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.intsrvifattriballocatedbits = None
                self.intsrvifattriballocatedbuffer = None
                self.intsrvifattribflows = None
                self.intsrvifattribmaxallocatedbits = None
                self.intsrvifattribpropagationdelay = None
                self.intsrvifattribstatus = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvIfAttribTable/INT-SERV-MIB:intSrvIfAttribEntry[INT-SERV-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.intsrvifattriballocatedbits is not None:
                    return True

                if self.intsrvifattriballocatedbuffer is not None:
                    return True

                if self.intsrvifattribflows is not None:
                    return True

                if self.intsrvifattribmaxallocatedbits is not None:
                    return True

                if self.intsrvifattribpropagationdelay is not None:
                    return True

                if self.intsrvifattribstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
                return meta._meta_table['IntServMib.Intsrvifattribtable.Intsrvifattribentry']['meta_info']

        @property
        def _common_path(self):

            return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvIfAttribTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.intsrvifattribentry is not None:
                for child_ref in self.intsrvifattribentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
            return meta._meta_table['IntServMib.Intsrvifattribtable']['meta_info']


    class Intsrvflowtable(object):
        """
        Information describing the reserved flows  us\-
        ing the system's interfaces.
        
        .. attribute:: intsrvflowentry
        
        	Information describing the use of a given  in\- terface   by   a   given   flow.   The  counter intSrvFlowPoliced starts counting  at  the  in\- stallation of the flow
        	**type**\: list of    :py:class:`Intsrvflowentry <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvflowtable.Intsrvflowentry>`
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            self.parent = None
            self.intsrvflowentry = YList()
            self.intsrvflowentry.parent = self
            self.intsrvflowentry.name = 'intsrvflowentry'


        class Intsrvflowentry(object):
            """
            Information describing the use of a given  in\-
            terface   by   a   given   flow.   The  counter
            intSrvFlowPoliced starts counting  at  the  in\-
            stallation of the flow.
            
            .. attribute:: intsrvflownumber  <key>
            
            	The number of this flow.  This is for SNMP In\- dexing purposes only and has no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowbesteffort
            
            	The number of packets that  were  remanded  to best effort service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowburst
            
            	The size of the largest  burst  expected  from the sender at a time.  If this is less than  the  sender's  advertised burst  size, the receiver is asking the network to provide flow pacing  beyond  what  would  be provided  under normal circumstances. Such pac\- ing is at the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: intsrvflowdestaddr
            
            	The destination address used by all senders in this  session.   This object may not be changed when the value of the RowStatus object is  'ac\- tive'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowdestaddrlength
            
            	The length of the destination address in bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowdestport
            
            	The UDP or TCP port number used as a  destina\- tion  port for all senders in this session.  If the  IP   protocol   in   use,   specified   by intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH), this  represents  a  virtual  destination  port number.   A value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowdiscard
            
            	If 'true', the flow  is  to  incur  loss  when traffic is policed.  If 'false', policed traff\- ic is treated as best effort traffic
            	**type**\:  bool
            
            .. attribute:: intsrvflowflowid
            
            	The flow ID that  this  sender  is  using,  if this  is  an IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: intsrvflowifaddr
            
            	The IP Address on the ifEntry  on  which  this reservation  exists.  This is present primarily to support those interfaces which layer  multi\- ple IP Addresses on the interface
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowinterface
            
            	The ifIndex value of the  interface  on  which this reservation exists
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: intsrvflowmaxtu
            
            	The maximum datagram size for this  flow  that will conform to the traffic specification. This value cannot exceed the MTU of the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowmintu
            
            	The minimum message size for  this  flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvfloworder
            
            	In the event of ambiguity, the order in  which the  classifier  should  make  its comparisons. The row with intSrvFlowOrder=0 is tried  first, and  comparisons  proceed  in  the order of in\- creasing value.  Non\-serial implementations  of the classifier should emulate this behavior
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: intsrvflowowner
            
            	The process that installed this  flow  in  the queue policy database
            	**type**\:   :py:class:`IntsrvflowownerEnum <ydk.models.cisco_ios_xe.INT_SERV_MIB.IntServMib.Intsrvflowtable.Intsrvflowentry.IntsrvflowownerEnum>`
            
            .. attribute:: intsrvflowpoliced
            
            	The number of packets policed since the incep\- tion of the flow's service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowport
            
            	The UDP or TCP port number used  as  a  source port  for  this sender in this session.  If the IP    protocol    in    use,    specified    by intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH), this represents a generalized  port  identifier (GPI).   A  value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowprotocol
            
            	The IP Protocol used by a session.   This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowqueue
            
            	The number of the queue used by this  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of queue identifiers
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: intsrvflowrate
            
            	The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec  rate  parameter (r).   If  this  is  a Guaranteed service flow, this rate is derived from  the  Rspec  clearing rate parameter (R)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: intsrvflowsenderaddr
            
            	The source address of the sender  selected  by this  reservation.  The value of all zeroes in\- dicates 'all senders'.  This object may not  be changed  when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowsenderaddrlength
            
            	The length of the sender's  address  in  bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowservice
            
            	The QoS service being applied to this flow
            	**type**\:   :py:class:`QosserviceEnum <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosserviceEnum>`
            
            .. attribute:: intsrvflowstatus
            
            	'active' for all active  flows.   This  object may be used to install static classifier infor\- mation, delete classifier information,  or  au\- thorize such
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: intsrvflowtype
            
            	The type of session (IP4, IP6, IP6  with  flow information, etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowweight
            
            	The weight used  to  prioritize  the  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of weighting procedures
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'INT-SERV-MIB'
            _revision = '1997-10-03'

            def __init__(self):
                self.parent = None
                self.intsrvflownumber = None
                self.intsrvflowbesteffort = None
                self.intsrvflowburst = None
                self.intsrvflowdestaddr = None
                self.intsrvflowdestaddrlength = None
                self.intsrvflowdestport = None
                self.intsrvflowdiscard = None
                self.intsrvflowflowid = None
                self.intsrvflowifaddr = None
                self.intsrvflowinterface = None
                self.intsrvflowmaxtu = None
                self.intsrvflowmintu = None
                self.intsrvfloworder = None
                self.intsrvflowowner = None
                self.intsrvflowpoliced = None
                self.intsrvflowport = None
                self.intsrvflowprotocol = None
                self.intsrvflowqueue = None
                self.intsrvflowrate = None
                self.intsrvflowsenderaddr = None
                self.intsrvflowsenderaddrlength = None
                self.intsrvflowservice = None
                self.intsrvflowstatus = None
                self.intsrvflowtype = None
                self.intsrvflowweight = None

            class IntsrvflowownerEnum(Enum):
                """
                IntsrvflowownerEnum

                The process that installed this  flow  in  the

                queue policy database.

                .. data:: other = 1

                .. data:: rsvp = 2

                .. data:: management = 3

                """

                other = 1

                rsvp = 2

                management = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
                    return meta._meta_table['IntServMib.Intsrvflowtable.Intsrvflowentry.IntsrvflowownerEnum']


            @property
            def _common_path(self):
                if self.intsrvflownumber is None:
                    raise YPYModelError('Key property intsrvflownumber is None')

                return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvFlowTable/INT-SERV-MIB:intSrvFlowEntry[INT-SERV-MIB:intSrvFlowNumber = ' + str(self.intsrvflownumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.intsrvflownumber is not None:
                    return True

                if self.intsrvflowbesteffort is not None:
                    return True

                if self.intsrvflowburst is not None:
                    return True

                if self.intsrvflowdestaddr is not None:
                    return True

                if self.intsrvflowdestaddrlength is not None:
                    return True

                if self.intsrvflowdestport is not None:
                    return True

                if self.intsrvflowdiscard is not None:
                    return True

                if self.intsrvflowflowid is not None:
                    return True

                if self.intsrvflowifaddr is not None:
                    return True

                if self.intsrvflowinterface is not None:
                    return True

                if self.intsrvflowmaxtu is not None:
                    return True

                if self.intsrvflowmintu is not None:
                    return True

                if self.intsrvfloworder is not None:
                    return True

                if self.intsrvflowowner is not None:
                    return True

                if self.intsrvflowpoliced is not None:
                    return True

                if self.intsrvflowport is not None:
                    return True

                if self.intsrvflowprotocol is not None:
                    return True

                if self.intsrvflowqueue is not None:
                    return True

                if self.intsrvflowrate is not None:
                    return True

                if self.intsrvflowsenderaddr is not None:
                    return True

                if self.intsrvflowsenderaddrlength is not None:
                    return True

                if self.intsrvflowservice is not None:
                    return True

                if self.intsrvflowstatus is not None:
                    return True

                if self.intsrvflowtype is not None:
                    return True

                if self.intsrvflowweight is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
                return meta._meta_table['IntServMib.Intsrvflowtable.Intsrvflowentry']['meta_info']

        @property
        def _common_path(self):

            return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvFlowTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.intsrvflowentry is not None:
                for child_ref in self.intsrvflowentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
            return meta._meta_table['IntServMib.Intsrvflowtable']['meta_info']

    @property
    def _common_path(self):

        return '/INT-SERV-MIB:INT-SERV-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.intsrvflowtable is not None and self.intsrvflowtable._has_data():
            return True

        if self.intsrvgenobjects is not None and self.intsrvgenobjects._has_data():
            return True

        if self.intsrvifattribtable is not None and self.intsrvifattribtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _INT_SERV_MIB as meta
        return meta._meta_table['IntServMib']['meta_info']


