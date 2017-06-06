""" Cisco_IOS_XR_asr9k_lc_fca_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-fca package operational data.

This module contains definitions
for the following management objects\:
  mpa\-internal\: Management LAN Operational data space
  mpa\: mpa

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SpaFailureReasonEnum(Enum):
    """
    SpaFailureReasonEnum

    SPA failure reasons

    .. data:: spa_failure_reason_unknown = 1

    	spa failure reason unknown

    .. data:: spa_failure_reason_spi_failure = 2

    	spa failure reason spi failure

    .. data:: spa_failure_reason_boot = 3

    	spa failure reason boot

    .. data:: spa_failure_reason_hw_failed = 4

    	spa failure reason hw failed

    .. data:: spa_failure_reason_sw_failed = 5

    	spa failure reason sw failed

    .. data:: spa_failure_reason_sw_restart = 6

    	spa failure reason sw restart

    .. data:: spa_failure_reason_check_fpd = 7

    	spa failure reason check fpd

    .. data:: spa_failure_reason_read_type = 8

    	spa failure reason read type

    """

    spa_failure_reason_unknown = 1

    spa_failure_reason_spi_failure = 2

    spa_failure_reason_boot = 3

    spa_failure_reason_hw_failed = 4

    spa_failure_reason_sw_failed = 5

    spa_failure_reason_sw_restart = 6

    spa_failure_reason_check_fpd = 7

    spa_failure_reason_read_type = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
        return meta._meta_table['SpaFailureReasonEnum']


class SpaOperStateEnum(Enum):
    """
    SpaOperStateEnum

    SPA operational states

    .. data:: spa_state_reset = 1

    	spa state reset

    .. data:: spa_state_failed = 2

    	spa state failed

    .. data:: spa_state_booting = 3

    	spa state booting

    .. data:: spa_state_ready = 4

    	spa state ready

    """

    spa_state_reset = 1

    spa_state_failed = 2

    spa_state_booting = 3

    spa_state_ready = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
        return meta._meta_table['SpaOperStateEnum']


class SpaResetReasonEnum(Enum):
    """
    SpaResetReasonEnum

    SPA reset reasons

    .. data:: spa_reset_reason_unknown = 1

    	spa reset reason unknown

    .. data:: spa_reset_reason_manual = 2

    	spa reset reason manual

    .. data:: spa_reset_reason_fpd_upgrade = 3

    	spa reset reason fpd upgrade

    .. data:: spa_reset_reason_audit_fail = 4

    	spa reset reason audit fail

    .. data:: spa_reset_reason_failure = 5

    	spa reset reason failure

    """

    spa_reset_reason_unknown = 1

    spa_reset_reason_manual = 2

    spa_reset_reason_fpd_upgrade = 3

    spa_reset_reason_audit_fail = 4

    spa_reset_reason_failure = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
        return meta._meta_table['SpaResetReasonEnum']



class MpaInternal(object):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = MpaInternal.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of    :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.bay = YList()
                self.bay.parent = self
                self.bay.name = 'bay'


            class Bay(object):
                """
                Number
                
                .. attribute:: number  <key>
                
                	bay number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ifsubsies
                
                	Table of Ifsubsys
                	**type**\:   :py:class:`Ifsubsies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.number = None
                    self.ifsubsies = MpaInternal.Nodes.Node.Bay.Ifsubsies()
                    self.ifsubsies.parent = self


                class Ifsubsies(object):
                    """
                    Table of Ifsubsys
                    
                    .. attribute:: ifsubsy
                    
                    	Number
                    	**type**\: list of    :py:class:`Ifsubsy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ifsubsy = YList()
                        self.ifsubsy.parent = self
                        self.ifsubsy.name = 'ifsubsy'


                    class Ifsubsy(object):
                        """
                        Number
                        
                        .. attribute:: number  <key>
                        
                        	ifsubsys number
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: mpa_internal_info
                        
                        	mpa internal info
                        	**type**\:   :py:class:`MpaInternalInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.number = None
                            self.mpa_internal_info = MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo()
                            self.mpa_internal_info.parent = self


                        class MpaInternalInfo(object):
                            """
                            mpa internal info
                            
                            .. attribute:: bay
                            
                            	bay
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ep_idprom_data
                            
                            	ep idprom data
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: ep_idprom_major
                            
                            	ep idprom major
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_idprom_minor
                            
                            	ep idprom minor
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_presence
                            
                            	ep presence
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_state
                            
                            	ep state
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_type
                            
                            	ep type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: if_event
                            
                            	if event
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: if_state
                            
                            	if state
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ifsubsys
                            
                            	ifsubsys
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-fca-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bay = None
                                self.ep_idprom_data = None
                                self.ep_idprom_major = None
                                self.ep_idprom_minor = None
                                self.ep_presence = None
                                self.ep_state = None
                                self.ep_type = None
                                self.if_event = None
                                self.if_state = None
                                self.ifsubsys = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.bay is not None:
                                    return True

                                if self.ep_idprom_data is not None:
                                    return True

                                if self.ep_idprom_major is not None:
                                    return True

                                if self.ep_idprom_minor is not None:
                                    return True

                                if self.ep_presence is not None:
                                    return True

                                if self.ep_state is not None:
                                    return True

                                if self.ep_type is not None:
                                    return True

                                if self.if_event is not None:
                                    return True

                                if self.if_state is not None:
                                    return True

                                if self.ifsubsys is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                                return meta._meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.number is None:
                                raise YPYModelError('Key property number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:ifsubsy[Cisco-IOS-XR-asr9k-lc-fca-oper:number = ' + str(self.number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.number is not None:
                                return True

                            if self.mpa_internal_info is not None and self.mpa_internal_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                            return meta._meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:ifsubsies'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ifsubsy is not None:
                            for child_ref in self.ifsubsy:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                        return meta._meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.number is None:
                        raise YPYModelError('Key property number is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:bay[Cisco-IOS-XR-asr9k-lc-fca-oper:number = ' + str(self.number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.number is not None:
                        return True

                    if self.ifsubsies is not None and self.ifsubsies._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                    return meta._meta_table['MpaInternal.Nodes.Node.Bay']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/Cisco-IOS-XR-asr9k-lc-fca-oper:nodes/Cisco-IOS-XR-asr9k-lc-fca-oper:node[Cisco-IOS-XR-asr9k-lc-fca-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.bay is not None:
                    for child_ref in self.bay:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                return meta._meta_table['MpaInternal.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/Cisco-IOS-XR-asr9k-lc-fca-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
            return meta._meta_table['MpaInternal.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
        return meta._meta_table['MpaInternal']['meta_info']


class Mpa(object):
    """
    mpa
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Mpa.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Number
            
            .. attribute:: node  <key>
            
            	node number
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of    :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.bay = YList()
                self.bay.parent = self
                self.bay.name = 'bay'


            class Bay(object):
                """
                Number
                
                .. attribute:: number  <key>
                
                	bay number
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: mpa_detail_table
                
                	Table of Mpa Detail Info
                	**type**\:   :py:class:`MpaDetailTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.number = None
                    self.mpa_detail_table = Mpa.Nodes.Node.Bay.MpaDetailTable()
                    self.mpa_detail_table.parent = self


                class MpaDetailTable(object):
                    """
                    Table of Mpa Detail Info
                    
                    .. attribute:: mpa_detail
                    
                    	mpa detail status info
                    	**type**\:   :py:class:`MpaDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mpa_detail = Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail()
                        self.mpa_detail.parent = self


                    class MpaDetail(object):
                        """
                        mpa detail status info
                        
                        .. attribute:: bay_number
                        
                        	BAY number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: insertion_time
                        
                        	Time when SPA last insertedin calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: is_spa_admin_up
                        
                        	If SPA admin state is Up
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_in_reset
                        
                        	If SPA in reset
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_inserted
                        
                        	If SPA inserted
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_power_admin_up
                        
                        	If SPA power admin state is Up
                        	**type**\:  bool
                        
                        .. attribute:: is_spa_powered
                        
                        	If SPA powered
                        	**type**\:  bool
                        
                        .. attribute:: last_failure_reason
                        
                        	Last Failure Reason
                        	**type**\:   :py:class:`SpaFailureReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaFailureReasonEnum>`
                        
                        .. attribute:: last_ready_time
                        
                        	Time when SPA last reached Ready statein calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: last_reset_reason
                        
                        	Last reset reason
                        	**type**\:   :py:class:`SpaResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaResetReasonEnum>`
                        
                        .. attribute:: spa_oper_state
                        
                        	SPA operational state
                        	**type**\:   :py:class:`SpaOperStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaOperStateEnum>`
                        
                        .. attribute:: spa_type
                        
                        	SPA type
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: up_time
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bay_number = None
                            self.insertion_time = None
                            self.is_spa_admin_up = None
                            self.is_spa_in_reset = None
                            self.is_spa_inserted = None
                            self.is_spa_power_admin_up = None
                            self.is_spa_powered = None
                            self.last_failure_reason = None
                            self.last_ready_time = None
                            self.last_reset_reason = None
                            self.spa_oper_state = None
                            self.spa_type = None
                            self.up_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-detail'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bay_number is not None:
                                return True

                            if self.insertion_time is not None:
                                return True

                            if self.is_spa_admin_up is not None:
                                return True

                            if self.is_spa_in_reset is not None:
                                return True

                            if self.is_spa_inserted is not None:
                                return True

                            if self.is_spa_power_admin_up is not None:
                                return True

                            if self.is_spa_powered is not None:
                                return True

                            if self.last_failure_reason is not None:
                                return True

                            if self.last_ready_time is not None:
                                return True

                            if self.last_reset_reason is not None:
                                return True

                            if self.spa_oper_state is not None:
                                return True

                            if self.spa_type is not None:
                                return True

                            if self.up_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                            return meta._meta_table['Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-detail-table'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mpa_detail is not None and self.mpa_detail._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                        return meta._meta_table['Mpa.Nodes.Node.Bay.MpaDetailTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.number is None:
                        raise YPYModelError('Key property number is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-lc-fca-oper:bay[Cisco-IOS-XR-asr9k-lc-fca-oper:number = ' + str(self.number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.number is not None:
                        return True

                    if self.mpa_detail_table is not None and self.mpa_detail_table._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                    return meta._meta_table['Mpa.Nodes.Node.Bay']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/Cisco-IOS-XR-asr9k-lc-fca-oper:nodes/Cisco-IOS-XR-asr9k-lc-fca-oper:node[Cisco-IOS-XR-asr9k-lc-fca-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    return True

                if self.bay is not None:
                    for child_ref in self.bay:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
                return meta._meta_table['Mpa.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/Cisco-IOS-XR-asr9k-lc-fca-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
            return meta._meta_table['Mpa.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-lc-fca-oper:mpa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_fca_oper as meta
        return meta._meta_table['Mpa']['meta_info']


