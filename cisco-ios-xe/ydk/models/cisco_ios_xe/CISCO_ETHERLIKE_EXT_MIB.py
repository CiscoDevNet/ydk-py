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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoEtherlikeExtMib(object):
    """
    
    
    .. attribute:: ceedot3pauseexttable
    
    	A list of additional descriptive and status information about the MAC Control PAUSE  function on the ethernet\-like interfaces  attached to a particular system, in extension to dot3PauseTable in EtherLike\-MIB. There will be  one row in this table for each ethernet\-like  interface in the system which supports the MAC  Control PAUSE function
    	**type**\:   :py:class:`Ceedot3Pauseexttable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable>`
    
    .. attribute:: ceesubinterfacetable
    
    	This table provides the subinterface related information associated to the Ethernet\-like interfaces.  The subinterface is a division of one physical interface into multiple logical interfaces. As an example of what a typical subinterface setup might look like on a device, a single Ethernet port such as GigabitEthernet0/0 would be subdivided into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as if it were a separate interface
    	**type**\:   :py:class:`Ceesubinterfacetable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceesubinterfacetable>`
    
    

    """

    _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
    _revision = '2010-06-04'

    def __init__(self):
        self.ceedot3pauseexttable = CiscoEtherlikeExtMib.Ceedot3Pauseexttable()
        self.ceedot3pauseexttable.parent = self
        self.ceesubinterfacetable = CiscoEtherlikeExtMib.Ceesubinterfacetable()
        self.ceesubinterfacetable.parent = self


    class Ceedot3Pauseexttable(object):
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
        	**type**\: list of    :py:class:`Ceedot3Pauseextentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            self.parent = None
            self.ceedot3pauseextentry = YList()
            self.ceedot3pauseextentry.parent = self
            self.ceedot3pauseextentry.name = 'ceedot3pauseextentry'


        class Ceedot3Pauseextentry(object):
            """
            An entry in the table, containing additional
            information about the MAC Control PAUSE function 
            on a single ethernet\-like interface, in extension 
            to dot3PauseEntry in Etherlike\-MIB.
            
            .. attribute:: dot3statsindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherlikeMib.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: ceedot3pauseextadminmode
            
            	Indicates preference to send or process pause frames on this interface. txDesired(0)  \-  indicates preference to send pause                   frames, but autonegotiates flow                   control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledXmit' or                   'enabledXmitAndRcv'. rxDesired(1)  \-  indicates preference to process                   pause frames, but autonegotiates                   flow control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledRcv' or                   'enabledXmitAndRcv'
            	**type**\:   :py:class:`Ceedot3Pauseextadminmode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextadminmode>`
            
            .. attribute:: ceedot3pauseextopermode
            
            	Provides additional information about the flow control operational status on this interface. txDisagree(0) \- the transmit pause function on                  this interface is disabled due to                  disagreement from the far end on                  negotiation. rxDisagree(1) \- the receive pause function on                   this interface is disabled due to                  disagreement from the far end on                  negotiation. txDesired(2)  \- the transmit pause function on                  this interface is desired. rxDesired(3)  \- the receive pause function on                   this interface is desired
            	**type**\:   :py:class:`Ceedot3Pauseextopermode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextopermode>`
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                self.parent = None
                self.dot3statsindex = None
                self.ceedot3pauseextadminmode = CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextadminmode()
                self.ceedot3pauseextopermode = CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextopermode()

            class Ceedot3Pauseextadminmode(FixedBitsDict):
                """
                Ceedot3Pauseextadminmode

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

            class Ceedot3Pauseextopermode(FixedBitsDict):
                """
                Ceedot3Pauseextopermode

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
                Keys are:- txDisagree , rxDesired , txDesired , rxDisagree

                """

                def __init__(self):
                    self._dictionary = { 
                        'txDisagree':False,
                        'rxDesired':False,
                        'txDesired':False,
                        'rxDisagree':False,
                    }
                    self._pos_map = { 
                        'txDisagree':0,
                        'rxDesired':3,
                        'txDesired':2,
                        'rxDisagree':1,
                    }

            @property
            def _common_path(self):
                if self.dot3statsindex is None:
                    raise YPYModelError('Key property dot3statsindex is None')

                return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtTable/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtEntry[CISCO-ETHERLIKE-EXT-MIB:dot3StatsIndex = ' + str(self.dot3statsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot3statsindex is not None:
                    return True

                if self.ceedot3pauseextadminmode is not None:
                    if self.ceedot3pauseextadminmode._has_data():
                        return True

                if self.ceedot3pauseextopermode is not None:
                    if self.ceedot3pauseextopermode._has_data():
                        return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
                return meta._meta_table['CiscoEtherlikeExtMib.Ceedot3Pauseexttable.Ceedot3Pauseextentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeDot3PauseExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceedot3pauseextentry is not None:
                for child_ref in self.ceedot3pauseextentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
            return meta._meta_table['CiscoEtherlikeExtMib.Ceedot3Pauseexttable']['meta_info']


    class Ceesubinterfacetable(object):
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
        	**type**\: list of    :py:class:`Ceesubinterfaceentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            self.parent = None
            self.ceesubinterfaceentry = YList()
            self.ceesubinterfaceentry.parent = self
            self.ceesubinterfaceentry.name = 'ceesubinterfaceentry'


        class Ceesubinterfaceentry(object):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ceesubinterfacecount
            
            	This object represents the number of subinterfaces created on a Ethernet\-like interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: subifs
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.ceesubinterfacecount = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceTable/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceEntry[CISCO-ETHERLIKE-EXT-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.ceesubinterfacecount is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
                return meta._meta_table['CiscoEtherlikeExtMib.Ceesubinterfacetable.Ceesubinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/CISCO-ETHERLIKE-EXT-MIB:ceeSubInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceesubinterfaceentry is not None:
                for child_ref in self.ceesubinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
            return meta._meta_table['CiscoEtherlikeExtMib.Ceesubinterfacetable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ceedot3pauseexttable is not None and self.ceedot3pauseexttable._has_data():
            return True

        if self.ceesubinterfacetable is not None and self.ceesubinterfacetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ETHERLIKE_EXT_MIB as meta
        return meta._meta_table['CiscoEtherlikeExtMib']['meta_info']


