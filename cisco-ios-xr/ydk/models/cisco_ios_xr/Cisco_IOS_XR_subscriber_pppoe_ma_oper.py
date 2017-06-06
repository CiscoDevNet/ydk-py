""" Cisco_IOS_XR_subscriber_pppoe_ma_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma package operational data.

This module contains definitions
for the following management objects\:
  pppoe\: PPPoE operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PppoeMaLimitStateEnum(Enum):
    """
    PppoeMaLimitStateEnum

    Pppoe ma limit state

    .. data:: ok = 0

    	OK State

    .. data:: warning = 1

    	Warn State

    .. data:: block = 2

    	Block State

    """

    ok = 0

    warning = 1

    block = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaLimitStateEnum']


class PppoeMaSessionIdbSrgStateEnum(Enum):
    """
    PppoeMaSessionIdbSrgStateEnum

    Pppoe ma session idb srg state

    .. data:: none = 0

    	SRG-None state

    .. data:: active = 1

    	SRG-Active state

    .. data:: standby = 2

    	SRG-Standby state

    """

    none = 0

    active = 1

    standby = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaSessionIdbSrgStateEnum']


class PppoeMaThrottleStateEnum(Enum):
    """
    PppoeMaThrottleStateEnum

    Pppoe ma throttle state

    .. data:: idle = 0

    	Idle State

    .. data:: monitor = 1

    	Monitor State

    .. data:: block = 2

    	Block State

    """

    idle = 0

    monitor = 1

    block = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['PppoeMaThrottleStateEnum']



class Pppoe(object):
    """
    PPPoE operational data
    
    .. attribute:: access_interface_statistics
    
    	PPPoE access interface statistics information
    	**type**\:   :py:class:`AccessInterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics>`
    
    .. attribute:: nodes
    
    	Per\-node PPPoE operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes>`
    
    

    """

    _prefix = 'subscriber-pppoe-ma-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.access_interface_statistics = Pppoe.AccessInterfaceStatistics()
        self.access_interface_statistics.parent = self
        self.nodes = Pppoe.Nodes()
        self.nodes.parent = self


    class AccessInterfaceStatistics(object):
        """
        PPPoE access interface statistics information
        
        .. attribute:: access_interface_statistic
        
        	Statistics information for a PPPoE\-enabled access interface
        	**type**\: list of    :py:class:`AccessInterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.access_interface_statistic = YList()
            self.access_interface_statistic.parent = self
            self.access_interface_statistic.name = 'access_interface_statistic'


        class AccessInterfaceStatistic(object):
            """
            Statistics information for a PPPoE\-enabled
            access interface
            
            .. attribute:: interface_name  <key>
            
            	PPPoE Access Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: packet_counts
            
            	Packet Counts
            	**type**\:   :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.packet_counts = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts()
                self.packet_counts.parent = self


            class PacketCounts(object):
                """
                Packet Counts
                
                .. attribute:: other
                
                	Other counts
                	**type**\:   :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other>`
                
                .. attribute:: padi
                
                	PADI counts
                	**type**\:   :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi>`
                
                .. attribute:: pado
                
                	PADO counts
                	**type**\:   :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado>`
                
                .. attribute:: padr
                
                	PADR counts
                	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr>`
                
                .. attribute:: pads_error
                
                	PADS Error counts
                	**type**\:   :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError>`
                
                .. attribute:: pads_success
                
                	PADS Success counts
                	**type**\:   :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess>`
                
                .. attribute:: padt
                
                	PADT counts
                	**type**\:   :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt>`
                
                .. attribute:: session_state
                
                	Session Stage counts
                	**type**\:   :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.other = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other()
                    self.other.parent = self
                    self.padi = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi()
                    self.padi.parent = self
                    self.pado = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado()
                    self.pado.parent = self
                    self.padr = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr()
                    self.padr.parent = self
                    self.pads_error = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError()
                    self.pads_error.parent = self
                    self.pads_success = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess()
                    self.pads_success.parent = self
                    self.padt = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt()
                    self.padt.parent = self
                    self.session_state = Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState()
                    self.session_state.parent = self


                class Padi(object):
                    """
                    PADI counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padi'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi']['meta_info']


                class Pado(object):
                    """
                    PADO counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pado'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado']['meta_info']


                class Padr(object):
                    """
                    PADR counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr']['meta_info']


                class PadsSuccess(object):
                    """
                    PADS Success counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pads-success'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess']['meta_info']


                class PadsError(object):
                    """
                    PADS Error counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pads-error'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError']['meta_info']


                class Padt(object):
                    """
                    PADT counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padt'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt']['meta_info']


                class SessionState(object):
                    """
                    Session Stage counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:session-state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState']['meta_info']


                class Other(object):
                    """
                    Other counts
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received
                    
                    	Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent
                    
                    	Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dropped = None
                        self.received = None
                        self.sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:other'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dropped is not None:
                            return True

                        if self.received is not None:
                            return True

                        if self.sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:packet-counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.other is not None and self.other._has_data():
                        return True

                    if self.padi is not None and self.padi._has_data():
                        return True

                    if self.pado is not None and self.pado._has_data():
                        return True

                    if self.padr is not None and self.padr._has_data():
                        return True

                    if self.pads_error is not None and self.pads_error._has_data():
                        return True

                    if self.pads_success is not None and self.pads_success._has_data():
                        return True

                    if self.padt is not None and self.padt._has_data():
                        return True

                    if self.session_state is not None and self.session_state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-interface-statistics/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-interface-statistic[Cisco-IOS-XR-subscriber-pppoe-ma-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.packet_counts is not None and self.packet_counts._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                return meta._meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-interface-statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.access_interface_statistic is not None:
                for child_ref in self.access_interface_statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
            return meta._meta_table['Pppoe.AccessInterfaceStatistics']['meta_info']


    class Nodes(object):
        """
        Per\-node PPPoE operational data
        
        .. attribute:: node
        
        	PPPoE operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            PPPoE operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: access_interface
            
            	PPPoE access interface information
            	**type**\:   :py:class:`AccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface>`
            
            .. attribute:: bba_groups
            
            	PPPoE BBA\-Group information
            	**type**\:   :py:class:`BbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups>`
            
            .. attribute:: interfaces
            
            	Per interface PPPoE operational data
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces>`
            
            .. attribute:: statistics
            
            	PPPoE statistics for a given node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics>`
            
            .. attribute:: summary_total
            
            	PPPoE statistics for a given node
            	**type**\:   :py:class:`SummaryTotal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.SummaryTotal>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.access_interface = Pppoe.Nodes.Node.AccessInterface()
                self.access_interface.parent = self
                self.bba_groups = Pppoe.Nodes.Node.BbaGroups()
                self.bba_groups.parent = self
                self.interfaces = Pppoe.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.statistics = Pppoe.Nodes.Node.Statistics()
                self.statistics.parent = self
                self.summary_total = Pppoe.Nodes.Node.SummaryTotal()
                self.summary_total.parent = self


            class Statistics(object):
                """
                PPPoE statistics for a given node
                
                .. attribute:: packet_counts
                
                	Packet Counts
                	**type**\:   :py:class:`PacketCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts>`
                
                .. attribute:: packet_error_counts
                
                	Packet Error Counts
                	**type**\:   :py:class:`PacketErrorCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketErrorCounts>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.packet_counts = Pppoe.Nodes.Node.Statistics.PacketCounts()
                    self.packet_counts.parent = self
                    self.packet_error_counts = Pppoe.Nodes.Node.Statistics.PacketErrorCounts()
                    self.packet_error_counts.parent = self


                class PacketCounts(object):
                    """
                    Packet Counts
                    
                    .. attribute:: other
                    
                    	Other counts
                    	**type**\:   :py:class:`Other <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Other>`
                    
                    .. attribute:: padi
                    
                    	PADI counts
                    	**type**\:   :py:class:`Padi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padi>`
                    
                    .. attribute:: pado
                    
                    	PADO counts
                    	**type**\:   :py:class:`Pado <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Pado>`
                    
                    .. attribute:: padr
                    
                    	PADR counts
                    	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padr>`
                    
                    .. attribute:: pads_error
                    
                    	PADS Error counts
                    	**type**\:   :py:class:`PadsError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError>`
                    
                    .. attribute:: pads_success
                    
                    	PADS Success counts
                    	**type**\:   :py:class:`PadsSuccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess>`
                    
                    .. attribute:: padt
                    
                    	PADT counts
                    	**type**\:   :py:class:`Padt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.Padt>`
                    
                    .. attribute:: session_state
                    
                    	Session Stage counts
                    	**type**\:   :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.other = Pppoe.Nodes.Node.Statistics.PacketCounts.Other()
                        self.other.parent = self
                        self.padi = Pppoe.Nodes.Node.Statistics.PacketCounts.Padi()
                        self.padi.parent = self
                        self.pado = Pppoe.Nodes.Node.Statistics.PacketCounts.Pado()
                        self.pado.parent = self
                        self.padr = Pppoe.Nodes.Node.Statistics.PacketCounts.Padr()
                        self.padr.parent = self
                        self.pads_error = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError()
                        self.pads_error.parent = self
                        self.pads_success = Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess()
                        self.pads_success.parent = self
                        self.padt = Pppoe.Nodes.Node.Statistics.PacketCounts.Padt()
                        self.padt.parent = self
                        self.session_state = Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState()
                        self.session_state.parent = self


                    class Padi(object):
                        """
                        PADI counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padi'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padi']['meta_info']


                    class Pado(object):
                        """
                        PADO counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pado'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Pado']['meta_info']


                    class Padr(object):
                        """
                        PADR counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padr']['meta_info']


                    class PadsSuccess(object):
                        """
                        PADS Success counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pads-success'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess']['meta_info']


                    class PadsError(object):
                        """
                        PADS Error counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pads-error'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError']['meta_info']


                    class Padt(object):
                        """
                        PADT counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:padt'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padt']['meta_info']


                    class SessionState(object):
                        """
                        Session Stage counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:session-state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState']['meta_info']


                    class Other(object):
                        """
                        Other counts
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received
                        
                        	Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sent
                        
                        	Sent
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dropped = None
                            self.received = None
                            self.sent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:other'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dropped is not None:
                                return True

                            if self.received is not None:
                                return True

                            if self.sent is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Other']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:packet-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.other is not None and self.other._has_data():
                            return True

                        if self.padi is not None and self.padi._has_data():
                            return True

                        if self.pado is not None and self.pado._has_data():
                            return True

                        if self.padr is not None and self.padr._has_data():
                            return True

                        if self.pads_error is not None and self.pads_error._has_data():
                            return True

                        if self.pads_success is not None and self.pads_success._has_data():
                            return True

                        if self.padt is not None and self.padt._has_data():
                            return True

                        if self.session_state is not None and self.session_state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']


                class PacketErrorCounts(object):
                    """
                    Packet Error Counts
                    
                    .. attribute:: bad_packet_length
                    
                    	Bad packet length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_tag_length_field
                    
                    	Bad tag\-length field
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_vendor_tag_length_field
                    
                    	Bad vendor tag length field
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_host_uniq_tag_received
                    
                    	Duplicate Host\-Uniq tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_relay_session_id_tag_received
                    
                    	Duplicate Relay Session ID tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_ale_tag
                    
                    	Invalid ALE tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_dsl_tag
                    
                    	Invalid DSL tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iana_code_invendor_tag
                    
                    	Invalid IANA code in vendor tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_iwf_tag
                    
                    	Invalid IWF tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_max_payload_tag
                    
                    	Invalid Max\-Payload tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_peer_mac
                    
                    	Invalid Peer MAC
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_service_name
                    
                    	Invalid Service Name
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_type_value
                    
                    	Invalid version\-type value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_vlan_tags
                    
                    	Invalid VLAN Tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_ale_tags
                    
                    	Multiple ALE tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_circuit_id_tags
                    
                    	Multiple Circuit\-ID tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_host_uniq_tags
                    
                    	Multiple Host\-Uniq tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_iwf_tags
                    
                    	Multiple IWF tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_max_payload_tags
                    
                    	Multiple Max\-Payload tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_of_the_same_dsl_tag
                    
                    	Multiple of the same DSL tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_relay_session_id_tags
                    
                    	Multiple relay\-session\-id tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_remote_id_tags
                    
                    	Multiple Remote\-ID tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_service_name_tags
                    
                    	Multiple Service\-Name tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multiple_vendor_specific_tags
                    
                    	Multiple Vendor\-specific tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_iana_code_invendor_tag
                    
                    	No IANA code in vendor tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_interface_handle
                    
                    	No interface handle
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_mac_address
                    
                    	No packet mac\-address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_packet_payload
                    
                    	No packet payload
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_service_name_tag
                    
                    	No Service\-Name Tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_space_left_in_packet
                    
                    	No space left in packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_on_srg_slave
                    
                    	Packet Received on SRG Slave
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_too_long
                    
                    	Packet too long
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pado_received
                    
                    	PADO received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pads_received
                    
                    	PADS received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_before_pads_sent
                    
                    	PADT before PADS sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_for_unknown_session
                    
                    	PADT for unknown session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_peer_mac
                    
                    	PADT with wrong peer\-mac
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: padt_with_wrong_vlan_tags
                    
                    	PADT with wrong VLAN tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_for_unknown_session
                    
                    	Session\-stage packet for unknown session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_no_error
                    
                    	Session\-stage packet with no error
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_mac
                    
                    	Session\-stage packet with wrong mac
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_stage_packet_with_wrong_vlan_tags
                    
                    	Session\-stage packet with wrong VLAN tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tag_too_short
                    
                    	Tag too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_ac_name_tag
                    
                    	Unexpected AC\-Name tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_error_tags
                    
                    	Unexpected error tags
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unexpected_session_id_in_packet
                    
                    	Unexpected Session\-ID in packet
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_interface
                    
                    	Unknown interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_packet_type_received
                    
                    	Unknown packet type received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_tag_received
                    
                    	Unknown tag received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknownvendor_tag
                    
                    	Unknown vendor\-tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vendor_tag_too_short
                    
                    	Vendor tag too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: zero_length_host_uniq
                    
                    	Zero\-length Host\-Uniq tag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bad_packet_length = None
                        self.bad_tag_length_field = None
                        self.bad_vendor_tag_length_field = None
                        self.duplicate_host_uniq_tag_received = None
                        self.duplicate_relay_session_id_tag_received = None
                        self.invalid_ale_tag = None
                        self.invalid_dsl_tag = None
                        self.invalid_iana_code_invendor_tag = None
                        self.invalid_iwf_tag = None
                        self.invalid_max_payload_tag = None
                        self.invalid_peer_mac = None
                        self.invalid_service_name = None
                        self.invalid_version_type_value = None
                        self.invalid_vlan_tags = None
                        self.multiple_ale_tags = None
                        self.multiple_circuit_id_tags = None
                        self.multiple_host_uniq_tags = None
                        self.multiple_iwf_tags = None
                        self.multiple_max_payload_tags = None
                        self.multiple_of_the_same_dsl_tag = None
                        self.multiple_relay_session_id_tags = None
                        self.multiple_remote_id_tags = None
                        self.multiple_service_name_tags = None
                        self.multiple_vendor_specific_tags = None
                        self.no_iana_code_invendor_tag = None
                        self.no_interface_handle = None
                        self.no_packet_mac_address = None
                        self.no_packet_payload = None
                        self.no_service_name_tag = None
                        self.no_space_left_in_packet = None
                        self.packet_on_srg_slave = None
                        self.packet_too_long = None
                        self.pado_received = None
                        self.pads_received = None
                        self.padt_before_pads_sent = None
                        self.padt_for_unknown_session = None
                        self.padt_with_wrong_peer_mac = None
                        self.padt_with_wrong_vlan_tags = None
                        self.session_stage_packet_for_unknown_session = None
                        self.session_stage_packet_with_no_error = None
                        self.session_stage_packet_with_wrong_mac = None
                        self.session_stage_packet_with_wrong_vlan_tags = None
                        self.tag_too_short = None
                        self.unexpected_ac_name_tag = None
                        self.unexpected_error_tags = None
                        self.unexpected_session_id_in_packet = None
                        self.unknown_interface = None
                        self.unknown_packet_type_received = None
                        self.unknown_tag_received = None
                        self.unknownvendor_tag = None
                        self.vendor_tag_too_short = None
                        self.zero_length_host_uniq = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:packet-error-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bad_packet_length is not None:
                            return True

                        if self.bad_tag_length_field is not None:
                            return True

                        if self.bad_vendor_tag_length_field is not None:
                            return True

                        if self.duplicate_host_uniq_tag_received is not None:
                            return True

                        if self.duplicate_relay_session_id_tag_received is not None:
                            return True

                        if self.invalid_ale_tag is not None:
                            return True

                        if self.invalid_dsl_tag is not None:
                            return True

                        if self.invalid_iana_code_invendor_tag is not None:
                            return True

                        if self.invalid_iwf_tag is not None:
                            return True

                        if self.invalid_max_payload_tag is not None:
                            return True

                        if self.invalid_peer_mac is not None:
                            return True

                        if self.invalid_service_name is not None:
                            return True

                        if self.invalid_version_type_value is not None:
                            return True

                        if self.invalid_vlan_tags is not None:
                            return True

                        if self.multiple_ale_tags is not None:
                            return True

                        if self.multiple_circuit_id_tags is not None:
                            return True

                        if self.multiple_host_uniq_tags is not None:
                            return True

                        if self.multiple_iwf_tags is not None:
                            return True

                        if self.multiple_max_payload_tags is not None:
                            return True

                        if self.multiple_of_the_same_dsl_tag is not None:
                            return True

                        if self.multiple_relay_session_id_tags is not None:
                            return True

                        if self.multiple_remote_id_tags is not None:
                            return True

                        if self.multiple_service_name_tags is not None:
                            return True

                        if self.multiple_vendor_specific_tags is not None:
                            return True

                        if self.no_iana_code_invendor_tag is not None:
                            return True

                        if self.no_interface_handle is not None:
                            return True

                        if self.no_packet_mac_address is not None:
                            return True

                        if self.no_packet_payload is not None:
                            return True

                        if self.no_service_name_tag is not None:
                            return True

                        if self.no_space_left_in_packet is not None:
                            return True

                        if self.packet_on_srg_slave is not None:
                            return True

                        if self.packet_too_long is not None:
                            return True

                        if self.pado_received is not None:
                            return True

                        if self.pads_received is not None:
                            return True

                        if self.padt_before_pads_sent is not None:
                            return True

                        if self.padt_for_unknown_session is not None:
                            return True

                        if self.padt_with_wrong_peer_mac is not None:
                            return True

                        if self.padt_with_wrong_vlan_tags is not None:
                            return True

                        if self.session_stage_packet_for_unknown_session is not None:
                            return True

                        if self.session_stage_packet_with_no_error is not None:
                            return True

                        if self.session_stage_packet_with_wrong_mac is not None:
                            return True

                        if self.session_stage_packet_with_wrong_vlan_tags is not None:
                            return True

                        if self.tag_too_short is not None:
                            return True

                        if self.unexpected_ac_name_tag is not None:
                            return True

                        if self.unexpected_error_tags is not None:
                            return True

                        if self.unexpected_session_id_in_packet is not None:
                            return True

                        if self.unknown_interface is not None:
                            return True

                        if self.unknown_packet_type_received is not None:
                            return True

                        if self.unknown_tag_received is not None:
                            return True

                        if self.unknownvendor_tag is not None:
                            return True

                        if self.vendor_tag_too_short is not None:
                            return True

                        if self.zero_length_host_uniq is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Statistics.PacketErrorCounts']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.packet_counts is not None and self.packet_counts._has_data():
                        return True

                    if self.packet_error_counts is not None and self.packet_error_counts._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.Statistics']['meta_info']


            class AccessInterface(object):
                """
                PPPoE access interface information
                
                .. attribute:: summaries
                
                	PPPoE access interface summary information
                	**type**\:   :py:class:`Summaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.summaries = Pppoe.Nodes.Node.AccessInterface.Summaries()
                    self.summaries.parent = self


                class Summaries(object):
                    """
                    PPPoE access interface summary information
                    
                    .. attribute:: summary
                    
                    	Summary information for a PPPoE\-enabled access interface
                    	**type**\: list of    :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.AccessInterface.Summaries.Summary>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.summary = YList()
                        self.summary.parent = self
                        self.summary.name = 'summary'


                    class Summary(object):
                        """
                        Summary information for a PPPoE\-enabled
                        access interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	PPPoE Access Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: bba_group_name
                        
                        	BBA Group
                        	**type**\:  str
                        
                        .. attribute:: incomplete_sessions
                        
                        	Incomplete Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_ready
                        
                        	Is Ready
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: mac_address
                        
                        	Mac Address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: sessions
                        
                        	Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.bba_group_name = None
                            self.incomplete_sessions = None
                            self.interface_name_xr = None
                            self.interface_state = None
                            self.is_ready = None
                            self.mac_address = None
                            self.sessions = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:summary[Cisco-IOS-XR-subscriber-pppoe-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.bba_group_name is not None:
                                return True

                            if self.incomplete_sessions is not None:
                                return True

                            if self.interface_name_xr is not None:
                                return True

                            if self.interface_state is not None:
                                return True

                            if self.is_ready is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.sessions is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries.Summary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.summary is not None:
                            for child_ref in self.summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.summaries is not None and self.summaries._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.AccessInterface']['meta_info']


            class Interfaces(object):
                """
                Per interface PPPoE operational data
                
                .. attribute:: interface
                
                	Data for a PPPoE interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Data for a PPPoE interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	PPPoE Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: access_interface_name
                    
                    	Access Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bba_group_name
                    
                    	BBA Group
                    	**type**\:  str
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: is_complete
                    
                    	Is Complete
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: local_mac_address
                    
                    	Local Mac\-Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: peer_mac_address
                    
                    	Peer Mac\-Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srg_state
                    
                    	SRG state
                    	**type**\:   :py:class:`PppoeMaSessionIdbSrgStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaSessionIdbSrgStateEnum>`
                    
                    .. attribute:: tags
                    
                    	Tags
                    	**type**\:   :py:class:`Tags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags>`
                    
                    .. attribute:: vlan_inner_id
                    
                    	VLAN Inner ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vlan_outer_id
                    
                    	VLAN Outer ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.access_interface_name = None
                        self.bba_group_name = None
                        self.interface_name_xr = None
                        self.is_complete = None
                        self.local_mac_address = None
                        self.peer_mac_address = None
                        self.session_id = None
                        self.srg_state = None
                        self.tags = Pppoe.Nodes.Node.Interfaces.Interface.Tags()
                        self.tags.parent = self
                        self.vlan_inner_id = None
                        self.vlan_outer_id = None


                    class Tags(object):
                        """
                        Tags
                        
                        .. attribute:: access_loop_encapsulation
                        
                        	Access Loop Encapsulation
                        	**type**\:   :py:class:`AccessLoopEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  str
                        
                        .. attribute:: dsl_actual_delay_down
                        
                        	DSL Actual Delay Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_delay_up
                        
                        	DSL Actual Delay Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_down
                        
                        	DSL Actual Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_actual_up
                        
                        	DSL Actual Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_down
                        
                        	DSL Attain Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_attain_up
                        
                        	DSL Attain Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_down
                        
                        	DSL Max Delay Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_delay_up
                        
                        	DSL Max Delay Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_down
                        
                        	DSL Max Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_max_up
                        
                        	DSL Max Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down
                        
                        	DSL Min Down
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_down_low
                        
                        	DSL Min Down Low
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up
                        
                        	DSL Min Up
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dsl_min_up_low
                        
                        	DSL Min Up Low
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: host_uniq
                        
                        	Host Uniq
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: is_iwf
                        
                        	Is IWF
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: max_payload
                        
                        	Max Payload
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: relay_session_id
                        
                        	Relay Session ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  str
                        
                        .. attribute:: service_name
                        
                        	Service Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.access_loop_encapsulation = Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation()
                            self.access_loop_encapsulation.parent = self
                            self.circuit_id = None
                            self.dsl_actual_delay_down = None
                            self.dsl_actual_delay_up = None
                            self.dsl_actual_down = None
                            self.dsl_actual_up = None
                            self.dsl_attain_down = None
                            self.dsl_attain_up = None
                            self.dsl_max_delay_down = None
                            self.dsl_max_delay_up = None
                            self.dsl_max_down = None
                            self.dsl_max_up = None
                            self.dsl_min_down = None
                            self.dsl_min_down_low = None
                            self.dsl_min_up = None
                            self.dsl_min_up_low = None
                            self.host_uniq = None
                            self.is_iwf = None
                            self.max_payload = None
                            self.relay_session_id = None
                            self.remote_id = None
                            self.service_name = None


                        class AccessLoopEncapsulation(object):
                            """
                            Access Loop Encapsulation
                            
                            .. attribute:: data_link
                            
                            	Data Link
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps1
                            
                            	Encaps 1
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: encaps2
                            
                            	Encaps 2
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_link = None
                                self.encaps1 = None
                                self.encaps2 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-loop-encapsulation'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.data_link is not None:
                                    return True

                                if self.encaps1 is not None:
                                    return True

                                if self.encaps2 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:tags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.access_loop_encapsulation is not None and self.access_loop_encapsulation._has_data():
                                return True

                            if self.circuit_id is not None:
                                return True

                            if self.dsl_actual_delay_down is not None:
                                return True

                            if self.dsl_actual_delay_up is not None:
                                return True

                            if self.dsl_actual_down is not None:
                                return True

                            if self.dsl_actual_up is not None:
                                return True

                            if self.dsl_attain_down is not None:
                                return True

                            if self.dsl_attain_up is not None:
                                return True

                            if self.dsl_max_delay_down is not None:
                                return True

                            if self.dsl_max_delay_up is not None:
                                return True

                            if self.dsl_max_down is not None:
                                return True

                            if self.dsl_max_up is not None:
                                return True

                            if self.dsl_min_down is not None:
                                return True

                            if self.dsl_min_down_low is not None:
                                return True

                            if self.dsl_min_up is not None:
                                return True

                            if self.dsl_min_up_low is not None:
                                return True

                            if self.host_uniq is not None:
                                return True

                            if self.is_iwf is not None:
                                return True

                            if self.max_payload is not None:
                                return True

                            if self.relay_session_id is not None:
                                return True

                            if self.remote_id is not None:
                                return True

                            if self.service_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:interface[Cisco-IOS-XR-subscriber-pppoe-ma-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.access_interface_name is not None:
                            return True

                        if self.bba_group_name is not None:
                            return True

                        if self.interface_name_xr is not None:
                            return True

                        if self.is_complete is not None:
                            return True

                        if self.local_mac_address is not None:
                            return True

                        if self.peer_mac_address is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.srg_state is not None:
                            return True

                        if self.tags is not None and self.tags._has_data():
                            return True

                        if self.vlan_inner_id is not None:
                            return True

                        if self.vlan_outer_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.Interfaces']['meta_info']


            class BbaGroups(object):
                """
                PPPoE BBA\-Group information
                
                .. attribute:: bba_group
                
                	PPPoE BBA\-Group information
                	**type**\: list of    :py:class:`BbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bba_group = YList()
                    self.bba_group.parent = self
                    self.bba_group.name = 'bba_group'


                class BbaGroup(object):
                    """
                    PPPoE BBA\-Group information
                    
                    .. attribute:: bba_group_name  <key>
                    
                    	BBA Group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: limit_config
                    
                    	BBA\-Group limit configuration information
                    	**type**\:   :py:class:`LimitConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig>`
                    
                    .. attribute:: limits
                    
                    	PPPoE session limit information
                    	**type**\:   :py:class:`Limits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits>`
                    
                    .. attribute:: throttle_config
                    
                    	BBA\-Group throttle configuration information
                    	**type**\:   :py:class:`ThrottleConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig>`
                    
                    .. attribute:: throttles
                    
                    	PPPoE throttle information
                    	**type**\:   :py:class:`Throttles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bba_group_name = None
                        self.limit_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig()
                        self.limit_config.parent = self
                        self.limits = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits()
                        self.limits.parent = self
                        self.throttle_config = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig()
                        self.throttle_config.parent = self
                        self.throttles = Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles()
                        self.throttles.parent = self


                    class LimitConfig(object):
                        """
                        BBA\-Group limit configuration information
                        
                        .. attribute:: access_intf
                        
                        	Access Interface
                        	**type**\:   :py:class:`AccessIntf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf>`
                        
                        .. attribute:: card
                        
                        	Card
                        	**type**\:   :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card>`
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:   :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:   :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:   :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId>`
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:   :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf
                        
                        	MAC IWF
                        	**type**\:   :py:class:`MacIwf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:   :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:   :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:   :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.access_intf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf()
                            self.access_intf.parent = self
                            self.card = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card()
                            self.card.parent = self
                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId()
                            self.circuit_id.parent = self
                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac()
                            self.mac.parent = self
                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self.mac_iwf = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf()
                            self.mac_iwf.parent = self
                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId()
                            self.remote_id.parent = self
                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId()
                            self.vlan_id.parent = self


                        class Card(object):
                            """
                            Card
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:card'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card']['meta_info']


                        class AccessIntf(object):
                            """
                            Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:access-intf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf']['meta_info']


                        class Mac(object):
                            """
                            MAC
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac']['meta_info']


                        class MacIwf(object):
                            """
                            MAC IWF
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac-iwf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf']['meta_info']


                        class MacAccessInterface(object):
                            """
                            MAC Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac-access-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface']['meta_info']


                        class MacIwfAccessInterface(object):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac-iwf-access-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface']['meta_info']


                        class CircuitId(object):
                            """
                            Circuit ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:circuit-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId']['meta_info']


                        class RemoteId(object):
                            """
                            Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:remote-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId']['meta_info']


                        class CircuitIdAndRemoteId(object):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:circuit-id-and-remote-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId']['meta_info']


                        class OuterVlanId(object):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:outer-vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId']['meta_info']


                        class InnerVlanId(object):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:inner-vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId']['meta_info']


                        class VlanId(object):
                            """
                            VLAN ID
                            
                            .. attribute:: max_limit
                            
                            	Max Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_enabled
                            
                            	Radius override is enabled
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold
                            
                            	Threshold
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_limit = None
                                self.radius_override_enabled = None
                                self.threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.max_limit is not None:
                                    return True

                                if self.radius_override_enabled is not None:
                                    return True

                                if self.threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:limit-config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.access_intf is not None and self.access_intf._has_data():
                                return True

                            if self.card is not None and self.card._has_data():
                                return True

                            if self.circuit_id is not None and self.circuit_id._has_data():
                                return True

                            if self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id._has_data():
                                return True

                            if self.inner_vlan_id is not None and self.inner_vlan_id._has_data():
                                return True

                            if self.mac is not None and self.mac._has_data():
                                return True

                            if self.mac_access_interface is not None and self.mac_access_interface._has_data():
                                return True

                            if self.mac_iwf is not None and self.mac_iwf._has_data():
                                return True

                            if self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface._has_data():
                                return True

                            if self.outer_vlan_id is not None and self.outer_vlan_id._has_data():
                                return True

                            if self.remote_id is not None and self.remote_id._has_data():
                                return True

                            if self.vlan_id is not None and self.vlan_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']


                    class Limits(object):
                        """
                        PPPoE session limit information
                        
                        .. attribute:: limit
                        
                        	PPPoE session limit state
                        	**type**\: list of    :py:class:`Limit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.limit = YList()
                            self.limit.parent = self
                            self.limit.name = 'limit'


                        class Limit(object):
                            """
                            PPPoE session limit state
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\:  bool
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: override_limit
                            
                            	Overridden limit if set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: radius_override_set
                            
                            	Overridden limit has been set
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: session_count
                            
                            	Session Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:   :py:class:`PppoeMaLimitStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaLimitStateEnum>`
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.circuit_id = None
                                self.inner_vlan_id = None
                                self.interface_name = None
                                self.iwf = None
                                self.mac_address = None
                                self.outer_vlan_id = None
                                self.override_limit = None
                                self.radius_override_set = None
                                self.remote_id = None
                                self.session_count = None
                                self.state = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.circuit_id is not None:
                                    return True

                                if self.inner_vlan_id is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.iwf is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.outer_vlan_id is not None:
                                    return True

                                if self.override_limit is not None:
                                    return True

                                if self.radius_override_set is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                if self.session_count is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:limits'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.limit is not None:
                                for child_ref in self.limit:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits']['meta_info']


                    class Throttles(object):
                        """
                        PPPoE throttle information
                        
                        .. attribute:: throttle
                        
                        	PPPoE session throttle state
                        	**type**\: list of    :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.throttle = YList()
                            self.throttle.parent = self
                            self.throttle.name = 'throttle'


                        class Throttle(object):
                            """
                            PPPoE session throttle state
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: inner_vlan_id
                            
                            	Inner VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: interface_name
                            
                            	Access Interface
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: iwf
                            
                            	IWF flag
                            	**type**\:  bool
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: outer_vlan_id
                            
                            	Outer VLAN ID
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: padi_count
                            
                            	PADI Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: padr_count
                            
                            	PADR Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: since_reset
                            
                            	Number of seconds since counters reset
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\:   :py:class:`PppoeMaThrottleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.PppoeMaThrottleStateEnum>`
                            
                            .. attribute:: time_left
                            
                            	Time left in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.circuit_id = None
                                self.inner_vlan_id = None
                                self.interface_name = None
                                self.iwf = None
                                self.mac_address = None
                                self.outer_vlan_id = None
                                self.padi_count = None
                                self.padr_count = None
                                self.remote_id = None
                                self.since_reset = None
                                self.state = None
                                self.time_left = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:throttle'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.circuit_id is not None:
                                    return True

                                if self.inner_vlan_id is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.iwf is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                if self.outer_vlan_id is not None:
                                    return True

                                if self.padi_count is not None:
                                    return True

                                if self.padr_count is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                if self.since_reset is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.time_left is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:throttles'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.throttle is not None:
                                for child_ref in self.throttle:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles']['meta_info']


                    class ThrottleConfig(object):
                        """
                        BBA\-Group throttle configuration information
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:   :py:class:`CircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId>`
                        
                        .. attribute:: circuit_id_and_remote_id
                        
                        	Circuit ID and Remote ID
                        	**type**\:   :py:class:`CircuitIdAndRemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId>`
                        
                        .. attribute:: inner_vlan_id
                        
                        	Inner VLAN ID
                        	**type**\:   :py:class:`InnerVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId>`
                        
                        .. attribute:: mac
                        
                        	MAC
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac>`
                        
                        .. attribute:: mac_access_interface
                        
                        	MAC Access Interface
                        	**type**\:   :py:class:`MacAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface>`
                        
                        .. attribute:: mac_iwf_access_interface
                        
                        	MAC IWF Access Interface
                        	**type**\:   :py:class:`MacIwfAccessInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface>`
                        
                        .. attribute:: outer_vlan_id
                        
                        	Outer VLAN ID
                        	**type**\:   :py:class:`OuterVlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId>`
                        
                        .. attribute:: vlan_id
                        
                        	VLAN ID
                        	**type**\:   :py:class:`VlanId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper.Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId>`
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.circuit_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId()
                            self.circuit_id.parent = self
                            self.circuit_id_and_remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId()
                            self.circuit_id_and_remote_id.parent = self
                            self.inner_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId()
                            self.inner_vlan_id.parent = self
                            self.mac = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac()
                            self.mac.parent = self
                            self.mac_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface()
                            self.mac_access_interface.parent = self
                            self.mac_iwf_access_interface = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface()
                            self.mac_iwf_access_interface.parent = self
                            self.outer_vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId()
                            self.outer_vlan_id.parent = self
                            self.remote_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId()
                            self.remote_id.parent = self
                            self.vlan_id = Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId()
                            self.vlan_id.parent = self


                        class Mac(object):
                            """
                            MAC
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac']['meta_info']


                        class MacAccessInterface(object):
                            """
                            MAC Access Interface
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac-access-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface']['meta_info']


                        class MacIwfAccessInterface(object):
                            """
                            MAC IWF Access Interface
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:mac-iwf-access-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface']['meta_info']


                        class CircuitId(object):
                            """
                            Circuit ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:circuit-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId']['meta_info']


                        class RemoteId(object):
                            """
                            Remote ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:remote-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId']['meta_info']


                        class CircuitIdAndRemoteId(object):
                            """
                            Circuit ID and Remote ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:circuit-id-and-remote-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId']['meta_info']


                        class OuterVlanId(object):
                            """
                            Outer VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:outer-vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId']['meta_info']


                        class InnerVlanId(object):
                            """
                            Inner VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:inner-vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId']['meta_info']


                        class VlanId(object):
                            """
                            VLAN ID
                            
                            .. attribute:: blocking_period
                            
                            	Blocking Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: limit
                            
                            	Limit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: request_period
                            
                            	Request Period
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'subscriber-pppoe-ma-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.blocking_period = None
                                self.limit = None
                                self.request_period = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:vlan-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.blocking_period is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request_period is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                                return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:throttle-config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.circuit_id is not None and self.circuit_id._has_data():
                                return True

                            if self.circuit_id_and_remote_id is not None and self.circuit_id_and_remote_id._has_data():
                                return True

                            if self.inner_vlan_id is not None and self.inner_vlan_id._has_data():
                                return True

                            if self.mac is not None and self.mac._has_data():
                                return True

                            if self.mac_access_interface is not None and self.mac_access_interface._has_data():
                                return True

                            if self.mac_iwf_access_interface is not None and self.mac_iwf_access_interface._has_data():
                                return True

                            if self.outer_vlan_id is not None and self.outer_vlan_id._has_data():
                                return True

                            if self.remote_id is not None and self.remote_id._has_data():
                                return True

                            if self.vlan_id is not None and self.vlan_id._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                            return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.bba_group_name is None:
                            raise YPYModelError('Key property bba_group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:bba-group[Cisco-IOS-XR-subscriber-pppoe-ma-oper:bba-group-name = ' + str(self.bba_group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bba_group_name is not None:
                            return True

                        if self.limit_config is not None and self.limit_config._has_data():
                            return True

                        if self.limits is not None and self.limits._has_data():
                            return True

                        if self.throttle_config is not None and self.throttle_config._has_data():
                            return True

                        if self.throttles is not None and self.throttles._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                        return meta._meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:bba-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bba_group is not None:
                        for child_ref in self.bba_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.BbaGroups']['meta_info']


            class SummaryTotal(object):
                """
                PPPoE statistics for a given node
                
                .. attribute:: complete_sessions
                
                	Complete Session Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_disconnected_sessions
                
                	Flow Control Disconnected Count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_dropped_sessions
                
                	Flow Control Drop Count
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: flow_control_in_flight_sessions
                
                	Flow Control In\-Flight Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_limit
                
                	Flow Control credit limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow_control_successful_sessions
                
                	Flow Control Success Count, sessions completing call flow
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: incomplete_sessions
                
                	Incomplete Session Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_ready_access_interfaces
                
                	Not Ready Access Interface Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoema_subscriber_infra_flow_control
                
                	PPPoEMASubscriberInfraFlowControl
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ready_access_interfaces
                
                	Ready Access Interface Count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-pppoe-ma-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.complete_sessions = None
                    self.flow_control_disconnected_sessions = None
                    self.flow_control_dropped_sessions = None
                    self.flow_control_in_flight_sessions = None
                    self.flow_control_limit = None
                    self.flow_control_successful_sessions = None
                    self.incomplete_sessions = None
                    self.not_ready_access_interfaces = None
                    self.pppoema_subscriber_infra_flow_control = None
                    self.ready_access_interfaces = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-oper:summary-total'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.complete_sessions is not None:
                        return True

                    if self.flow_control_disconnected_sessions is not None:
                        return True

                    if self.flow_control_dropped_sessions is not None:
                        return True

                    if self.flow_control_in_flight_sessions is not None:
                        return True

                    if self.flow_control_limit is not None:
                        return True

                    if self.flow_control_successful_sessions is not None:
                        return True

                    if self.incomplete_sessions is not None:
                        return True

                    if self.not_ready_access_interfaces is not None:
                        return True

                    if self.pppoema_subscriber_infra_flow_control is not None:
                        return True

                    if self.ready_access_interfaces is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                    return meta._meta_table['Pppoe.Nodes.Node.SummaryTotal']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/Cisco-IOS-XR-subscriber-pppoe-ma-oper:nodes/Cisco-IOS-XR-subscriber-pppoe-ma-oper:node[Cisco-IOS-XR-subscriber-pppoe-ma-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.access_interface is not None and self.access_interface._has_data():
                    return True

                if self.bba_groups is not None and self.bba_groups._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                if self.summary_total is not None and self.summary_total._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
                return meta._meta_table['Pppoe.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe/Cisco-IOS-XR-subscriber-pppoe-ma-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
            return meta._meta_table['Pppoe.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-pppoe-ma-oper:pppoe'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.access_interface_statistics is not None and self.access_interface_statistics._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_oper as meta
        return meta._meta_table['Pppoe']['meta_info']


