""" Cisco_IOS_XR_sdr_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\: SDR information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SdrInventory(object):
    """
    SDR information
    
    .. attribute:: racks
    
    	RackTable
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.racks = SdrInventory.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        RackTable
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
            """
            Rack name
            
            .. attribute:: name  <key>
            
            	Rack name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slot
            
            	Slot name
            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot>`
            
            

            """

            _prefix = 'sdr-invmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.slot = YList()
                self.slot.parent = self
                self.slot.name = 'slot'


            class Slot(object):
                """
                Slot name
                
                .. attribute:: name  <key>
                
                	Slot name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: card
                
                	Card
                	**type**\: list of    :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card>`
                
                

                """

                _prefix = 'sdr-invmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.card = YList()
                    self.card.parent = self
                    self.card.name = 'card'


                class Card(object):
                    """
                    Card
                    
                    .. attribute:: name  <key>
                    
                    	Card
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card.Attributes>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.attributes = SdrInventory.Racks.Rack.Slot.Card.Attributes()
                        self.attributes.parent = self


                    class Attributes(object):
                        """
                        Attributes
                        
                        .. attribute:: card_admin_state
                        
                        	Card Admin State
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state
                        
                        	CardState
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state_string
                        
                        	Card State String
                        	**type**\:  str
                        
                        .. attribute:: card_type
                        
                        	CardType
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_type_string
                        
                        	Card Type String
                        	**type**\:  str
                        
                        .. attribute:: config_state
                        
                        	ConfigState
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: config_state_string
                        
                        	Config State String
                        	**type**\:  str
                        
                        .. attribute:: ctype
                        
                        	CType
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: monitor
                        
                        	Monitor
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: node_name_string
                        
                        	Node Name String
                        	**type**\:  str
                        
                        .. attribute:: pi_slot_number
                        
                        	Pi Slot Number
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: power
                        
                        	Power
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: shutdown
                        
                        	Shutdown
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: vm_state
                        
                        	VM State information
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'sdr-invmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.card_admin_state = None
                            self.card_state = None
                            self.card_state_string = None
                            self.card_type = None
                            self.card_type_string = None
                            self.config_state = None
                            self.config_state_string = None
                            self.ctype = None
                            self.monitor = None
                            self.node_name_string = None
                            self.pi_slot_number = None
                            self.power = None
                            self.shutdown = None
                            self.vm_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-oper:attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.card_admin_state is not None:
                                return True

                            if self.card_state is not None:
                                return True

                            if self.card_state_string is not None:
                                return True

                            if self.card_type is not None:
                                return True

                            if self.card_type_string is not None:
                                return True

                            if self.config_state is not None:
                                return True

                            if self.config_state_string is not None:
                                return True

                            if self.ctype is not None:
                                return True

                            if self.monitor is not None:
                                return True

                            if self.node_name_string is not None:
                                return True

                            if self.pi_slot_number is not None:
                                return True

                            if self.power is not None:
                                return True

                            if self.shutdown is not None:
                                return True

                            if self.vm_state is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                            return meta._meta_table['SdrInventory.Racks.Rack.Slot.Card.Attributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-oper:card[Cisco-IOS-XR-sdr-invmgr-oper:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.attributes is not None and self.attributes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                        return meta._meta_table['SdrInventory.Racks.Rack.Slot.Card']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-oper:slot[Cisco-IOS-XR-sdr-invmgr-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.card is not None:
                        for child_ref in self.card:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                    return meta._meta_table['SdrInventory.Racks.Rack.Slot']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/Cisco-IOS-XR-sdr-invmgr-oper:racks/Cisco-IOS-XR-sdr-invmgr-oper:rack[Cisco-IOS-XR-sdr-invmgr-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.slot is not None:
                    for child_ref in self.slot:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                return meta._meta_table['SdrInventory.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/Cisco-IOS-XR-sdr-invmgr-oper:racks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rack is not None:
                for child_ref in self.rack:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
            return meta._meta_table['SdrInventory.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
        return meta._meta_table['SdrInventory']['meta_info']


