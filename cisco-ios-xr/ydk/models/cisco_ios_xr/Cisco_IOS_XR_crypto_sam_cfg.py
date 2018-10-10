""" Cisco_IOS_XR_crypto_sam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package configuration.

This module contains definitions
for the following management objects\:
  sam\: Software Authentication Manager (SAM) Config

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CryptoSamAction(Enum):
    """
    CryptoSamAction (Enum Class)

    Crypto sam action

    .. data:: proceed = 1

    	To respond YES to the SAM prompt

    .. data:: terminate = 2

    	To respond NO to the SAM prompt

    """

    proceed = Enum.YLeaf(1, "proceed")

    terminate = Enum.YLeaf(2, "terminate")



class Sam(Entity):
    """
    Software Authentication Manager (SAM) Config
    
    .. attribute:: prompt_interval
    
    	Set prompt interval at reboot time
    	**type**\:  :py:class:`PromptInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.Sam.PromptInterval>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'crypto-sam-cfg'
    _revision = '2017-11-21'

    def __init__(self):
        super(Sam, self).__init__()
        self._top_entity = None

        self.yang_name = "sam"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-sam-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("prompt-interval", ("prompt_interval", Sam.PromptInterval))])
        self._leafs = OrderedDict()

        self.prompt_interval = None
        self._children_name_map["prompt_interval"] = "prompt-interval"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:sam"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sam, [], name, value)


    class PromptInterval(Entity):
        """
        Set prompt interval at reboot time
        
        .. attribute:: action
        
        	Respond to SAM prompt either Proceed/Terminate
        	**type**\:  :py:class:`CryptoSamAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg.CryptoSamAction>`
        
        	**mandatory**\: True
        
        .. attribute:: prompt_time
        
        	Prompt time from 0 \- 300 seconds
        	**type**\: int
        
        	**range:** 0..300
        
        	**mandatory**\: True
        
        	**units**\: second
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'crypto-sam-cfg'
        _revision = '2017-11-21'

        def __init__(self):
            super(Sam.PromptInterval, self).__init__()

            self.yang_name = "prompt-interval"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'CryptoSamAction', '')])),
                ('prompt_time', (YLeaf(YType.uint32, 'prompt-time'), ['int'])),
            ])
            self.action = None
            self.prompt_time = None
            self._segment_path = lambda: "prompt-interval"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-cfg:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.PromptInterval, ['action', 'prompt_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Sam()
        return self._top_entity

