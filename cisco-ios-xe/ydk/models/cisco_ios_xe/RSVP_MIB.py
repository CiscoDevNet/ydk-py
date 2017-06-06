""" RSVP_MIB 

The MIB module to describe the RSVP Protocol

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class RsvpencapsulationEnum(Enum):
    """
    RsvpencapsulationEnum

    This indicates the encapsulation that an  RSVP

    Neighbor is perceived to be using.

    .. data:: ip = 1

    .. data:: udp = 2

    .. data:: both = 3

    """

    ip = 1

    udp = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
        return meta._meta_table['RsvpencapsulationEnum']



class RsvpMib(object):
    """
    
    
    .. attribute:: rsvpgenobjects
    
    	
    	**type**\:   :py:class:`Rsvpgenobjects <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpgenobjects>`
    
    .. attribute:: rsvpiftable
    
    	The	RSVP\-specific attributes of  the  system's interfaces
    	**type**\:   :py:class:`Rsvpiftable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpiftable>`
    
    .. attribute:: rsvpnbrtable
    
    	Information	describing  the	 Neighbors  of	an RSVP	system
    	**type**\:   :py:class:`Rsvpnbrtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpnbrtable>`
    
    .. attribute:: rsvpresvfwdtable
    
    	Information	describing the	state  information displayed upstream in RESV messages
    	**type**\:   :py:class:`Rsvpresvfwdtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvfwdtable>`
    
    .. attribute:: rsvpresvtable
    
    	Information	describing the	state  information displayed by	receivers in RESV messages
    	**type**\:   :py:class:`Rsvpresvtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvtable>`
    
    .. attribute:: rsvpsenderoutinterfacetable
    
    	List of outgoing interfaces	that PATH messages use.	 The  ifIndex  is the ifIndex value of the egress interface
    	**type**\:   :py:class:`Rsvpsenderoutinterfacetable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsenderoutinterfacetable>`
    
    .. attribute:: rsvpsendertable
    
    	Information	describing the	state  information displayed by	senders	in PATH	messages
    	**type**\:   :py:class:`Rsvpsendertable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable>`
    
    .. attribute:: rsvpsessiontable
    
    	A table  of	 all  sessions	seen  by  a  given system
    	**type**\:   :py:class:`Rsvpsessiontable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable>`
    
    

    """

    _prefix = 'RSVP-MIB'
    _revision = '1998-08-25'

    def __init__(self):
        self.rsvpgenobjects = RsvpMib.Rsvpgenobjects()
        self.rsvpgenobjects.parent = self
        self.rsvpiftable = RsvpMib.Rsvpiftable()
        self.rsvpiftable.parent = self
        self.rsvpnbrtable = RsvpMib.Rsvpnbrtable()
        self.rsvpnbrtable.parent = self
        self.rsvpresvfwdtable = RsvpMib.Rsvpresvfwdtable()
        self.rsvpresvfwdtable.parent = self
        self.rsvpresvtable = RsvpMib.Rsvpresvtable()
        self.rsvpresvtable.parent = self
        self.rsvpsenderoutinterfacetable = RsvpMib.Rsvpsenderoutinterfacetable()
        self.rsvpsenderoutinterfacetable.parent = self
        self.rsvpsendertable = RsvpMib.Rsvpsendertable()
        self.rsvpsendertable.parent = self
        self.rsvpsessiontable = RsvpMib.Rsvpsessiontable()
        self.rsvpsessiontable.parent = self


    class Rsvpgenobjects(object):
        """
        
        
        .. attribute:: rsvpbadpackets
        
        	This object	keeps a	count of the number of bad RSVP	packets	received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: rsvpresvfwdnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvFwdNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvFwdEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpresvnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvNumber   as	 described   in	  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvEntry.   If the SET fails with the code 'inconsistentValue',	then the process  must	be repeated;  If the SET succeeds, then	the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpsendernewindex
        
        	This  object  is  used  to	assign	values	to rsvpSenderNumber   as   described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSenderEntry.   If  the  SET  fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpsessionnewindex
        
        	This  object  is  used  to	assign	values	to rsvpSessionNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSessionEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpbadpackets = None
            self.rsvpresvfwdnewindex = None
            self.rsvpresvnewindex = None
            self.rsvpsendernewindex = None
            self.rsvpsessionnewindex = None

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpGenObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpbadpackets is not None:
                return True

            if self.rsvpresvfwdnewindex is not None:
                return True

            if self.rsvpresvnewindex is not None:
                return True

            if self.rsvpsendernewindex is not None:
                return True

            if self.rsvpsessionnewindex is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpgenobjects']['meta_info']


    class Rsvpsessiontable(object):
        """
        A table  of	 all  sessions	seen  by  a  given
        system.
        
        .. attribute:: rsvpsessionentry
        
        	A single session seen by a given system
        	**type**\: list of    :py:class:`Rsvpsessionentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpsessionentry = YList()
            self.rsvpsessionentry.parent = self
            self.rsvpsessionentry.name = 'rsvpsessionentry'


        class Rsvpsessionentry(object):
            """
            A single session seen by a given system.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	The	number of this session.	 This is for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsessiondestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsessiondestaddrlength
            
            	The	CIDR prefix length of the session address, which   is	32  for	 IP4  host  and	 multicast addresses, and 128  for  IP6	 addresses.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsessionport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsessionprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsessionreceivers
            
            	The	number of reservations being requested	of this	system for this	session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionrequests
            
            	The	number of reservation requests this system is sending upstream for this	session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionsenders
            
            	The	number of distinct senders currently known to be part of this session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessiontype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.rsvpsessionnumber = None
                self.rsvpsessiondestaddr = None
                self.rsvpsessiondestaddrlength = None
                self.rsvpsessionport = None
                self.rsvpsessionprotocol = None
                self.rsvpsessionreceivers = None
                self.rsvpsessionrequests = None
                self.rsvpsessionsenders = None
                self.rsvpsessiontype = None

            @property
            def _common_path(self):
                if self.rsvpsessionnumber is None:
                    raise YPYModelError('Key property rsvpsessionnumber is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSessionTable/RSVP-MIB:rsvpSessionEntry[RSVP-MIB:rsvpSessionNumber = ' + str(self.rsvpsessionnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rsvpsessionnumber is not None:
                    return True

                if self.rsvpsessiondestaddr is not None:
                    return True

                if self.rsvpsessiondestaddrlength is not None:
                    return True

                if self.rsvpsessionport is not None:
                    return True

                if self.rsvpsessionprotocol is not None:
                    return True

                if self.rsvpsessionreceivers is not None:
                    return True

                if self.rsvpsessionrequests is not None:
                    return True

                if self.rsvpsessionsenders is not None:
                    return True

                if self.rsvpsessiontype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpsessiontable.Rsvpsessionentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSessionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpsessionentry is not None:
                for child_ref in self.rsvpsessionentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpsessiontable']['meta_info']


    class Rsvpsendertable(object):
        """
        Information	describing the	state  information
        displayed by	senders	in PATH	messages.
        
        .. attribute:: rsvpsenderentry
        
        	Information	describing the	state  information displayed by	a single sender's PATH message
        	**type**\: list of    :py:class:`Rsvpsenderentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable.Rsvpsenderentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpsenderentry = YList()
            self.rsvpsenderentry.parent = self
            self.rsvpsenderentry.name = 'rsvpsenderentry'


        class Rsvpsenderentry(object):
            """
            Information	describing the	state  information
            displayed by	a single sender's PATH message.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	The	number of this sender.	This is	 for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderaddr
            
            	The	source address used by this sender in this session.   This  object may not be changed when the value of	the RowStatus object is	'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderadspecbreak
            
            	The	global break bit general  characterization parameter  from  the	ADSPEC.	 If TRUE, at least one non\-IS hop was detected in  the	path.	If FALSE, no non\-IS hops were detected
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecctrlloadbreak
            
            	If TRUE, the Controlled Load Service  fragment has its 'break' bit set, indicating that one	or more	nodes along the	path do	 not  support  the controlled	load   service.	   If  FALSE,  and rsvpSenderAdspecCtrlLoadSvc	 is   TRUE,    the 'break' bit is not set.  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns FALSE or noSuchValue
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecctrlloadhopcount
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecctrlloadminlatency
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecctrlloadmtu
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecctrlloadpathbw
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecctrlloadsvc
            
            	If TRUE, the ADSPEC	contains a Controlled Load Service  fragment.	If  FALSE, the ADSPEC does not	 contain   a   Controlled   Load   Service fragment
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecguaranteedbreak
            
            	If TRUE, the Guaranteed Service  fragment  has its	'break'	 bit  set,  indicating that one	or more	nodes along the	path do	 not  support  the guaranteed	  service.     If    FALSE,    and rsvpSenderAdspecGuaranteedSvc  is   TRUE,   the 'break' bit is not set.  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns FALSE or noSuchValue
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecguaranteedcsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'C' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedctot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'C' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'D' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteeddtot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'D' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedhopcount
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecguaranteedminlatency
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedmtu
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedpathbw
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecguaranteedsvc
            
            	If TRUE,  the  ADSPEC  contains  a	Guaranteed Service  fragment.	If  FALSE, the ADSPEC does not contain a Guaranteed Service fragment
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspechopcount
            
            	The	  hop	count	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecminlatency
            
            	The	   minimum    path     latency	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecmtu
            
            	The	composed Maximum Transmission Unit general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecpathbw
            
            	The	  path	  bandwidth    estimate	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderflowid
            
            	The	flow ID	that  this  sender  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpsenderhopaddr
            
            	The	address	used  by  the  previous	 RSVP  hop (which may be the original sender)
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderhoplih
            
            	The	 Logical  Interface  Handle  used  by  the previous  RSVP  hop	(which may be the original sender)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpsenderinterface
            
            	The	ifIndex	value of the  interface	 on  which this	PATH message was most recently received
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpsenderinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Previous Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderlastchange
            
            	The	time of	 the  last  change  in	this  PATH message;  This  is either the first time it was received or the time	of the most recent  change in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsenderpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 4..65536
            
            .. attribute:: rsvpsenderport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpSenderProtocol is 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsenderrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpsenderstatus
            
            	'active' for all active PATH  messages.   This object  may	be  used  to  install  static PATH information or delete PATH information
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: rsvpsendertspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsendertspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpSenderTSpecPeakRate  (if	 supported  by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpSenderTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpsendertype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.rsvpsessionnumber = None
                self.rsvpsendernumber = None
                self.rsvpsenderaddr = None
                self.rsvpsenderaddrlength = None
                self.rsvpsenderadspecbreak = None
                self.rsvpsenderadspecctrlloadbreak = None
                self.rsvpsenderadspecctrlloadhopcount = None
                self.rsvpsenderadspecctrlloadminlatency = None
                self.rsvpsenderadspecctrlloadmtu = None
                self.rsvpsenderadspecctrlloadpathbw = None
                self.rsvpsenderadspecctrlloadsvc = None
                self.rsvpsenderadspecguaranteedbreak = None
                self.rsvpsenderadspecguaranteedcsum = None
                self.rsvpsenderadspecguaranteedctot = None
                self.rsvpsenderadspecguaranteeddsum = None
                self.rsvpsenderadspecguaranteeddtot = None
                self.rsvpsenderadspecguaranteedhopcount = None
                self.rsvpsenderadspecguaranteedminlatency = None
                self.rsvpsenderadspecguaranteedmtu = None
                self.rsvpsenderadspecguaranteedpathbw = None
                self.rsvpsenderadspecguaranteedsvc = None
                self.rsvpsenderadspechopcount = None
                self.rsvpsenderadspecminlatency = None
                self.rsvpsenderadspecmtu = None
                self.rsvpsenderadspecpathbw = None
                self.rsvpsenderdestaddr = None
                self.rsvpsenderdestaddrlength = None
                self.rsvpsenderdestport = None
                self.rsvpsenderflowid = None
                self.rsvpsenderhopaddr = None
                self.rsvpsenderhoplih = None
                self.rsvpsenderinterface = None
                self.rsvpsenderinterval = None
                self.rsvpsenderlastchange = None
                self.rsvpsenderpolicy = None
                self.rsvpsenderport = None
                self.rsvpsenderprotocol = None
                self.rsvpsenderrsvphop = None
                self.rsvpsenderstatus = None
                self.rsvpsendertspecburst = None
                self.rsvpsendertspecmaxtu = None
                self.rsvpsendertspecmintu = None
                self.rsvpsendertspecpeakrate = None
                self.rsvpsendertspecrate = None
                self.rsvpsenderttl = None
                self.rsvpsendertype = None

            @property
            def _common_path(self):
                if self.rsvpsessionnumber is None:
                    raise YPYModelError('Key property rsvpsessionnumber is None')
                if self.rsvpsendernumber is None:
                    raise YPYModelError('Key property rsvpsendernumber is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSenderTable/RSVP-MIB:rsvpSenderEntry[RSVP-MIB:rsvpSessionNumber = ' + str(self.rsvpsessionnumber) + '][RSVP-MIB:rsvpSenderNumber = ' + str(self.rsvpsendernumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rsvpsessionnumber is not None:
                    return True

                if self.rsvpsendernumber is not None:
                    return True

                if self.rsvpsenderaddr is not None:
                    return True

                if self.rsvpsenderaddrlength is not None:
                    return True

                if self.rsvpsenderadspecbreak is not None:
                    return True

                if self.rsvpsenderadspecctrlloadbreak is not None:
                    return True

                if self.rsvpsenderadspecctrlloadhopcount is not None:
                    return True

                if self.rsvpsenderadspecctrlloadminlatency is not None:
                    return True

                if self.rsvpsenderadspecctrlloadmtu is not None:
                    return True

                if self.rsvpsenderadspecctrlloadpathbw is not None:
                    return True

                if self.rsvpsenderadspecctrlloadsvc is not None:
                    return True

                if self.rsvpsenderadspecguaranteedbreak is not None:
                    return True

                if self.rsvpsenderadspecguaranteedcsum is not None:
                    return True

                if self.rsvpsenderadspecguaranteedctot is not None:
                    return True

                if self.rsvpsenderadspecguaranteeddsum is not None:
                    return True

                if self.rsvpsenderadspecguaranteeddtot is not None:
                    return True

                if self.rsvpsenderadspecguaranteedhopcount is not None:
                    return True

                if self.rsvpsenderadspecguaranteedminlatency is not None:
                    return True

                if self.rsvpsenderadspecguaranteedmtu is not None:
                    return True

                if self.rsvpsenderadspecguaranteedpathbw is not None:
                    return True

                if self.rsvpsenderadspecguaranteedsvc is not None:
                    return True

                if self.rsvpsenderadspechopcount is not None:
                    return True

                if self.rsvpsenderadspecminlatency is not None:
                    return True

                if self.rsvpsenderadspecmtu is not None:
                    return True

                if self.rsvpsenderadspecpathbw is not None:
                    return True

                if self.rsvpsenderdestaddr is not None:
                    return True

                if self.rsvpsenderdestaddrlength is not None:
                    return True

                if self.rsvpsenderdestport is not None:
                    return True

                if self.rsvpsenderflowid is not None:
                    return True

                if self.rsvpsenderhopaddr is not None:
                    return True

                if self.rsvpsenderhoplih is not None:
                    return True

                if self.rsvpsenderinterface is not None:
                    return True

                if self.rsvpsenderinterval is not None:
                    return True

                if self.rsvpsenderlastchange is not None:
                    return True

                if self.rsvpsenderpolicy is not None:
                    return True

                if self.rsvpsenderport is not None:
                    return True

                if self.rsvpsenderprotocol is not None:
                    return True

                if self.rsvpsenderrsvphop is not None:
                    return True

                if self.rsvpsenderstatus is not None:
                    return True

                if self.rsvpsendertspecburst is not None:
                    return True

                if self.rsvpsendertspecmaxtu is not None:
                    return True

                if self.rsvpsendertspecmintu is not None:
                    return True

                if self.rsvpsendertspecpeakrate is not None:
                    return True

                if self.rsvpsendertspecrate is not None:
                    return True

                if self.rsvpsenderttl is not None:
                    return True

                if self.rsvpsendertype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpsendertable.Rsvpsenderentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSenderTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpsenderentry is not None:
                for child_ref in self.rsvpsenderentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpsendertable']['meta_info']


    class Rsvpsenderoutinterfacetable(object):
        """
        List of outgoing interfaces	that PATH messages
        use.	 The  ifIndex  is the ifIndex value of the
        egress interface.
        
        .. attribute:: rsvpsenderoutinterfaceentry
        
        	List of outgoing interfaces	that a	particular PATH	message	has
        	**type**\: list of    :py:class:`Rsvpsenderoutinterfaceentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpsenderoutinterfaceentry = YList()
            self.rsvpsenderoutinterfaceentry.parent = self
            self.rsvpsenderoutinterfaceentry.name = 'rsvpsenderoutinterfaceentry'


        class Rsvpsenderoutinterfaceentry(object):
            """
            List of outgoing interfaces	that a	particular
            PATH	message	has.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsendernumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable.Rsvpsenderentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpsenderoutinterfacestatus
            
            	'active' for all active PATH messages
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.rsvpsessionnumber = None
                self.rsvpsendernumber = None
                self.ifindex = None
                self.rsvpsenderoutinterfacestatus = None

            @property
            def _common_path(self):
                if self.rsvpsessionnumber is None:
                    raise YPYModelError('Key property rsvpsessionnumber is None')
                if self.rsvpsendernumber is None:
                    raise YPYModelError('Key property rsvpsendernumber is None')
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSenderOutInterfaceTable/RSVP-MIB:rsvpSenderOutInterfaceEntry[RSVP-MIB:rsvpSessionNumber = ' + str(self.rsvpsessionnumber) + '][RSVP-MIB:rsvpSenderNumber = ' + str(self.rsvpsendernumber) + '][RSVP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rsvpsessionnumber is not None:
                    return True

                if self.rsvpsendernumber is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.rsvpsenderoutinterfacestatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpSenderOutInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpsenderoutinterfaceentry is not None:
                for child_ref in self.rsvpsenderoutinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpsenderoutinterfacetable']['meta_info']


    class Rsvpresvtable(object):
        """
        Information	describing the	state  information
        displayed by	receivers in RESV messages.
        
        .. attribute:: rsvpresventry
        
        	Information	describing the	state  information displayed  by  a single receiver's RESV message concerning a	single sender
        	**type**\: list of    :py:class:`Rsvpresventry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvtable.Rsvpresventry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpresventry = YList()
            self.rsvpresventry.parent = self
            self.rsvpresventry.name = 'rsvpresventry'


        class Rsvpresventry(object):
            """
            Information	describing the	state  information
            displayed  by  a single receiver's RESV message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpResvProtocol,  is  50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\:  bool
            
            .. attribute:: rsvpresvflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpresvhopaddr
            
            	The	address	used by	the next RSVP  hop  (which may be the ultimate receiver)
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvhoplih
            
            	The	Logical	Interface Handle received from the previous  RSVP  hop	(which may be the ultimate receiver)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently received
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Next Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvlastchange
            
            	The	 time  of  the	 last	change	 in   this reservation	request;  This is either the first time	it was received	or the time  of	 the  most recent change in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvProtocol  is	 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpresvscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length.  If the length  is  non\-zero,	 this  contains	 a series of IP4 or IP6	addresses
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvservice
            
            	The	QoS Service  classification  requested	by the receiver
            	**type**\:   :py:class:`QosserviceEnum <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosserviceEnum>`
            
            .. attribute:: rsvpresvshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\:  bool
            
            .. attribute:: rsvpresvstatus
            
            	'active' for all active RESV  messages.   This object  may	be  used  to  install  static RESV information or delete RESV information
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: rsvpresvtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvTSpecPeakRate   (if	supported  by  the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.rsvpsessionnumber = None
                self.rsvpresvnumber = None
                self.rsvpresvdestaddr = None
                self.rsvpresvdestaddrlength = None
                self.rsvpresvdestport = None
                self.rsvpresvexplicit = None
                self.rsvpresvflowid = None
                self.rsvpresvhopaddr = None
                self.rsvpresvhoplih = None
                self.rsvpresvinterface = None
                self.rsvpresvinterval = None
                self.rsvpresvlastchange = None
                self.rsvpresvpolicy = None
                self.rsvpresvport = None
                self.rsvpresvprotocol = None
                self.rsvpresvrspecrate = None
                self.rsvpresvrspecslack = None
                self.rsvpresvrsvphop = None
                self.rsvpresvscope = None
                self.rsvpresvsenderaddr = None
                self.rsvpresvsenderaddrlength = None
                self.rsvpresvservice = None
                self.rsvpresvshared = None
                self.rsvpresvstatus = None
                self.rsvpresvtspecburst = None
                self.rsvpresvtspecmaxtu = None
                self.rsvpresvtspecmintu = None
                self.rsvpresvtspecpeakrate = None
                self.rsvpresvtspecrate = None
                self.rsvpresvttl = None
                self.rsvpresvtype = None

            @property
            def _common_path(self):
                if self.rsvpsessionnumber is None:
                    raise YPYModelError('Key property rsvpsessionnumber is None')
                if self.rsvpresvnumber is None:
                    raise YPYModelError('Key property rsvpresvnumber is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpResvTable/RSVP-MIB:rsvpResvEntry[RSVP-MIB:rsvpSessionNumber = ' + str(self.rsvpsessionnumber) + '][RSVP-MIB:rsvpResvNumber = ' + str(self.rsvpresvnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rsvpsessionnumber is not None:
                    return True

                if self.rsvpresvnumber is not None:
                    return True

                if self.rsvpresvdestaddr is not None:
                    return True

                if self.rsvpresvdestaddrlength is not None:
                    return True

                if self.rsvpresvdestport is not None:
                    return True

                if self.rsvpresvexplicit is not None:
                    return True

                if self.rsvpresvflowid is not None:
                    return True

                if self.rsvpresvhopaddr is not None:
                    return True

                if self.rsvpresvhoplih is not None:
                    return True

                if self.rsvpresvinterface is not None:
                    return True

                if self.rsvpresvinterval is not None:
                    return True

                if self.rsvpresvlastchange is not None:
                    return True

                if self.rsvpresvpolicy is not None:
                    return True

                if self.rsvpresvport is not None:
                    return True

                if self.rsvpresvprotocol is not None:
                    return True

                if self.rsvpresvrspecrate is not None:
                    return True

                if self.rsvpresvrspecslack is not None:
                    return True

                if self.rsvpresvrsvphop is not None:
                    return True

                if self.rsvpresvscope is not None:
                    return True

                if self.rsvpresvsenderaddr is not None:
                    return True

                if self.rsvpresvsenderaddrlength is not None:
                    return True

                if self.rsvpresvservice is not None:
                    return True

                if self.rsvpresvshared is not None:
                    return True

                if self.rsvpresvstatus is not None:
                    return True

                if self.rsvpresvtspecburst is not None:
                    return True

                if self.rsvpresvtspecmaxtu is not None:
                    return True

                if self.rsvpresvtspecmintu is not None:
                    return True

                if self.rsvpresvtspecpeakrate is not None:
                    return True

                if self.rsvpresvtspecrate is not None:
                    return True

                if self.rsvpresvttl is not None:
                    return True

                if self.rsvpresvtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpresvtable.Rsvpresventry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpResvTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpresventry is not None:
                for child_ref in self.rsvpresventry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpresvtable']['meta_info']


    class Rsvpresvfwdtable(object):
        """
        Information	describing the	state  information
        displayed upstream in RESV messages.
        
        .. attribute:: rsvpresvfwdentry
        
        	Information	describing the	state  information displayed   upstream	  in   an   RESV   message concerning a	single sender
        	**type**\: list of    :py:class:`Rsvpresvfwdentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpresvfwdentry = YList()
            self.rsvpresvfwdentry.parent = self
            self.rsvpresvfwdentry.name = 'rsvpresvfwdentry'


        class Rsvpresvfwdentry(object):
            """
            Information	describing the	state  information
            displayed   upstream	  in   an   RESV   message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvfwdnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwddestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwddestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwddestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by rsvpResvFwdProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpresvfwdhopaddr
            
            	The	address	of the (previous) RSVP	that  will receive this	message
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdhoplih
            
            	The	 Logical  Interface  Handle  sent  to  the (previous)	RSVP   that   will   receive  this message
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvfwdinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently sent
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvfwdinterval
            
            	The	  interval   between   refresh	  messages advertised to the Previous Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdlastchange
            
            	The	time of	the last change	in  this  request; This	 is  either  the first time it was sent	or the	time  of  the  most   recent   change	in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvfwdpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvFwdProtocol	is  50	(ESP)  or 51 (AH), this	represents a generalized  port	identifier (GPI).   A  value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdprotocol
            
            	The	IP Protocol used by a session. for  secure sessions,  this  indicates  IP  Security.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvfwdrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes per second
            
            .. attribute:: rsvpresvfwdrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvfwdrsvphop
            
            	If TRUE, the node believes that  the  next	IP hop	is  an	RSVP  hop.   If	 FALSE,	 the  node believes that the next IP hop  may  not  be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwdservice
            
            	The	QoS Service classification requested
            	**type**\:   :py:class:`QosserviceEnum <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosserviceEnum>`
            
            .. attribute:: rsvpresvfwdshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdstatus
            
            	'active' for all active RESV  messages.   This object may be used to delete	RESV information
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: rsvpresvfwdtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvfwdtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data  stream Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvFwdTSpecPeakRate  (if  supported by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvFwdTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvfwdtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.rsvpsessionnumber = None
                self.rsvpresvfwdnumber = None
                self.rsvpresvfwddestaddr = None
                self.rsvpresvfwddestaddrlength = None
                self.rsvpresvfwddestport = None
                self.rsvpresvfwdexplicit = None
                self.rsvpresvfwdflowid = None
                self.rsvpresvfwdhopaddr = None
                self.rsvpresvfwdhoplih = None
                self.rsvpresvfwdinterface = None
                self.rsvpresvfwdinterval = None
                self.rsvpresvfwdlastchange = None
                self.rsvpresvfwdpolicy = None
                self.rsvpresvfwdport = None
                self.rsvpresvfwdprotocol = None
                self.rsvpresvfwdrspecrate = None
                self.rsvpresvfwdrspecslack = None
                self.rsvpresvfwdrsvphop = None
                self.rsvpresvfwdscope = None
                self.rsvpresvfwdsenderaddr = None
                self.rsvpresvfwdsenderaddrlength = None
                self.rsvpresvfwdservice = None
                self.rsvpresvfwdshared = None
                self.rsvpresvfwdstatus = None
                self.rsvpresvfwdtspecburst = None
                self.rsvpresvfwdtspecmaxtu = None
                self.rsvpresvfwdtspecmintu = None
                self.rsvpresvfwdtspecpeakrate = None
                self.rsvpresvfwdtspecrate = None
                self.rsvpresvfwdttl = None
                self.rsvpresvfwdtype = None

            @property
            def _common_path(self):
                if self.rsvpsessionnumber is None:
                    raise YPYModelError('Key property rsvpsessionnumber is None')
                if self.rsvpresvfwdnumber is None:
                    raise YPYModelError('Key property rsvpresvfwdnumber is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpResvFwdTable/RSVP-MIB:rsvpResvFwdEntry[RSVP-MIB:rsvpSessionNumber = ' + str(self.rsvpsessionnumber) + '][RSVP-MIB:rsvpResvFwdNumber = ' + str(self.rsvpresvfwdnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rsvpsessionnumber is not None:
                    return True

                if self.rsvpresvfwdnumber is not None:
                    return True

                if self.rsvpresvfwddestaddr is not None:
                    return True

                if self.rsvpresvfwddestaddrlength is not None:
                    return True

                if self.rsvpresvfwddestport is not None:
                    return True

                if self.rsvpresvfwdexplicit is not None:
                    return True

                if self.rsvpresvfwdflowid is not None:
                    return True

                if self.rsvpresvfwdhopaddr is not None:
                    return True

                if self.rsvpresvfwdhoplih is not None:
                    return True

                if self.rsvpresvfwdinterface is not None:
                    return True

                if self.rsvpresvfwdinterval is not None:
                    return True

                if self.rsvpresvfwdlastchange is not None:
                    return True

                if self.rsvpresvfwdpolicy is not None:
                    return True

                if self.rsvpresvfwdport is not None:
                    return True

                if self.rsvpresvfwdprotocol is not None:
                    return True

                if self.rsvpresvfwdrspecrate is not None:
                    return True

                if self.rsvpresvfwdrspecslack is not None:
                    return True

                if self.rsvpresvfwdrsvphop is not None:
                    return True

                if self.rsvpresvfwdscope is not None:
                    return True

                if self.rsvpresvfwdsenderaddr is not None:
                    return True

                if self.rsvpresvfwdsenderaddrlength is not None:
                    return True

                if self.rsvpresvfwdservice is not None:
                    return True

                if self.rsvpresvfwdshared is not None:
                    return True

                if self.rsvpresvfwdstatus is not None:
                    return True

                if self.rsvpresvfwdtspecburst is not None:
                    return True

                if self.rsvpresvfwdtspecmaxtu is not None:
                    return True

                if self.rsvpresvfwdtspecmintu is not None:
                    return True

                if self.rsvpresvfwdtspecpeakrate is not None:
                    return True

                if self.rsvpresvfwdtspecrate is not None:
                    return True

                if self.rsvpresvfwdttl is not None:
                    return True

                if self.rsvpresvfwdtype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpResvFwdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpresvfwdentry is not None:
                for child_ref in self.rsvpresvfwdentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpresvfwdtable']['meta_info']


    class Rsvpiftable(object):
        """
        The	RSVP\-specific attributes of  the  system's
        interfaces.
        
        .. attribute:: rsvpifentry
        
        	The	RSVP\-specific attributes of  the  a  given interface
        	**type**\: list of    :py:class:`Rsvpifentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpiftable.Rsvpifentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpifentry = YList()
            self.rsvpifentry.parent = self
            self.rsvpifentry.name = 'rsvpifentry'


        class Rsvpifentry(object):
            """
            The	RSVP\-specific attributes of  the  a  given
            interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpifenabled
            
            	If TRUE, RSVP is enabled  on  this	Interface. If	FALSE,	 RSVP	is  not	 enabled  on  this interface
            	**type**\:  bool
            
            .. attribute:: rsvpifipnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP IP Encapsulation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifnbrs
            
            	The	number of neighbors  currently	perceived; this	 will  exceed rsvpIfIpNbrs + rsvpIfUdpNbrs by  the  number   of	  neighbors   using   both encapsulations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifrefreshblockademultiple
            
            	The	value of the RSVP value	'Kb', Which is the minimum   number   of  refresh  intervals  that blockade state will last once entered
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifrefreshinterval
            
            	The	value of the RSVP value	'R', which is  the minimum period between refresh transmissions	of a given PATH	or RESV	message	on an interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rsvpifrefreshmultiple
            
            	The	value of the RSVP value	'K', which is  the number  of  refresh intervals which must elapse (minimum) before a PATH or RESV  message  which is not being	refreshed will be aged out
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifroutedelay
            
            	The	approximate period from	the time  a  route is  changed	to  the	 time  a resulting message appears on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: hundredths	of a second
            
            .. attribute:: rsvpifstatus
            
            	'active' on	interfaces that	are configured for RSVP
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: rsvpifttl
            
            	The	value of SEND\_TTL used on  this	 interface for	messages  this node originates.	 If set	to zero, the node determines  the  TTL	via  other means
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpifudpnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP UDP Encapsulation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifudprequired
            
            	If TRUE, manual configuration forces  the  use of  UDP  encapsulation  on  the  interface.	If FALSE,  UDP	encapsulation  is  only	 used	if rsvpIfUdpNbrs is not	zero
            	**type**\:  bool
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.rsvpifenabled = None
                self.rsvpifipnbrs = None
                self.rsvpifnbrs = None
                self.rsvpifrefreshblockademultiple = None
                self.rsvpifrefreshinterval = None
                self.rsvpifrefreshmultiple = None
                self.rsvpifroutedelay = None
                self.rsvpifstatus = None
                self.rsvpifttl = None
                self.rsvpifudpnbrs = None
                self.rsvpifudprequired = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpIfTable/RSVP-MIB:rsvpIfEntry[RSVP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.rsvpifenabled is not None:
                    return True

                if self.rsvpifipnbrs is not None:
                    return True

                if self.rsvpifnbrs is not None:
                    return True

                if self.rsvpifrefreshblockademultiple is not None:
                    return True

                if self.rsvpifrefreshinterval is not None:
                    return True

                if self.rsvpifrefreshmultiple is not None:
                    return True

                if self.rsvpifroutedelay is not None:
                    return True

                if self.rsvpifstatus is not None:
                    return True

                if self.rsvpifttl is not None:
                    return True

                if self.rsvpifudpnbrs is not None:
                    return True

                if self.rsvpifudprequired is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpiftable.Rsvpifentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpifentry is not None:
                for child_ref in self.rsvpifentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpiftable']['meta_info']


    class Rsvpnbrtable(object):
        """
        Information	describing  the	 Neighbors  of	an
        RSVP	system.
        
        .. attribute:: rsvpnbrentry
        
        	Information	  describing   a    single    RSVP Neighbor
        	**type**\: list of    :py:class:`Rsvpnbrentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpnbrtable.Rsvpnbrentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            self.parent = None
            self.rsvpnbrentry = YList()
            self.rsvpnbrentry.parent = self
            self.rsvpnbrentry.name = 'rsvpnbrentry'


        class Rsvpnbrentry(object):
            """
            Information	  describing   a    single    RSVP
            Neighbor.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpnbraddress  <key>
            
            	The	IP4 or IP6 Address used	by this	 neighbor. This	 object	 may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpnbrprotocol
            
            	The	  encapsulation	  being	  used	 by   this neighbor
            	**type**\:   :py:class:`RsvpencapsulationEnum <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpencapsulationEnum>`
            
            .. attribute:: rsvpnbrstatus
            
            	'active' for all neighbors.	 This  object  may be	used   to  configure  neighbors.   In  the presence   of   configured	 neighbors,    the implementation  may	(but  is  not required to) limit the  set  of  valid  neighbors	 to  those configured
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.rsvpnbraddress = None
                self.rsvpnbrprotocol = None
                self.rsvpnbrstatus = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')
                if self.rsvpnbraddress is None:
                    raise YPYModelError('Key property rsvpnbraddress is None')

                return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpNbrTable/RSVP-MIB:rsvpNbrEntry[RSVP-MIB:ifIndex = ' + str(self.ifindex) + '][RSVP-MIB:rsvpNbrAddress = ' + str(self.rsvpnbraddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.rsvpnbraddress is not None:
                    return True

                if self.rsvpnbrprotocol is not None:
                    return True

                if self.rsvpnbrstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
                return meta._meta_table['RsvpMib.Rsvpnbrtable.Rsvpnbrentry']['meta_info']

        @property
        def _common_path(self):

            return '/RSVP-MIB:RSVP-MIB/RSVP-MIB:rsvpNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rsvpnbrentry is not None:
                for child_ref in self.rsvpnbrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
            return meta._meta_table['RsvpMib.Rsvpnbrtable']['meta_info']

    @property
    def _common_path(self):

        return '/RSVP-MIB:RSVP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.rsvpgenobjects is not None and self.rsvpgenobjects._has_data():
            return True

        if self.rsvpiftable is not None and self.rsvpiftable._has_data():
            return True

        if self.rsvpnbrtable is not None and self.rsvpnbrtable._has_data():
            return True

        if self.rsvpresvfwdtable is not None and self.rsvpresvfwdtable._has_data():
            return True

        if self.rsvpresvtable is not None and self.rsvpresvtable._has_data():
            return True

        if self.rsvpsenderoutinterfacetable is not None and self.rsvpsenderoutinterfacetable._has_data():
            return True

        if self.rsvpsendertable is not None and self.rsvpsendertable._has_data():
            return True

        if self.rsvpsessiontable is not None and self.rsvpsessiontable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _RSVP_MIB as meta
        return meta._meta_table['RsvpMib']['meta_info']


