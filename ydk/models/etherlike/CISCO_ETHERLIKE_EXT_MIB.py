""" CISCO_ETHERLIKE_EXT_MIB 

The MIB module to describe generic objects for
ethernet\-like network interfaces. 

This MIB provides ethernet\-like network interfaces 
information that are either excluded by EtherLike\-MIB 
or specific to Cisco products.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class CISCOETHERLIKEEXTMIB(object):
    """
    
    
    .. attribute:: ceedot3pauseexttable
    
    	A list of additional descriptive and status information about the MAC Control PAUSE  function on the ethernet\-like interfaces  attached to a particular system, in extension to dot3PauseTable in EtherLike\-MIB. There will be  one row in this table for each ethernet\-like  interface in the system which supports the MAC  Control PAUSE function
    	**type**\: :py:class:`CeeDot3PauseExtTable <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable>`
    
    .. attribute:: ceesubinterfacetable
    
    	This table provides the subinterface related information associated to the Ethernet\-like interfaces.  The subinterface is a division of one physical interface into multiple logical interfaces. As an example of what a typical subinterface setup might look like on a device, a single Ethernet port such as GigabitEthernet0/0 would be subdivided into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as if it were a separate interface
    	**type**\: :py:class:`CeeSubInterfaceTable <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable>`
    
    

    """

    _prefix = 'cisco-etherlike'
    _revision = '2010-06-04'

    def __init__(self):
        self.ceedot3pauseexttable = CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable()
        self.ceedot3pauseexttable.parent = self
        self.ceesubinterfacetable = CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable()
        self.ceesubinterfacetable.parent = self


    class CeeDot3PauseExtTable(object):
        """
        A list of additional descriptive and status
        information about the MAC Control PAUSE 
        function on the ethernet\-like interfaces 
        attached to a particular system, in extension to
        dot3PauseTable in EtherLike\-MIB. There will be 
        one row in this table for each ethernet\-like 
        interface in the system which supports the MAC 
        Control PAUSE function.
        
        .. attribute:: ceedot3pauseextentry
        
        	An entry in the table, containing additional information about the MAC Control PAUSE function  on a single ethernet\-like interface, in extension  to dot3PauseEntry in Etherlike\-MIB
        	**type**\: list of :py:class:`CeeDot3PauseExtEntry <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry>`
        
        

        """

        _prefix = 'cisco-etherlike'
        _revision = '2010-06-04'

        def __init__(self):
            self.parent = None
            self.ceedot3pauseextentry = YList()
            self.ceedot3pauseextentry.parent = self
            self.ceedot3pauseextentry.name = 'ceedot3pauseextentry'


        class CeeDot3PauseExtEntry(object):
            """
            An entry in the table, containing additional
            information about the MAC Control PAUSE function 
            on a single ethernet\-like interface, in extension 
            to dot3PauseEntry in Etherlike\-MIB.
            
            .. attribute:: dot3statsindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceedot3pauseextadminmode
            
            	Indicates preference to send or process pause frames on this interface. txDesired(0)  \-  indicates preference to send pause                   frames, but autonegotiates flow                   control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledXmit' or                   'enabledXmitAndRcv'. rxDesired(1)  \-  indicates preference to process                   pause frames, but autonegotiates                   flow control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledRcv' or                   'enabledXmitAndRcv'
            	**type**\: :py:class:`CeeDot3PauseExtAdminMode_Bits <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtAdminMode_Bits>`
            
            .. attribute:: ceedot3pauseextopermode
            
            	Provides additional information about the flow control operational status on this interface. txDisagree(0) \- the transmit pause function on                  this interface is disabled due to                  disagreement from the far end on                  negotiation. rxDisagree(1) \- the receive pause function on                   this interface is disabled due to                  disagreement from the far end on                  negotiation. txDesired(2)  \- the transmit pause function on                  this interface is desired. rxDesired(3)  \- the receive pause function on                   this interface is desired
            	**type**\: :py:class:`CeeDot3PauseExtOperMode_Bits <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtOperMode_Bits>`
            
            

            """

            _prefix = 'cisco-etherlike'
            _revision = '2010-06-04'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.ceedot3pauseextadminmode = CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtAdminMode_Bits()
                self.ceedot3pauseextopermode = CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtOperMode_Bits()

            class CeeDot3PauseExtAdminMode_Bits(FixedBitsDict):
                """
                CeeDot3PauseExtAdminMode_Bits

                Indicates preference to send or process pause
                frames on this interface.
                txDesired(0)  \-  indicates preference to send pause 
                                 frames, but autonegotiates flow 
                                 control. This bit can only be 
                                 turned on when the corresponding 
                                 instance of dot3PauseAdminMode 
                                 has the value of 'enabledXmit' or 
                                 'enabledXmitAndRcv'.
                rxDesired(1)  \-  indicates preference to process 
                                 pause frames, but autonegotiates 
                                 flow control. This bit can only be 
                                 turned on when the corresponding 
                                 instance of dot3PauseAdminMode 
                                 has the value of 'enabledRcv' or 
                                 'enabledXmitAndRcv'.
                Keys are:- rxDesired , txDesired

                """

                def __init__(self):
                    self._dictionary = { 
                        'rxDesired':False,
                        'txDesired':False,
                    }
                    self._pos_map = { 
                        'rxDesired':1,
                        'txDesired':0,
                    }

            class CeeDot3PauseExtOperMode_Bits(FixedBitsDict):
                """
                CeeDot3PauseExtOperMode_Bits

                Provides additional information about the flow
                control operational status on this interface.
                txDisagree(0) \- the transmit pause function on 
                                this interface is disabled due to 
                                disagreement from the far end on 
                                negotiation.
                rxDisagree(1) \- the receive pause function on  
                                this interface is disabled due to 
                                disagreement from the far end on 
                                negotiation.
                txDesired(2)  \- the transmit pause function on 
                                this interface is desired.
                rxDesired(3)  \- the receive pause function on  
                                this interface is desired.
                Keys are:- rxDesired , txDisagree , txDesired , rxDisagree

                """

                def __init__(self):
                    self._dictionary = { 
                        'rxDesired':False,
                        'txDisagree':False,
                        'txDesired':False,
                        'rxDisagree':False,
                    }
                    self._pos_map = { 
                        'rxDesired':3,
                        'txDisagree':0,
                        'txDesired':2,
                        'rxDisagree':1,
                    }

            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYDataValidationError('Key property dot3statsindex is None')

                return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtTable/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtEntry[CISCO-ETHERLIKE-EXT-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3statsindex is not None:
                    return True

                if self.ceedot3pauseextadminmode is not None:
                    if self.ceedot3pauseextadminmode._has_data():
                        return True

                if self.ceedot3pauseextopermode is not None:
                    if self.ceedot3pauseextopermode._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.etherlike._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
                return meta._meta_table['CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceedot3pauseextentry is not None:
                for child_ref in self.ceedot3pauseextentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.etherlike._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
            return meta._meta_table['CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable']['meta_info']


    class CeeSubInterfaceTable(object):
        """
        This table provides the subinterface related information
        associated to the Ethernet\-like interfaces.
        
        The subinterface is a division of one physical interface into
        multiple logical interfaces. As an example of what a typical
        subinterface setup might look like on a device, a single
        Ethernet port such as GigabitEthernet0/0 would be subdivided
        into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as
        if it were a separate interface.
        
        .. attribute:: ceesubinterfaceentry
        
        	This table contains a row for each Ethernet\-like interface by it's ifTable ifIndex in the system, which supports the sub\-interface.  An entry is created by an agent, when it detects a Ethernet\-like interface is created in ifTable and it  can support sub\-interface.  An entry is deleted by an agent, when the ifTable entry associated to the Ethernet\-like interface is deleted. Typically, when the card is removed from the device
        	**type**\: list of :py:class:`CeeSubInterfaceEntry <ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry>`
        
        

        """

        _prefix = 'cisco-etherlike'
        _revision = '2010-06-04'

        def __init__(self):
            self.parent = None
            self.ceesubinterfaceentry = YList()
            self.ceesubinterfaceentry.parent = self
            self.ceesubinterfaceentry.name = 'ceesubinterfaceentry'


        class CeeSubInterfaceEntry(object):
            """
            This table contains a row for each Ethernet\-like interface
            by it's ifTable ifIndex in the system, which supports the
            sub\-interface.
            
            An entry is created by an agent, when it detects a
            Ethernet\-like interface is created in ifTable and it 
            can support sub\-interface.
            
            An entry is deleted by an agent, when the ifTable entry
            associated to the Ethernet\-like interface is deleted.
            Typically, when the card is removed from the device.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceesubinterfacecount
            
            	This object represents the number of subinterfaces created on a Ethernet\-like interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-etherlike'
            _revision = '2010-06-04'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ceesubinterfacecount = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceTable/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceEntry[CISCO-ETHERLIKE-EXT-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.ceesubinterfacecount is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.etherlike._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
                return meta._meta_table['CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceesubinterfaceentry is not None:
                for child_ref in self.ceesubinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.etherlike._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
            return meta._meta_table['CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ceedot3pauseexttable is not None and self.ceedot3pauseexttable._has_data():
            return True

        if self.ceedot3pauseexttable is not None and self.ceedot3pauseexttable.is_presence():
            return True

        if self.ceesubinterfacetable is not None and self.ceesubinterfacetable._has_data():
            return True

        if self.ceesubinterfacetable is not None and self.ceesubinterfacetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.etherlike._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
        return meta._meta_table['CISCOETHERLIKEEXTMIB']['meta_info']


