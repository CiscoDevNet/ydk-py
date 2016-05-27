""" Cisco_IOS_XR_ncs1k_mxp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package operational data.

This module contains definitions
for the following management objects\:
  hw\-module\: mxp hw\-module command chain

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class HwModuleSliceStatusEnum(Enum):
    """
    HwModuleSliceStatusEnum

    Hw module slice status

    .. data:: NOT_PROVISIONED = 0

    	Not Provisioned

    .. data:: PROVISIONING_IN_PROGRESS = 1

    	Provisioning In-Progress

    .. data:: PROVISIONED = 2

    	Provisioned

    .. data:: PROVISIONING_FAILED = 3

    	Provisioning Failed

    .. data:: PROVISIONING_SCHEDULED = 4

    	Provisioning Scheduled

    """

    NOT_PROVISIONED = 0

    PROVISIONING_IN_PROGRESS = 1

    PROVISIONED = 2

    PROVISIONING_FAILED = 3

    PROVISIONING_SCHEDULED = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
        return meta._meta_table['HwModuleSliceStatusEnum']



class HwModule(object):
    """
    mxp hw\-module command chain
    
    .. attribute:: slice_ids
    
    	Slice information
    	**type**\: :py:class:`SliceIds <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds>`
    
    .. attribute:: slice_all
    
    	Information for all slices
    	**type**\: :py:class:`SliceAll <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll>`
    
    

    """

    _prefix = 'ncs1k-mxp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.slice_ids = HwModule.SliceIds()
        self.slice_ids.parent = self
        self.slice_all = HwModule.SliceAll()
        self.slice_all.parent = self


    class SliceIds(object):
        """
        Slice information
        
        .. attribute:: slice_id
        
        	Per slice num data
        	**type**\: list of :py:class:`SliceId <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.slice_id = YList()
            self.slice_id.parent = self
            self.slice_id.name = 'slice_id'


        class SliceId(object):
            """
            Per slice num data
            
            .. attribute:: slice_num  <key>
            
            	Details associated with a particular slice number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slice_info
            
            	slice info
            	**type**\: list of :py:class:`SliceInfo <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo>`
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.slice_num = None
                self.slice_info = YList()
                self.slice_info.parent = self
                self.slice_info.name = 'slice_info'


            class SliceInfo(object):
                """
                slice info
                
                .. attribute:: slice_id
                
                	SliceId
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: client_rate
                
                	ClientRate
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: hardware_status
                
                	HardwareStatus
                	**type**\: :py:class:`HwModuleSliceStatusEnum <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatusEnum>`
                
                .. attribute:: dp_fpg_ver
                
                	DpFpgVer
                	**type**\: str
                
                	**range:** 0..16
                
                .. attribute:: client_port
                
                	client port
                	**type**\: list of :py:class:`ClientPort <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo.ClientPort>`
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slice_id = None
                    self.client_rate = None
                    self.trunk_rate = None
                    self.hardware_status = None
                    self.dp_fpg_ver = None
                    self.client_port = YList()
                    self.client_port.parent = self
                    self.client_port.name = 'client_port'


                class ClientPort(object):
                    """
                    client port
                    
                    .. attribute:: client_name
                    
                    	ClientName
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: trunk_port
                    
                    	trunk port
                    	**type**\: list of :py:class:`TrunkPort <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort>`
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.client_name = None
                        self.trunk_port = YList()
                        self.trunk_port.parent = self
                        self.trunk_port.name = 'trunk_port'


                    class TrunkPort(object):
                        """
                        trunk port
                        
                        .. attribute:: trunk_name
                        
                        	TrunkName
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: percentage
                        
                        	Percentage
                        	**type**\: str
                        
                        	**range:** 0..8
                        
                        

                        """

                        _prefix = 'ncs1k-mxp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.trunk_name = None
                            self.percentage = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-oper:trunk-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.trunk_name is not None:
                                return True

                            if self.percentage is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                            return meta._meta_table['HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-oper:client-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.client_name is not None:
                            return True

                        if self.trunk_port is not None:
                            for child_ref in self.trunk_port:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                        return meta._meta_table['HwModule.SliceIds.SliceId.SliceInfo.ClientPort']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-oper:slice-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.slice_id is not None:
                        return True

                    if self.client_rate is not None:
                        return True

                    if self.trunk_rate is not None:
                        return True

                    if self.hardware_status is not None:
                        return True

                    if self.dp_fpg_ver is not None:
                        return True

                    if self.client_port is not None:
                        for child_ref in self.client_port:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                    return meta._meta_table['HwModule.SliceIds.SliceId.SliceInfo']['meta_info']

            @property
            def _common_path(self):
                if self.slice_num is None:
                    raise YPYDataValidationError('Key property slice_num is None')

                return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-ids/Cisco-IOS-XR-ncs1k-mxp-oper:slice-id[Cisco-IOS-XR-ncs1k-mxp-oper:slice-num = ' + str(self.slice_num) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.slice_num is not None:
                    return True

                if self.slice_info is not None:
                    for child_ref in self.slice_info:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                return meta._meta_table['HwModule.SliceIds.SliceId']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-ids'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.slice_id is not None:
                for child_ref in self.slice_id:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
            return meta._meta_table['HwModule.SliceIds']['meta_info']


    class SliceAll(object):
        """
        Information for all slices
        
        .. attribute:: slice_info
        
        	slice info
        	**type**\: list of :py:class:`SliceInfo <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.slice_info = YList()
            self.slice_info.parent = self
            self.slice_info.name = 'slice_info'


        class SliceInfo(object):
            """
            slice info
            
            .. attribute:: slice_id
            
            	SliceId
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_rate
            
            	ClientRate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: trunk_rate
            
            	TrunkRate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hardware_status
            
            	HardwareStatus
            	**type**\: :py:class:`HwModuleSliceStatusEnum <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatusEnum>`
            
            .. attribute:: dp_fpg_ver
            
            	DpFpgVer
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: client_port
            
            	client port
            	**type**\: list of :py:class:`ClientPort <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort>`
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.slice_id = None
                self.client_rate = None
                self.trunk_rate = None
                self.hardware_status = None
                self.dp_fpg_ver = None
                self.client_port = YList()
                self.client_port.parent = self
                self.client_port.name = 'client_port'


            class ClientPort(object):
                """
                client port
                
                .. attribute:: client_name
                
                	ClientName
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: trunk_port
                
                	trunk port
                	**type**\: list of :py:class:`TrunkPort <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort>`
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_name = None
                    self.trunk_port = YList()
                    self.trunk_port.parent = self
                    self.trunk_port.name = 'trunk_port'


                class TrunkPort(object):
                    """
                    trunk port
                    
                    .. attribute:: trunk_name
                    
                    	TrunkName
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: percentage
                    
                    	Percentage
                    	**type**\: str
                    
                    	**range:** 0..8
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.trunk_name = None
                        self.percentage = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-all/Cisco-IOS-XR-ncs1k-mxp-oper:slice-info/Cisco-IOS-XR-ncs1k-mxp-oper:client-port/Cisco-IOS-XR-ncs1k-mxp-oper:trunk-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.trunk_name is not None:
                            return True

                        if self.percentage is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                        return meta._meta_table['HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-all/Cisco-IOS-XR-ncs1k-mxp-oper:slice-info/Cisco-IOS-XR-ncs1k-mxp-oper:client-port'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.client_name is not None:
                        return True

                    if self.trunk_port is not None:
                        for child_ref in self.trunk_port:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                    return meta._meta_table['HwModule.SliceAll.SliceInfo.ClientPort']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-all/Cisco-IOS-XR-ncs1k-mxp-oper:slice-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.slice_id is not None:
                    return True

                if self.client_rate is not None:
                    return True

                if self.trunk_rate is not None:
                    return True

                if self.hardware_status is not None:
                    return True

                if self.dp_fpg_ver is not None:
                    return True

                if self.client_port is not None:
                    for child_ref in self.client_port:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
                return meta._meta_table['HwModule.SliceAll.SliceInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/Cisco-IOS-XR-ncs1k-mxp-oper:slice-all'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.slice_info is not None:
                for child_ref in self.slice_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
            return meta._meta_table['HwModule.SliceAll']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-oper:hw-module'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.slice_ids is not None and self.slice_ids._has_data():
            return True

        if self.slice_all is not None and self.slice_all._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_oper as meta
        return meta._meta_table['HwModule']['meta_info']


