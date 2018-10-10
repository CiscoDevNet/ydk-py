""" Cisco_IOS_XR_ncs1k_mxp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs1k\-mxp package operational data.

This module contains definitions
for the following management objects\:
  hw\-module\: mxp hw\-module command chain

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ClientDataRate(Enum):
    """
    ClientDataRate (Enum Class)

    Client data rate

    .. data:: ten_gig = 1

    	Ten Gig

    .. data:: forty_gig = 2

    	Forty Gig

    .. data:: hundred_gig = 3

    	Hundread Gig

    .. data:: ten_and_hundred_gig = 4

    	Ten and Hundread Gig

    """

    ten_gig = Enum.YLeaf(1, "ten-gig")

    forty_gig = Enum.YLeaf(2, "forty-gig")

    hundred_gig = Enum.YLeaf(3, "hundred-gig")

    ten_and_hundred_gig = Enum.YLeaf(4, "ten-and-hundred-gig")


class HwModuleSliceStatus(Enum):
    """
    HwModuleSliceStatus (Enum Class)

    Hw module slice status

    .. data:: not_provisioned = 0

    	Not Provisioned

    .. data:: provisioning_in_progress = 1

    	Provisioning In-Progress

    .. data:: provisioned = 2

    	Provisioned

    .. data:: provisioning_failed = 3

    	Provisioning Failed

    .. data:: provisioning_scheduled = 4

    	Provisioning Scheduled

    .. data:: reprovisioning_aborted = 5

    	Reprovisioning Aborted

    """

    not_provisioned = Enum.YLeaf(0, "not-provisioned")

    provisioning_in_progress = Enum.YLeaf(1, "provisioning-in-progress")

    provisioned = Enum.YLeaf(2, "provisioned")

    provisioning_failed = Enum.YLeaf(3, "provisioning-failed")

    provisioning_scheduled = Enum.YLeaf(4, "provisioning-scheduled")

    reprovisioning_aborted = Enum.YLeaf(5, "reprovisioning-aborted")


class TrunkDataRate(Enum):
    """
    TrunkDataRate (Enum Class)

    Trunk data rate

    .. data:: fifty_gig = 1

    	FiftyGig

    .. data:: hundred_gig = 2

    	HundredGig

    .. data:: two_hundred_gig = 3

    	TwoHundredGig

    .. data:: two_hundred_fifty_gig = 4

    	TwoHundredFiftyGig

    """

    fifty_gig = Enum.YLeaf(1, "fifty-gig")

    hundred_gig = Enum.YLeaf(2, "hundred-gig")

    two_hundred_gig = Enum.YLeaf(3, "two-hundred-gig")

    two_hundred_fifty_gig = Enum.YLeaf(4, "two-hundred-fifty-gig")



class HwModule(Entity):
    """
    mxp hw\-module command chain
    
    .. attribute:: slice_ids
    
    	Slice information
    	**type**\:  :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds>`
    
    .. attribute:: slice_all
    
    	Information for all slices
    	**type**\:  :py:class:`SliceAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll>`
    
    

    """

    _prefix = 'ncs1k-mxp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(HwModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module"
        self.yang_parent_name = "Cisco-IOS-XR-ncs1k-mxp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("slice-ids", ("slice_ids", HwModule.SliceIds)), ("slice-all", ("slice_all", HwModule.SliceAll))])
        self._leafs = OrderedDict()

        self.slice_ids = HwModule.SliceIds()
        self.slice_ids.parent = self
        self._children_name_map["slice_ids"] = "slice-ids"

        self.slice_all = HwModule.SliceAll()
        self.slice_all.parent = self
        self._children_name_map["slice_all"] = "slice-all"
        self._segment_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModule, [], name, value)


    class SliceIds(Entity):
        """
        Slice information
        
        .. attribute:: slice_id
        
        	Per slice num data
        	**type**\: list of  		 :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HwModule.SliceIds, self).__init__()

            self.yang_name = "slice-ids"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("slice-id", ("slice_id", HwModule.SliceIds.SliceId))])
            self._leafs = OrderedDict()

            self.slice_id = YList(self)
            self._segment_path = lambda: "slice-ids"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.SliceIds, [], name, value)


        class SliceId(Entity):
            """
            Per slice num data
            
            .. attribute:: slice_num  (key)
            
            	Details associated with a particular slice number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: slice_id
            
            	SliceId
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_rate
            
            	ClientRate
            	**type**\:  :py:class:`ClientDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.ClientDataRate>`
            
            .. attribute:: trunk_rate
            
            	TrunkRate
            	**type**\:  :py:class:`TrunkDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.TrunkDataRate>`
            
            .. attribute:: hardware_status
            
            	HardwareStatus
            	**type**\:  :py:class:`HwModuleSliceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatus>`
            
            .. attribute:: dp_fpga_fw_type
            
            	DpFpgaFwType
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: dp_fpga_fw_ver
            
            	DpFpgaFwVer
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: need_upg
            
            	NeedUpg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: encryption_supported
            
            	EncryptionSupported
            	**type**\: bool
            
            .. attribute:: lldp_drop_status
            
            	LldpDropStatus
            	**type**\: bool
            
            .. attribute:: client_port
            
            	client port
            	**type**\: list of  		 :py:class:`ClientPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.ClientPort>`
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HwModule.SliceIds.SliceId, self).__init__()

                self.yang_name = "slice-id"
                self.yang_parent_name = "slice-ids"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['slice_num']
                self._child_classes = OrderedDict([("client-port", ("client_port", HwModule.SliceIds.SliceId.ClientPort))])
                self._leafs = OrderedDict([
                    ('slice_num', (YLeaf(YType.uint32, 'slice-num'), ['int'])),
                    ('slice_id', (YLeaf(YType.uint32, 'slice-id'), ['int'])),
                    ('client_rate', (YLeaf(YType.enumeration, 'client-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'ClientDataRate', '')])),
                    ('trunk_rate', (YLeaf(YType.enumeration, 'trunk-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'TrunkDataRate', '')])),
                    ('hardware_status', (YLeaf(YType.enumeration, 'hardware-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModuleSliceStatus', '')])),
                    ('dp_fpga_fw_type', (YLeaf(YType.str, 'dp-fpga-fw-type'), ['str'])),
                    ('dp_fpga_fw_ver', (YLeaf(YType.str, 'dp-fpga-fw-ver'), ['str'])),
                    ('need_upg', (YLeaf(YType.uint32, 'need-upg'), ['int'])),
                    ('encryption_supported', (YLeaf(YType.boolean, 'encryption-supported'), ['bool'])),
                    ('lldp_drop_status', (YLeaf(YType.boolean, 'lldp-drop-status'), ['bool'])),
                ])
                self.slice_num = None
                self.slice_id = None
                self.client_rate = None
                self.trunk_rate = None
                self.hardware_status = None
                self.dp_fpga_fw_type = None
                self.dp_fpga_fw_ver = None
                self.need_upg = None
                self.encryption_supported = None
                self.lldp_drop_status = None

                self.client_port = YList(self)
                self._segment_path = lambda: "slice-id" + "[slice-num='" + str(self.slice_num) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-ids/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.SliceIds.SliceId, ['slice_num', u'slice_id', u'client_rate', u'trunk_rate', u'hardware_status', u'dp_fpga_fw_type', u'dp_fpga_fw_ver', u'need_upg', u'encryption_supported', u'lldp_drop_status'], name, value)


            class ClientPort(Entity):
                """
                client port
                
                .. attribute:: client_name
                
                	ClientName
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: if_index
                
                	IfIndex
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: trunk_port
                
                	trunk port
                	**type**\: list of  		 :py:class:`TrunkPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceIds.SliceId.ClientPort.TrunkPort>`
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HwModule.SliceIds.SliceId.ClientPort, self).__init__()

                    self.yang_name = "client-port"
                    self.yang_parent_name = "slice-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trunk-port", ("trunk_port", HwModule.SliceIds.SliceId.ClientPort.TrunkPort))])
                    self._leafs = OrderedDict([
                        ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                        ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                    ])
                    self.client_name = None
                    self.if_index = None

                    self.trunk_port = YList(self)
                    self._segment_path = lambda: "client-port"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.SliceIds.SliceId.ClientPort, [u'client_name', u'if_index'], name, value)


                class TrunkPort(Entity):
                    """
                    trunk port
                    
                    .. attribute:: trunk_name
                    
                    	TrunkName
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: percentage
                    
                    	Percentage
                    	**type**\: str
                    
                    	**length:** 0..8
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HwModule.SliceIds.SliceId.ClientPort.TrunkPort, self).__init__()

                        self.yang_name = "trunk-port"
                        self.yang_parent_name = "client-port"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('trunk_name', (YLeaf(YType.str, 'trunk-name'), ['str'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                            ('percentage', (YLeaf(YType.str, 'percentage'), ['str'])),
                        ])
                        self.trunk_name = None
                        self.if_index = None
                        self.percentage = None
                        self._segment_path = lambda: "trunk-port"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.SliceIds.SliceId.ClientPort.TrunkPort, [u'trunk_name', u'if_index', u'percentage'], name, value)


    class SliceAll(Entity):
        """
        Information for all slices
        
        .. attribute:: slice_info
        
        	slice info
        	**type**\: list of  		 :py:class:`SliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo>`
        
        

        """

        _prefix = 'ncs1k-mxp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(HwModule.SliceAll, self).__init__()

            self.yang_name = "slice-all"
            self.yang_parent_name = "hw-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("slice-info", ("slice_info", HwModule.SliceAll.SliceInfo))])
            self._leafs = OrderedDict()

            self.slice_info = YList(self)
            self._segment_path = lambda: "slice-all"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModule.SliceAll, [], name, value)


        class SliceInfo(Entity):
            """
            slice info
            
            .. attribute:: slice_id
            
            	SliceId
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_rate
            
            	ClientRate
            	**type**\:  :py:class:`ClientDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.ClientDataRate>`
            
            .. attribute:: trunk_rate
            
            	TrunkRate
            	**type**\:  :py:class:`TrunkDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.TrunkDataRate>`
            
            .. attribute:: hardware_status
            
            	HardwareStatus
            	**type**\:  :py:class:`HwModuleSliceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModuleSliceStatus>`
            
            .. attribute:: dp_fpga_fw_type
            
            	DpFpgaFwType
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: dp_fpga_fw_ver
            
            	DpFpgaFwVer
            	**type**\: str
            
            	**length:** 0..10
            
            .. attribute:: need_upg
            
            	NeedUpg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: encryption_supported
            
            	EncryptionSupported
            	**type**\: bool
            
            .. attribute:: lldp_drop_status
            
            	LldpDropStatus
            	**type**\: bool
            
            .. attribute:: client_port
            
            	client port
            	**type**\: list of  		 :py:class:`ClientPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort>`
            
            

            """

            _prefix = 'ncs1k-mxp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(HwModule.SliceAll.SliceInfo, self).__init__()

                self.yang_name = "slice-info"
                self.yang_parent_name = "slice-all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("client-port", ("client_port", HwModule.SliceAll.SliceInfo.ClientPort))])
                self._leafs = OrderedDict([
                    ('slice_id', (YLeaf(YType.uint32, 'slice-id'), ['int'])),
                    ('client_rate', (YLeaf(YType.enumeration, 'client-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'ClientDataRate', '')])),
                    ('trunk_rate', (YLeaf(YType.enumeration, 'trunk-rate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'TrunkDataRate', '')])),
                    ('hardware_status', (YLeaf(YType.enumeration, 'hardware-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModuleSliceStatus', '')])),
                    ('dp_fpga_fw_type', (YLeaf(YType.str, 'dp-fpga-fw-type'), ['str'])),
                    ('dp_fpga_fw_ver', (YLeaf(YType.str, 'dp-fpga-fw-ver'), ['str'])),
                    ('need_upg', (YLeaf(YType.uint32, 'need-upg'), ['int'])),
                    ('encryption_supported', (YLeaf(YType.boolean, 'encryption-supported'), ['bool'])),
                    ('lldp_drop_status', (YLeaf(YType.boolean, 'lldp-drop-status'), ['bool'])),
                ])
                self.slice_id = None
                self.client_rate = None
                self.trunk_rate = None
                self.hardware_status = None
                self.dp_fpga_fw_type = None
                self.dp_fpga_fw_ver = None
                self.need_upg = None
                self.encryption_supported = None
                self.lldp_drop_status = None

                self.client_port = YList(self)
                self._segment_path = lambda: "slice-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModule.SliceAll.SliceInfo, [u'slice_id', u'client_rate', u'trunk_rate', u'hardware_status', u'dp_fpga_fw_type', u'dp_fpga_fw_ver', u'need_upg', u'encryption_supported', u'lldp_drop_status'], name, value)


            class ClientPort(Entity):
                """
                client port
                
                .. attribute:: client_name
                
                	ClientName
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: if_index
                
                	IfIndex
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: trunk_port
                
                	trunk port
                	**type**\: list of  		 :py:class:`TrunkPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper.HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort>`
                
                

                """

                _prefix = 'ncs1k-mxp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HwModule.SliceAll.SliceInfo.ClientPort, self).__init__()

                    self.yang_name = "client-port"
                    self.yang_parent_name = "slice-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("trunk-port", ("trunk_port", HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort))])
                    self._leafs = OrderedDict([
                        ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                        ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                    ])
                    self.client_name = None
                    self.if_index = None

                    self.trunk_port = YList(self)
                    self._segment_path = lambda: "client-port"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/slice-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModule.SliceAll.SliceInfo.ClientPort, [u'client_name', u'if_index'], name, value)


                class TrunkPort(Entity):
                    """
                    trunk port
                    
                    .. attribute:: trunk_name
                    
                    	TrunkName
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: if_index
                    
                    	IfIndex
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: percentage
                    
                    	Percentage
                    	**type**\: str
                    
                    	**length:** 0..8
                    
                    

                    """

                    _prefix = 'ncs1k-mxp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort, self).__init__()

                        self.yang_name = "trunk-port"
                        self.yang_parent_name = "client-port"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('trunk_name', (YLeaf(YType.str, 'trunk-name'), ['str'])),
                            ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                            ('percentage', (YLeaf(YType.str, 'percentage'), ['str'])),
                        ])
                        self.trunk_name = None
                        self.if_index = None
                        self.percentage = None
                        self._segment_path = lambda: "trunk-port"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ncs1k-mxp-oper:hw-module/slice-all/slice-info/client-port/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort, [u'trunk_name', u'if_index', u'percentage'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModule()
        return self._top_entity

