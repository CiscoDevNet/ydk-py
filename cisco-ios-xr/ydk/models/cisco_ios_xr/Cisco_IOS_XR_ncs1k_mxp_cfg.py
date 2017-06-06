""" Cisco_IOS_XR_ncs1k_mxp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: NCS1k HW module config

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: ten_gig = 1

    	TenGig

    .. data:: forty_gig = 2

    	FortyGig

    .. data:: hundred_gig = 3

    	HundredGig

    """

    ten_gig = 1

    forty_gig = 2

    hundred_gig = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['ClientDataRateEnum']


class FecEnum(Enum):
    """
    FecEnum

    Fec

    .. data:: sd7 = 1

    	SoftDecision7

    .. data:: sd20 = 2

    	SoftDecision20

    """

    sd7 = 1

    sd20 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['FecEnum']


class TrunkDataRateEnum(Enum):
    """
    TrunkDataRateEnum

    Trunk data rate

    .. data:: hundred_gig = 2

    	HundredGig

    .. data:: two_hundred_gig = 3

    	TwoHundredGig

    .. data:: two_hundred_fifty_gig = 4

    	TwoHundredFiftyGig

    """

    hundred_gig = 2

    two_hundred_gig = 3

    two_hundred_fifty_gig = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['TrunkDataRateEnum']



class HardwareModule(object):
    """
    NCS1k HW module config
    
    .. attribute:: node
    
    	Node
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node>`
    
    

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
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: slice
        
        	Slice to be Provisioned
        	**type**\: list of    :py:class:`Slice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice>`
        
        

        """

        _prefix = 'ncs1k-mxp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location = None
            self.slice = YList()
            self.slice.parent = self
            self.slice.name = 'slice'


        class Slice(object):
            """
            Slice to be Provisioned
            
            .. attribute:: slice_id  <key>
            
            	Set Slice
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: lldp
            
            	Drop LLDP Packets
            	**type**\:  bool
            
            .. attribute:: values
            
            	Data rates & FEC
            	**type**\:   :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.HardwareModule.Node.Slice.Values>`
            
            

            """

            _prefix = 'ncs1k-mxp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.slice_id = None
                self.lldp = None
                self.values = HardwareModule.Node.Slice.Values()
                self.values.parent = self


            class Values(object):
                """
                Data rates & FEC
                
                .. attribute:: client_rate
                
                	Client Rate
                	**type**\:   :py:class:`ClientDataRateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.ClientDataRateEnum>`
                
                .. attribute:: encrypted
                
                	Encrypted
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: fec
                
                	FEC
                	**type**\:   :py:class:`FecEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.FecEnum>`
                
                .. attribute:: trunk_rate
                
                	TrunkRate
                	**type**\:   :py:class:`TrunkDataRateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg.TrunkDataRateEnum>`
                
                

                """

                _prefix = 'ncs1k-mxp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_rate = None
                    self.encrypted = None
                    self.fec = None
                    self.trunk_rate = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-cfg:values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.client_rate is not None:
                        return True

                    if self.encrypted is not None:
                        return True

                    if self.fec is not None:
                        return True

                    if self.trunk_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
                    return meta._meta_table['HardwareModule.Node.Slice.Values']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.slice_id is None:
                    raise YPYModelError('Key property slice_id is None')

                return self.parent._common_path +'/Cisco-IOS-XR-ncs1k-mxp-cfg:slice[Cisco-IOS-XR-ncs1k-mxp-cfg:slice-id = ' + str(self.slice_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.slice_id is not None:
                    return True

                if self.lldp is not None:
                    return True

                if self.values is not None and self.values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
                return meta._meta_table['HardwareModule.Node.Slice']['meta_info']

        @property
        def _common_path(self):
            if self.location is None:
                raise YPYModelError('Key property location is None')

            return '/Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module/Cisco-IOS-XR-ncs1k-mxp-cfg:node[Cisco-IOS-XR-ncs1k-mxp-cfg:location = ' + str(self.location) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.location is not None:
                return True

            if self.slice is not None:
                for child_ref in self.slice:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
            return meta._meta_table['HardwareModule.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs1k-mxp-cfg:hardware-module'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs1k_mxp_cfg as meta
        return meta._meta_table['HardwareModule']['meta_info']


