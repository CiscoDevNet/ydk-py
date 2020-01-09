""" Cisco_IOS_XR_segment_routing_srv6_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR segment\-routing\-srv6 package operational data.

This module contains definitions
for the following management objects\:
  srv6\: Segment Routing with IPv6 dataplane

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SidAllocation(Enum):
    """
    SidAllocation (Enum Class)

    SID allocation type

    .. data:: unknown = 0

    	Unknown

    .. data:: dynamic = 1

    	Dynamic

    .. data:: explicit = 2

    	Explicit

    """

    unknown = Enum.YLeaf(0, "unknown")

    dynamic = Enum.YLeaf(1, "dynamic")

    explicit = Enum.YLeaf(2, "explicit")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
        return meta._meta_table['SidAllocation']


class SidState(Enum):
    """
    SidState (Enum Class)

    SID manager SID state

    .. data:: unknown = 0

    	Unknown

    .. data:: in_use = 1

    	In Use

    .. data:: pending = 2

    	Pending

    .. data:: stale = 3

    	Stale

    """

    unknown = Enum.YLeaf(0, "unknown")

    in_use = Enum.YLeaf(1, "in-use")

    pending = Enum.YLeaf(2, "pending")

    stale = Enum.YLeaf(3, "stale")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
        return meta._meta_table['SidState']


class Srv6EndFunction(Enum):
    """
    Srv6EndFunction (Enum Class)

    SRv6 End Function Type

    .. data:: unknown = 0

    	Unknown

    .. data:: end = 1

    	End (no PSP/USP)

    .. data:: end_with_psp = 2

    	End with PSP

    .. data:: end_with_usp = 3

    	End with USP

    .. data:: end_with_psp_usp = 4

    	End with PSP/USP

    .. data:: end_x = 5

    	End.X (no PSP/USP)

    .. data:: end_x_with_psp = 6

    	End.X with PSP

    .. data:: end_x_with_usp = 7

    	End.X with USP

    .. data:: end_x_with_psp_usp = 8

    	End.X with PSP/USP

    .. data:: end_tbl = 9

    	End.T (no PSP/USP)

    .. data:: end_tbl_with_psp = 10

    	End.T with PSP

    .. data:: end_tbl_with_usp = 11

    	End.T with USP

    .. data:: end_tbl_with_psp_usp = 12

    	End.T with PSP/USP

    .. data:: end_b6 = 13

    	End.B6

    .. data:: end_b6_encaps = 14

    	End.B6.Encaps

    .. data:: end_bm = 15

    	End.BM

    .. data:: end_dx6 = 16

    	End.DX6

    .. data:: end_dx4 = 17

    	End.DX4

    .. data:: end_dt6 = 18

    	End.DT6

    .. data:: end_dt4 = 19

    	End.DT4

    .. data:: end_dt46 = 20

    	End.DT46

    .. data:: end_dx2 = 21

    	End.DX2

    .. data:: end_dx2v = 22

    	End.DX2V

    .. data:: end_dx2u = 23

    	End.DX2U

    .. data:: end_dx2m = 24

    	End.DX2M

    .. data:: end_otp = 25

    	End.OTP

    .. data:: end_s = 26

    	End.S

    """

    unknown = Enum.YLeaf(0, "unknown")

    end = Enum.YLeaf(1, "end")

    end_with_psp = Enum.YLeaf(2, "end-with-psp")

    end_with_usp = Enum.YLeaf(3, "end-with-usp")

    end_with_psp_usp = Enum.YLeaf(4, "end-with-psp-usp")

    end_x = Enum.YLeaf(5, "end-x")

    end_x_with_psp = Enum.YLeaf(6, "end-x-with-psp")

    end_x_with_usp = Enum.YLeaf(7, "end-x-with-usp")

    end_x_with_psp_usp = Enum.YLeaf(8, "end-x-with-psp-usp")

    end_tbl = Enum.YLeaf(9, "end-tbl")

    end_tbl_with_psp = Enum.YLeaf(10, "end-tbl-with-psp")

    end_tbl_with_usp = Enum.YLeaf(11, "end-tbl-with-usp")

    end_tbl_with_psp_usp = Enum.YLeaf(12, "end-tbl-with-psp-usp")

    end_b6 = Enum.YLeaf(13, "end-b6")

    end_b6_encaps = Enum.YLeaf(14, "end-b6-encaps")

    end_bm = Enum.YLeaf(15, "end-bm")

    end_dx6 = Enum.YLeaf(16, "end-dx6")

    end_dx4 = Enum.YLeaf(17, "end-dx4")

    end_dt6 = Enum.YLeaf(18, "end-dt6")

    end_dt4 = Enum.YLeaf(19, "end-dt4")

    end_dt46 = Enum.YLeaf(20, "end-dt46")

    end_dx2 = Enum.YLeaf(21, "end-dx2")

    end_dx2v = Enum.YLeaf(22, "end-dx2v")

    end_dx2u = Enum.YLeaf(23, "end-dx2u")

    end_dx2m = Enum.YLeaf(24, "end-dx2m")

    end_otp = Enum.YLeaf(25, "end-otp")

    end_s = Enum.YLeaf(26, "end-s")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
        return meta._meta_table['Srv6EndFunction']


class Srv6OutOfResourceState(Enum):
    """
    Srv6OutOfResourceState (Enum Class)

    SRv6 Out of Resource State

    .. data:: oor_green = 0

    	Resources Available

    .. data:: oor_yellow = 1

    	Resources Warning. Have exceeded minor

    	threshold

    .. data:: oor_red = 2

    	Out of Resources. Have exceeded major threshold

    """

    oor_green = Enum.YLeaf(0, "oor-green")

    oor_yellow = Enum.YLeaf(1, "oor-yellow")

    oor_red = Enum.YLeaf(2, "oor-red")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
        return meta._meta_table['Srv6OutOfResourceState']



class Srv6(_Entity_):
    """
    Segment Routing with IPv6 dataplane
    
    .. attribute:: active
    
    	Active SRv6 operational data
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active>`
    
    	**config**\: False
    
    .. attribute:: standby
    
    	Standby SRv6 operational data
    	**type**\:  :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby>`
    
    	**config**\: False
    
    

    """

    _prefix = 'segment-routing-srv6-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Srv6, self).__init__()
        self._top_entity = None

        self.yang_name = "srv6"
        self.yang_parent_name = "Cisco-IOS-XR-segment-routing-srv6-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("active", ("active", Srv6.Active)), ("standby", ("standby", Srv6.Standby))])
        self._leafs = OrderedDict()

        self.active = Srv6.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"

        self.standby = Srv6.Standby()
        self.standby.parent = self
        self._children_name_map["standby"] = "standby"
        self._segment_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Srv6, [], name, value)


    class Active(_Entity_):
        """
        Active SRv6 operational data
        
        .. attribute:: locator_all_stale_sids
        
        	Operational container for all Stale SIDs across all Locators
        	**type**\:  :py:class:`LocatorAllStaleSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids>`
        
        	**config**\: False
        
        .. attribute:: manager
        
        	SID Manager information
        	**type**\:  :py:class:`Manager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager>`
        
        	**config**\: False
        
        .. attribute:: locators
        
        	SRv6 locators related information
        	**type**\:  :py:class:`Locators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators>`
        
        	**config**\: False
        
        .. attribute:: locator_all_sids
        
        	Operational container for all (Active and Stale) SIDs across all Locators
        	**type**\:  :py:class:`LocatorAllSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids>`
        
        	**config**\: False
        
        .. attribute:: locator_all_active_sids
        
        	Operational container for Active SIDs across all Locators
        	**type**\:  :py:class:`LocatorAllActiveSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-srv6-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srv6.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "srv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("locator-all-stale-sids", ("locator_all_stale_sids", Srv6.Active.LocatorAllStaleSids)), ("manager", ("manager", Srv6.Active.Manager)), ("locators", ("locators", Srv6.Active.Locators)), ("locator-all-sids", ("locator_all_sids", Srv6.Active.LocatorAllSids)), ("locator-all-active-sids", ("locator_all_active_sids", Srv6.Active.LocatorAllActiveSids))])
            self._leafs = OrderedDict()

            self.locator_all_stale_sids = Srv6.Active.LocatorAllStaleSids()
            self.locator_all_stale_sids.parent = self
            self._children_name_map["locator_all_stale_sids"] = "locator-all-stale-sids"

            self.manager = Srv6.Active.Manager()
            self.manager.parent = self
            self._children_name_map["manager"] = "manager"

            self.locators = Srv6.Active.Locators()
            self.locators.parent = self
            self._children_name_map["locators"] = "locators"

            self.locator_all_sids = Srv6.Active.LocatorAllSids()
            self.locator_all_sids.parent = self
            self._children_name_map["locator_all_sids"] = "locator-all-sids"

            self.locator_all_active_sids = Srv6.Active.LocatorAllActiveSids()
            self.locator_all_active_sids.parent = self
            self._children_name_map["locator_all_active_sids"] = "locator-all-active-sids"
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srv6.Active, [], name, value)


        class LocatorAllStaleSids(_Entity_):
            """
            Operational container for all Stale SIDs across
            all Locators
            
            .. attribute:: locator_all_stale_sid
            
            	Operational data for given locator and SID opcode
            	**type**\: list of  		 :py:class:`LocatorAllStaleSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Active.LocatorAllStaleSids, self).__init__()

                self.yang_name = "locator-all-stale-sids"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator-all-stale-sid", ("locator_all_stale_sid", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid))])
                self._leafs = OrderedDict()

                self.locator_all_stale_sid = YList(self)
                self._segment_path = lambda: "locator-all-stale-sids"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Active.LocatorAllStaleSids, [], name, value)


            class LocatorAllStaleSid(_Entity_):
                """
                Operational data for given locator and SID
                opcode
                
                .. attribute:: locator_name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: sid_opcode  (key)
                
                	Sid opcode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_context
                
                	SID Context
                	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext>`
                
                	**config**\: False
                
                .. attribute:: create_timestamp
                
                	Creation timestamp
                	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp>`
                
                	**config**\: False
                
                .. attribute:: sid
                
                	SID
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: allocation_type
                
                	Allocation Type
                	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                
                	**config**\: False
                
                .. attribute:: function_type
                
                	Function Type
                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                
                	**config**\: False
                
                .. attribute:: has_forwarding
                
                	Rewrite done or not
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: locator
                
                	Associated locator
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: owner
                
                	Owner
                	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.Owner>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid, self).__init__()

                    self.yang_name = "locator-all-stale-sid"
                    self.yang_parent_name = "locator-all-stale-sids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locator_name','sid_opcode']
                    self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp)), ("owner", ("owner", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.Owner))])
                    self._leafs = OrderedDict([
                        ('locator_name', (YLeaf(YType.str, 'locator-name'), ['str'])),
                        ('sid_opcode', (YLeaf(YType.uint32, 'sid-opcode'), ['int'])),
                        ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                        ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                        ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                        ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                        ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                    ])
                    self.locator_name = None
                    self.sid_opcode = None
                    self.sid = None
                    self.allocation_type = None
                    self.function_type = None
                    self.state = None
                    self.has_forwarding = None
                    self.locator = None

                    self.sid_context = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext()
                    self.sid_context.parent = self
                    self._children_name_map["sid_context"] = "sid-context"

                    self.create_timestamp = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp()
                    self.create_timestamp.parent = self
                    self._children_name_map["create_timestamp"] = "create-timestamp"

                    self.owner = YList(self)
                    self._segment_path = lambda: "locator-all-stale-sid" + "[locator-name='" + str(self.locator_name) + "']" + "[sid-opcode='" + str(self.sid_opcode) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/locator-all-stale-sids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid, ['locator_name', 'sid_opcode', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                class SidContext(_Entity_):
                    """
                    SID Context
                    
                    .. attribute:: key
                    
                    	SID Key
                    	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key>`
                    
                    	**config**\: False
                    
                    .. attribute:: application_data
                    
                    	Application opaque data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext, self).__init__()

                        self.yang_name = "sid-context"
                        self.yang_parent_name = "locator-all-stale-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key))])
                        self._leafs = OrderedDict([
                            ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                        ])
                        self.application_data = None

                        self.key = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                        self._segment_path = lambda: "sid-context"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext, ['application_data'], name, value)


                    class Key(_Entity_):
                        """
                        SID Key
                        
                        .. attribute:: e
                        
                        	End (PSP) SID context
                        	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E>`
                        
                        	**config**\: False
                        
                        .. attribute:: x
                        
                        	End.X (PSP) SID context
                        	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X>`
                        
                        	**config**\: False
                        
                        .. attribute:: dx4
                        
                        	End.DX4 SID context
                        	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4>`
                        
                        	**config**\: False
                        
                        .. attribute:: dt4
                        
                        	End.DT4 SID context
                        	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context_type
                        
                        	SIDContextType
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "sid-context"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("e", ("e", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E)), ("x", ("x", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4))])
                            self._leafs = OrderedDict([
                                ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                            ])
                            self.sid_context_type = None

                            self.e = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E()
                            self.e.parent = self
                            self._children_name_map["e"] = "e"

                            self.x = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X()
                            self.x.parent = self
                            self._children_name_map["x"] = "x"

                            self.dx4 = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4()
                            self.dx4.parent = self
                            self._children_name_map["dx4"] = "dx4"

                            self.dt4 = Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4()
                            self.dt4.parent = self
                            self._children_name_map["dt4"] = "dt4"
                            self._segment_path = lambda: "key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key, ['sid_context_type'], name, value)


                        class E(_Entity_):
                            """
                            End (PSP) SID context
                            
                            .. attribute:: table_id
                            
                            	Table Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E, self).__init__()

                                self.yang_name = "e"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.opaque_id = None
                                self._segment_path = lambda: "e"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.E']['meta_info']


                        class X(_Entity_):
                            """
                            End.X (PSP) SID context
                            
                            .. attribute:: is_protected
                            
                            	Is protected?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: interface
                            
                            	Nexthop interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: nexthop_address
                            
                            	Nexthop IP address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X, self).__init__()

                                self.yang_name = "x"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                ])
                                self.is_protected = None
                                self.opaque_id = None
                                self.interface = None
                                self.nexthop_address = None
                                self._segment_path = lambda: "x"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.X']['meta_info']


                        class Dx4(_Entity_):
                            """
                            End.DX4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_set_id
                            
                            	Next Hop Set ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4, self).__init__()

                                self.yang_name = "dx4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.next_hop_set_id = None
                                self._segment_path = lambda: "dx4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dx4']['meta_info']


                        class Dt4(_Entity_):
                            """
                            End.DT4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4, self).__init__()

                                self.yang_name = "dt4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ])
                                self.table_id = None
                                self._segment_path = lambda: "dt4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4, ['table_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key.Dt4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext.Key']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.SidContext']['meta_info']


                class CreateTimestamp(_Entity_):
                    """
                    Creation timestamp
                    
                    .. attribute:: time_in_nano_seconds
                    
                    	Timestamp in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: age_in_nano_seconds
                    
                    	Age in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp, self).__init__()

                        self.yang_name = "create-timestamp"
                        self.yang_parent_name = "locator-all-stale-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                            ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                        ])
                        self.time_in_nano_seconds = None
                        self.age_in_nano_seconds = None
                        self._segment_path = lambda: "create-timestamp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.CreateTimestamp']['meta_info']


                class Owner(_Entity_):
                    """
                    Owner
                    
                    .. attribute:: owner
                    
                    	Owner
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.Owner, self).__init__()

                        self.yang_name = "owner"
                        self.yang_parent_name = "locator-all-stale-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                        ])
                        self.owner = None
                        self._segment_path = lambda: "owner"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.Owner, ['owner'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid.Owner']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.LocatorAllStaleSids.LocatorAllStaleSid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Active.LocatorAllStaleSids']['meta_info']


        class Manager(_Entity_):
            """
            SID Manager information
            
            .. attribute:: sid_mgr_params
            
            	SID Mgr parameters
            	**type**\:  :py:class:`SidMgrParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.SidMgrParams>`
            
            	**config**\: False
            
            .. attribute:: sid_mgr_summary
            
            	SID Mgr summary info
            	**type**\:  :py:class:`SidMgrSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.SidMgrSummary>`
            
            	**config**\: False
            
            .. attribute:: platform_capabilities
            
            	Platform Capabilities
            	**type**\:  :py:class:`PlatformCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Active.Manager, self).__init__()

                self.yang_name = "manager"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sid-mgr-params", ("sid_mgr_params", Srv6.Active.Manager.SidMgrParams)), ("sid-mgr-summary", ("sid_mgr_summary", Srv6.Active.Manager.SidMgrSummary)), ("platform-capabilities", ("platform_capabilities", Srv6.Active.Manager.PlatformCapabilities))])
                self._leafs = OrderedDict()

                self.sid_mgr_params = Srv6.Active.Manager.SidMgrParams()
                self.sid_mgr_params.parent = self
                self._children_name_map["sid_mgr_params"] = "sid-mgr-params"

                self.sid_mgr_summary = Srv6.Active.Manager.SidMgrSummary()
                self.sid_mgr_summary.parent = self
                self._children_name_map["sid_mgr_summary"] = "sid-mgr-summary"

                self.platform_capabilities = Srv6.Active.Manager.PlatformCapabilities()
                self.platform_capabilities.parent = self
                self._children_name_map["platform_capabilities"] = "platform-capabilities"
                self._segment_path = lambda: "manager"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Active.Manager, [], name, value)


            class SidMgrParams(_Entity_):
                """
                SID Mgr parameters
                
                .. attribute:: encap_hop_limit
                
                	Encap Hop\-limit info
                	**type**\:  :py:class:`EncapHopLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.SidMgrParams.EncapHopLimit>`
                
                	**config**\: False
                
                .. attribute:: srv6_enabled
                
                	Is SRv6 enabled?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: configured_encap_source_address
                
                	Configured Encap Source address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: default_encap_source_address
                
                	Default Encap Source address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: encap_ttl_propagate
                
                	Is TTL propagate enabled?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_sid_holdtime_configured
                
                	Is SID Holdtime configured?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sid_holdtime_mins_configured
                
                	Configured SID Holdtime in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: minute
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.Manager.SidMgrParams, self).__init__()

                    self.yang_name = "sid-mgr-params"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("encap-hop-limit", ("encap_hop_limit", Srv6.Active.Manager.SidMgrParams.EncapHopLimit))])
                    self._leafs = OrderedDict([
                        ('srv6_enabled', (YLeaf(YType.boolean, 'srv6-enabled'), ['bool'])),
                        ('configured_encap_source_address', (YLeaf(YType.str, 'configured-encap-source-address'), ['str'])),
                        ('default_encap_source_address', (YLeaf(YType.str, 'default-encap-source-address'), ['str'])),
                        ('encap_ttl_propagate', (YLeaf(YType.boolean, 'encap-ttl-propagate'), ['bool'])),
                        ('is_sid_holdtime_configured', (YLeaf(YType.boolean, 'is-sid-holdtime-configured'), ['bool'])),
                        ('sid_holdtime_mins_configured', (YLeaf(YType.uint32, 'sid-holdtime-mins-configured'), ['int'])),
                    ])
                    self.srv6_enabled = None
                    self.configured_encap_source_address = None
                    self.default_encap_source_address = None
                    self.encap_ttl_propagate = None
                    self.is_sid_holdtime_configured = None
                    self.sid_holdtime_mins_configured = None

                    self.encap_hop_limit = Srv6.Active.Manager.SidMgrParams.EncapHopLimit()
                    self.encap_hop_limit.parent = self
                    self._children_name_map["encap_hop_limit"] = "encap-hop-limit"
                    self._segment_path = lambda: "sid-mgr-params"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.Manager.SidMgrParams, ['srv6_enabled', 'configured_encap_source_address', 'default_encap_source_address', 'encap_ttl_propagate', 'is_sid_holdtime_configured', 'sid_holdtime_mins_configured'], name, value)


                class EncapHopLimit(_Entity_):
                    """
                    Encap Hop\-limit info
                    
                    .. attribute:: use_default
                    
                    	Use default IPv6 hop\-limit value
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: do_propagate
                    
                    	Propagate IP TTL to Encap IPv6 hop\-limit
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: value
                    
                    	Specific value set for hop\-limit count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.Manager.SidMgrParams.EncapHopLimit, self).__init__()

                        self.yang_name = "encap-hop-limit"
                        self.yang_parent_name = "sid-mgr-params"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('use_default', (YLeaf(YType.boolean, 'use-default'), ['bool'])),
                            ('do_propagate', (YLeaf(YType.boolean, 'do-propagate'), ['bool'])),
                            ('value', (YLeaf(YType.uint8, 'value'), ['int'])),
                        ])
                        self.use_default = None
                        self.do_propagate = None
                        self.value = None
                        self._segment_path = lambda: "encap-hop-limit"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/sid-mgr-params/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.Manager.SidMgrParams.EncapHopLimit, ['use_default', 'do_propagate', 'value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.Manager.SidMgrParams.EncapHopLimit']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.Manager.SidMgrParams']['meta_info']


            class SidMgrSummary(_Entity_):
                """
                SID Mgr summary info
                
                .. attribute:: sids_out_of_resource_summary
                
                	SIDs Global Out of Resource info
                	**type**\:  :py:class:`SidsOutOfResourceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary>`
                
                	**config**\: False
                
                .. attribute:: locators_count
                
                	Number of locators
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: oper_locators_count
                
                	Number of operational locators
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: sids_count
                
                	Number of SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: stale_sids_count
                
                	Number of Stale SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: maximum_sids_count
                
                	Global Maximum number of SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.Manager.SidMgrSummary, self).__init__()

                    self.yang_name = "sid-mgr-summary"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sids-out-of-resource-summary", ("sids_out_of_resource_summary", Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary))])
                    self._leafs = OrderedDict([
                        ('locators_count', (YLeaf(YType.uint16, 'locators-count'), ['int'])),
                        ('oper_locators_count', (YLeaf(YType.uint16, 'oper-locators-count'), ['int'])),
                        ('sids_count', (YLeaf(YType.uint32, 'sids-count'), ['int'])),
                        ('stale_sids_count', (YLeaf(YType.uint32, 'stale-sids-count'), ['int'])),
                        ('maximum_sids_count', (YLeaf(YType.uint32, 'maximum-sids-count'), ['int'])),
                    ])
                    self.locators_count = None
                    self.oper_locators_count = None
                    self.sids_count = None
                    self.stale_sids_count = None
                    self.maximum_sids_count = None

                    self.sids_out_of_resource_summary = Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary()
                    self.sids_out_of_resource_summary.parent = self
                    self._children_name_map["sids_out_of_resource_summary"] = "sids-out-of-resource-summary"
                    self._segment_path = lambda: "sid-mgr-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.Manager.SidMgrSummary, ['locators_count', 'oper_locators_count', 'sids_count', 'stale_sids_count', 'maximum_sids_count'], name, value)


                class SidsOutOfResourceSummary(_Entity_):
                    """
                    SIDs Global Out of Resource info
                    
                    .. attribute:: out_of_resources_state
                    
                    	Global Resources State for SIDs
                    	**type**\:  :py:class:`Srv6OutOfResourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6OutOfResourceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: oor_yellow_free_sid_threshold
                    
                    	Threshold for Number of Free SID below which OOR Yellow State is reached
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_green_free_sid_threshold
                    
                    	Threshold for Number of Free SID above which OOR Green State is restored
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_green_count
                    
                    	Number of times Resources Warning or Out of Resources state has been cleared
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_yellow_count
                    
                    	Number of times system went into Resources Warning state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_red_count
                    
                    	Number of times system went into Out of Resources state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary, self).__init__()

                        self.yang_name = "sids-out-of-resource-summary"
                        self.yang_parent_name = "sid-mgr-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('out_of_resources_state', (YLeaf(YType.enumeration, 'out-of-resources-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6OutOfResourceState', '')])),
                            ('oor_yellow_free_sid_threshold', (YLeaf(YType.uint32, 'oor-yellow-free-sid-threshold'), ['int'])),
                            ('oor_green_free_sid_threshold', (YLeaf(YType.uint32, 'oor-green-free-sid-threshold'), ['int'])),
                            ('oor_green_count', (YLeaf(YType.uint32, 'oor-green-count'), ['int'])),
                            ('oor_yellow_count', (YLeaf(YType.uint32, 'oor-yellow-count'), ['int'])),
                            ('oor_red_count', (YLeaf(YType.uint32, 'oor-red-count'), ['int'])),
                        ])
                        self.out_of_resources_state = None
                        self.oor_yellow_free_sid_threshold = None
                        self.oor_green_free_sid_threshold = None
                        self.oor_green_count = None
                        self.oor_yellow_count = None
                        self.oor_red_count = None
                        self._segment_path = lambda: "sids-out-of-resource-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/sid-mgr-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary, ['out_of_resources_state', 'oor_yellow_free_sid_threshold', 'oor_green_free_sid_threshold', 'oor_green_count', 'oor_yellow_count', 'oor_red_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.Manager.SidMgrSummary.SidsOutOfResourceSummary']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.Manager.SidMgrSummary']['meta_info']


            class PlatformCapabilities(_Entity_):
                """
                Platform Capabilities
                
                .. attribute:: support
                
                	Feature support
                	**type**\:  :py:class:`Support <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support>`
                
                	**config**\: False
                
                .. attribute:: max_sid
                
                	Maximum Sids
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_holdtime_mins
                
                	Freed SID holdtime in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: minute
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.Manager.PlatformCapabilities, self).__init__()

                    self.yang_name = "platform-capabilities"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("support", ("support", Srv6.Active.Manager.PlatformCapabilities.Support))])
                    self._leafs = OrderedDict([
                        ('max_sid', (YLeaf(YType.uint32, 'max-sid'), ['int'])),
                        ('sid_holdtime_mins', (YLeaf(YType.uint32, 'sid-holdtime-mins'), ['int'])),
                    ])
                    self.max_sid = None
                    self.sid_holdtime_mins = None

                    self.support = Srv6.Active.Manager.PlatformCapabilities.Support()
                    self.support.parent = self
                    self._children_name_map["support"] = "support"
                    self._segment_path = lambda: "platform-capabilities"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities, ['max_sid', 'sid_holdtime_mins'], name, value)


                class Support(_Entity_):
                    """
                    Feature support
                    
                    .. attribute:: signaled_parameters
                    
                    	Signaled Parameters
                    	**type**\:  :py:class:`SignaledParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters>`
                    
                    	**config**\: False
                    
                    .. attribute:: srv6
                    
                    	SRv6 support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: tilfa
                    
                    	TI LFA support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: microloop_avoidance
                    
                    	Microloop\-avoidance support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: end_func
                    
                    	Supported end functions
                    	**type**\: list of  		 :py:class:`EndFunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support.EndFunc>`
                    
                    	**config**\: False
                    
                    .. attribute:: transit_func
                    
                    	Supported Transit functions
                    	**type**\: list of  		 :py:class:`TransitFunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support.TransitFunc>`
                    
                    	**config**\: False
                    
                    .. attribute:: security_rule
                    
                    	Security rules
                    	**type**\: list of  		 :py:class:`SecurityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support.SecurityRule>`
                    
                    	**config**\: False
                    
                    .. attribute:: counter
                    
                    	Counters
                    	**type**\: list of  		 :py:class:`Counter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Manager.PlatformCapabilities.Support.Counter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.Manager.PlatformCapabilities.Support, self).__init__()

                        self.yang_name = "support"
                        self.yang_parent_name = "platform-capabilities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("signaled-parameters", ("signaled_parameters", Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters)), ("end-func", ("end_func", Srv6.Active.Manager.PlatformCapabilities.Support.EndFunc)), ("transit-func", ("transit_func", Srv6.Active.Manager.PlatformCapabilities.Support.TransitFunc)), ("security-rule", ("security_rule", Srv6.Active.Manager.PlatformCapabilities.Support.SecurityRule)), ("counter", ("counter", Srv6.Active.Manager.PlatformCapabilities.Support.Counter))])
                        self._leafs = OrderedDict([
                            ('srv6', (YLeaf(YType.boolean, 'srv6'), ['bool'])),
                            ('tilfa', (YLeaf(YType.boolean, 'tilfa'), ['bool'])),
                            ('microloop_avoidance', (YLeaf(YType.boolean, 'microloop-avoidance'), ['bool'])),
                        ])
                        self.srv6 = None
                        self.tilfa = None
                        self.microloop_avoidance = None

                        self.signaled_parameters = Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters()
                        self.signaled_parameters.parent = self
                        self._children_name_map["signaled_parameters"] = "signaled-parameters"

                        self.end_func = YList(self)
                        self.transit_func = YList(self)
                        self.security_rule = YList(self)
                        self.counter = YList(self)
                        self._segment_path = lambda: "support"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support, ['srv6', 'tilfa', 'microloop_avoidance'], name, value)


                    class SignaledParameters(_Entity_):
                        """
                        Signaled Parameters
                        
                        .. attribute:: max_sl
                        
                        	Max value of SegmentLeft field in received SRH
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_end_pop_srh
                        
                        	Max num of SIDs in rcvd SRH for pop
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_t_insert
                        
                        	Max num of SIDs for T.Insert op
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_t_encap
                        
                        	Max num of SIDs for T.Encaps op
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_end_d
                        
                        	Max num of SIDs in rcvd SRH for decap
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters, self).__init__()

                            self.yang_name = "signaled-parameters"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('max_sl', (YLeaf(YType.uint8, 'max-sl'), ['int'])),
                                ('max_end_pop_srh', (YLeaf(YType.uint8, 'max-end-pop-srh'), ['int'])),
                                ('max_t_insert', (YLeaf(YType.uint8, 'max-t-insert'), ['int'])),
                                ('max_t_encap', (YLeaf(YType.uint8, 'max-t-encap'), ['int'])),
                                ('max_end_d', (YLeaf(YType.uint8, 'max-end-d'), ['int'])),
                            ])
                            self.max_sl = None
                            self.max_end_pop_srh = None
                            self.max_t_insert = None
                            self.max_t_encap = None
                            self.max_end_d = None
                            self._segment_path = lambda: "signaled-parameters"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters, ['max_sl', 'max_end_pop_srh', 'max_t_insert', 'max_t_encap', 'max_end_d'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support.SignaledParameters']['meta_info']


                    class EndFunc(_Entity_):
                        """
                        Supported end functions
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Manager.PlatformCapabilities.Support.EndFunc, self).__init__()

                            self.yang_name = "end-func"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "end-func"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support.EndFunc, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support.EndFunc']['meta_info']


                    class TransitFunc(_Entity_):
                        """
                        Supported Transit functions
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Manager.PlatformCapabilities.Support.TransitFunc, self).__init__()

                            self.yang_name = "transit-func"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "transit-func"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support.TransitFunc, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support.TransitFunc']['meta_info']


                    class SecurityRule(_Entity_):
                        """
                        Security rules
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Manager.PlatformCapabilities.Support.SecurityRule, self).__init__()

                            self.yang_name = "security-rule"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "security-rule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support.SecurityRule, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support.SecurityRule']['meta_info']


                    class Counter(_Entity_):
                        """
                        Counters
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Manager.PlatformCapabilities.Support.Counter, self).__init__()

                            self.yang_name = "counter"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "counter"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Manager.PlatformCapabilities.Support.Counter, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support.Counter']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities.Support']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.Manager.PlatformCapabilities']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Active.Manager']['meta_info']


        class Locators(_Entity_):
            """
            SRv6 locators related information
            
            .. attribute:: locator
            
            	Operational data for given SRv6 locator
            	**type**\: list of  		 :py:class:`Locator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Active.Locators, self).__init__()

                self.yang_name = "locators"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator", ("locator", Srv6.Active.Locators.Locator))])
                self._leafs = OrderedDict()

                self.locator = YList(self)
                self._segment_path = lambda: "locators"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Active.Locators, [], name, value)


            class Locator(_Entity_):
                """
                Operational data for given SRv6 locator
                
                .. attribute:: name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: info
                
                	Operational data for given SRv6 locator
                	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Info>`
                
                	**config**\: False
                
                .. attribute:: sids
                
                	SRv6 locator SID table
                	**type**\:  :py:class:`Sids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.Locators.Locator, self).__init__()

                    self.yang_name = "locator"
                    self.yang_parent_name = "locators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("info", ("info", Srv6.Active.Locators.Locator.Info)), ("sids", ("sids", Srv6.Active.Locators.Locator.Sids))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.info = Srv6.Active.Locators.Locator.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"

                    self.sids = Srv6.Active.Locators.Locator.Sids()
                    self.sids.parent = self
                    self._children_name_map["sids"] = "sids"
                    self._segment_path = lambda: "locator" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/locators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.Locators.Locator, ['name'], name, value)


                class Info(_Entity_):
                    """
                    Operational data for given SRv6 locator
                    
                    .. attribute:: interface
                    
                    	Locator IM intf info
                    	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Info.Interface>`
                    
                    	**config**\: False
                    
                    .. attribute:: create_timestamp
                    
                    	Creation timestamp
                    	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Info.CreateTimestamp>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Locator Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	Locator ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: prefix
                    
                    	Locator Prefix
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_operational
                    
                    	Locator status is Up or Down
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_default
                    
                    	Locator is the default locator
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: out_of_resources_state
                    
                    	Locator Resources State for SIDs
                    	**type**\:  :py:class:`Srv6OutOfResourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6OutOfResourceState>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.Locators.Locator.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "locator"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Srv6.Active.Locators.Locator.Info.Interface)), ("create-timestamp", ("create_timestamp", Srv6.Active.Locators.Locator.Info.CreateTimestamp))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('is_operational', (YLeaf(YType.boolean, 'is-operational'), ['bool'])),
                            ('is_default', (YLeaf(YType.boolean, 'is-default'), ['bool'])),
                            ('out_of_resources_state', (YLeaf(YType.enumeration, 'out-of-resources-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6OutOfResourceState', '')])),
                        ])
                        self.name = None
                        self.id = None
                        self.prefix = None
                        self.is_operational = None
                        self.is_default = None
                        self.out_of_resources_state = None

                        self.interface = Srv6.Active.Locators.Locator.Info.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"

                        self.create_timestamp = Srv6.Active.Locators.Locator.Info.CreateTimestamp()
                        self.create_timestamp.parent = self
                        self._children_name_map["create_timestamp"] = "create-timestamp"
                        self._segment_path = lambda: "info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.Locators.Locator.Info, ['name', 'id', 'prefix', 'is_operational', 'is_default', 'out_of_resources_state'], name, value)


                    class Interface(_Entity_):
                        """
                        Locator IM intf info
                        
                        .. attribute:: name
                        
                        	Interface name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: if_handle
                        
                        	Interface handle
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**config**\: False
                        
                        .. attribute:: programmed_prefix
                        
                        	Interface prefix/addr programmed
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Locators.Locator.Info.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                                ('programmed_prefix', (YLeaf(YType.str, 'programmed-prefix'), ['str'])),
                            ])
                            self.name = None
                            self.if_handle = None
                            self.programmed_prefix = None
                            self._segment_path = lambda: "interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Locators.Locator.Info.Interface, ['name', 'if_handle', 'programmed_prefix'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Locators.Locator.Info.Interface']['meta_info']


                    class CreateTimestamp(_Entity_):
                        """
                        Creation timestamp
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Timestamp in nano seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: age_in_nano_seconds
                        
                        	Age in nano seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Locators.Locator.Info.CreateTimestamp, self).__init__()

                            self.yang_name = "create-timestamp"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                                ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                            ])
                            self.time_in_nano_seconds = None
                            self.age_in_nano_seconds = None
                            self._segment_path = lambda: "create-timestamp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Locators.Locator.Info.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Locators.Locator.Info.CreateTimestamp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.Locators.Locator.Info']['meta_info']


                class Sids(_Entity_):
                    """
                    SRv6 locator SID table
                    
                    .. attribute:: sid
                    
                    	Operational data for given SRv6 SID
                    	**type**\: list of  		 :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.Locators.Locator.Sids, self).__init__()

                        self.yang_name = "sids"
                        self.yang_parent_name = "locator"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid", ("sid", Srv6.Active.Locators.Locator.Sids.Sid))])
                        self._leafs = OrderedDict()

                        self.sid = YList(self)
                        self._segment_path = lambda: "sids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.Locators.Locator.Sids, [], name, value)


                    class Sid(_Entity_):
                        """
                        Operational data for given SRv6 SID
                        
                        .. attribute:: address  (key)
                        
                        	IPv6 address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context
                        
                        	SID Context
                        	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext>`
                        
                        	**config**\: False
                        
                        .. attribute:: create_timestamp
                        
                        	Creation timestamp
                        	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid
                        
                        	SID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: allocation_type
                        
                        	Allocation Type
                        	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                        
                        	**config**\: False
                        
                        .. attribute:: function_type
                        
                        	Function Type
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                        
                        	**config**\: False
                        
                        .. attribute:: has_forwarding
                        
                        	Rewrite done or not
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: locator
                        
                        	Associated locator
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: owner
                        
                        	Owner
                        	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.Owner>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.Locators.Locator.Sids.Sid, self).__init__()

                            self.yang_name = "sid"
                            self.yang_parent_name = "sids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Active.Locators.Locator.Sids.Sid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp)), ("owner", ("owner", Srv6.Active.Locators.Locator.Sids.Sid.Owner))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                                ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                                ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                                ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                                ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                            ])
                            self.address = None
                            self.sid = None
                            self.allocation_type = None
                            self.function_type = None
                            self.state = None
                            self.has_forwarding = None
                            self.locator = None

                            self.sid_context = Srv6.Active.Locators.Locator.Sids.Sid.SidContext()
                            self.sid_context.parent = self
                            self._children_name_map["sid_context"] = "sid-context"

                            self.create_timestamp = Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp()
                            self.create_timestamp.parent = self
                            self._children_name_map["create_timestamp"] = "create-timestamp"

                            self.owner = YList(self)
                            self._segment_path = lambda: "sid" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid, ['address', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                        class SidContext(_Entity_):
                            """
                            SID Context
                            
                            .. attribute:: key
                            
                            	SID Key
                            	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key>`
                            
                            	**config**\: False
                            
                            .. attribute:: application_data
                            
                            	Application opaque data
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext, self).__init__()

                                self.yang_name = "sid-context"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("key", ("key", Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key))])
                                self._leafs = OrderedDict([
                                    ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                                ])
                                self.application_data = None

                                self.key = Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key()
                                self.key.parent = self
                                self._children_name_map["key"] = "key"
                                self._segment_path = lambda: "sid-context"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext, ['application_data'], name, value)


                            class Key(_Entity_):
                                """
                                SID Key
                                
                                .. attribute:: e
                                
                                	End (PSP) SID context
                                	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E>`
                                
                                	**config**\: False
                                
                                .. attribute:: x
                                
                                	End.X (PSP) SID context
                                	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X>`
                                
                                	**config**\: False
                                
                                .. attribute:: dx4
                                
                                	End.DX4 SID context
                                	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4>`
                                
                                	**config**\: False
                                
                                .. attribute:: dt4
                                
                                	End.DT4 SID context
                                	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4>`
                                
                                	**config**\: False
                                
                                .. attribute:: sid_context_type
                                
                                	SIDContextType
                                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'segment-routing-srv6-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key, self).__init__()

                                    self.yang_name = "key"
                                    self.yang_parent_name = "sid-context"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("e", ("e", Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E)), ("x", ("x", Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4))])
                                    self._leafs = OrderedDict([
                                        ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                                    ])
                                    self.sid_context_type = None

                                    self.e = Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E()
                                    self.e.parent = self
                                    self._children_name_map["e"] = "e"

                                    self.x = Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X()
                                    self.x.parent = self
                                    self._children_name_map["x"] = "x"

                                    self.dx4 = Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4()
                                    self.dx4.parent = self
                                    self._children_name_map["dx4"] = "dx4"

                                    self.dt4 = Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4()
                                    self.dt4.parent = self
                                    self._children_name_map["dt4"] = "dt4"
                                    self._segment_path = lambda: "key"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key, ['sid_context_type'], name, value)


                                class E(_Entity_):
                                    """
                                    End (PSP) SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table Id
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Additional differentiator \- opaque to SIDMgr
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E, self).__init__()

                                        self.yang_name = "e"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                            ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self.opaque_id = None
                                        self._segment_path = lambda: "e"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.E']['meta_info']


                                class X(_Entity_):
                                    """
                                    End.X (PSP) SID context
                                    
                                    .. attribute:: is_protected
                                    
                                    	Is protected?
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Additional differentiator \- opaque to SIDMgr
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface
                                    
                                    	Nexthop interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nexthop_address
                                    
                                    	Nexthop IP address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X, self).__init__()

                                        self.yang_name = "x"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                            ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                            ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                        ])
                                        self.is_protected = None
                                        self.opaque_id = None
                                        self.interface = None
                                        self.nexthop_address = None
                                        self._segment_path = lambda: "x"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.X']['meta_info']


                                class Dx4(_Entity_):
                                    """
                                    End.DX4 SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: next_hop_set_id
                                    
                                    	Next Hop Set ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4, self).__init__()

                                        self.yang_name = "dx4"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                            ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self.next_hop_set_id = None
                                        self._segment_path = lambda: "dx4"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dx4']['meta_info']


                                class Dt4(_Entity_):
                                    """
                                    End.DT4 SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4, self).__init__()

                                        self.yang_name = "dt4"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self._segment_path = lambda: "dt4"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4, ['table_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key.Dt4']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                    return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext.Key']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.SidContext']['meta_info']


                        class CreateTimestamp(_Entity_):
                            """
                            Creation timestamp
                            
                            .. attribute:: time_in_nano_seconds
                            
                            	Timestamp in nano seconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: nanosecond
                            
                            .. attribute:: age_in_nano_seconds
                            
                            	Age in nano seconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: nanosecond
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp, self).__init__()

                                self.yang_name = "create-timestamp"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                                    ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                                ])
                                self.time_in_nano_seconds = None
                                self.age_in_nano_seconds = None
                                self._segment_path = lambda: "create-timestamp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.CreateTimestamp']['meta_info']


                        class Owner(_Entity_):
                            """
                            Owner
                            
                            .. attribute:: owner
                            
                            	Owner
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.Locators.Locator.Sids.Sid.Owner, self).__init__()

                                self.yang_name = "owner"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                                ])
                                self.owner = None
                                self._segment_path = lambda: "owner"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.Locators.Locator.Sids.Sid.Owner, ['owner'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid.Owner']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.Locators.Locator.Sids.Sid']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.Locators.Locator.Sids']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.Locators.Locator']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Active.Locators']['meta_info']


        class LocatorAllSids(_Entity_):
            """
            Operational container for all (Active and Stale)
            SIDs across all Locators
            
            .. attribute:: locator_all_sid
            
            	Operational data for given locator and SID opcode
            	**type**\: list of  		 :py:class:`LocatorAllSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Active.LocatorAllSids, self).__init__()

                self.yang_name = "locator-all-sids"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator-all-sid", ("locator_all_sid", Srv6.Active.LocatorAllSids.LocatorAllSid))])
                self._leafs = OrderedDict()

                self.locator_all_sid = YList(self)
                self._segment_path = lambda: "locator-all-sids"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Active.LocatorAllSids, [], name, value)


            class LocatorAllSid(_Entity_):
                """
                Operational data for given locator and SID
                opcode
                
                .. attribute:: locator_name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: sid_opcode  (key)
                
                	Sid opcode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_context
                
                	SID Context
                	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext>`
                
                	**config**\: False
                
                .. attribute:: create_timestamp
                
                	Creation timestamp
                	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp>`
                
                	**config**\: False
                
                .. attribute:: sid
                
                	SID
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: allocation_type
                
                	Allocation Type
                	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                
                	**config**\: False
                
                .. attribute:: function_type
                
                	Function Type
                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                
                	**config**\: False
                
                .. attribute:: has_forwarding
                
                	Rewrite done or not
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: locator
                
                	Associated locator
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: owner
                
                	Owner
                	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.Owner>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.LocatorAllSids.LocatorAllSid, self).__init__()

                    self.yang_name = "locator-all-sid"
                    self.yang_parent_name = "locator-all-sids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locator_name','sid_opcode']
                    self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp)), ("owner", ("owner", Srv6.Active.LocatorAllSids.LocatorAllSid.Owner))])
                    self._leafs = OrderedDict([
                        ('locator_name', (YLeaf(YType.str, 'locator-name'), ['str'])),
                        ('sid_opcode', (YLeaf(YType.uint32, 'sid-opcode'), ['int'])),
                        ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                        ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                        ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                        ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                        ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                    ])
                    self.locator_name = None
                    self.sid_opcode = None
                    self.sid = None
                    self.allocation_type = None
                    self.function_type = None
                    self.state = None
                    self.has_forwarding = None
                    self.locator = None

                    self.sid_context = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext()
                    self.sid_context.parent = self
                    self._children_name_map["sid_context"] = "sid-context"

                    self.create_timestamp = Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp()
                    self.create_timestamp.parent = self
                    self._children_name_map["create_timestamp"] = "create-timestamp"

                    self.owner = YList(self)
                    self._segment_path = lambda: "locator-all-sid" + "[locator-name='" + str(self.locator_name) + "']" + "[sid-opcode='" + str(self.sid_opcode) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/locator-all-sids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid, ['locator_name', 'sid_opcode', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                class SidContext(_Entity_):
                    """
                    SID Context
                    
                    .. attribute:: key
                    
                    	SID Key
                    	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key>`
                    
                    	**config**\: False
                    
                    .. attribute:: application_data
                    
                    	Application opaque data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext, self).__init__()

                        self.yang_name = "sid-context"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key))])
                        self._leafs = OrderedDict([
                            ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                        ])
                        self.application_data = None

                        self.key = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                        self._segment_path = lambda: "sid-context"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext, ['application_data'], name, value)


                    class Key(_Entity_):
                        """
                        SID Key
                        
                        .. attribute:: e
                        
                        	End (PSP) SID context
                        	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E>`
                        
                        	**config**\: False
                        
                        .. attribute:: x
                        
                        	End.X (PSP) SID context
                        	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X>`
                        
                        	**config**\: False
                        
                        .. attribute:: dx4
                        
                        	End.DX4 SID context
                        	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4>`
                        
                        	**config**\: False
                        
                        .. attribute:: dt4
                        
                        	End.DT4 SID context
                        	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context_type
                        
                        	SIDContextType
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "sid-context"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("e", ("e", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E)), ("x", ("x", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4))])
                            self._leafs = OrderedDict([
                                ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                            ])
                            self.sid_context_type = None

                            self.e = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E()
                            self.e.parent = self
                            self._children_name_map["e"] = "e"

                            self.x = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X()
                            self.x.parent = self
                            self._children_name_map["x"] = "x"

                            self.dx4 = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4()
                            self.dx4.parent = self
                            self._children_name_map["dx4"] = "dx4"

                            self.dt4 = Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4()
                            self.dt4.parent = self
                            self._children_name_map["dt4"] = "dt4"
                            self._segment_path = lambda: "key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key, ['sid_context_type'], name, value)


                        class E(_Entity_):
                            """
                            End (PSP) SID context
                            
                            .. attribute:: table_id
                            
                            	Table Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E, self).__init__()

                                self.yang_name = "e"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.opaque_id = None
                                self._segment_path = lambda: "e"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.E']['meta_info']


                        class X(_Entity_):
                            """
                            End.X (PSP) SID context
                            
                            .. attribute:: is_protected
                            
                            	Is protected?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: interface
                            
                            	Nexthop interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: nexthop_address
                            
                            	Nexthop IP address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X, self).__init__()

                                self.yang_name = "x"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                ])
                                self.is_protected = None
                                self.opaque_id = None
                                self.interface = None
                                self.nexthop_address = None
                                self._segment_path = lambda: "x"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.X']['meta_info']


                        class Dx4(_Entity_):
                            """
                            End.DX4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_set_id
                            
                            	Next Hop Set ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4, self).__init__()

                                self.yang_name = "dx4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.next_hop_set_id = None
                                self._segment_path = lambda: "dx4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4']['meta_info']


                        class Dt4(_Entity_):
                            """
                            End.DT4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4, self).__init__()

                                self.yang_name = "dt4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ])
                                self.table_id = None
                                self._segment_path = lambda: "dt4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4, ['table_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext.Key']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.SidContext']['meta_info']


                class CreateTimestamp(_Entity_):
                    """
                    Creation timestamp
                    
                    .. attribute:: time_in_nano_seconds
                    
                    	Timestamp in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: age_in_nano_seconds
                    
                    	Age in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp, self).__init__()

                        self.yang_name = "create-timestamp"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                            ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                        ])
                        self.time_in_nano_seconds = None
                        self.age_in_nano_seconds = None
                        self._segment_path = lambda: "create-timestamp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.CreateTimestamp']['meta_info']


                class Owner(_Entity_):
                    """
                    Owner
                    
                    .. attribute:: owner
                    
                    	Owner
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllSids.LocatorAllSid.Owner, self).__init__()

                        self.yang_name = "owner"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                        ])
                        self.owner = None
                        self._segment_path = lambda: "owner"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllSids.LocatorAllSid.Owner, ['owner'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid.Owner']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.LocatorAllSids.LocatorAllSid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Active.LocatorAllSids']['meta_info']


        class LocatorAllActiveSids(_Entity_):
            """
            Operational container for Active SIDs across all
            Locators
            
            .. attribute:: locator_all_active_sid
            
            	Operational data for given locator and SID opcode
            	**type**\: list of  		 :py:class:`LocatorAllActiveSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Active.LocatorAllActiveSids, self).__init__()

                self.yang_name = "locator-all-active-sids"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator-all-active-sid", ("locator_all_active_sid", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid))])
                self._leafs = OrderedDict()

                self.locator_all_active_sid = YList(self)
                self._segment_path = lambda: "locator-all-active-sids"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Active.LocatorAllActiveSids, [], name, value)


            class LocatorAllActiveSid(_Entity_):
                """
                Operational data for given locator and SID
                opcode
                
                .. attribute:: locator_name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: sid_opcode  (key)
                
                	Sid opcode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_context
                
                	SID Context
                	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext>`
                
                	**config**\: False
                
                .. attribute:: create_timestamp
                
                	Creation timestamp
                	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp>`
                
                	**config**\: False
                
                .. attribute:: sid
                
                	SID
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: allocation_type
                
                	Allocation Type
                	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                
                	**config**\: False
                
                .. attribute:: function_type
                
                	Function Type
                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                
                	**config**\: False
                
                .. attribute:: has_forwarding
                
                	Rewrite done or not
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: locator
                
                	Associated locator
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: owner
                
                	Owner
                	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.Owner>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid, self).__init__()

                    self.yang_name = "locator-all-active-sid"
                    self.yang_parent_name = "locator-all-active-sids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locator_name','sid_opcode']
                    self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp)), ("owner", ("owner", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.Owner))])
                    self._leafs = OrderedDict([
                        ('locator_name', (YLeaf(YType.str, 'locator-name'), ['str'])),
                        ('sid_opcode', (YLeaf(YType.uint32, 'sid-opcode'), ['int'])),
                        ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                        ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                        ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                        ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                        ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                    ])
                    self.locator_name = None
                    self.sid_opcode = None
                    self.sid = None
                    self.allocation_type = None
                    self.function_type = None
                    self.state = None
                    self.has_forwarding = None
                    self.locator = None

                    self.sid_context = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext()
                    self.sid_context.parent = self
                    self._children_name_map["sid_context"] = "sid-context"

                    self.create_timestamp = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp()
                    self.create_timestamp.parent = self
                    self._children_name_map["create_timestamp"] = "create-timestamp"

                    self.owner = YList(self)
                    self._segment_path = lambda: "locator-all-active-sid" + "[locator-name='" + str(self.locator_name) + "']" + "[sid-opcode='" + str(self.sid_opcode) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/locator-all-active-sids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid, ['locator_name', 'sid_opcode', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                class SidContext(_Entity_):
                    """
                    SID Context
                    
                    .. attribute:: key
                    
                    	SID Key
                    	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key>`
                    
                    	**config**\: False
                    
                    .. attribute:: application_data
                    
                    	Application opaque data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext, self).__init__()

                        self.yang_name = "sid-context"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key))])
                        self._leafs = OrderedDict([
                            ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                        ])
                        self.application_data = None

                        self.key = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                        self._segment_path = lambda: "sid-context"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext, ['application_data'], name, value)


                    class Key(_Entity_):
                        """
                        SID Key
                        
                        .. attribute:: e
                        
                        	End (PSP) SID context
                        	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E>`
                        
                        	**config**\: False
                        
                        .. attribute:: x
                        
                        	End.X (PSP) SID context
                        	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X>`
                        
                        	**config**\: False
                        
                        .. attribute:: dx4
                        
                        	End.DX4 SID context
                        	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4>`
                        
                        	**config**\: False
                        
                        .. attribute:: dt4
                        
                        	End.DT4 SID context
                        	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context_type
                        
                        	SIDContextType
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "sid-context"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("e", ("e", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E)), ("x", ("x", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4))])
                            self._leafs = OrderedDict([
                                ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                            ])
                            self.sid_context_type = None

                            self.e = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E()
                            self.e.parent = self
                            self._children_name_map["e"] = "e"

                            self.x = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X()
                            self.x.parent = self
                            self._children_name_map["x"] = "x"

                            self.dx4 = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4()
                            self.dx4.parent = self
                            self._children_name_map["dx4"] = "dx4"

                            self.dt4 = Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4()
                            self.dt4.parent = self
                            self._children_name_map["dt4"] = "dt4"
                            self._segment_path = lambda: "key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key, ['sid_context_type'], name, value)


                        class E(_Entity_):
                            """
                            End (PSP) SID context
                            
                            .. attribute:: table_id
                            
                            	Table Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E, self).__init__()

                                self.yang_name = "e"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.opaque_id = None
                                self._segment_path = lambda: "e"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E']['meta_info']


                        class X(_Entity_):
                            """
                            End.X (PSP) SID context
                            
                            .. attribute:: is_protected
                            
                            	Is protected?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: interface
                            
                            	Nexthop interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: nexthop_address
                            
                            	Nexthop IP address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X, self).__init__()

                                self.yang_name = "x"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                ])
                                self.is_protected = None
                                self.opaque_id = None
                                self.interface = None
                                self.nexthop_address = None
                                self._segment_path = lambda: "x"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X']['meta_info']


                        class Dx4(_Entity_):
                            """
                            End.DX4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_set_id
                            
                            	Next Hop Set ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4, self).__init__()

                                self.yang_name = "dx4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.next_hop_set_id = None
                                self._segment_path = lambda: "dx4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4']['meta_info']


                        class Dt4(_Entity_):
                            """
                            End.DT4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4, self).__init__()

                                self.yang_name = "dt4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ])
                                self.table_id = None
                                self._segment_path = lambda: "dt4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4, ['table_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.SidContext']['meta_info']


                class CreateTimestamp(_Entity_):
                    """
                    Creation timestamp
                    
                    .. attribute:: time_in_nano_seconds
                    
                    	Timestamp in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: age_in_nano_seconds
                    
                    	Age in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp, self).__init__()

                        self.yang_name = "create-timestamp"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                            ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                        ])
                        self.time_in_nano_seconds = None
                        self.age_in_nano_seconds = None
                        self._segment_path = lambda: "create-timestamp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp']['meta_info']


                class Owner(_Entity_):
                    """
                    Owner
                    
                    .. attribute:: owner
                    
                    	Owner
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.Owner, self).__init__()

                        self.yang_name = "owner"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                        ])
                        self.owner = None
                        self._segment_path = lambda: "owner"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.Owner, ['owner'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid.Owner']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Active.LocatorAllActiveSids.LocatorAllActiveSid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Active.LocatorAllActiveSids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
            return meta._meta_table['Srv6.Active']['meta_info']


    class Standby(_Entity_):
        """
        Standby SRv6 operational data
        
        .. attribute:: manager
        
        	SID Manager information
        	**type**\:  :py:class:`Manager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager>`
        
        	**config**\: False
        
        .. attribute:: locators
        
        	SRv6 locators related information
        	**type**\:  :py:class:`Locators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators>`
        
        	**config**\: False
        
        .. attribute:: locator_all_sids
        
        	Operational container for all (Active and Stale) SIDs across all Locators
        	**type**\:  :py:class:`LocatorAllSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids>`
        
        	**config**\: False
        
        .. attribute:: locator_all_active_sids
        
        	Operational container for Active SIDs across all Locators
        	**type**\:  :py:class:`LocatorAllActiveSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids>`
        
        	**config**\: False
        
        

        """

        _prefix = 'segment-routing-srv6-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srv6.Standby, self).__init__()

            self.yang_name = "standby"
            self.yang_parent_name = "srv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("manager", ("manager", Srv6.Standby.Manager)), ("locators", ("locators", Srv6.Standby.Locators)), ("locator-all-sids", ("locator_all_sids", Srv6.Standby.LocatorAllSids)), ("locator-all-active-sids", ("locator_all_active_sids", Srv6.Standby.LocatorAllActiveSids))])
            self._leafs = OrderedDict()

            self.manager = Srv6.Standby.Manager()
            self.manager.parent = self
            self._children_name_map["manager"] = "manager"

            self.locators = Srv6.Standby.Locators()
            self.locators.parent = self
            self._children_name_map["locators"] = "locators"

            self.locator_all_sids = Srv6.Standby.LocatorAllSids()
            self.locator_all_sids.parent = self
            self._children_name_map["locator_all_sids"] = "locator-all-sids"

            self.locator_all_active_sids = Srv6.Standby.LocatorAllActiveSids()
            self.locator_all_active_sids.parent = self
            self._children_name_map["locator_all_active_sids"] = "locator-all-active-sids"
            self._segment_path = lambda: "standby"
            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srv6.Standby, [], name, value)


        class Manager(_Entity_):
            """
            SID Manager information
            
            .. attribute:: sid_mgr_params
            
            	SID Mgr parameters
            	**type**\:  :py:class:`SidMgrParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.SidMgrParams>`
            
            	**config**\: False
            
            .. attribute:: sid_mgr_summary
            
            	SID Mgr summary info
            	**type**\:  :py:class:`SidMgrSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.SidMgrSummary>`
            
            	**config**\: False
            
            .. attribute:: platform_capabilities
            
            	Platform Capabilities
            	**type**\:  :py:class:`PlatformCapabilities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Standby.Manager, self).__init__()

                self.yang_name = "manager"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sid-mgr-params", ("sid_mgr_params", Srv6.Standby.Manager.SidMgrParams)), ("sid-mgr-summary", ("sid_mgr_summary", Srv6.Standby.Manager.SidMgrSummary)), ("platform-capabilities", ("platform_capabilities", Srv6.Standby.Manager.PlatformCapabilities))])
                self._leafs = OrderedDict()

                self.sid_mgr_params = Srv6.Standby.Manager.SidMgrParams()
                self.sid_mgr_params.parent = self
                self._children_name_map["sid_mgr_params"] = "sid-mgr-params"

                self.sid_mgr_summary = Srv6.Standby.Manager.SidMgrSummary()
                self.sid_mgr_summary.parent = self
                self._children_name_map["sid_mgr_summary"] = "sid-mgr-summary"

                self.platform_capabilities = Srv6.Standby.Manager.PlatformCapabilities()
                self.platform_capabilities.parent = self
                self._children_name_map["platform_capabilities"] = "platform-capabilities"
                self._segment_path = lambda: "manager"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Standby.Manager, [], name, value)


            class SidMgrParams(_Entity_):
                """
                SID Mgr parameters
                
                .. attribute:: encap_hop_limit
                
                	Encap Hop\-limit info
                	**type**\:  :py:class:`EncapHopLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.SidMgrParams.EncapHopLimit>`
                
                	**config**\: False
                
                .. attribute:: srv6_enabled
                
                	Is SRv6 enabled?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: configured_encap_source_address
                
                	Configured Encap Source address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: default_encap_source_address
                
                	Default Encap Source address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: encap_ttl_propagate
                
                	Is TTL propagate enabled?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_sid_holdtime_configured
                
                	Is SID Holdtime configured?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sid_holdtime_mins_configured
                
                	Configured SID Holdtime in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: minute
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.Manager.SidMgrParams, self).__init__()

                    self.yang_name = "sid-mgr-params"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("encap-hop-limit", ("encap_hop_limit", Srv6.Standby.Manager.SidMgrParams.EncapHopLimit))])
                    self._leafs = OrderedDict([
                        ('srv6_enabled', (YLeaf(YType.boolean, 'srv6-enabled'), ['bool'])),
                        ('configured_encap_source_address', (YLeaf(YType.str, 'configured-encap-source-address'), ['str'])),
                        ('default_encap_source_address', (YLeaf(YType.str, 'default-encap-source-address'), ['str'])),
                        ('encap_ttl_propagate', (YLeaf(YType.boolean, 'encap-ttl-propagate'), ['bool'])),
                        ('is_sid_holdtime_configured', (YLeaf(YType.boolean, 'is-sid-holdtime-configured'), ['bool'])),
                        ('sid_holdtime_mins_configured', (YLeaf(YType.uint32, 'sid-holdtime-mins-configured'), ['int'])),
                    ])
                    self.srv6_enabled = None
                    self.configured_encap_source_address = None
                    self.default_encap_source_address = None
                    self.encap_ttl_propagate = None
                    self.is_sid_holdtime_configured = None
                    self.sid_holdtime_mins_configured = None

                    self.encap_hop_limit = Srv6.Standby.Manager.SidMgrParams.EncapHopLimit()
                    self.encap_hop_limit.parent = self
                    self._children_name_map["encap_hop_limit"] = "encap-hop-limit"
                    self._segment_path = lambda: "sid-mgr-params"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.Manager.SidMgrParams, ['srv6_enabled', 'configured_encap_source_address', 'default_encap_source_address', 'encap_ttl_propagate', 'is_sid_holdtime_configured', 'sid_holdtime_mins_configured'], name, value)


                class EncapHopLimit(_Entity_):
                    """
                    Encap Hop\-limit info
                    
                    .. attribute:: use_default
                    
                    	Use default IPv6 hop\-limit value
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: do_propagate
                    
                    	Propagate IP TTL to Encap IPv6 hop\-limit
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: value
                    
                    	Specific value set for hop\-limit count
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.Manager.SidMgrParams.EncapHopLimit, self).__init__()

                        self.yang_name = "encap-hop-limit"
                        self.yang_parent_name = "sid-mgr-params"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('use_default', (YLeaf(YType.boolean, 'use-default'), ['bool'])),
                            ('do_propagate', (YLeaf(YType.boolean, 'do-propagate'), ['bool'])),
                            ('value', (YLeaf(YType.uint8, 'value'), ['int'])),
                        ])
                        self.use_default = None
                        self.do_propagate = None
                        self.value = None
                        self._segment_path = lambda: "encap-hop-limit"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/sid-mgr-params/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.Manager.SidMgrParams.EncapHopLimit, ['use_default', 'do_propagate', 'value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.Manager.SidMgrParams.EncapHopLimit']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.Manager.SidMgrParams']['meta_info']


            class SidMgrSummary(_Entity_):
                """
                SID Mgr summary info
                
                .. attribute:: sids_out_of_resource_summary
                
                	SIDs Global Out of Resource info
                	**type**\:  :py:class:`SidsOutOfResourceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary>`
                
                	**config**\: False
                
                .. attribute:: locators_count
                
                	Number of locators
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: oper_locators_count
                
                	Number of operational locators
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: sids_count
                
                	Number of SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: stale_sids_count
                
                	Number of Stale SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: maximum_sids_count
                
                	Global Maximum number of SIDs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.Manager.SidMgrSummary, self).__init__()

                    self.yang_name = "sid-mgr-summary"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sids-out-of-resource-summary", ("sids_out_of_resource_summary", Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary))])
                    self._leafs = OrderedDict([
                        ('locators_count', (YLeaf(YType.uint16, 'locators-count'), ['int'])),
                        ('oper_locators_count', (YLeaf(YType.uint16, 'oper-locators-count'), ['int'])),
                        ('sids_count', (YLeaf(YType.uint32, 'sids-count'), ['int'])),
                        ('stale_sids_count', (YLeaf(YType.uint32, 'stale-sids-count'), ['int'])),
                        ('maximum_sids_count', (YLeaf(YType.uint32, 'maximum-sids-count'), ['int'])),
                    ])
                    self.locators_count = None
                    self.oper_locators_count = None
                    self.sids_count = None
                    self.stale_sids_count = None
                    self.maximum_sids_count = None

                    self.sids_out_of_resource_summary = Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary()
                    self.sids_out_of_resource_summary.parent = self
                    self._children_name_map["sids_out_of_resource_summary"] = "sids-out-of-resource-summary"
                    self._segment_path = lambda: "sid-mgr-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.Manager.SidMgrSummary, ['locators_count', 'oper_locators_count', 'sids_count', 'stale_sids_count', 'maximum_sids_count'], name, value)


                class SidsOutOfResourceSummary(_Entity_):
                    """
                    SIDs Global Out of Resource info
                    
                    .. attribute:: out_of_resources_state
                    
                    	Global Resources State for SIDs
                    	**type**\:  :py:class:`Srv6OutOfResourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6OutOfResourceState>`
                    
                    	**config**\: False
                    
                    .. attribute:: oor_yellow_free_sid_threshold
                    
                    	Threshold for Number of Free SID below which OOR Yellow State is reached
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_green_free_sid_threshold
                    
                    	Threshold for Number of Free SID above which OOR Green State is restored
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_green_count
                    
                    	Number of times Resources Warning or Out of Resources state has been cleared
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_yellow_count
                    
                    	Number of times system went into Resources Warning state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oor_red_count
                    
                    	Number of times system went into Out of Resources state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary, self).__init__()

                        self.yang_name = "sids-out-of-resource-summary"
                        self.yang_parent_name = "sid-mgr-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('out_of_resources_state', (YLeaf(YType.enumeration, 'out-of-resources-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6OutOfResourceState', '')])),
                            ('oor_yellow_free_sid_threshold', (YLeaf(YType.uint32, 'oor-yellow-free-sid-threshold'), ['int'])),
                            ('oor_green_free_sid_threshold', (YLeaf(YType.uint32, 'oor-green-free-sid-threshold'), ['int'])),
                            ('oor_green_count', (YLeaf(YType.uint32, 'oor-green-count'), ['int'])),
                            ('oor_yellow_count', (YLeaf(YType.uint32, 'oor-yellow-count'), ['int'])),
                            ('oor_red_count', (YLeaf(YType.uint32, 'oor-red-count'), ['int'])),
                        ])
                        self.out_of_resources_state = None
                        self.oor_yellow_free_sid_threshold = None
                        self.oor_green_free_sid_threshold = None
                        self.oor_green_count = None
                        self.oor_yellow_count = None
                        self.oor_red_count = None
                        self._segment_path = lambda: "sids-out-of-resource-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/sid-mgr-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary, ['out_of_resources_state', 'oor_yellow_free_sid_threshold', 'oor_green_free_sid_threshold', 'oor_green_count', 'oor_yellow_count', 'oor_red_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.Manager.SidMgrSummary.SidsOutOfResourceSummary']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.Manager.SidMgrSummary']['meta_info']


            class PlatformCapabilities(_Entity_):
                """
                Platform Capabilities
                
                .. attribute:: support
                
                	Feature support
                	**type**\:  :py:class:`Support <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support>`
                
                	**config**\: False
                
                .. attribute:: max_sid
                
                	Maximum Sids
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_holdtime_mins
                
                	Freed SID holdtime in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: minute
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.Manager.PlatformCapabilities, self).__init__()

                    self.yang_name = "platform-capabilities"
                    self.yang_parent_name = "manager"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("support", ("support", Srv6.Standby.Manager.PlatformCapabilities.Support))])
                    self._leafs = OrderedDict([
                        ('max_sid', (YLeaf(YType.uint32, 'max-sid'), ['int'])),
                        ('sid_holdtime_mins', (YLeaf(YType.uint32, 'sid-holdtime-mins'), ['int'])),
                    ])
                    self.max_sid = None
                    self.sid_holdtime_mins = None

                    self.support = Srv6.Standby.Manager.PlatformCapabilities.Support()
                    self.support.parent = self
                    self._children_name_map["support"] = "support"
                    self._segment_path = lambda: "platform-capabilities"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities, ['max_sid', 'sid_holdtime_mins'], name, value)


                class Support(_Entity_):
                    """
                    Feature support
                    
                    .. attribute:: signaled_parameters
                    
                    	Signaled Parameters
                    	**type**\:  :py:class:`SignaledParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters>`
                    
                    	**config**\: False
                    
                    .. attribute:: srv6
                    
                    	SRv6 support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: tilfa
                    
                    	TI LFA support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: microloop_avoidance
                    
                    	Microloop\-avoidance support
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: end_func
                    
                    	Supported end functions
                    	**type**\: list of  		 :py:class:`EndFunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support.EndFunc>`
                    
                    	**config**\: False
                    
                    .. attribute:: transit_func
                    
                    	Supported Transit functions
                    	**type**\: list of  		 :py:class:`TransitFunc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support.TransitFunc>`
                    
                    	**config**\: False
                    
                    .. attribute:: security_rule
                    
                    	Security rules
                    	**type**\: list of  		 :py:class:`SecurityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support.SecurityRule>`
                    
                    	**config**\: False
                    
                    .. attribute:: counter
                    
                    	Counters
                    	**type**\: list of  		 :py:class:`Counter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Manager.PlatformCapabilities.Support.Counter>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.Manager.PlatformCapabilities.Support, self).__init__()

                        self.yang_name = "support"
                        self.yang_parent_name = "platform-capabilities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("signaled-parameters", ("signaled_parameters", Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters)), ("end-func", ("end_func", Srv6.Standby.Manager.PlatformCapabilities.Support.EndFunc)), ("transit-func", ("transit_func", Srv6.Standby.Manager.PlatformCapabilities.Support.TransitFunc)), ("security-rule", ("security_rule", Srv6.Standby.Manager.PlatformCapabilities.Support.SecurityRule)), ("counter", ("counter", Srv6.Standby.Manager.PlatformCapabilities.Support.Counter))])
                        self._leafs = OrderedDict([
                            ('srv6', (YLeaf(YType.boolean, 'srv6'), ['bool'])),
                            ('tilfa', (YLeaf(YType.boolean, 'tilfa'), ['bool'])),
                            ('microloop_avoidance', (YLeaf(YType.boolean, 'microloop-avoidance'), ['bool'])),
                        ])
                        self.srv6 = None
                        self.tilfa = None
                        self.microloop_avoidance = None

                        self.signaled_parameters = Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters()
                        self.signaled_parameters.parent = self
                        self._children_name_map["signaled_parameters"] = "signaled-parameters"

                        self.end_func = YList(self)
                        self.transit_func = YList(self)
                        self.security_rule = YList(self)
                        self.counter = YList(self)
                        self._segment_path = lambda: "support"
                        self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support, ['srv6', 'tilfa', 'microloop_avoidance'], name, value)


                    class SignaledParameters(_Entity_):
                        """
                        Signaled Parameters
                        
                        .. attribute:: max_sl
                        
                        	Max value of SegmentLeft field in received SRH
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_end_pop_srh
                        
                        	Max num of SIDs in rcvd SRH for pop
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_t_insert
                        
                        	Max num of SIDs for T.Insert op
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_t_encap
                        
                        	Max num of SIDs for T.Encaps op
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: max_end_d
                        
                        	Max num of SIDs in rcvd SRH for decap
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters, self).__init__()

                            self.yang_name = "signaled-parameters"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('max_sl', (YLeaf(YType.uint8, 'max-sl'), ['int'])),
                                ('max_end_pop_srh', (YLeaf(YType.uint8, 'max-end-pop-srh'), ['int'])),
                                ('max_t_insert', (YLeaf(YType.uint8, 'max-t-insert'), ['int'])),
                                ('max_t_encap', (YLeaf(YType.uint8, 'max-t-encap'), ['int'])),
                                ('max_end_d', (YLeaf(YType.uint8, 'max-end-d'), ['int'])),
                            ])
                            self.max_sl = None
                            self.max_end_pop_srh = None
                            self.max_t_insert = None
                            self.max_t_encap = None
                            self.max_end_d = None
                            self._segment_path = lambda: "signaled-parameters"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters, ['max_sl', 'max_end_pop_srh', 'max_t_insert', 'max_t_encap', 'max_end_d'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support.SignaledParameters']['meta_info']


                    class EndFunc(_Entity_):
                        """
                        Supported end functions
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Manager.PlatformCapabilities.Support.EndFunc, self).__init__()

                            self.yang_name = "end-func"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "end-func"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support.EndFunc, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support.EndFunc']['meta_info']


                    class TransitFunc(_Entity_):
                        """
                        Supported Transit functions
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Manager.PlatformCapabilities.Support.TransitFunc, self).__init__()

                            self.yang_name = "transit-func"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "transit-func"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support.TransitFunc, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support.TransitFunc']['meta_info']


                    class SecurityRule(_Entity_):
                        """
                        Security rules
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Manager.PlatformCapabilities.Support.SecurityRule, self).__init__()

                            self.yang_name = "security-rule"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "security-rule"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support.SecurityRule, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support.SecurityRule']['meta_info']


                    class Counter(_Entity_):
                        """
                        Counters
                        
                        .. attribute:: string
                        
                        	String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Manager.PlatformCapabilities.Support.Counter, self).__init__()

                            self.yang_name = "counter"
                            self.yang_parent_name = "support"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('string', (YLeaf(YType.str, 'string'), ['str'])),
                            ])
                            self.string = None
                            self._segment_path = lambda: "counter"
                            self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/manager/platform-capabilities/support/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Manager.PlatformCapabilities.Support.Counter, ['string'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support.Counter']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities.Support']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.Manager.PlatformCapabilities']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Standby.Manager']['meta_info']


        class Locators(_Entity_):
            """
            SRv6 locators related information
            
            .. attribute:: locator
            
            	Operational data for given SRv6 locator
            	**type**\: list of  		 :py:class:`Locator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Standby.Locators, self).__init__()

                self.yang_name = "locators"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator", ("locator", Srv6.Standby.Locators.Locator))])
                self._leafs = OrderedDict()

                self.locator = YList(self)
                self._segment_path = lambda: "locators"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Standby.Locators, [], name, value)


            class Locator(_Entity_):
                """
                Operational data for given SRv6 locator
                
                .. attribute:: name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: info
                
                	Operational data for given SRv6 locator
                	**type**\:  :py:class:`Info <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Info>`
                
                	**config**\: False
                
                .. attribute:: sids
                
                	SRv6 locator SID table
                	**type**\:  :py:class:`Sids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.Locators.Locator, self).__init__()

                    self.yang_name = "locator"
                    self.yang_parent_name = "locators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("info", ("info", Srv6.Standby.Locators.Locator.Info)), ("sids", ("sids", Srv6.Standby.Locators.Locator.Sids))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.info = Srv6.Standby.Locators.Locator.Info()
                    self.info.parent = self
                    self._children_name_map["info"] = "info"

                    self.sids = Srv6.Standby.Locators.Locator.Sids()
                    self.sids.parent = self
                    self._children_name_map["sids"] = "sids"
                    self._segment_path = lambda: "locator" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/locators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.Locators.Locator, ['name'], name, value)


                class Info(_Entity_):
                    """
                    Operational data for given SRv6 locator
                    
                    .. attribute:: interface
                    
                    	Locator IM intf info
                    	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Info.Interface>`
                    
                    	**config**\: False
                    
                    .. attribute:: create_timestamp
                    
                    	Creation timestamp
                    	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Info.CreateTimestamp>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Locator Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: id
                    
                    	Locator ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: prefix
                    
                    	Locator Prefix
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: is_operational
                    
                    	Locator status is Up or Down
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_default
                    
                    	Locator is the default locator
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: out_of_resources_state
                    
                    	Locator Resources State for SIDs
                    	**type**\:  :py:class:`Srv6OutOfResourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6OutOfResourceState>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.Locators.Locator.Info, self).__init__()

                        self.yang_name = "info"
                        self.yang_parent_name = "locator"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Srv6.Standby.Locators.Locator.Info.Interface)), ("create-timestamp", ("create_timestamp", Srv6.Standby.Locators.Locator.Info.CreateTimestamp))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('is_operational', (YLeaf(YType.boolean, 'is-operational'), ['bool'])),
                            ('is_default', (YLeaf(YType.boolean, 'is-default'), ['bool'])),
                            ('out_of_resources_state', (YLeaf(YType.enumeration, 'out-of-resources-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6OutOfResourceState', '')])),
                        ])
                        self.name = None
                        self.id = None
                        self.prefix = None
                        self.is_operational = None
                        self.is_default = None
                        self.out_of_resources_state = None

                        self.interface = Srv6.Standby.Locators.Locator.Info.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"

                        self.create_timestamp = Srv6.Standby.Locators.Locator.Info.CreateTimestamp()
                        self.create_timestamp.parent = self
                        self._children_name_map["create_timestamp"] = "create-timestamp"
                        self._segment_path = lambda: "info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.Locators.Locator.Info, ['name', 'id', 'prefix', 'is_operational', 'is_default', 'out_of_resources_state'], name, value)


                    class Interface(_Entity_):
                        """
                        Locator IM intf info
                        
                        .. attribute:: name
                        
                        	Interface name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: if_handle
                        
                        	Interface handle
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        	**config**\: False
                        
                        .. attribute:: programmed_prefix
                        
                        	Interface prefix/addr programmed
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Locators.Locator.Info.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                                ('programmed_prefix', (YLeaf(YType.str, 'programmed-prefix'), ['str'])),
                            ])
                            self.name = None
                            self.if_handle = None
                            self.programmed_prefix = None
                            self._segment_path = lambda: "interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Locators.Locator.Info.Interface, ['name', 'if_handle', 'programmed_prefix'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Locators.Locator.Info.Interface']['meta_info']


                    class CreateTimestamp(_Entity_):
                        """
                        Creation timestamp
                        
                        .. attribute:: time_in_nano_seconds
                        
                        	Timestamp in nano seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: age_in_nano_seconds
                        
                        	Age in nano seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Locators.Locator.Info.CreateTimestamp, self).__init__()

                            self.yang_name = "create-timestamp"
                            self.yang_parent_name = "info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                                ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                            ])
                            self.time_in_nano_seconds = None
                            self.age_in_nano_seconds = None
                            self._segment_path = lambda: "create-timestamp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Locators.Locator.Info.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Locators.Locator.Info.CreateTimestamp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.Locators.Locator.Info']['meta_info']


                class Sids(_Entity_):
                    """
                    SRv6 locator SID table
                    
                    .. attribute:: sid
                    
                    	Operational data for given SRv6 SID
                    	**type**\: list of  		 :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.Locators.Locator.Sids, self).__init__()

                        self.yang_name = "sids"
                        self.yang_parent_name = "locator"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid", ("sid", Srv6.Standby.Locators.Locator.Sids.Sid))])
                        self._leafs = OrderedDict()

                        self.sid = YList(self)
                        self._segment_path = lambda: "sids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.Locators.Locator.Sids, [], name, value)


                    class Sid(_Entity_):
                        """
                        Operational data for given SRv6 SID
                        
                        .. attribute:: address  (key)
                        
                        	IPv6 address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context
                        
                        	SID Context
                        	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext>`
                        
                        	**config**\: False
                        
                        .. attribute:: create_timestamp
                        
                        	Creation timestamp
                        	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid
                        
                        	SID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: allocation_type
                        
                        	Allocation Type
                        	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                        
                        	**config**\: False
                        
                        .. attribute:: function_type
                        
                        	Function Type
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                        
                        	**config**\: False
                        
                        .. attribute:: has_forwarding
                        
                        	Rewrite done or not
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: locator
                        
                        	Associated locator
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: owner
                        
                        	Owner
                        	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.Owner>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.Locators.Locator.Sids.Sid, self).__init__()

                            self.yang_name = "sid"
                            self.yang_parent_name = "sids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp)), ("owner", ("owner", Srv6.Standby.Locators.Locator.Sids.Sid.Owner))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                                ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                                ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                                ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                                ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                            ])
                            self.address = None
                            self.sid = None
                            self.allocation_type = None
                            self.function_type = None
                            self.state = None
                            self.has_forwarding = None
                            self.locator = None

                            self.sid_context = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext()
                            self.sid_context.parent = self
                            self._children_name_map["sid_context"] = "sid-context"

                            self.create_timestamp = Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp()
                            self.create_timestamp.parent = self
                            self._children_name_map["create_timestamp"] = "create-timestamp"

                            self.owner = YList(self)
                            self._segment_path = lambda: "sid" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid, ['address', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                        class SidContext(_Entity_):
                            """
                            SID Context
                            
                            .. attribute:: key
                            
                            	SID Key
                            	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key>`
                            
                            	**config**\: False
                            
                            .. attribute:: application_data
                            
                            	Application opaque data
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext, self).__init__()

                                self.yang_name = "sid-context"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("key", ("key", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key))])
                                self._leafs = OrderedDict([
                                    ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                                ])
                                self.application_data = None

                                self.key = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key()
                                self.key.parent = self
                                self._children_name_map["key"] = "key"
                                self._segment_path = lambda: "sid-context"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext, ['application_data'], name, value)


                            class Key(_Entity_):
                                """
                                SID Key
                                
                                .. attribute:: e
                                
                                	End (PSP) SID context
                                	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E>`
                                
                                	**config**\: False
                                
                                .. attribute:: x
                                
                                	End.X (PSP) SID context
                                	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X>`
                                
                                	**config**\: False
                                
                                .. attribute:: dx4
                                
                                	End.DX4 SID context
                                	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4>`
                                
                                	**config**\: False
                                
                                .. attribute:: dt4
                                
                                	End.DT4 SID context
                                	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4>`
                                
                                	**config**\: False
                                
                                .. attribute:: sid_context_type
                                
                                	SIDContextType
                                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'segment-routing-srv6-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key, self).__init__()

                                    self.yang_name = "key"
                                    self.yang_parent_name = "sid-context"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("e", ("e", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E)), ("x", ("x", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4))])
                                    self._leafs = OrderedDict([
                                        ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                                    ])
                                    self.sid_context_type = None

                                    self.e = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E()
                                    self.e.parent = self
                                    self._children_name_map["e"] = "e"

                                    self.x = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X()
                                    self.x.parent = self
                                    self._children_name_map["x"] = "x"

                                    self.dx4 = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4()
                                    self.dx4.parent = self
                                    self._children_name_map["dx4"] = "dx4"

                                    self.dt4 = Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4()
                                    self.dt4.parent = self
                                    self._children_name_map["dt4"] = "dt4"
                                    self._segment_path = lambda: "key"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key, ['sid_context_type'], name, value)


                                class E(_Entity_):
                                    """
                                    End (PSP) SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table Id
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Additional differentiator \- opaque to SIDMgr
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E, self).__init__()

                                        self.yang_name = "e"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                            ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self.opaque_id = None
                                        self._segment_path = lambda: "e"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.E']['meta_info']


                                class X(_Entity_):
                                    """
                                    End.X (PSP) SID context
                                    
                                    .. attribute:: is_protected
                                    
                                    	Is protected?
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Additional differentiator \- opaque to SIDMgr
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface
                                    
                                    	Nexthop interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: nexthop_address
                                    
                                    	Nexthop IP address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X, self).__init__()

                                        self.yang_name = "x"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                            ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                            ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                        ])
                                        self.is_protected = None
                                        self.opaque_id = None
                                        self.interface = None
                                        self.nexthop_address = None
                                        self._segment_path = lambda: "x"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.X']['meta_info']


                                class Dx4(_Entity_):
                                    """
                                    End.DX4 SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: next_hop_set_id
                                    
                                    	Next Hop Set ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4, self).__init__()

                                        self.yang_name = "dx4"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                            ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self.next_hop_set_id = None
                                        self._segment_path = lambda: "dx4"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dx4']['meta_info']


                                class Dt4(_Entity_):
                                    """
                                    End.DT4 SID context
                                    
                                    .. attribute:: table_id
                                    
                                    	Table ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'segment-routing-srv6-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4, self).__init__()

                                        self.yang_name = "dt4"
                                        self.yang_parent_name = "key"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                        ])
                                        self.table_id = None
                                        self._segment_path = lambda: "dt4"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4, ['table_id'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                        return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key.Dt4']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                    return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext.Key']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.SidContext']['meta_info']


                        class CreateTimestamp(_Entity_):
                            """
                            Creation timestamp
                            
                            .. attribute:: time_in_nano_seconds
                            
                            	Timestamp in nano seconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: nanosecond
                            
                            .. attribute:: age_in_nano_seconds
                            
                            	Age in nano seconds
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: nanosecond
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp, self).__init__()

                                self.yang_name = "create-timestamp"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                                    ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                                ])
                                self.time_in_nano_seconds = None
                                self.age_in_nano_seconds = None
                                self._segment_path = lambda: "create-timestamp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.CreateTimestamp']['meta_info']


                        class Owner(_Entity_):
                            """
                            Owner
                            
                            .. attribute:: owner
                            
                            	Owner
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.Locators.Locator.Sids.Sid.Owner, self).__init__()

                                self.yang_name = "owner"
                                self.yang_parent_name = "sid"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                                ])
                                self.owner = None
                                self._segment_path = lambda: "owner"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.Locators.Locator.Sids.Sid.Owner, ['owner'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid.Owner']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.Locators.Locator.Sids.Sid']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.Locators.Locator.Sids']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.Locators.Locator']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Standby.Locators']['meta_info']


        class LocatorAllSids(_Entity_):
            """
            Operational container for all (Active and Stale)
            SIDs across all Locators
            
            .. attribute:: locator_all_sid
            
            	Operational data for given locator and SID opcode
            	**type**\: list of  		 :py:class:`LocatorAllSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Standby.LocatorAllSids, self).__init__()

                self.yang_name = "locator-all-sids"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator-all-sid", ("locator_all_sid", Srv6.Standby.LocatorAllSids.LocatorAllSid))])
                self._leafs = OrderedDict()

                self.locator_all_sid = YList(self)
                self._segment_path = lambda: "locator-all-sids"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Standby.LocatorAllSids, [], name, value)


            class LocatorAllSid(_Entity_):
                """
                Operational data for given locator and SID
                opcode
                
                .. attribute:: locator_name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: sid_opcode  (key)
                
                	Sid opcode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_context
                
                	SID Context
                	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext>`
                
                	**config**\: False
                
                .. attribute:: create_timestamp
                
                	Creation timestamp
                	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp>`
                
                	**config**\: False
                
                .. attribute:: sid
                
                	SID
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: allocation_type
                
                	Allocation Type
                	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                
                	**config**\: False
                
                .. attribute:: function_type
                
                	Function Type
                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                
                	**config**\: False
                
                .. attribute:: has_forwarding
                
                	Rewrite done or not
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: locator
                
                	Associated locator
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: owner
                
                	Owner
                	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.Owner>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.LocatorAllSids.LocatorAllSid, self).__init__()

                    self.yang_name = "locator-all-sid"
                    self.yang_parent_name = "locator-all-sids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locator_name','sid_opcode']
                    self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp)), ("owner", ("owner", Srv6.Standby.LocatorAllSids.LocatorAllSid.Owner))])
                    self._leafs = OrderedDict([
                        ('locator_name', (YLeaf(YType.str, 'locator-name'), ['str'])),
                        ('sid_opcode', (YLeaf(YType.uint32, 'sid-opcode'), ['int'])),
                        ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                        ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                        ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                        ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                        ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                    ])
                    self.locator_name = None
                    self.sid_opcode = None
                    self.sid = None
                    self.allocation_type = None
                    self.function_type = None
                    self.state = None
                    self.has_forwarding = None
                    self.locator = None

                    self.sid_context = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext()
                    self.sid_context.parent = self
                    self._children_name_map["sid_context"] = "sid-context"

                    self.create_timestamp = Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp()
                    self.create_timestamp.parent = self
                    self._children_name_map["create_timestamp"] = "create-timestamp"

                    self.owner = YList(self)
                    self._segment_path = lambda: "locator-all-sid" + "[locator-name='" + str(self.locator_name) + "']" + "[sid-opcode='" + str(self.sid_opcode) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/locator-all-sids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid, ['locator_name', 'sid_opcode', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                class SidContext(_Entity_):
                    """
                    SID Context
                    
                    .. attribute:: key
                    
                    	SID Key
                    	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key>`
                    
                    	**config**\: False
                    
                    .. attribute:: application_data
                    
                    	Application opaque data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext, self).__init__()

                        self.yang_name = "sid-context"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key))])
                        self._leafs = OrderedDict([
                            ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                        ])
                        self.application_data = None

                        self.key = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                        self._segment_path = lambda: "sid-context"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext, ['application_data'], name, value)


                    class Key(_Entity_):
                        """
                        SID Key
                        
                        .. attribute:: e
                        
                        	End (PSP) SID context
                        	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E>`
                        
                        	**config**\: False
                        
                        .. attribute:: x
                        
                        	End.X (PSP) SID context
                        	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X>`
                        
                        	**config**\: False
                        
                        .. attribute:: dx4
                        
                        	End.DX4 SID context
                        	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4>`
                        
                        	**config**\: False
                        
                        .. attribute:: dt4
                        
                        	End.DT4 SID context
                        	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context_type
                        
                        	SIDContextType
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "sid-context"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("e", ("e", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E)), ("x", ("x", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4))])
                            self._leafs = OrderedDict([
                                ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                            ])
                            self.sid_context_type = None

                            self.e = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E()
                            self.e.parent = self
                            self._children_name_map["e"] = "e"

                            self.x = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X()
                            self.x.parent = self
                            self._children_name_map["x"] = "x"

                            self.dx4 = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4()
                            self.dx4.parent = self
                            self._children_name_map["dx4"] = "dx4"

                            self.dt4 = Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4()
                            self.dt4.parent = self
                            self._children_name_map["dt4"] = "dt4"
                            self._segment_path = lambda: "key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key, ['sid_context_type'], name, value)


                        class E(_Entity_):
                            """
                            End (PSP) SID context
                            
                            .. attribute:: table_id
                            
                            	Table Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E, self).__init__()

                                self.yang_name = "e"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.opaque_id = None
                                self._segment_path = lambda: "e"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.E']['meta_info']


                        class X(_Entity_):
                            """
                            End.X (PSP) SID context
                            
                            .. attribute:: is_protected
                            
                            	Is protected?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: interface
                            
                            	Nexthop interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: nexthop_address
                            
                            	Nexthop IP address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X, self).__init__()

                                self.yang_name = "x"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                ])
                                self.is_protected = None
                                self.opaque_id = None
                                self.interface = None
                                self.nexthop_address = None
                                self._segment_path = lambda: "x"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.X']['meta_info']


                        class Dx4(_Entity_):
                            """
                            End.DX4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_set_id
                            
                            	Next Hop Set ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4, self).__init__()

                                self.yang_name = "dx4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.next_hop_set_id = None
                                self._segment_path = lambda: "dx4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dx4']['meta_info']


                        class Dt4(_Entity_):
                            """
                            End.DT4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4, self).__init__()

                                self.yang_name = "dt4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ])
                                self.table_id = None
                                self._segment_path = lambda: "dt4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4, ['table_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key.Dt4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext.Key']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.SidContext']['meta_info']


                class CreateTimestamp(_Entity_):
                    """
                    Creation timestamp
                    
                    .. attribute:: time_in_nano_seconds
                    
                    	Timestamp in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: age_in_nano_seconds
                    
                    	Age in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp, self).__init__()

                        self.yang_name = "create-timestamp"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                            ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                        ])
                        self.time_in_nano_seconds = None
                        self.age_in_nano_seconds = None
                        self._segment_path = lambda: "create-timestamp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.CreateTimestamp']['meta_info']


                class Owner(_Entity_):
                    """
                    Owner
                    
                    .. attribute:: owner
                    
                    	Owner
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllSids.LocatorAllSid.Owner, self).__init__()

                        self.yang_name = "owner"
                        self.yang_parent_name = "locator-all-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                        ])
                        self.owner = None
                        self._segment_path = lambda: "owner"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllSids.LocatorAllSid.Owner, ['owner'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid.Owner']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.LocatorAllSids.LocatorAllSid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Standby.LocatorAllSids']['meta_info']


        class LocatorAllActiveSids(_Entity_):
            """
            Operational container for Active SIDs across all
            Locators
            
            .. attribute:: locator_all_active_sid
            
            	Operational data for given locator and SID opcode
            	**type**\: list of  		 :py:class:`LocatorAllActiveSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid>`
            
            	**config**\: False
            
            

            """

            _prefix = 'segment-routing-srv6-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srv6.Standby.LocatorAllActiveSids, self).__init__()

                self.yang_name = "locator-all-active-sids"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("locator-all-active-sid", ("locator_all_active_sid", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid))])
                self._leafs = OrderedDict()

                self.locator_all_active_sid = YList(self)
                self._segment_path = lambda: "locator-all-active-sids"
                self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srv6.Standby.LocatorAllActiveSids, [], name, value)


            class LocatorAllActiveSid(_Entity_):
                """
                Operational data for given locator and SID
                opcode
                
                .. attribute:: locator_name  (key)
                
                	Locator name
                	**type**\: str
                
                	**length:** 1..58
                
                	**config**\: False
                
                .. attribute:: sid_opcode  (key)
                
                	Sid opcode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sid_context
                
                	SID Context
                	**type**\:  :py:class:`SidContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext>`
                
                	**config**\: False
                
                .. attribute:: create_timestamp
                
                	Creation timestamp
                	**type**\:  :py:class:`CreateTimestamp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp>`
                
                	**config**\: False
                
                .. attribute:: sid
                
                	SID
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: allocation_type
                
                	Allocation Type
                	**type**\:  :py:class:`SidAllocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidAllocation>`
                
                	**config**\: False
                
                .. attribute:: function_type
                
                	Function Type
                	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State
                	**type**\:  :py:class:`SidState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.SidState>`
                
                	**config**\: False
                
                .. attribute:: has_forwarding
                
                	Rewrite done or not
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: locator
                
                	Associated locator
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: owner
                
                	Owner
                	**type**\: list of  		 :py:class:`Owner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.Owner>`
                
                	**config**\: False
                
                

                """

                _prefix = 'segment-routing-srv6-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid, self).__init__()

                    self.yang_name = "locator-all-active-sid"
                    self.yang_parent_name = "locator-all-active-sids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locator_name','sid_opcode']
                    self._child_classes = OrderedDict([("sid-context", ("sid_context", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext)), ("create-timestamp", ("create_timestamp", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp)), ("owner", ("owner", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.Owner))])
                    self._leafs = OrderedDict([
                        ('locator_name', (YLeaf(YType.str, 'locator-name'), ['str'])),
                        ('sid_opcode', (YLeaf(YType.uint32, 'sid-opcode'), ['int'])),
                        ('sid', (YLeaf(YType.str, 'sid'), ['str'])),
                        ('allocation_type', (YLeaf(YType.enumeration, 'allocation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidAllocation', '')])),
                        ('function_type', (YLeaf(YType.enumeration, 'function-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'SidState', '')])),
                        ('has_forwarding', (YLeaf(YType.boolean, 'has-forwarding'), ['bool'])),
                        ('locator', (YLeaf(YType.str, 'locator'), ['str'])),
                    ])
                    self.locator_name = None
                    self.sid_opcode = None
                    self.sid = None
                    self.allocation_type = None
                    self.function_type = None
                    self.state = None
                    self.has_forwarding = None
                    self.locator = None

                    self.sid_context = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext()
                    self.sid_context.parent = self
                    self._children_name_map["sid_context"] = "sid-context"

                    self.create_timestamp = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp()
                    self.create_timestamp.parent = self
                    self._children_name_map["create_timestamp"] = "create-timestamp"

                    self.owner = YList(self)
                    self._segment_path = lambda: "locator-all-active-sid" + "[locator-name='" + str(self.locator_name) + "']" + "[sid-opcode='" + str(self.sid_opcode) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-segment-routing-srv6-oper:srv6/standby/locator-all-active-sids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid, ['locator_name', 'sid_opcode', 'sid', 'allocation_type', 'function_type', 'state', 'has_forwarding', 'locator'], name, value)


                class SidContext(_Entity_):
                    """
                    SID Context
                    
                    .. attribute:: key
                    
                    	SID Key
                    	**type**\:  :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key>`
                    
                    	**config**\: False
                    
                    .. attribute:: application_data
                    
                    	Application opaque data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext, self).__init__()

                        self.yang_name = "sid-context"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key))])
                        self._leafs = OrderedDict([
                            ('application_data', (YLeaf(YType.str, 'application-data'), ['str'])),
                        ])
                        self.application_data = None

                        self.key = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key()
                        self.key.parent = self
                        self._children_name_map["key"] = "key"
                        self._segment_path = lambda: "sid-context"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext, ['application_data'], name, value)


                    class Key(_Entity_):
                        """
                        SID Key
                        
                        .. attribute:: e
                        
                        	End (PSP) SID context
                        	**type**\:  :py:class:`E <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E>`
                        
                        	**config**\: False
                        
                        .. attribute:: x
                        
                        	End.X (PSP) SID context
                        	**type**\:  :py:class:`X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X>`
                        
                        	**config**\: False
                        
                        .. attribute:: dx4
                        
                        	End.DX4 SID context
                        	**type**\:  :py:class:`Dx4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4>`
                        
                        	**config**\: False
                        
                        .. attribute:: dt4
                        
                        	End.DT4 SID context
                        	**type**\:  :py:class:`Dt4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_context_type
                        
                        	SIDContextType
                        	**type**\:  :py:class:`Srv6EndFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper.Srv6EndFunction>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'segment-routing-srv6-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "sid-context"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("e", ("e", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E)), ("x", ("x", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X)), ("dx4", ("dx4", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4)), ("dt4", ("dt4", Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4))])
                            self._leafs = OrderedDict([
                                ('sid_context_type', (YLeaf(YType.enumeration, 'sid-context-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_srv6_oper', 'Srv6EndFunction', '')])),
                            ])
                            self.sid_context_type = None

                            self.e = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E()
                            self.e.parent = self
                            self._children_name_map["e"] = "e"

                            self.x = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X()
                            self.x.parent = self
                            self._children_name_map["x"] = "x"

                            self.dx4 = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4()
                            self.dx4.parent = self
                            self._children_name_map["dx4"] = "dx4"

                            self.dt4 = Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4()
                            self.dt4.parent = self
                            self._children_name_map["dt4"] = "dt4"
                            self._segment_path = lambda: "key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key, ['sid_context_type'], name, value)


                        class E(_Entity_):
                            """
                            End (PSP) SID context
                            
                            .. attribute:: table_id
                            
                            	Table Id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E, self).__init__()

                                self.yang_name = "e"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.opaque_id = None
                                self._segment_path = lambda: "e"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E, ['table_id', 'opaque_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.E']['meta_info']


                        class X(_Entity_):
                            """
                            End.X (PSP) SID context
                            
                            .. attribute:: is_protected
                            
                            	Is protected?
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_id
                            
                            	Additional differentiator \- opaque to SIDMgr
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: interface
                            
                            	Nexthop interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            	**config**\: False
                            
                            .. attribute:: nexthop_address
                            
                            	Nexthop IP address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X, self).__init__()

                                self.yang_name = "x"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                    ('opaque_id', (YLeaf(YType.uint8, 'opaque-id'), ['int'])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('nexthop_address', (YLeaf(YType.str, 'nexthop-address'), ['str'])),
                                ])
                                self.is_protected = None
                                self.opaque_id = None
                                self.interface = None
                                self.nexthop_address = None
                                self._segment_path = lambda: "x"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X, ['is_protected', 'opaque_id', 'interface', 'nexthop_address'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.X']['meta_info']


                        class Dx4(_Entity_):
                            """
                            End.DX4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: next_hop_set_id
                            
                            	Next Hop Set ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4, self).__init__()

                                self.yang_name = "dx4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                    ('next_hop_set_id', (YLeaf(YType.uint32, 'next-hop-set-id'), ['int'])),
                                ])
                                self.table_id = None
                                self.next_hop_set_id = None
                                self._segment_path = lambda: "dx4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4, ['table_id', 'next_hop_set_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dx4']['meta_info']


                        class Dt4(_Entity_):
                            """
                            End.DT4 SID context
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'segment-routing-srv6-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4, self).__init__()

                                self.yang_name = "dt4"
                                self.yang_parent_name = "key"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ])
                                self.table_id = None
                                self._segment_path = lambda: "dt4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4, ['table_id'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                                return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key.Dt4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                            return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext.Key']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.SidContext']['meta_info']


                class CreateTimestamp(_Entity_):
                    """
                    Creation timestamp
                    
                    .. attribute:: time_in_nano_seconds
                    
                    	Timestamp in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    .. attribute:: age_in_nano_seconds
                    
                    	Age in nano seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp, self).__init__()

                        self.yang_name = "create-timestamp"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_in_nano_seconds', (YLeaf(YType.uint64, 'time-in-nano-seconds'), ['int'])),
                            ('age_in_nano_seconds', (YLeaf(YType.uint64, 'age-in-nano-seconds'), ['int'])),
                        ])
                        self.time_in_nano_seconds = None
                        self.age_in_nano_seconds = None
                        self._segment_path = lambda: "create-timestamp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp, ['time_in_nano_seconds', 'age_in_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.CreateTimestamp']['meta_info']


                class Owner(_Entity_):
                    """
                    Owner
                    
                    .. attribute:: owner
                    
                    	Owner
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'segment-routing-srv6-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.Owner, self).__init__()

                        self.yang_name = "owner"
                        self.yang_parent_name = "locator-all-active-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('owner', (YLeaf(YType.str, 'owner'), ['str'])),
                        ])
                        self.owner = None
                        self._segment_path = lambda: "owner"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.Owner, ['owner'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                        return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid.Owner']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                    return meta._meta_table['Srv6.Standby.LocatorAllActiveSids.LocatorAllActiveSid']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
                return meta._meta_table['Srv6.Standby.LocatorAllActiveSids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
            return meta._meta_table['Srv6.Standby']['meta_info']

    def clone_ptr(self):
        self._top_entity = Srv6()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_segment_routing_srv6_oper as meta
        return meta._meta_table['Srv6']['meta_info']


