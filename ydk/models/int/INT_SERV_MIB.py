""" INT_SERV_MIB 

The MIB module to describe the Integrated Services
Protocol

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class QosService_Enum(Enum):
    """
    QosService_Enum

    The class of service in use by a flow.

    """

    BESTEFFORT = 1

    GUARANTEEDDELAY = 2

    CONTROLLEDLOAD = 5


    @staticmethod
    def _meta_info():
        from ydk.models.int._meta import _INT_SERV_MIB as meta
        return meta._meta_table['QosService_Enum']



class INTSERVMIB(object):
    """
    
    
    .. attribute:: intsrvflowtable
    
    	Information describing the reserved flows  us\- ing the system's interfaces
    	**type**\: :py:class:`IntSrvFlowTable <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable>`
    
    .. attribute:: intsrvgenobjects
    
    	
    	**type**\: :py:class:`IntSrvGenObjects <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvGenObjects>`
    
    .. attribute:: intsrvifattribtable
    
    	The reservable attributes of the system's  in\- terfaces
    	**type**\: :py:class:`IntSrvIfAttribTable <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvIfAttribTable>`
    
    

    """

    _prefix = 'int-serv'
    _revision = '1997-10-03'

    def __init__(self):
        self.intsrvflowtable = INTSERVMIB.IntSrvFlowTable()
        self.intsrvflowtable.parent = self
        self.intsrvgenobjects = INTSERVMIB.IntSrvGenObjects()
        self.intsrvgenobjects.parent = self
        self.intsrvifattribtable = INTSERVMIB.IntSrvIfAttribTable()
        self.intsrvifattribtable.parent = self


    class IntSrvFlowTable(object):
        """
        Information describing the reserved flows  us\-
        ing the system's interfaces.
        
        .. attribute:: intsrvflowentry
        
        	Information describing the use of a given  in\- terface   by   a   given   flow.   The  counter intSrvFlowPoliced starts counting  at  the  in\- stallation of the flow
        	**type**\: list of :py:class:`IntSrvFlowEntry <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry>`
        
        

        """

        _prefix = 'int-serv'
        _revision = '1997-10-03'

        def __init__(self):
            self.parent = None
            self.intsrvflowentry = YList()
            self.intsrvflowentry.parent = self
            self.intsrvflowentry.name = 'intsrvflowentry'


        class IntSrvFlowEntry(object):
            """
            Information describing the use of a given  in\-
            terface   by   a   given   flow.   The  counter
            intSrvFlowPoliced starts counting  at  the  in\-
            stallation of the flow.
            
            .. attribute:: intsrvflownumber
            
            	The number of this flow.  This is for SNMP In\- dexing purposes only and has no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowbesteffort
            
            	The number of packets that  were  remanded  to best effort service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowburst
            
            	The size of the largest  burst  expected  from the sender at a time.  If this is less than  the  sender's  advertised burst  size, the receiver is asking the network to provide flow pacing  beyond  what  would  be provided  under normal circumstances. Such pac\- ing is at the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowdestaddr
            
            	The destination address used by all senders in this  session.   This object may not be changed when the value of the RowStatus object is  'ac\- tive'
            	**type**\: str
            
            	**range:** 4..16
            
            .. attribute:: intsrvflowdestaddrlength
            
            	The length of the destination address in bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowdestport
            
            	The UDP or TCP port number used as a  destina\- tion  port for all senders in this session.  If the  IP   protocol   in   use,   specified   by intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH), this  represents  a  virtual  destination  port number.   A value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**range:** 2..4
            
            .. attribute:: intsrvflowdiscard
            
            	If 'true', the flow  is  to  incur  loss  when traffic is policed.  If 'false', policed traff\- ic is treated as best effort traffic
            	**type**\: bool
            
            .. attribute:: intsrvflowflowid
            
            	The flow ID that  this  sender  is  using,  if this  is  an IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: intsrvflowifaddr
            
            	The IP Address on the ifEntry  on  which  this reservation  exists.  This is present primarily to support those interfaces which layer  multi\- ple IP Addresses on the interface
            	**type**\: str
            
            	**range:** 4..16
            
            .. attribute:: intsrvflowinterface
            
            	The ifIndex value of the  interface  on  which this reservation exists
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: intsrvflowmaxtu
            
            	The maximum datagram size for this  flow  that will conform to the traffic specification. This value cannot exceed the MTU of the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowmintu
            
            	The minimum message size for  this  flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvfloworder
            
            	In the event of ambiguity, the order in  which the  classifier  should  make  its comparisons. The row with intSrvFlowOrder=0 is tried  first, and  comparisons  proceed  in  the order of in\- creasing value.  Non\-serial implementations  of the classifier should emulate this behavior
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: intsrvflowowner
            
            	The process that installed this  flow  in  the queue policy database
            	**type**\: :py:class:`IntSrvFlowOwner_Enum <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry.IntSrvFlowOwner_Enum>`
            
            .. attribute:: intsrvflowpoliced
            
            	The number of packets policed since the incep\- tion of the flow's service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowport
            
            	The UDP or TCP port number used  as  a  source port  for  this sender in this session.  If the IP    protocol    in    use,    specified    by intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH), this represents a generalized  port  identifier (GPI).   A  value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**range:** 2..4
            
            .. attribute:: intsrvflowprotocol
            
            	The IP Protocol used by a session.   This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowqueue
            
            	The number of the queue used by this  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of queue identifiers
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: intsrvflowrate
            
            	The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec  rate  parameter (r).   If  this  is  a Guaranteed service flow, this rate is derived from  the  Rspec  clearing rate parameter (R)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowsenderaddr
            
            	The source address of the sender  selected  by this  reservation.  The value of all zeroes in\- dicates 'all senders'.  This object may not  be changed  when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**range:** 4..16
            
            .. attribute:: intsrvflowsenderaddrlength
            
            	The length of the sender's  address  in  bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowservice
            
            	The QoS service being applied to this flow
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: intsrvflowstatus
            
            	'active' for all active  flows.   This  object may be used to install static classifier infor\- mation, delete classifier information,  or  au\- thorize such
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: intsrvflowtype
            
            	The type of session (IP4, IP6, IP6  with  flow information, etc)
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowweight
            
            	The weight used  to  prioritize  the  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of weighting procedures
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'int-serv'
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

            class IntSrvFlowOwner_Enum(Enum):
                """
                IntSrvFlowOwner_Enum

                The process that installed this  flow  in  the
                queue policy database.

                """

                OTHER = 1

                RSVP = 2

                MANAGEMENT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.int._meta import _INT_SERV_MIB as meta
                    return meta._meta_table['INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry.IntSrvFlowOwner_Enum']


            @property
            def _common_path(self):
                if self.intsrvflownumber is None:
                    raise YPYDataValidationError('Key property intsrvflownumber is None')

                return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvFlowTable/INT-SERV-MIB:intSrvFlowEntry[INT-SERV-MIB:intSrvFlowNumber = ' + str(self.intsrvflownumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.int._meta import _INT_SERV_MIB as meta
                return meta._meta_table['INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry']['meta_info']

        @property
        def _common_path(self):

            return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvFlowTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.intsrvflowentry is not None:
                for child_ref in self.intsrvflowentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.int._meta import _INT_SERV_MIB as meta
            return meta._meta_table['INTSERVMIB.IntSrvFlowTable']['meta_info']


    class IntSrvGenObjects(object):
        """
        
        
        .. attribute:: intsrvflownewindex
        
        	This  object  is  used  to  assign  values  to intSrvFlowNumber  as described in 'Textual Con\- ventions  for  SNMPv2'.   The  network  manager reads  the  object,  and  then writes the value back in the SET that creates a new instance  of intSrvFlowEntry.   If  the  SET  fails with the code 'inconsistentValue', then the process must be  repeated; If the SET succeeds, then the ob\- ject is incremented, and the  new  instance  is created according to the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'int-serv'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.intsrvflownewindex is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.int._meta import _INT_SERV_MIB as meta
            return meta._meta_table['INTSERVMIB.IntSrvGenObjects']['meta_info']


    class IntSrvIfAttribTable(object):
        """
        The reservable attributes of the system's  in\-
        terfaces.
        
        .. attribute:: intsrvifattribentry
        
        	The reservable attributes of  a  given  inter\- face
        	**type**\: list of :py:class:`IntSrvIfAttribEntry <ydk.models.int.INT_SERV_MIB.INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry>`
        
        

        """

        _prefix = 'int-serv'
        _revision = '1997-10-03'

        def __init__(self):
            self.parent = None
            self.intsrvifattribentry = YList()
            self.intsrvifattribentry.parent = self
            self.intsrvifattribentry.name = 'intsrvifattribentry'


        class IntSrvIfAttribEntry(object):
            """
            The reservable attributes of  a  given  inter\-
            face.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: intsrvifattriballocatedbits
            
            	The number of bits/second currently  allocated to reserved sessions on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvifattriballocatedbuffer
            
            	The amount of buffer space  required  to  hold the simultaneous burst of all reserved flows on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvifattribflows
            
            	The number of reserved flows currently  active on  this  interface.  A flow can be created ei\- ther from a reservation protocol (such as  RSVP or ST\-II) or via configuration information
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvifattribmaxallocatedbits
            
            	The maximum number of bits/second that may  be allocated  to  reserved  sessions on the inter\- face
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvifattribpropagationdelay
            
            	The amount of propagation delay that this  in\- terface  introduces  in addition to that intro\- diced by bit propagation delays
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: intsrvifattribstatus
            
            	'active' on interfaces that are configured for RSVP
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'int-serv'
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
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvIfAttribTable/INT-SERV-MIB:intSrvIfAttribEntry[INT-SERV-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.int._meta import _INT_SERV_MIB as meta
                return meta._meta_table['INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry']['meta_info']

        @property
        def _common_path(self):

            return '/INT-SERV-MIB:INT-SERV-MIB/INT-SERV-MIB:intSrvIfAttribTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.intsrvifattribentry is not None:
                for child_ref in self.intsrvifattribentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.int._meta import _INT_SERV_MIB as meta
            return meta._meta_table['INTSERVMIB.IntSrvIfAttribTable']['meta_info']

    @property
    def _common_path(self):

        return '/INT-SERV-MIB:INT-SERV-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.intsrvflowtable is not None and self.intsrvflowtable._has_data():
            return True

        if self.intsrvflowtable is not None and self.intsrvflowtable.is_presence():
            return True

        if self.intsrvgenobjects is not None and self.intsrvgenobjects._has_data():
            return True

        if self.intsrvgenobjects is not None and self.intsrvgenobjects.is_presence():
            return True

        if self.intsrvifattribtable is not None and self.intsrvifattribtable._has_data():
            return True

        if self.intsrvifattribtable is not None and self.intsrvifattribtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.int._meta import _INT_SERV_MIB as meta
        return meta._meta_table['INTSERVMIB']['meta_info']


