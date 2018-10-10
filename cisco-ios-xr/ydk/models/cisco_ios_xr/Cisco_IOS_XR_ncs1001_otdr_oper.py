""" Cisco_IOS_XR_ncs1001_otdr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1001\-otdr package operational data.

This module contains definitions
for the following management objects\:
  hw\-module\: ncs1001 hw\-module command chain

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Direction(Enum):
    """
    Direction (Enum Class)

    Direction

    .. data:: direction_tx = 0

    	Tx

    .. data:: direction_rx = 1

    	Rx

    """

    direction_tx = Enum.YLeaf(0, "direction-tx")

    direction_rx = Enum.YLeaf(1, "direction-rx")


class OtdrEvent(Enum):
    """
    OtdrEvent (Enum Class)

    Otdr event

    .. data:: otdr_event_type_loss = 1

    	Loss

    .. data:: otdr_event_type_reflect_ion = 2

    	Reflection

    .. data:: otdr_event_type_loss_and_reflect_ion = 3

    	Loss And Reflection

    .. data:: otdr_event_type_end_of_fiber = 4

    	End Of Fiber

    """

    otdr_event_type_loss = Enum.YLeaf(1, "otdr-event-type-loss")

    otdr_event_type_reflect_ion = Enum.YLeaf(2, "otdr-event-type-reflect-ion")

    otdr_event_type_loss_and_reflect_ion = Enum.YLeaf(3, "otdr-event-type-loss-and-reflect-ion")

    otdr_event_type_end_of_fiber = Enum.YLeaf(4, "otdr-event-type-end-of-fiber")


class OtdrScanMode(Enum):
    """
    OtdrScanMode (Enum Class)

    Otdr scan mode

    .. data:: otdr_scan_auto = 0

    	Auto

    .. data:: otdr_scan_expert = 1

    	Expert

    """

    otdr_scan_auto = Enum.YLeaf(0, "otdr-scan-auto")

    otdr_scan_expert = Enum.YLeaf(1, "otdr-scan-expert")


class OtdrStatus(Enum):
    """
    OtdrStatus (Enum Class)

    Otdr status

    .. data:: otdr_status_unknown = 0

    	Unknown

    .. data:: otdr_status_ok = 1

    	Ok

    .. data:: otdr_status_orl_progress = 2

    	ORL Progress

    .. data:: otdr_status_otdr_progress = 3

    	OTDR Progress

    .. data:: otdr_status_progress = 4

    	Progress

    .. data:: otdr_status_failure = 5

    	Failure

    .. data:: otdr_status_aborted = 6

    	Aborted

    """

    otdr_status_unknown = Enum.YLeaf(0, "otdr-status-unknown")

    otdr_status_ok = Enum.YLeaf(1, "otdr-status-ok")

    otdr_status_orl_progress = Enum.YLeaf(2, "otdr-status-orl-progress")

    otdr_status_otdr_progress = Enum.YLeaf(3, "otdr-status-otdr-progress")

    otdr_status_progress = Enum.YLeaf(4, "otdr-status-progress")

    otdr_status_failure = Enum.YLeaf(5, "otdr-status-failure")

    otdr_status_aborted = Enum.YLeaf(6, "otdr-status-aborted")


class OtsOtdrData(Enum):
    """
    OtsOtdrData (Enum Class)

    Ots otdr data

    .. data:: status = 0

    	Display otdr status

    .. data:: scan = 1

    	Display the list of saved measurements

    .. data:: base_line = 2

    	Display the list of saved baseline

    """

    status = Enum.YLeaf(0, "status")

    scan = Enum.YLeaf(1, "scan")

    base_line = Enum.YLeaf(2, "base-line")


class OtsOtdrDataTypeDetails(Enum):
    """
    OtsOtdrDataTypeDetails (Enum Class)

    Ots otdr data type details

    .. data:: scan_details = 1

    	Displays Scan Details

    .. data:: base_line_details = 2

    	Displays Baseline Details

    """

    scan_details = Enum.YLeaf(1, "scan-details")

    base_line_details = Enum.YLeaf(2, "base-line-details")



class HwModule(Entity):
    """
    ncs1001 hw\-module command chain
    
    .. attribute:: otdr_details
    
    	Otdr Details Root Info
    	**type**\:  :py:class:`OtdrDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails>`
    
    .. attribute:: otdrs
    
    	Otdr Root Info
    	**type**\:  :py:class:`Otdrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs>`
    
    

    """

    _prefix = 'ncs1001-otdr-oper'
    _revision = '2018-03-15'

    def __init__(self):
        super(HwModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1001-otdr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("otdr-details", ("otdr_details", HwModule.OtdrDetails)), ("otdrs", ("otdrs", HwModule.Otdrs))])
        self._leafs = OrderedDict()

        self.otdr_details = HwModule.OtdrDetails()
        self.otdr_details.parent = self
        self._children_name_map["otdr_details"] = "otdr-details"

        self.otdrs = HwModule.Otdrs()
        self.otdrs.parent = self
        self._children_name_map["otdrs"] = "otdrs"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1001-otdr-oper:hw-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModule, [], name, value)


    class OtdrDetails(Entity):
        """
        Otdr Details Root Info
        
        .. attribute:: otdr_detail
        
        	Otdr Details
        	**type**\: list of  		 :py:class:`OtdrDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail>`
        
        

        """

        _prefix = 'ncs1001-otdr-oper'
        _revision = '2018-03-15'

        def __init__(self):
            super(HwModule.OtdrDetails, self).__init__()

            self.yang_name = "otdr-details"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("otdr-detail", ("otdr_detail", HwModule.OtdrDetails.OtdrDetail))])
            self._leafs = OrderedDict()

            self.otdr_detail = YList(self)
            self._segment_path = lambda: "otdr-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-otdr-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.OtdrDetails, [], name, value)


        class OtdrDetail(Entity):
            """
            Otdr Details
            
            .. attribute:: slot_id  (key)
            
            	Details associated with a particular slot number
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: data_type_detail
            
            	Dispaly data type list
            	**type**\: list of  		 :py:class:`DataTypeDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail>`
            
            

            """

            _prefix = 'ncs1001-otdr-oper'
            _revision = '2018-03-15'

            def __init__(self):
                super(HwModule.OtdrDetails.OtdrDetail, self).__init__()

                self.yang_name = "otdr-detail"
                self.yang_parent_name = "otdr-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['slot_id']
                self._child_classes = OrderedDict([("data-type-detail", ("data_type_detail", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail))])
                self._leafs = OrderedDict([
                    ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                ])
                self.slot_id = None

                self.data_type_detail = YList(self)
                self._segment_path = lambda: "otdr-detail" + "[slot-id='" + str(self.slot_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-otdr-oper:hw-module/otdr-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.OtdrDetails.OtdrDetail, ['slot_id'], name, value)


            class DataTypeDetail(Entity):
                """
                Dispaly data type list
                
                .. attribute:: otdr_data_type_details  (key)
                
                	Details associated with a particular Data type
                	**type**\:  :py:class:`OtsOtdrDataTypeDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtsOtdrDataTypeDetails>`
                
                .. attribute:: identifier
                
                	Dispaly details
                	**type**\: list of  		 :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier>`
                
                

                """

                _prefix = 'ncs1001-otdr-oper'
                _revision = '2018-03-15'

                def __init__(self):
                    super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail, self).__init__()

                    self.yang_name = "data-type-detail"
                    self.yang_parent_name = "otdr-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['otdr_data_type_details']
                    self._child_classes = OrderedDict([("identifier", ("identifier", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier))])
                    self._leafs = OrderedDict([
                        ('otdr_data_type_details', (YLeaf(YType.enumeration, 'otdr-data-type-details'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtsOtdrDataTypeDetails', '')])),
                    ])
                    self.otdr_data_type_details = None

                    self.identifier = YList(self)
                    self._segment_path = lambda: "data-type-detail" + "[otdr-data-type-details='" + str(self.otdr_data_type_details) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail, ['otdr_data_type_details'], name, value)


                class Identifier(Entity):
                    """
                    Dispaly details
                    
                    .. attribute:: scan_detail  (key)
                    
                    	Dispaly details
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: otdr_item
                    
                    	otdr item
                    	**type**\:  :py:class:`OtdrItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem>`
                    
                    .. attribute:: otdr_scan
                    
                    	otdr scan
                    	**type**\: list of  		 :py:class:`OtdrScan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrScan>`
                    
                    .. attribute:: otdr_status
                    
                    	otdr status
                    	**type**\: list of  		 :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrStatus>`
                    
                    

                    """

                    _prefix = 'ncs1001-otdr-oper'
                    _revision = '2018-03-15'

                    def __init__(self):
                        super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier, self).__init__()

                        self.yang_name = "identifier"
                        self.yang_parent_name = "data-type-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['scan_detail']
                        self._child_classes = OrderedDict([("otdr-item", ("otdr_item", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem)), ("otdr-scan", ("otdr_scan", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrScan)), ("otdr-status", ("otdr_status", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrStatus))])
                        self._leafs = OrderedDict([
                            ('scan_detail', (YLeaf(YType.uint32, 'scan-detail'), ['int'])),
                        ])
                        self.scan_detail = None

                        self.otdr_item = HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem()
                        self.otdr_item.parent = self
                        self._children_name_map["otdr_item"] = "otdr-item"

                        self.otdr_scan = YList(self)
                        self.otdr_status = YList(self)
                        self._segment_path = lambda: "identifier" + "[scan-detail='" + str(self.scan_detail) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier, ['scan_detail'], name, value)


                    class OtdrItem(Entity):
                        """
                        otdr item
                        
                        .. attribute:: otdr_number
                        
                        	Otdr Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: direction
                        
                        	Scan Direction
                        	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                        
                        .. attribute:: timestamp
                        
                        	Timestamp
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: sor_file
                        
                        	Sor file name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: sor_directory
                        
                        	Sor file location
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: scan_mode
                        
                        	Scan Mode
                        	**type**\:  :py:class:`OtdrScanMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrScanMode>`
                        
                        .. attribute:: distance
                        
                        	Distance in Km
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: total_orl
                        
                        	Total Orl in dB
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: otdr_event
                        
                        	Event list
                        	**type**\: list of  		 :py:class:`OtdrEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem.OtdrEvent>`
                        
                        

                        """

                        _prefix = 'ncs1001-otdr-oper'
                        _revision = '2018-03-15'

                        def __init__(self):
                            super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem, self).__init__()

                            self.yang_name = "otdr-item"
                            self.yang_parent_name = "identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("otdr-event", ("otdr_event", HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem.OtdrEvent))])
                            self._leafs = OrderedDict([
                                ('otdr_number', (YLeaf(YType.uint8, 'otdr-number'), ['int'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                ('sor_file', (YLeaf(YType.str, 'sor-file'), ['str'])),
                                ('sor_directory', (YLeaf(YType.str, 'sor-directory'), ['str'])),
                                ('scan_mode', (YLeaf(YType.enumeration, 'scan-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrScanMode', '')])),
                                ('distance', (YLeaf(YType.str, 'distance'), ['str'])),
                                ('total_orl', (YLeaf(YType.str, 'total-orl'), ['str'])),
                            ])
                            self.otdr_number = None
                            self.direction = None
                            self.timestamp = None
                            self.sor_file = None
                            self.sor_directory = None
                            self.scan_mode = None
                            self.distance = None
                            self.total_orl = None

                            self.otdr_event = YList(self)
                            self._segment_path = lambda: "otdr-item"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem, ['otdr_number', 'direction', 'timestamp', 'sor_file', 'sor_directory', 'scan_mode', 'distance', 'total_orl'], name, value)


                        class OtdrEvent(Entity):
                            """
                            Event list
                            
                            .. attribute:: event_id
                            
                            	Event Id
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: type
                            
                            	Event Type
                            	**type**\:  :py:class:`OtdrEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrEvent>`
                            
                            .. attribute:: position
                            
                            	Event Position in Km
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: accuracy
                            
                            	Event accuracy in meters
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: magnitude
                            
                            	Event Magnitude in dB
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: attenuation
                            
                            	Event Attenuation in dB
                            	**type**\: str
                            
                            	**length:** 0..16
                            
                            .. attribute:: eof_confidence
                            
                            	Event End of Fiber Confidence
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: threshold_crossing
                            
                            	Threshold Crossing
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'ncs1001-otdr-oper'
                            _revision = '2018-03-15'

                            def __init__(self):
                                super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem.OtdrEvent, self).__init__()

                                self.yang_name = "otdr-event"
                                self.yang_parent_name = "otdr-item"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('event_id', (YLeaf(YType.uint16, 'event-id'), ['int'])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrEvent', '')])),
                                    ('position', (YLeaf(YType.str, 'position'), ['str'])),
                                    ('accuracy', (YLeaf(YType.str, 'accuracy'), ['str'])),
                                    ('magnitude', (YLeaf(YType.str, 'magnitude'), ['str'])),
                                    ('attenuation', (YLeaf(YType.str, 'attenuation'), ['str'])),
                                    ('eof_confidence', (YLeaf(YType.uint32, 'eof-confidence'), ['int'])),
                                    ('threshold_crossing', (YLeaf(YType.uint8, 'threshold-crossing'), ['int'])),
                                ])
                                self.event_id = None
                                self.type = None
                                self.position = None
                                self.accuracy = None
                                self.magnitude = None
                                self.attenuation = None
                                self.eof_confidence = None
                                self.threshold_crossing = None
                                self._segment_path = lambda: "otdr-event"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrItem.OtdrEvent, ['event_id', 'type', 'position', 'accuracy', 'magnitude', 'attenuation', 'eof_confidence', 'threshold_crossing'], name, value)


                    class OtdrScan(Entity):
                        """
                        otdr scan
                        
                        .. attribute:: index
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: otdr_number
                        
                        	Otdr Number
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: direction
                        
                        	Direction
                        	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                        
                        .. attribute:: scan_mode
                        
                        	Scan Mode
                        	**type**\:  :py:class:`OtdrScanMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrScanMode>`
                        
                        .. attribute:: timestamp
                        
                        	Timestamp
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: sor_file
                        
                        	Sor File Name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        

                        """

                        _prefix = 'ncs1001-otdr-oper'
                        _revision = '2018-03-15'

                        def __init__(self):
                            super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrScan, self).__init__()

                            self.yang_name = "otdr-scan"
                            self.yang_parent_name = "identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                ('otdr_number', (YLeaf(YType.uint8, 'otdr-number'), ['int'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                                ('scan_mode', (YLeaf(YType.enumeration, 'scan-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrScanMode', '')])),
                                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                ('sor_file', (YLeaf(YType.str, 'sor-file'), ['str'])),
                            ])
                            self.index = None
                            self.otdr_number = None
                            self.direction = None
                            self.scan_mode = None
                            self.timestamp = None
                            self.sor_file = None
                            self._segment_path = lambda: "otdr-scan"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrScan, ['index', 'otdr_number', 'direction', 'scan_mode', 'timestamp', 'sor_file'], name, value)


                    class OtdrStatus(Entity):
                        """
                        otdr status
                        
                        .. attribute:: otdr_id
                        
                        	Otdr Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: direction
                        
                        	Direction
                        	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                        
                        .. attribute:: timestamp
                        
                        	Timestamp
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: training_status
                        
                        	Training Status
                        	**type**\:  :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrStatus>`
                        
                        .. attribute:: measurement_status
                        
                        	Measurement Status
                        	**type**\:  :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrStatus>`
                        
                        .. attribute:: progress_pc
                        
                        	Progress %
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ncs1001-otdr-oper'
                        _revision = '2018-03-15'

                        def __init__(self):
                            super(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrStatus, self).__init__()

                            self.yang_name = "otdr-status"
                            self.yang_parent_name = "identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('otdr_id', (YLeaf(YType.uint8, 'otdr-id'), ['int'])),
                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                                ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                                ('training_status', (YLeaf(YType.enumeration, 'training-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrStatus', '')])),
                                ('measurement_status', (YLeaf(YType.enumeration, 'measurement-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrStatus', '')])),
                                ('progress_pc', (YLeaf(YType.uint16, 'progress-pc'), ['int'])),
                            ])
                            self.otdr_id = None
                            self.direction = None
                            self.timestamp = None
                            self.training_status = None
                            self.measurement_status = None
                            self.progress_pc = None
                            self._segment_path = lambda: "otdr-status"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.OtdrDetails.OtdrDetail.DataTypeDetail.Identifier.OtdrStatus, ['otdr_id', 'direction', 'timestamp', 'training_status', 'measurement_status', 'progress_pc'], name, value)


    class Otdrs(Entity):
        """
        Otdr Root Info
        
        .. attribute:: otdr
        
        	Otdr Info
        	**type**\: list of  		 :py:class:`Otdr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr>`
        
        

        """

        _prefix = 'ncs1001-otdr-oper'
        _revision = '2018-03-15'

        def __init__(self):
            super(HwModule.Otdrs, self).__init__()

            self.yang_name = "otdrs"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("otdr", ("otdr", HwModule.Otdrs.Otdr))])
            self._leafs = OrderedDict()

            self.otdr = YList(self)
            self._segment_path = lambda: "otdrs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-otdr-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.Otdrs, [], name, value)


        class Otdr(Entity):
            """
            Otdr Info
            
            .. attribute:: slot_id  (key)
            
            	Details associated with a particular slot number
            	**type**\: int
            
            	**range:** 1..3
            
            .. attribute:: data_type
            
            	Dispaly data type list
            	**type**\: list of  		 :py:class:`DataType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr.DataType>`
            
            

            """

            _prefix = 'ncs1001-otdr-oper'
            _revision = '2018-03-15'

            def __init__(self):
                super(HwModule.Otdrs.Otdr, self).__init__()

                self.yang_name = "otdr"
                self.yang_parent_name = "otdrs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['slot_id']
                self._child_classes = OrderedDict([("data-type", ("data_type", HwModule.Otdrs.Otdr.DataType))])
                self._leafs = OrderedDict([
                    ('slot_id', (YLeaf(YType.uint32, 'slot-id'), ['int'])),
                ])
                self.slot_id = None

                self.data_type = YList(self)
                self._segment_path = lambda: "otdr" + "[slot-id='" + str(self.slot_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1001-otdr-oper:hw-module/otdrs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.Otdrs.Otdr, ['slot_id'], name, value)


            class DataType(Entity):
                """
                Dispaly data type list
                
                .. attribute:: otdr_data_type  (key)
                
                	Details associated with a particular Data type
                	**type**\:  :py:class:`OtsOtdrData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtsOtdrData>`
                
                .. attribute:: otdr_item
                
                	otdr item
                	**type**\:  :py:class:`OtdrItem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr.DataType.OtdrItem>`
                
                .. attribute:: otdr_scan
                
                	otdr scan
                	**type**\: list of  		 :py:class:`OtdrScan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr.DataType.OtdrScan>`
                
                .. attribute:: otdr_status
                
                	otdr status
                	**type**\: list of  		 :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr.DataType.OtdrStatus>`
                
                

                """

                _prefix = 'ncs1001-otdr-oper'
                _revision = '2018-03-15'

                def __init__(self):
                    super(HwModule.Otdrs.Otdr.DataType, self).__init__()

                    self.yang_name = "data-type"
                    self.yang_parent_name = "otdr"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['otdr_data_type']
                    self._child_classes = OrderedDict([("otdr-item", ("otdr_item", HwModule.Otdrs.Otdr.DataType.OtdrItem)), ("otdr-scan", ("otdr_scan", HwModule.Otdrs.Otdr.DataType.OtdrScan)), ("otdr-status", ("otdr_status", HwModule.Otdrs.Otdr.DataType.OtdrStatus))])
                    self._leafs = OrderedDict([
                        ('otdr_data_type', (YLeaf(YType.enumeration, 'otdr-data-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtsOtdrData', '')])),
                    ])
                    self.otdr_data_type = None

                    self.otdr_item = HwModule.Otdrs.Otdr.DataType.OtdrItem()
                    self.otdr_item.parent = self
                    self._children_name_map["otdr_item"] = "otdr-item"

                    self.otdr_scan = YList(self)
                    self.otdr_status = YList(self)
                    self._segment_path = lambda: "data-type" + "[otdr-data-type='" + str(self.otdr_data_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.Otdrs.Otdr.DataType, ['otdr_data_type'], name, value)


                class OtdrItem(Entity):
                    """
                    otdr item
                    
                    .. attribute:: otdr_number
                    
                    	Otdr Number
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: direction
                    
                    	Scan Direction
                    	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: sor_file
                    
                    	Sor file name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: sor_directory
                    
                    	Sor file location
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: scan_mode
                    
                    	Scan Mode
                    	**type**\:  :py:class:`OtdrScanMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrScanMode>`
                    
                    .. attribute:: distance
                    
                    	Distance in Km
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: total_orl
                    
                    	Total Orl in dB
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: otdr_event
                    
                    	Event list
                    	**type**\: list of  		 :py:class:`OtdrEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.HwModule.Otdrs.Otdr.DataType.OtdrItem.OtdrEvent>`
                    
                    

                    """

                    _prefix = 'ncs1001-otdr-oper'
                    _revision = '2018-03-15'

                    def __init__(self):
                        super(HwModule.Otdrs.Otdr.DataType.OtdrItem, self).__init__()

                        self.yang_name = "otdr-item"
                        self.yang_parent_name = "data-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("otdr-event", ("otdr_event", HwModule.Otdrs.Otdr.DataType.OtdrItem.OtdrEvent))])
                        self._leafs = OrderedDict([
                            ('otdr_number', (YLeaf(YType.uint8, 'otdr-number'), ['int'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('sor_file', (YLeaf(YType.str, 'sor-file'), ['str'])),
                            ('sor_directory', (YLeaf(YType.str, 'sor-directory'), ['str'])),
                            ('scan_mode', (YLeaf(YType.enumeration, 'scan-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrScanMode', '')])),
                            ('distance', (YLeaf(YType.str, 'distance'), ['str'])),
                            ('total_orl', (YLeaf(YType.str, 'total-orl'), ['str'])),
                        ])
                        self.otdr_number = None
                        self.direction = None
                        self.timestamp = None
                        self.sor_file = None
                        self.sor_directory = None
                        self.scan_mode = None
                        self.distance = None
                        self.total_orl = None

                        self.otdr_event = YList(self)
                        self._segment_path = lambda: "otdr-item"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Otdrs.Otdr.DataType.OtdrItem, ['otdr_number', 'direction', 'timestamp', 'sor_file', 'sor_directory', 'scan_mode', 'distance', 'total_orl'], name, value)


                    class OtdrEvent(Entity):
                        """
                        Event list
                        
                        .. attribute:: event_id
                        
                        	Event Id
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: type
                        
                        	Event Type
                        	**type**\:  :py:class:`OtdrEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrEvent>`
                        
                        .. attribute:: position
                        
                        	Event Position in Km
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: accuracy
                        
                        	Event accuracy in meters
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: magnitude
                        
                        	Event Magnitude in dB
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: attenuation
                        
                        	Event Attenuation in dB
                        	**type**\: str
                        
                        	**length:** 0..16
                        
                        .. attribute:: eof_confidence
                        
                        	Event End of Fiber Confidence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: threshold_crossing
                        
                        	Threshold Crossing
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ncs1001-otdr-oper'
                        _revision = '2018-03-15'

                        def __init__(self):
                            super(HwModule.Otdrs.Otdr.DataType.OtdrItem.OtdrEvent, self).__init__()

                            self.yang_name = "otdr-event"
                            self.yang_parent_name = "otdr-item"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('event_id', (YLeaf(YType.uint16, 'event-id'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrEvent', '')])),
                                ('position', (YLeaf(YType.str, 'position'), ['str'])),
                                ('accuracy', (YLeaf(YType.str, 'accuracy'), ['str'])),
                                ('magnitude', (YLeaf(YType.str, 'magnitude'), ['str'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['str'])),
                                ('eof_confidence', (YLeaf(YType.uint32, 'eof-confidence'), ['int'])),
                                ('threshold_crossing', (YLeaf(YType.uint8, 'threshold-crossing'), ['int'])),
                            ])
                            self.event_id = None
                            self.type = None
                            self.position = None
                            self.accuracy = None
                            self.magnitude = None
                            self.attenuation = None
                            self.eof_confidence = None
                            self.threshold_crossing = None
                            self._segment_path = lambda: "otdr-event"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModule.Otdrs.Otdr.DataType.OtdrItem.OtdrEvent, ['event_id', 'type', 'position', 'accuracy', 'magnitude', 'attenuation', 'eof_confidence', 'threshold_crossing'], name, value)


                class OtdrScan(Entity):
                    """
                    otdr scan
                    
                    .. attribute:: index
                    
                    	Index
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: otdr_number
                    
                    	Otdr Number
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: direction
                    
                    	Direction
                    	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                    
                    .. attribute:: scan_mode
                    
                    	Scan Mode
                    	**type**\:  :py:class:`OtdrScanMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrScanMode>`
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: sor_file
                    
                    	Sor File Name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    

                    """

                    _prefix = 'ncs1001-otdr-oper'
                    _revision = '2018-03-15'

                    def __init__(self):
                        super(HwModule.Otdrs.Otdr.DataType.OtdrScan, self).__init__()

                        self.yang_name = "otdr-scan"
                        self.yang_parent_name = "data-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                            ('otdr_number', (YLeaf(YType.uint8, 'otdr-number'), ['int'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                            ('scan_mode', (YLeaf(YType.enumeration, 'scan-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrScanMode', '')])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('sor_file', (YLeaf(YType.str, 'sor-file'), ['str'])),
                        ])
                        self.index = None
                        self.otdr_number = None
                        self.direction = None
                        self.scan_mode = None
                        self.timestamp = None
                        self.sor_file = None
                        self._segment_path = lambda: "otdr-scan"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Otdrs.Otdr.DataType.OtdrScan, ['index', 'otdr_number', 'direction', 'scan_mode', 'timestamp', 'sor_file'], name, value)


                class OtdrStatus(Entity):
                    """
                    otdr status
                    
                    .. attribute:: otdr_id
                    
                    	Otdr Id
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: direction
                    
                    	Direction
                    	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.Direction>`
                    
                    .. attribute:: timestamp
                    
                    	Timestamp
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: training_status
                    
                    	Training Status
                    	**type**\:  :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrStatus>`
                    
                    .. attribute:: measurement_status
                    
                    	Measurement Status
                    	**type**\:  :py:class:`OtdrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper.OtdrStatus>`
                    
                    .. attribute:: progress_pc
                    
                    	Progress %
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ncs1001-otdr-oper'
                    _revision = '2018-03-15'

                    def __init__(self):
                        super(HwModule.Otdrs.Otdr.DataType.OtdrStatus, self).__init__()

                        self.yang_name = "otdr-status"
                        self.yang_parent_name = "data-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('otdr_id', (YLeaf(YType.uint8, 'otdr-id'), ['int'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'Direction', '')])),
                            ('timestamp', (YLeaf(YType.str, 'timestamp'), ['str'])),
                            ('training_status', (YLeaf(YType.enumeration, 'training-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrStatus', '')])),
                            ('measurement_status', (YLeaf(YType.enumeration, 'measurement-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1001_otdr_oper', 'OtdrStatus', '')])),
                            ('progress_pc', (YLeaf(YType.uint16, 'progress-pc'), ['int'])),
                        ])
                        self.otdr_id = None
                        self.direction = None
                        self.timestamp = None
                        self.training_status = None
                        self.measurement_status = None
                        self.progress_pc = None
                        self._segment_path = lambda: "otdr-status"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.Otdrs.Otdr.DataType.OtdrStatus, ['otdr_id', 'direction', 'timestamp', 'training_status', 'measurement_status', 'progress_pc'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModule()
        return self._top_entity

