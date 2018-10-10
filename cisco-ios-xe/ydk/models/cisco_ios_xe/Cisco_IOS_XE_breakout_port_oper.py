""" Cisco_IOS_XE_breakout_port_oper 

This module contains a collection of YANG definitions for
monitoring breakout ports in a Network Element.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BcChannelSpeed(Enum):
    """
    BcChannelSpeed (Enum Class)

    Speed of each channel

    .. data:: Y_10gb = 0

    .. data:: unknown = 1

    """

    Y_10gb = Enum.YLeaf(0, "10gb")

    unknown = Enum.YLeaf(1, "unknown")



class BreakoutPortOperData(Entity):
    """
    Informaton about breakout ports
    
    .. attribute:: port_breakout
    
    	List of breakout ports, keyed by name
    	**type**\: list of  		 :py:class:`PortBreakout <ydk.models.cisco_ios_xe.Cisco_IOS_XE_breakout_port_oper.BreakoutPortOperData.PortBreakout>`
    
    

    """

    _prefix = 'bc-port-ios-xe-oper'
    _revision = '2018-01-02'

    def __init__(self):
        super(BreakoutPortOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "breakout-port-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-breakout-port-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("port-breakout", ("port_breakout", BreakoutPortOperData.PortBreakout))])
        self._leafs = OrderedDict()

        self.port_breakout = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-breakout-port-oper:breakout-port-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(BreakoutPortOperData, [], name, value)


    class PortBreakout(Entity):
        """
        List of breakout ports, keyed by name
        
        .. attribute:: name  (key)
        
        	Name of the breakout port
        	**type**\: str
        
        .. attribute:: number
        
        	Number of channels to 'breakout' on a port capable of channelization
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: speed
        
        	Channel speed on each channel
        	**type**\:  :py:class:`BcChannelSpeed <ydk.models.cisco_ios_xe.Cisco_IOS_XE_breakout_port_oper.BcChannelSpeed>`
        
        

        """

        _prefix = 'bc-port-ios-xe-oper'
        _revision = '2018-01-02'

        def __init__(self):
            super(BreakoutPortOperData.PortBreakout, self).__init__()

            self.yang_name = "port-breakout"
            self.yang_parent_name = "breakout-port-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('number', (YLeaf(YType.int16, 'number'), ['int'])),
                ('speed', (YLeaf(YType.enumeration, 'speed'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_breakout_port_oper', 'BcChannelSpeed', '')])),
            ])
            self.name = None
            self.number = None
            self.speed = None
            self._segment_path = lambda: "port-breakout" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-breakout-port-oper:breakout-port-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(BreakoutPortOperData.PortBreakout, ['name', 'number', 'speed'], name, value)

    def clone_ptr(self):
        self._top_entity = BreakoutPortOperData()
        return self._top_entity

