""" CISCO_PPPOE_MIB 

Cisco PPPoE sessions management MIB Module.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOPPPOEMIB(object):
    """
    
    
    .. attribute:: cpppoesessionsperinterfacetable
    
    	A list of interfaces' PPPoE session information
    	**type**\: :py:class:`CPppoeSessionsPerInterfaceTable <ydk.models.pppoe.CISCO_PPPOE_MIB.CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable>`
    
    .. attribute:: cpppoesystemsessioninfo
    
    	
    	**type**\: :py:class:`CPppoeSystemSessionInfo <ydk.models.pppoe.CISCO_PPPOE_MIB.CISCOPPPOEMIB.CPppoeSystemSessionInfo>`
    
    .. attribute:: cpppoevcsessionstable
    
    	Table of configuration and statistics about the  number of PPPoE sessions on a list of VCLs(ATM  Interface Virtual Channel Link)
    	**type**\: :py:class:`CPppoeVcSessionsTable <ydk.models.pppoe.CISCO_PPPOE_MIB.CISCOPPPOEMIB.CPppoeVcSessionsTable>`
    
    

    """

    _prefix = 'cisco-pppoe'
    _revision = '2011-04-25'

    def __init__(self):
        self.cpppoesessionsperinterfacetable = CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable()
        self.cpppoesessionsperinterfacetable.parent = self
        self.cpppoesystemsessioninfo = CISCOPPPOEMIB.CPppoeSystemSessionInfo()
        self.cpppoesystemsessioninfo.parent = self
        self.cpppoevcsessionstable = CISCOPPPOEMIB.CPppoeVcSessionsTable()
        self.cpppoevcsessionstable.parent = self


    class CPppoeSessionsPerInterfaceTable(object):
        """
        A list of interfaces' PPPoE session information.
        
        .. attribute:: cpppoesessionsperinterfaceentry
        
        	An entry in the table containing PPPoE sessions  information such as count information of various  states like PPP Termination Aggregation(PTA),  Forwarded(FWDED), Transient (TRANS) and TOTAL count and  the configured loss threshold per given physical  interface
        	**type**\: list of :py:class:`CPppoeSessionsPerInterfaceEntry <ydk.models.pppoe.CISCO_PPPOE_MIB.CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry>`
        
        

        """

        _prefix = 'cisco-pppoe'
        _revision = '2011-04-25'

        def __init__(self):
            self.parent = None
            self.cpppoesessionsperinterfaceentry = YList()
            self.cpppoesessionsperinterfaceentry.parent = self
            self.cpppoesessionsperinterfaceentry.name = 'cpppoesessionsperinterfaceentry'


        class CPppoeSessionsPerInterfaceEntry(object):
            """
            An entry in the table containing PPPoE sessions 
            information such as count information of various 
            states like PPP Termination Aggregation(PTA), 
            Forwarded(FWDED), Transient (TRANS) and TOTAL count and 
            the configured loss threshold per given physical 
            interface
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpppoefwdedsessions
            
            	Number of PPPoE sessions which are in Forwarded(FWDED) state on a particular physical interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoeperinterfacesessionlosspercent
            
            	This object is used to monitor the percentage of PPPoE  sessions loss on a particular physical interface  including all of its sub\-interfaces. If during a  configured interval of time, percentage of PPPoE  sessions lost on a physical interface is above this  object value we send a trap
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoeperinterfacesessionlossthreshold
            
            	This object is used to monitor number of active PPPoE  sessions, initiated from a particular physical interface.  The sssion count is accumulation of all the pppoe session  came on a physical and its sub\-interfaces. If this count  drops below this object water mark, we expect some  problem and send out trap indicating drop of sessions  below watermark
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoeptasessions
            
            	Number of PPPoE sessions which are in PPP Termination   Aggregation(PTA) state on a particular physical  interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoetotalsessions
            
            	The total number of PPPoE sessions which includes PPP Termination Aggregation(PTA), Forwarded(FWDED) and  Transient(TRANS) state on a physical interface. 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoetranssessions
            
            	Number of PPPoE sessions which are in Transient(TRANS) state on a particular physical interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-pppoe'
            _revision = '2011-04-25'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cpppoefwdedsessions = None
                self.cpppoeperinterfacesessionlosspercent = None
                self.cpppoeperinterfacesessionlossthreshold = None
                self.cpppoeptasessions = None
                self.cpppoetotalsessions = None
                self.cpppoetranssessions = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB/CISCO-PPPOE-MIB:cPppoeSessionsPerInterfaceTable/CISCO-PPPOE-MIB:cPppoeSessionsPerInterfaceEntry[CISCO-PPPOE-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cpppoefwdedsessions is not None:
                    return True

                if self.cpppoeperinterfacesessionlosspercent is not None:
                    return True

                if self.cpppoeperinterfacesessionlossthreshold is not None:
                    return True

                if self.cpppoeptasessions is not None:
                    return True

                if self.cpppoetotalsessions is not None:
                    return True

                if self.cpppoetranssessions is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
                return meta._meta_table['CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB/CISCO-PPPOE-MIB:cPppoeSessionsPerInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpppoesessionsperinterfaceentry is not None:
                for child_ref in self.cpppoesessionsperinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
            return meta._meta_table['CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable']['meta_info']


    class CPppoeSystemSessionInfo(object):
        """
        
        
        .. attribute:: cpppoesystemcurrsessions
        
        	The current number of active PPPoE sessions within  this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystemexceededsessionerrors
        
        	The accumulated number of errors for  establishing PPPoE session in the system due  to the cPppoeSystemCurrSessions value exceeds  the cPppoeSystemMaxAllowedSessions value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystemhighwatersessions
        
        	The high water mark of the established PPPoE  sessions since the system was initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystemmaxallowedsessions
        
        	Maximum number of allowed PPPoE sessions within the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempermaciwfsessionlimit
        
        	This object provides limit on number of PPPoE sessions  with interworking flag(IWF) enabled, from a single client MAC address. If the limit is reached new session request  would be denied
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempermacsessionlimit
        
        	This object provides limit on number of PPPoE sessions for a single client Ethernet MAC address. If the limit  is reached new session request from the client would  be denied
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempermacthrottleratelimit
        
        	This object provides the rate limit at which PPPoE  session were created from a single client MAC address.  During a configured time interval, once the number of  new session requests coming from a particular client  MAC address reaches this limit, it's expected to have  delay in response for those clients
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempervclimit
        
        	This object provides limit on number of PPPoE sessions on  a particular ATM\-VC. If the limit is reached new session  request on this VC would be denied
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempervcthrottleratelimit
        
        	This object provides the rate limit at which PPPoE  session were created on an ATM\-VC. During a configured  time interval, once the number of new session requests  coming on an ATM\-VC reaches this limit, it's expected to  have delay in response for those clients on this VC
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempervlanlimit
        
        	This object provides limit on number of PPPoE sessions  on a particular Vlan. If the limit is reached new session  request on this vlan would be denied
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystempervlanthrottleratelimit
        
        	This object provides the rate limit at which PPPoE  session were created on a Vlan. During a configured time interval once the number of new session requests  coming on a particular Vlan reaches this limit,  it's expected to have delay in response for client  on this Vlan
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystemsessionlosspercent
        
        	This object is used to monitor the percentage of PPPoE  sessions going down at a configured time interval.     During a time interval if percentage of PPPoE sessions  lost, falls above this object value, we send trap  indicating loss of sessions above percentage expected
        	**type**\: int
        
        	**range:** 0..100
        
        .. attribute:: cpppoesystemsessionlossthreshold
        
        	This object is used to monitor number of active PPPoE  sessions above a healthy watermark. If number of PPPoE sessions falls below this watermark then we can expect something wrong happened.  So we send out trap to user indicating session loss below watermark
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cpppoesystemthresholdsessions
        
        	Threshold value of the established PPPoE sessions  within the system. Default value is equal to cPppoeSystemMaxSessionsConfigurable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-pppoe'
        _revision = '2011-04-25'

        def __init__(self):
            self.parent = None
            self.cpppoesystemcurrsessions = None
            self.cpppoesystemexceededsessionerrors = None
            self.cpppoesystemhighwatersessions = None
            self.cpppoesystemmaxallowedsessions = None
            self.cpppoesystempermaciwfsessionlimit = None
            self.cpppoesystempermacsessionlimit = None
            self.cpppoesystempermacthrottleratelimit = None
            self.cpppoesystempervclimit = None
            self.cpppoesystempervcthrottleratelimit = None
            self.cpppoesystempervlanlimit = None
            self.cpppoesystempervlanthrottleratelimit = None
            self.cpppoesystemsessionlosspercent = None
            self.cpppoesystemsessionlossthreshold = None
            self.cpppoesystemthresholdsessions = None

        @property
        def _common_path(self):

            return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB/CISCO-PPPOE-MIB:cPppoeSystemSessionInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpppoesystemcurrsessions is not None:
                return True

            if self.cpppoesystemexceededsessionerrors is not None:
                return True

            if self.cpppoesystemhighwatersessions is not None:
                return True

            if self.cpppoesystemmaxallowedsessions is not None:
                return True

            if self.cpppoesystempermaciwfsessionlimit is not None:
                return True

            if self.cpppoesystempermacsessionlimit is not None:
                return True

            if self.cpppoesystempermacthrottleratelimit is not None:
                return True

            if self.cpppoesystempervclimit is not None:
                return True

            if self.cpppoesystempervcthrottleratelimit is not None:
                return True

            if self.cpppoesystempervlanlimit is not None:
                return True

            if self.cpppoesystempervlanthrottleratelimit is not None:
                return True

            if self.cpppoesystemsessionlosspercent is not None:
                return True

            if self.cpppoesystemsessionlossthreshold is not None:
                return True

            if self.cpppoesystemthresholdsessions is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
            return meta._meta_table['CISCOPPPOEMIB.CPppoeSystemSessionInfo']['meta_info']


    class CPppoeVcSessionsTable(object):
        """
        Table of configuration and statistics about the 
        number of PPPoE sessions on a list of VCLs(ATM 
        Interface Virtual Channel Link).
        
        .. attribute:: cpppoevcsessionsentry
        
        	An entry in the table containing PPPoE session related information on a VCL. The entry of this table is created when the value of cPppoeVcEnable  object is set to `true` for the entry associated  VCL. The entry of this table is deleted when the of cPppoeVcEnable object set to `false` or the entry associated VCL is deleted from  atmVclTable
        	**type**\: list of :py:class:`CPppoeVcSessionsEntry <ydk.models.pppoe.CISCO_PPPOE_MIB.CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry>`
        
        

        """

        _prefix = 'cisco-pppoe'
        _revision = '2011-04-25'

        def __init__(self):
            self.parent = None
            self.cpppoevcsessionsentry = YList()
            self.cpppoevcsessionsentry.parent = self
            self.cpppoevcsessionsentry.name = 'cpppoevcsessionsentry'


        class CPppoeVcSessionsEntry(object):
            """
            An entry in the table containing PPPoE session
            related information on a VCL. The entry of this
            table is created when the value of cPppoeVcEnable 
            object is set to `true` for the entry associated 
            VCL. The entry of this table is deleted when the
            of cPppoeVcEnable object set to `false` or the
            entry associated VCL is deleted from 
            atmVclTable.
            
            .. attribute:: atmvclvci
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: atmvclvpi
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpppoevccurrsessions
            
            	The current number of active PPPoE sessions on  the VCL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoevcexceededsessionerrors
            
            	The accumulated number of errors for  establishing PPPoE session in the VC  due to the cPppoeVcCurrSessions value exceeds the cPppoeVcMaxAllowedSessions  value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoevchighwatersessions
            
            	The high water mark of the established PPPoE  sessions on the VCL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoevcmaxallowedsessions
            
            	The maximum number of allowed PPPoE sessions on  the VCL
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpppoevcthresholdsessions
            
            	The Threshold value of the established PPPoE  sessions on the VCL. Default value is equal to  cPppoeVcMaxAllowedSessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-pppoe'
            _revision = '2011-04-25'

            def __init__(self):
                self.parent = None
                self.atmvclvci = None
                self.atmvclvpi = None
                self.ifindex = None
                self.cpppoevccurrsessions = None
                self.cpppoevcexceededsessionerrors = None
                self.cpppoevchighwatersessions = None
                self.cpppoevcmaxallowedsessions = None
                self.cpppoevcthresholdsessions = None

            @property
            def _common_path(self):
                if self.atmvclvci is None:
                    raise YPYDataValidationError('Key property atmvclvci is None')
                if self.atmvclvpi is None:
                    raise YPYDataValidationError('Key property atmvclvpi is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB/CISCO-PPPOE-MIB:cPppoeVcSessionsTable/CISCO-PPPOE-MIB:cPppoeVcSessionsEntry[CISCO-PPPOE-MIB:atmVclVci = ' + str(self.atmvclvci) + '][CISCO-PPPOE-MIB:atmVclVpi = ' + str(self.atmvclvpi) + '][CISCO-PPPOE-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.atmvclvci is not None:
                    return True

                if self.atmvclvpi is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cpppoevccurrsessions is not None:
                    return True

                if self.cpppoevcexceededsessionerrors is not None:
                    return True

                if self.cpppoevchighwatersessions is not None:
                    return True

                if self.cpppoevcmaxallowedsessions is not None:
                    return True

                if self.cpppoevcthresholdsessions is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
                return meta._meta_table['CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB/CISCO-PPPOE-MIB:cPppoeVcSessionsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpppoevcsessionsentry is not None:
                for child_ref in self.cpppoevcsessionsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
            return meta._meta_table['CISCOPPPOEMIB.CPppoeVcSessionsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PPPOE-MIB:CISCO-PPPOE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cpppoesessionsperinterfacetable is not None and self.cpppoesessionsperinterfacetable._has_data():
            return True

        if self.cpppoesessionsperinterfacetable is not None and self.cpppoesessionsperinterfacetable.is_presence():
            return True

        if self.cpppoesystemsessioninfo is not None and self.cpppoesystemsessioninfo._has_data():
            return True

        if self.cpppoesystemsessioninfo is not None and self.cpppoesystemsessioninfo.is_presence():
            return True

        if self.cpppoevcsessionstable is not None and self.cpppoevcsessionstable._has_data():
            return True

        if self.cpppoevcsessionstable is not None and self.cpppoevcsessionstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.pppoe._meta import _CISCO_PPPOE_MIB as meta
        return meta._meta_table['CISCOPPPOEMIB']['meta_info']


