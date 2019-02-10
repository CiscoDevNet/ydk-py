""" Cisco_IOS_XE_transceiver_oper 

This module contains a collection of YANG definitions for
monitoring transceivers in a Network Element.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class XcvrOtnCode(Enum):
    """
    XcvrOtnCode (Enum Class)

    OTN application code supported by the port

    .. data:: p1l1_2d1 = 0

    .. data:: p1s1_2d2 = 1

    .. data:: p1l1_2d2 = 2

    .. data:: otn_undefined = 3

    """

    p1l1_2d1 = Enum.YLeaf(0, "p1l1-2d1")

    p1s1_2d2 = Enum.YLeaf(1, "p1s1-2d2")

    p1l1_2d2 = Enum.YLeaf(2, "p1l1-2d2")

    otn_undefined = Enum.YLeaf(3, "otn-undefined")


class XcvrSonetCode(Enum):
    """
    XcvrSonetCode (Enum Class)

    SONET/SDH application code supported by the port

    .. data:: oc_48_short_reach = 0

    .. data:: oc_48_intermediate_reach = 1

    .. data:: oc_48_long_reach = 2

    .. data:: sonet_sr_compliant = 3

    .. data:: sonet_lr_compliant = 4

    .. data:: oc_192_short_reach = 5

    .. data:: escon_smf_1310_laser = 6

    .. data:: escon_mmf_1310_led = 7

    .. data:: unknown = 8

    """

    oc_48_short_reach = Enum.YLeaf(0, "oc-48-short-reach")

    oc_48_intermediate_reach = Enum.YLeaf(1, "oc-48-intermediate-reach")

    oc_48_long_reach = Enum.YLeaf(2, "oc-48-long-reach")

    sonet_sr_compliant = Enum.YLeaf(3, "sonet-sr-compliant")

    sonet_lr_compliant = Enum.YLeaf(4, "sonet-lr-compliant")

    oc_192_short_reach = Enum.YLeaf(5, "oc-192-short-reach")

    escon_smf_1310_laser = Enum.YLeaf(6, "escon-smf-1310-laser")

    escon_mmf_1310_led = Enum.YLeaf(7, "escon-mmf-1310-led")

    unknown = Enum.YLeaf(8, "unknown")



class TransceiverOperData(Entity):
    """
    Top\-level container for transceiver operational data
    
    .. attribute:: transceiver
    
    	List of transceiver instance, keyed by name
    	**type**\: list of  		 :py:class:`Transceiver <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver>`
    
    	**config**\: False
    
    

    """

    _prefix = 'xcvr-ios-xe-oper'
    _revision = '2018-01-18'

    def __init__(self):
        super(TransceiverOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "transceiver-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-transceiver-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("transceiver", ("transceiver", TransceiverOperData.Transceiver))])
        self._leafs = OrderedDict()

        self.transceiver = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-transceiver-oper:transceiver-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TransceiverOperData, [], name, value)


    class Transceiver(Entity):
        """
        List of transceiver instance, keyed by name
        
        .. attribute:: name  (key)
        
        	Port name
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: enabled
        
        	Turns power on/off to the transceiver
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: present
        
        	Transceiver is present on the port
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: identifier
        
        	Indicates the type of optical transceiver used on this port
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: connector
        
        	Connector type used on this port
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: ethernet_pmd
        
        	Ethernet PMD (physical medium dependent sublayer) that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: vendor
        
        	Full name of transceiver vendor
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: vendor_part
        
        	Transceiver vendor's part number
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: vendor_rev
        
        	Transceiver vendor's revision number
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: serial_no
        
        	Transceiver serial number
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: fault_condition
        
        	Indicates if a fault condition exists in the transceiver
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: date
        
        	Representation of the transceiver date
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: sonet
        
        	SONET/SDH application code supported by the port
        	**type**\:  :py:class:`XcvrSonetCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.XcvrSonetCode>`
        
        	**config**\: False
        
        .. attribute:: otn
        
        	OTN application code supported by the port
        	**type**\:  :py:class:`XcvrOtnCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.XcvrOtnCode>`
        
        	**config**\: False
        
        .. attribute:: internal_temp
        
        	Internally measured temperature in degrees Celsius
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**config**\: False
        
        .. attribute:: output_power
        
        	The output optical power of overall transceiver(dBm)
        	**type**\:  :py:class:`OutputPower <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.OutputPower>`
        
        	**config**\: False
        
        .. attribute:: input_power
        
        	The input optical power of overall transceiver(dBm)
        	**type**\:  :py:class:`InputPower <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.InputPower>`
        
        	**config**\: False
        
        .. attribute:: laser_bias_current
        
        	The current applied by the system to the transmit laser to achieve the output power(mA)
        	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.LaserBiasCurrent>`
        
        	**config**\: False
        
        .. attribute:: xcvr_physical_channel
        
        	List of physical channel for transceiver
        	**type**\: list of  		 :py:class:`XcvrPhysicalChannel <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.XcvrPhysicalChannel>`
        
        	**config**\: False
        
        

        """

        _prefix = 'xcvr-ios-xe-oper'
        _revision = '2018-01-18'

        def __init__(self):
            super(TransceiverOperData.Transceiver, self).__init__()

            self.yang_name = "transceiver"
            self.yang_parent_name = "transceiver-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("output-power", ("output_power", TransceiverOperData.Transceiver.OutputPower)), ("input-power", ("input_power", TransceiverOperData.Transceiver.InputPower)), ("laser-bias-current", ("laser_bias_current", TransceiverOperData.Transceiver.LaserBiasCurrent)), ("xcvr-physical-channel", ("xcvr_physical_channel", TransceiverOperData.Transceiver.XcvrPhysicalChannel))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                ('present', (YLeaf(YType.boolean, 'present'), ['bool'])),
                ('identifier', (YLeaf(YType.str, 'identifier'), ['str'])),
                ('connector', (YLeaf(YType.str, 'connector'), ['str'])),
                ('ethernet_pmd', (YLeaf(YType.str, 'ethernet-pmd'), ['str'])),
                ('vendor', (YLeaf(YType.str, 'vendor'), ['str'])),
                ('vendor_part', (YLeaf(YType.str, 'vendor-part'), ['str'])),
                ('vendor_rev', (YLeaf(YType.str, 'vendor-rev'), ['str'])),
                ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                ('fault_condition', (YLeaf(YType.boolean, 'fault-condition'), ['bool'])),
                ('date', (YLeaf(YType.str, 'date'), ['str'])),
                ('sonet', (YLeaf(YType.enumeration, 'sonet'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper', 'XcvrSonetCode', '')])),
                ('otn', (YLeaf(YType.enumeration, 'otn'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper', 'XcvrOtnCode', '')])),
                ('internal_temp', (YLeaf(YType.str, 'internal-temp'), ['Decimal64'])),
            ])
            self.name = None
            self.enabled = None
            self.present = None
            self.identifier = None
            self.connector = None
            self.ethernet_pmd = None
            self.vendor = None
            self.vendor_part = None
            self.vendor_rev = None
            self.serial_no = None
            self.fault_condition = None
            self.date = None
            self.sonet = None
            self.otn = None
            self.internal_temp = None

            self.output_power = TransceiverOperData.Transceiver.OutputPower()
            self.output_power.parent = self
            self._children_name_map["output_power"] = "output-power"

            self.input_power = TransceiverOperData.Transceiver.InputPower()
            self.input_power.parent = self
            self._children_name_map["input_power"] = "input-power"

            self.laser_bias_current = TransceiverOperData.Transceiver.LaserBiasCurrent()
            self.laser_bias_current.parent = self
            self._children_name_map["laser_bias_current"] = "laser-bias-current"

            self.xcvr_physical_channel = YList(self)
            self._segment_path = lambda: "transceiver" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-transceiver-oper:transceiver-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TransceiverOperData.Transceiver, ['name', 'enabled', 'present', 'identifier', 'connector', 'ethernet_pmd', 'vendor', 'vendor_part', 'vendor_rev', 'serial_no', 'fault_condition', 'date', 'sonet', 'otn', 'internal_temp'], name, value)


        class OutputPower(Entity):
            """
            The output optical power of overall transceiver(dBm)
            
            .. attribute:: instant
            
            	Instant value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: avg
            
            	Average value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: max
            
            	Maximum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: min
            
            	Minimum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            

            """

            _prefix = 'xcvr-ios-xe-oper'
            _revision = '2018-01-18'

            def __init__(self):
                super(TransceiverOperData.Transceiver.OutputPower, self).__init__()

                self.yang_name = "output-power"
                self.yang_parent_name = "transceiver"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                ])
                self.instant = None
                self.avg = None
                self.max = None
                self.min = None
                self._segment_path = lambda: "output-power"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TransceiverOperData.Transceiver.OutputPower, ['instant', 'avg', 'max', 'min'], name, value)



        class InputPower(Entity):
            """
            The input optical power of overall transceiver(dBm)
            
            .. attribute:: instant
            
            	Instant value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: avg
            
            	Average value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: max
            
            	Maximum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: min
            
            	Minimum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            

            """

            _prefix = 'xcvr-ios-xe-oper'
            _revision = '2018-01-18'

            def __init__(self):
                super(TransceiverOperData.Transceiver.InputPower, self).__init__()

                self.yang_name = "input-power"
                self.yang_parent_name = "transceiver"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                ])
                self.instant = None
                self.avg = None
                self.max = None
                self.min = None
                self._segment_path = lambda: "input-power"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TransceiverOperData.Transceiver.InputPower, ['instant', 'avg', 'max', 'min'], name, value)



        class LaserBiasCurrent(Entity):
            """
            The current applied by the system to the transmit laser to achieve the output power(mA)
            
            .. attribute:: instant
            
            	Instant value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: avg
            
            	Average value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: max
            
            	Maximum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: min
            
            	Minimum value
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            

            """

            _prefix = 'xcvr-ios-xe-oper'
            _revision = '2018-01-18'

            def __init__(self):
                super(TransceiverOperData.Transceiver.LaserBiasCurrent, self).__init__()

                self.yang_name = "laser-bias-current"
                self.yang_parent_name = "transceiver"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                ])
                self.instant = None
                self.avg = None
                self.max = None
                self.min = None
                self._segment_path = lambda: "laser-bias-current"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TransceiverOperData.Transceiver.LaserBiasCurrent, ['instant', 'avg', 'max', 'min'], name, value)



        class XcvrPhysicalChannel(Entity):
            """
            List of physical channel for transceiver
            
            .. attribute:: index  (key)
            
            	Index of the physical channnel
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: description
            
            	Text description for the client physical channel
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: tx_laser
            
            	Enable (true) or disable (false) the transmit label for the channel
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: target_output_power
            
            	Target output optical power level of the optical channel(dBm)
            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
            
            	**range:** \-92233720368547758.08..92233720368547758.07
            
            	**config**\: False
            
            .. attribute:: output_frequency
            
            	The frequency in MHz of the individual physical channel
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: output_power
            
            	The output optical power of a physical channel(dBm)
            	**type**\:  :py:class:`OutputPower <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.XcvrPhysicalChannel.OutputPower>`
            
            	**config**\: False
            
            .. attribute:: input_power
            
            	The input optical power of a physical channel(dBm)
            	**type**\:  :py:class:`InputPower <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.XcvrPhysicalChannel.InputPower>`
            
            	**config**\: False
            
            .. attribute:: laser_bias_current
            
            	The current applied by the system to the transmit laser to achieve the output power(mA)
            	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_transceiver_oper.TransceiverOperData.Transceiver.XcvrPhysicalChannel.LaserBiasCurrent>`
            
            	**config**\: False
            
            

            """

            _prefix = 'xcvr-ios-xe-oper'
            _revision = '2018-01-18'

            def __init__(self):
                super(TransceiverOperData.Transceiver.XcvrPhysicalChannel, self).__init__()

                self.yang_name = "xcvr-physical-channel"
                self.yang_parent_name = "transceiver"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['index']
                self._child_classes = OrderedDict([("output-power", ("output_power", TransceiverOperData.Transceiver.XcvrPhysicalChannel.OutputPower)), ("input-power", ("input_power", TransceiverOperData.Transceiver.XcvrPhysicalChannel.InputPower)), ("laser-bias-current", ("laser_bias_current", TransceiverOperData.Transceiver.XcvrPhysicalChannel.LaserBiasCurrent))])
                self._leafs = OrderedDict([
                    ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('tx_laser', (YLeaf(YType.boolean, 'tx-laser'), ['bool'])),
                    ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                    ('output_frequency', (YLeaf(YType.uint64, 'output-frequency'), ['int'])),
                ])
                self.index = None
                self.description = None
                self.tx_laser = None
                self.target_output_power = None
                self.output_frequency = None

                self.output_power = TransceiverOperData.Transceiver.XcvrPhysicalChannel.OutputPower()
                self.output_power.parent = self
                self._children_name_map["output_power"] = "output-power"

                self.input_power = TransceiverOperData.Transceiver.XcvrPhysicalChannel.InputPower()
                self.input_power.parent = self
                self._children_name_map["input_power"] = "input-power"

                self.laser_bias_current = TransceiverOperData.Transceiver.XcvrPhysicalChannel.LaserBiasCurrent()
                self.laser_bias_current.parent = self
                self._children_name_map["laser_bias_current"] = "laser-bias-current"
                self._segment_path = lambda: "xcvr-physical-channel" + "[index='" + str(self.index) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TransceiverOperData.Transceiver.XcvrPhysicalChannel, ['index', 'description', 'tx_laser', 'target_output_power', 'output_frequency'], name, value)


            class OutputPower(Entity):
                """
                The output optical power of a physical channel(dBm)
                
                .. attribute:: instant
                
                	Instant value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: avg
                
                	Average value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: max
                
                	Maximum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: min
                
                	Minimum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                

                """

                _prefix = 'xcvr-ios-xe-oper'
                _revision = '2018-01-18'

                def __init__(self):
                    super(TransceiverOperData.Transceiver.XcvrPhysicalChannel.OutputPower, self).__init__()

                    self.yang_name = "output-power"
                    self.yang_parent_name = "xcvr-physical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                        ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                        ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                    ])
                    self.instant = None
                    self.avg = None
                    self.max = None
                    self.min = None
                    self._segment_path = lambda: "output-power"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TransceiverOperData.Transceiver.XcvrPhysicalChannel.OutputPower, ['instant', 'avg', 'max', 'min'], name, value)



            class InputPower(Entity):
                """
                The input optical power of a physical channel(dBm)
                
                .. attribute:: instant
                
                	Instant value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: avg
                
                	Average value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: max
                
                	Maximum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: min
                
                	Minimum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                

                """

                _prefix = 'xcvr-ios-xe-oper'
                _revision = '2018-01-18'

                def __init__(self):
                    super(TransceiverOperData.Transceiver.XcvrPhysicalChannel.InputPower, self).__init__()

                    self.yang_name = "input-power"
                    self.yang_parent_name = "xcvr-physical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                        ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                        ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                    ])
                    self.instant = None
                    self.avg = None
                    self.max = None
                    self.min = None
                    self._segment_path = lambda: "input-power"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TransceiverOperData.Transceiver.XcvrPhysicalChannel.InputPower, ['instant', 'avg', 'max', 'min'], name, value)



            class LaserBiasCurrent(Entity):
                """
                The current applied by the system to the transmit laser to achieve the output power(mA)
                
                .. attribute:: instant
                
                	Instant value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: avg
                
                	Average value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: max
                
                	Maximum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                .. attribute:: min
                
                	Minimum value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                

                """

                _prefix = 'xcvr-ios-xe-oper'
                _revision = '2018-01-18'

                def __init__(self):
                    super(TransceiverOperData.Transceiver.XcvrPhysicalChannel.LaserBiasCurrent, self).__init__()

                    self.yang_name = "laser-bias-current"
                    self.yang_parent_name = "xcvr-physical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                        ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                        ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                    ])
                    self.instant = None
                    self.avg = None
                    self.max = None
                    self.min = None
                    self._segment_path = lambda: "laser-bias-current"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TransceiverOperData.Transceiver.XcvrPhysicalChannel.LaserBiasCurrent, ['instant', 'avg', 'max', 'min'], name, value)




    def clone_ptr(self):
        self._top_entity = TransceiverOperData()
        return self._top_entity



