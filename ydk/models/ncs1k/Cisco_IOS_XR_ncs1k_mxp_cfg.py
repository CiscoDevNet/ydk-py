""" Cisco_IOS_XR_ncs1k_mxp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ClientDataRateEnum(Enum):
    """
    ClientDataRateEnum

    Client data rate

    .. data:: TEN_GIG = 1

    	TenGig

    .. data:: FORTY_GIG = 2

    	FortyGig

    .. data:: HUNDRED_GIG = 3

    	HundredGig

    """

    TEN_GIG = 1

    FORTY_GIG = 2

    HUNDRED_GIG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['ClientDataRateEnum']


class FecEnum(Enum):
    """
    FecEnum

    Fec

    .. data:: SD7 = 1

    	SoftDecision7

    .. data:: SD20 = 2

    	SoftDecision20

    """

    SD7 = 1

    SD20 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['FecEnum']


class TrunkDataRateEnum(Enum):
    """
    TrunkDataRateEnum

    Trunk data rate

    .. data:: HUNDRED_GIG = 2

    	HundredGig

    .. data:: TWO_HUNDRED_GIG = 3

    	TwoHundredGig

    .. data:: TWO_HUNDRED_FIFTY_GIG = 4

    	TwoHundredFiftyGig

    """

    HUNDRED_GIG = 2

    TWO_HUNDRED_GIG = 3

    TWO_HUNDRED_FIFTY_GIG = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['TrunkDataRateEnum']



class HardwareModule(object):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of :py:class:`Node <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node>`
    
    

    """

    _prefix = 'ncs1k-mxp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.node = YList()
        self.node.parent = self
        self.node.name = 'node'


    class Node(object):
        """
        Node
        
        .. attribute:: location  <key>
        
        	Fully qualified line card specification
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: values
        
        	Slice to be Provisioned
        	**type**\: :py:class:`Values <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Values>`
        
        

        """

        _prefix = 'ncs1k-mxp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location = None
            self.values = HardwareModule.Node.Values()
            self.values.parent = self


        class Values(object):
            """
            Slice to be Provisioned
            
            .. attribute:: value
            
            	Data rates & FEC
            	**type**\: list of :py:class:`Value <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Values.Value>`
            
            

            """

            _prefix = 'ncs1k-mxp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.value = YList()
                self.value.parent = self
                self.value.name = 'value'


            class Value(object):
                """
                Data rates & FEC
                
                .. attribute:: slice_id  <key>
                
                	Set Slice
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: client_rate
                
                	Client Rate
                	**type**\: :py:class:`ClientDataRateEnum <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.ClientDataRateEnum>`
                
                .. attribute:: fec
                
                	FEC
                	**type**\: :py:class:`FecEnum <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.FecEnum>`
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\: :py:class:`TrunkDataRateEnum <ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg.TrunkDataRateEnum>`
                
                

                """

                _prefix = 'ncs1k-mxp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slice_id = None
                    self.client_rate = None
                    self.fec = None
                    self.trunk_rate = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.slice_id is None:
                        raise YPYModelError('Key property slice_id is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-cfg:value[Cisco-IOS-XR-ncs1k-mxp-cfg:slice-id = ' + str(self.slice_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.slice_id is not None:
                        return True

                    if self.client_rate is not None:
                        return True

                    if self.fec is not None:
                        return True

                    if self.trunk_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
                    return meta._meta_table['HardwareModule.Node.Values.Value']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-cfg:values'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.value is not None:
                    for child_ref in self.value:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
                return meta._meta_table['HardwareModule.Node.Values']['meta_info']

        @property
        def _common_path(self):
            if self.location is None:
                raise YPYModelError('Key property location is None')

            return '/Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module/Cisco-IOS-XR-ncs1k-mxp-cfg:node[Cisco-IOS-XR-ncs1k-mxp-cfg:location = ' + str(self.location) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.location is not None:
                return True

            if self.values is not None and self.values._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
            return meta._meta_table['HardwareModule.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ncs1k._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['HardwareModule']['meta_info']


