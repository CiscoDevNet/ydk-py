""" Cisco_IOS_XE_cfm_oper 

This module contains a collection of YANG definitions for
monitoring memory usage of processes in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CfmLastClearedTypeEnum(Enum):
    """
    CfmLastClearedTypeEnum

    .. data:: never_cleared = 0

    .. data:: cleared_before = 1

    """

    never_cleared = 0

    cleared_before = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_cfm_oper as meta
        return meta._meta_table['CfmLastClearedTypeEnum']



class CfmStatistics(object):
    """
    Data nodes for CFM Statistics.
    
    .. attribute:: cfm_meps
    
    	
    	**type**\:   :py:class:`CfmMeps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps>`
    
    

    """

    _prefix = 'cfm-stats-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.cfm_meps = CfmStatistics.CfmMeps()
        self.cfm_meps.parent = self


    class CfmMeps(object):
        """
        
        
        .. attribute:: cfm_mep
        
        	The list of MEP entries in the system
        	**type**\: list of    :py:class:`CfmMep <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep>`
        
        

        """

        _prefix = 'cfm-stats-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.cfm_mep = YList()
            self.cfm_mep.parent = self
            self.cfm_mep.name = 'cfm_mep'


        class CfmMep(object):
            """
            The list of MEP entries in the system.
            
            .. attribute:: domain_name  <key>
            
            	The name of the Domain corresponding the the MEP
            	**type**\:  str
            
            .. attribute:: ma_name  <key>
            
            	The name of the MA corresponding the the MEP
            	**type**\:  str
            
            .. attribute:: mpid  <key>
            
            	ID of the MEP
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccm_seq_errors
            
            	The number of CCM sequence number errors detected
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ccm_transmitted
            
            	The number of CCMs transmitted from the local MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_cleared
            
            	
            	**type**\:   :py:class:`LastCleared <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep.LastCleared>`
            
            .. attribute:: lbr_received_bad
            
            	The number of loopback reply packets received  with corrupted data pattern
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_received_ok
            
            	The number of valid loopback reply packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_seq_errors
            
            	The number of loopback reply packets received  with sequence number errors
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_transmitted
            
            	The number of loopback reply packets transmitted from the local MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ltr_unexpected
            
            	The number of unexpected linktrace reply packets  received at this MEP
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cfm-stats-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.domain_name = None
                self.ma_name = None
                self.mpid = None
                self.ccm_seq_errors = None
                self.ccm_transmitted = None
                self.last_cleared = CfmStatistics.CfmMeps.CfmMep.LastCleared()
                self.last_cleared.parent = self
                self.lbr_received_bad = None
                self.lbr_received_ok = None
                self.lbr_seq_errors = None
                self.lbr_transmitted = None
                self.ltr_unexpected = None


            class LastCleared(object):
                """
                
                
                .. attribute:: never
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: time
                
                	
                	**type**\:  str
                
                

                """

                _prefix = 'cfm-stats-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.never = None
                    self.time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-cfm-oper:last-cleared'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.never is not None:
                        return True

                    if self.time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_cfm_oper as meta
                    return meta._meta_table['CfmStatistics.CfmMeps.CfmMep.LastCleared']['meta_info']

            @property
            def _common_path(self):
                if self.domain_name is None:
                    raise YPYModelError('Key property domain_name is None')
                if self.ma_name is None:
                    raise YPYModelError('Key property ma_name is None')
                if self.mpid is None:
                    raise YPYModelError('Key property mpid is None')

                return '/Cisco-IOS-XE-cfm-oper:cfm-statistics/Cisco-IOS-XE-cfm-oper:cfm-meps/Cisco-IOS-XE-cfm-oper:cfm-mep[Cisco-IOS-XE-cfm-oper:domain-name = ' + str(self.domain_name) + '][Cisco-IOS-XE-cfm-oper:ma-name = ' + str(self.ma_name) + '][Cisco-IOS-XE-cfm-oper:mpid = ' + str(self.mpid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.domain_name is not None:
                    return True

                if self.ma_name is not None:
                    return True

                if self.mpid is not None:
                    return True

                if self.ccm_seq_errors is not None:
                    return True

                if self.ccm_transmitted is not None:
                    return True

                if self.last_cleared is not None and self.last_cleared._has_data():
                    return True

                if self.lbr_received_bad is not None:
                    return True

                if self.lbr_received_ok is not None:
                    return True

                if self.lbr_seq_errors is not None:
                    return True

                if self.lbr_transmitted is not None:
                    return True

                if self.ltr_unexpected is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_cfm_oper as meta
                return meta._meta_table['CfmStatistics.CfmMeps.CfmMep']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-cfm-oper:cfm-statistics/Cisco-IOS-XE-cfm-oper:cfm-meps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cfm_mep is not None:
                for child_ref in self.cfm_mep:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_cfm_oper as meta
            return meta._meta_table['CfmStatistics.CfmMeps']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-cfm-oper:cfm-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cfm_meps is not None and self.cfm_meps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_cfm_oper as meta
        return meta._meta_table['CfmStatistics']['meta_info']


