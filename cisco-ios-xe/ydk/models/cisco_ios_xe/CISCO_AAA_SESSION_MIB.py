""" CISCO_AAA_SESSION_MIB 

This MIB module provides data for accounting sessions
based on Authentication, Authorization, Accounting
(AAA) protocols.


References\:
    RFC 2139 RADIUS Accounting
    The TACACS+ Protocol Version 1.78, Internet Draft

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoAaaSessionMib(object):
    """
    
    
    .. attribute:: casnactive
    
    	
    	**type**\:   :py:class:`Casnactive <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactive>`
    
    .. attribute:: casnactivetable
    
    	This table contains entries for active AAA accounting sessions in the system
    	**type**\:   :py:class:`Casnactivetable <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactivetable>`
    
    .. attribute:: casngeneral
    
    	
    	**type**\:   :py:class:`Casngeneral <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casngeneral>`
    
    

    """

    _prefix = 'CISCO-AAA-SESSION-MIB'
    _revision = '2006-03-21'

    def __init__(self):
        self.casnactive = CiscoAaaSessionMib.Casnactive()
        self.casnactive.parent = self
        self.casnactivetable = CiscoAaaSessionMib.Casnactivetable()
        self.casnactivetable.parent = self
        self.casngeneral = CiscoAaaSessionMib.Casngeneral()
        self.casngeneral.parent = self


    class Casnactive(object):
        """
        
        
        .. attribute:: casnactivetableentries
        
        	Number of entries currently in casnActiveTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: casnactivetablehighwatermark
        
        	Maximum number of entries present in casnActiveTable since last system re\-initialization.  This corresponds to the maximum value reported by casnActiveTableEntries
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            self.parent = None
            self.casnactivetableentries = None
            self.casnactivetablehighwatermark = None

        @property
        def _common_path(self):

            return '/CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/CISCO-AAA-SESSION-MIB:casnActive'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.casnactivetableentries is not None:
                return True

            if self.casnactivetablehighwatermark is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_AAA_SESSION_MIB as meta
            return meta._meta_table['CiscoAaaSessionMib.Casnactive']['meta_info']


    class Casngeneral(object):
        """
        
        
        .. attribute:: casndisconnectedsessions
        
        	Total number of sessions which have been disconnected using casnDisconnect since last system re\-initialization.  This value includes any sessions still in the casnActiveTable with a casnDisconnect value of true(1) and all previous sessions which terminated as a result of setting casnDisconnect
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: casntotalsessions
        
        	Total number of sessions since last system re\-initialization.  This value includes all sessions currently in the casnActiveTable and all previous sessions whether terminated via casnDisconnect or via other mechanisms
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            self.parent = None
            self.casndisconnectedsessions = None
            self.casntotalsessions = None

        @property
        def _common_path(self):

            return '/CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/CISCO-AAA-SESSION-MIB:casnGeneral'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.casndisconnectedsessions is not None:
                return True

            if self.casntotalsessions is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_AAA_SESSION_MIB as meta
            return meta._meta_table['CiscoAaaSessionMib.Casngeneral']['meta_info']


    class Casnactivetable(object):
        """
        This table contains entries for active AAA accounting
        sessions in the system.
        
        .. attribute:: casnactiveentry
        
        	The information regarding a single accounting session.  Entries are created when a new accounting session is begun.  Entries are removed when the accounting session is ended.  Initiating termination of a session with the object casnDisconnect will cause removal of the entry when the session completes termination
        	**type**\: list of    :py:class:`Casnactiveentry <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactivetable.Casnactiveentry>`
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            self.parent = None
            self.casnactiveentry = YList()
            self.casnactiveentry.parent = self
            self.casnactiveentry.name = 'casnactiveentry'


        class Casnactiveentry(object):
            """
            The information regarding a single accounting session.
            
            Entries are created when a new accounting session
            is begun.
            
            Entries are removed when the accounting session
            is ended.
            
            Initiating termination of a session with the object
            casnDisconnect will cause removal of the entry when
            the session completes termination.
            
            .. attribute:: casnsessionid  <key>
            
            	This is the session identification used by the accounting protocol.  This value is unique to a session within the system, even if multiple accounting protocols are in use.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 44, Acct\-Session\-Id    TACACS+\: attribute 'task\_id'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: casncalltrackerid
            
            	The value of this object is the entry index in the CISCO\-CALL\-TRACKER\-MIB cctActiveTable of the call corresponding to this accounting session.  Using the value of this object to query the cctActiveTable will provide more detailed data regarding the session represented by this casnActiveEntry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casndisconnect
            
            	This object is used to terminate this session.  Setting the value to true(1) will initiate termination of this session.  The entry will be removed once the session has completed termination.  Once this object has been set to true(1), the session termination process can not be cancelled by setting the value false(2)
            	**type**\:  bool
            
            .. attribute:: casnidletime
            
            	The elapsed time that this session has been idle.  This is the time since the last user\-level data has been received or transmitted. Protocol level handshaking associated with the call is considered to be idle for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: casnipaddr
            
            	The IP address of the session or 0.0.0.0 if not applicable or unavailable.  RADIUS\:  attribute 8, Framed\-IP\-Address TACACS+\: attribute 'addr'
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: casnnasport
            
            	The value of this object identifies a particular conceptual row associated with the session identified by casnSessionId.  The conceptual row that this object points to represents a port that is used to transport a session.  If the port transporting the session cannot be determined, the value of this object will be zeroDotZero.  For example, suppose a session is established using an ATM PVC.  If the ifIndex of the ATM interface is 7, and the  VPI/VCI values of the PVC are 1, 100 respectively, then the value of this object might be as follows\:         casnNasPort.15 = atmVclAdminStatus.7.1.100                    ^                      ^ ^  ^                    \|                      \| \|  \|    casnSessionId \-\-+                      \| \|  \|          ifIndex \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  \|        atmVclVpi \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  \|        atmVclVci \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  where atmVclAdminStatus is the first accessible object of the atmVclTable of the ATM\-MIB
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: casnuserid
            
            	The User login ID or zero length string if unavailable.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 1, User\-Name    TACACS+\: attribute 'user'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: casnvaiifindex
            
            	The ifIndex of the Virtual Access Interface (VAI) that is associated with the PPP session.  This interface may not be represented in the IF\-MIB in which case the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-AAA-SESSION-MIB'
            _revision = '2006-03-21'

            def __init__(self):
                self.parent = None
                self.casnsessionid = None
                self.casncalltrackerid = None
                self.casndisconnect = None
                self.casnidletime = None
                self.casnipaddr = None
                self.casnnasport = None
                self.casnuserid = None
                self.casnvaiifindex = None

            @property
            def _common_path(self):
                if self.casnsessionid is None:
                    raise YPYModelError('Key property casnsessionid is None')

                return '/CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/CISCO-AAA-SESSION-MIB:casnActiveTable/CISCO-AAA-SESSION-MIB:casnActiveEntry[CISCO-AAA-SESSION-MIB:casnSessionId = ' + str(self.casnsessionid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.casnsessionid is not None:
                    return True

                if self.casncalltrackerid is not None:
                    return True

                if self.casndisconnect is not None:
                    return True

                if self.casnidletime is not None:
                    return True

                if self.casnipaddr is not None:
                    return True

                if self.casnnasport is not None:
                    return True

                if self.casnuserid is not None:
                    return True

                if self.casnvaiifindex is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_AAA_SESSION_MIB as meta
                return meta._meta_table['CiscoAaaSessionMib.Casnactivetable.Casnactiveentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/CISCO-AAA-SESSION-MIB:casnActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.casnactiveentry is not None:
                for child_ref in self.casnactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_AAA_SESSION_MIB as meta
            return meta._meta_table['CiscoAaaSessionMib.Casnactivetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.casnactive is not None and self.casnactive._has_data():
            return True

        if self.casnactivetable is not None and self.casnactivetable._has_data():
            return True

        if self.casngeneral is not None and self.casngeneral._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_AAA_SESSION_MIB as meta
        return meta._meta_table['CiscoAaaSessionMib']['meta_info']


