""" Cisco_IOS_XR_eigrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR eigrp package operational data.

This module contains definitions
for the following management objects\:
  eigrp\: EIGRP operational data

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



class EigrpBdDelayUnit(Enum):
    """
    EigrpBdDelayUnit (Enum Class)

    EIGRP delay unit

    .. data:: none = 0

    	No Delay configured

    .. data:: ten_microsecond = 1

    	Delay in 10's of Microseconds

    .. data:: picosecond = 2

    	Delay in Picoseconds

    .. data:: microsecond = 3

    	Delay in Microseconds

    """

    none = Enum.YLeaf(0, "none")

    ten_microsecond = Enum.YLeaf(1, "ten-microsecond")

    picosecond = Enum.YLeaf(2, "picosecond")

    microsecond = Enum.YLeaf(3, "microsecond")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdDelayUnit']


class EigrpBdMetricVersion(Enum):
    """
    EigrpBdMetricVersion (Enum Class)

    EIGRP metric version

    .. data:: metric_version32_bit = 0

    	Metric version is 32 bit

    .. data:: metric_version64_bit = 1

    	Metric version is 64 bit

    """

    metric_version32_bit = Enum.YLeaf(0, "metric-version32-bit")

    metric_version64_bit = Enum.YLeaf(1, "metric-version64-bit")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdMetricVersion']


class EigrpBdPathOrigin(Enum):
    """
    EigrpBdPathOrigin (Enum Class)

    EIGRP path origin

    .. data:: connected = 0

    	connected destination

    .. data:: static_redistributed = 1

    	static redistribution

    .. data:: connected_redistributed = 2

    	connected redistribution

    .. data:: subscriber_redistributed = 3

    	subscriber redistribution

    .. data:: redistributed = 4

    	redistributed destination

    .. data:: vpnv4_sourced = 5

    	vpnv4 destination

    .. data:: vpnv6_sourced = 6

    	vpnv6 destination

    .. data:: summary = 7

    	summary destination

    .. data:: dummy = 8

    	bogus drdb used for sia transmission

    .. data:: eigrp_destination = 9

    	igrp2 destination

    .. data:: origin_count = 10

    	Number of org types

    """

    connected = Enum.YLeaf(0, "connected")

    static_redistributed = Enum.YLeaf(1, "static-redistributed")

    connected_redistributed = Enum.YLeaf(2, "connected-redistributed")

    subscriber_redistributed = Enum.YLeaf(3, "subscriber-redistributed")

    redistributed = Enum.YLeaf(4, "redistributed")

    vpnv4_sourced = Enum.YLeaf(5, "vpnv4-sourced")

    vpnv6_sourced = Enum.YLeaf(6, "vpnv6-sourced")

    summary = Enum.YLeaf(7, "summary")

    dummy = Enum.YLeaf(8, "dummy")

    eigrp_destination = Enum.YLeaf(9, "eigrp-destination")

    origin_count = Enum.YLeaf(10, "origin-count")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdPathOrigin']


class EigrpBdPathRibState(Enum):
    """
    EigrpBdPathRibState (Enum Class)

    Eigrp bd path rib state

    .. data:: active_path = 0

    	Active path

    .. data:: backup_path = 1

    	Backup path

    .. data:: path_sent_to_rib = 2

    	Path sent to RIB

    .. data:: path_not_selected = 3

    	Path not selected for installation in RIB

    .. data:: error_state = 4

    	Path in error state

    """

    active_path = Enum.YLeaf(0, "active-path")

    backup_path = Enum.YLeaf(1, "backup-path")

    path_sent_to_rib = Enum.YLeaf(2, "path-sent-to-rib")

    path_not_selected = Enum.YLeaf(3, "path-not-selected")

    error_state = Enum.YLeaf(4, "error-state")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdPathRibState']


class EigrpBdPathSendFlag(Enum):
    """
    EigrpBdPathSendFlag (Enum Class)

    EIGRP path send flag

    .. data:: no_send_pending = 0

    	No packet send pending

    .. data:: multicast_update_pending = 1

    	Multicast update pending

    .. data:: multicast_query_pending = 2

    	Multicast query pending

    .. data:: reply_pending = 3

    	Reply pending

    .. data:: sia_query_pending = 4

    	SIA Query pending

    .. data:: sia_reply_pending = 5

    	SIA Reply pending

    """

    no_send_pending = Enum.YLeaf(0, "no-send-pending")

    multicast_update_pending = Enum.YLeaf(1, "multicast-update-pending")

    multicast_query_pending = Enum.YLeaf(2, "multicast-query-pending")

    reply_pending = Enum.YLeaf(3, "reply-pending")

    sia_query_pending = Enum.YLeaf(4, "sia-query-pending")

    sia_reply_pending = Enum.YLeaf(5, "sia-reply-pending")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdPathSendFlag']


class EigrpBdSoo(Enum):
    """
    EigrpBdSoo (Enum Class)

    EIGRP SoO types

    .. data:: none = 0

    	No SoO configured

    .. data:: as_ = 1

    	AS:nn format

    .. data:: ipv4_address = 2

    	IPV4Address:nn format

    .. data:: four_byte_as = 3

    	AS2.AS:nn format

    """

    none = Enum.YLeaf(0, "none")

    as_ = Enum.YLeaf(1, "as")

    ipv4_address = Enum.YLeaf(2, "ipv4-address")

    four_byte_as = Enum.YLeaf(3, "four-byte-as")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['EigrpBdSoo']



class Eigrp(_Entity_):
    """
    EIGRP operational data
    
    .. attribute:: processes
    
    	Operational data for an EIGRP process
    	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'eigrp-oper'
    _revision = '2018-04-05'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Eigrp, self).__init__()
        self._top_entity = None

        self.yang_name = "eigrp"
        self.yang_parent_name = "Cisco-IOS-XR-eigrp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("processes", ("processes", Eigrp.Processes))])
        self._leafs = OrderedDict()

        self.processes = Eigrp.Processes()
        self.processes.parent = self
        self._children_name_map["processes"] = "processes"
        self._segment_path = lambda: "Cisco-IOS-XR-eigrp-oper:eigrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Eigrp, [], name, value)


    class Processes(_Entity_):
        """
        Operational data for an EIGRP process
        
        .. attribute:: process
        
        	Operational data for an EIGRP process
        	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process>`
        
        	**config**\: False
        
        

        """

        _prefix = 'eigrp-oper'
        _revision = '2018-04-05'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Eigrp.Processes, self).__init__()

            self.yang_name = "processes"
            self.yang_parent_name = "eigrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("process", ("process", Eigrp.Processes.Process))])
            self._leafs = OrderedDict()

            self.process = YList(self)
            self._segment_path = lambda: "processes"
            self._absolute_path = lambda: "Cisco-IOS-XR-eigrp-oper:eigrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eigrp.Processes, [], name, value)


        class Process(_Entity_):
            """
            Operational data for an EIGRP process
            
            .. attribute:: process_id  (key)
            
            	AS number or Virtual instance name of the EIGRP process
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: vrfs_xr
            
            	List of VRFs
            	**type**\:  :py:class:`VrfsXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.VrfsXr>`
            
            	**config**\: False
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs>`
            
            	**config**\: False
            
            

            """

            _prefix = 'eigrp-oper'
            _revision = '2018-04-05'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Eigrp.Processes.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['process_id']
                self._child_classes = OrderedDict([("vrfs-xr", ("vrfs_xr", Eigrp.Processes.Process.VrfsXr)), ("vrfs", ("vrfs", Eigrp.Processes.Process.Vrfs))])
                self._leafs = OrderedDict([
                    ('process_id', (YLeaf(YType.str, 'process-id'), ['str'])),
                ])
                self.process_id = None

                self.vrfs_xr = Eigrp.Processes.Process.VrfsXr()
                self.vrfs_xr.parent = self
                self._children_name_map["vrfs_xr"] = "vrfs-xr"

                self.vrfs = Eigrp.Processes.Process.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._segment_path = lambda: "process" + "[process-id='" + str(self.process_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-eigrp-oper:eigrp/processes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eigrp.Processes.Process, ['process_id'], name, value)


            class VrfsXr(_Entity_):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A VRF
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.VrfsXr.Vrf>`
                
                	**config**\: False
                
                

                """

                _prefix = 'eigrp-oper'
                _revision = '2018-04-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Eigrp.Processes.Process.VrfsXr, self).__init__()

                    self.yang_name = "vrfs-xr"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", Eigrp.Processes.Process.VrfsXr.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Eigrp.Processes.Process.VrfsXr, [], name, value)


                class Vrf(_Entity_):
                    """
                    A VRF
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'eigrp-oper'
                    _revision = '2018-04-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Eigrp.Processes.Process.VrfsXr.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('vrf_name_xr', (YLeaf(YType.str, 'vrf-name-xr'), ['str'])),
                        ])
                        self.vrf_name = None
                        self.vrf_name_xr = None
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Eigrp.Processes.Process.VrfsXr.Vrf, ['vrf_name', 'vrf_name_xr'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                        return meta._meta_table['Eigrp.Processes.Process.VrfsXr.Vrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                    return meta._meta_table['Eigrp.Processes.Process.VrfsXr']['meta_info']


            class Vrfs(_Entity_):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	Operational data for a VRF
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf>`
                
                	**config**\: False
                
                

                """

                _prefix = 'eigrp-oper'
                _revision = '2018-04-05'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Eigrp.Processes.Process.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", Eigrp.Processes.Process.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Eigrp.Processes.Process.Vrfs, [], name, value)


                class Vrf(_Entity_):
                    """
                    Operational data for a VRF
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: afs
                    
                    	List of Address Families
                    	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'eigrp-oper'
                    _revision = '2018-04-05'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Eigrp.Processes.Process.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([("afs", ("afs", Eigrp.Processes.Process.Vrfs.Vrf.Afs))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ])
                        self.vrf_name = None

                        self.afs = Eigrp.Processes.Process.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf, ['vrf_name'], name, value)


                    class Afs(_Entity_):
                        """
                        List of Address Families
                        
                        .. attribute:: af
                        
                        	Operational data for one AF
                        	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'eigrp-oper'
                        _revision = '2018-04-05'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("af", ("af", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af))])
                            self._leafs = OrderedDict()

                            self.af = YList(self)
                            self._segment_path = lambda: "afs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs, [], name, value)


                        class Af(_Entity_):
                            """
                            Operational data for one AF
                            
                            .. attribute:: af_name  (key)
                            
                            	Address Family
                            	**type**\:  :py:class:`EigrpAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes.EigrpAf>`
                            
                            	**config**\: False
                            
                            .. attribute:: protocol
                            
                            	Address family specific protocol information
                            	**type**\:  :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol>`
                            
                            	**config**\: False
                            
                            .. attribute:: ases
                            
                            	List of Autonomous Systems
                            	**type**\:  :py:class:`Ases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'eigrp-oper'
                            _revision = '2018-04-05'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['af_name']
                                self._child_classes = OrderedDict([("protocol", ("protocol", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol)), ("ases", ("ases", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases))])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes', 'EigrpAf', '')])),
                                ])
                                self.af_name = None

                                self.protocol = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol()
                                self.protocol.parent = self
                                self._children_name_map["protocol"] = "protocol"

                                self.ases = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases()
                                self.ases.parent = self
                                self._children_name_map["ases"] = "ases"
                                self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af, ['af_name'], name, value)


                            class Protocol(_Entity_):
                                """
                                Address family specific protocol
                                information
                                
                                .. attribute:: afi
                                
                                	AFI
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: as_number
                                
                                	AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: router_id
                                
                                	Router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: auto_summarization
                                
                                	Auto Summarization
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: log_neighbor_changes
                                
                                	Neighbor changes logged
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: log_neighbor_warnings
                                
                                	Neighbor warnings logged
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rib_table_limit_reached
                                
                                	RIB Table limit has been reached
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: outbound_filter_policy
                                
                                	Outbound Filter Policy
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: inbound_filter_policy
                                
                                	Inbound Filter Policy
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_candidate_default_flagged
                                
                                	Default Allowed Out
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: outgoing_candidate_default_policy
                                
                                	Default Allowed Out Policy
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_candidate_default_flagged
                                
                                	Default Allowed In
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: incoming_candidate_default_policy
                                
                                	Default Allowed In Policy
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: internal_distance
                                
                                	Internal Distance
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: external_distance
                                
                                	External Distance
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum paths
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: variance
                                
                                	Variance
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k1
                                
                                	K1 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k2
                                
                                	K2 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k3
                                
                                	K3 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k4
                                
                                	K4 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k5
                                
                                	K5 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_weight_k6
                                
                                	K6 value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: rib_scale
                                
                                	RIB Scale
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: metric_version
                                
                                	Metric Version
                                	**type**\:  :py:class:`EigrpBdMetricVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdMetricVersion>`
                                
                                	**config**\: False
                                
                                .. attribute:: metric_maximum_hopcount
                                
                                	Metric MaxHops configured
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: default_metric_configured
                                
                                	Default Metric Configured
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: default_bandwidth
                                
                                	Default Bandwidth
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: default_delay
                                
                                	Default Delay
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: default_reliability
                                
                                	Default Reliability
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: default_load
                                
                                	Default Load
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: default_mtu
                                
                                	Default MTU
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: stub_configured
                                
                                	Stub Configured
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: stub_receive_only
                                
                                	Stub Receive\-only configured
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: stub_allow_connected_routes
                                
                                	ConnectedRoutes allowed
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: stub_allow_static_routes
                                
                                	Static Routes allowed
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: stub_allow_summary_routes
                                
                                	Summary Routes allowed
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: stub_allow_redistributed_routes
                                
                                	Redistributed Routes allowed
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: nsf_enabled
                                
                                	NSF Enabled
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: nsf_route_hold_time
                                
                                	NSF Route Hold Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: nsf_signal_time
                                
                                	NSF Signal Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: nsf_converge_time
                                
                                	NSF Converge Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: restart_configured
                                
                                	Is Restart time configured
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: restart_time
                                
                                	Restart time (seconds)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                .. attribute:: sia_active_time
                                
                                	SIA Active Time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: rib_protocol_id
                                
                                	RIB Protocol ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: table_id
                                
                                	Table ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_id
                                
                                	VRF ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ital_activation_received
                                
                                	VRF activated by ITAL
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: vrf_activated
                                
                                	VRF activated by EIGRP
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: up
                                
                                	VRF information available
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rib_initialized
                                
                                	RIB initialization for VRF
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rib_converged
                                
                                	RIB convergence for VRF
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: rib_converged_reload
                                
                                	Reload following RIB Convergence
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: socket_request
                                
                                	Requested Socket Option for VRF
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: socket_setup
                                
                                	Setup socket state for VRF
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: default_vrf
                                
                                	VRF represents default\-context
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: af_enabled
                                
                                	AF Enabled
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_passive_default
                                
                                	Passive\-Interface default configured
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: configured_items
                                
                                	VRF Configured Items
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: af_configured_items
                                
                                	AF Configured Items
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: ip_arm_router_id
                                
                                	IP ARM Router ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: first_interface_up_address
                                
                                	IP Address of first UP interface
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: nsf_in_progress
                                
                                	DDB NSF in progress indication
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: rib_table_converged
                                
                                	RIB Table convergence indication
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: redistributed_protocol
                                
                                	Redistributed Protocols
                                	**type**\: list of  		 :py:class:`RedistributedProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.RedistributedProtocol>`
                                
                                	**config**\: False
                                
                                .. attribute:: interface
                                
                                	Interfaces
                                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.Interface>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'eigrp-oper'
                                _revision = '2018-04-05'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol, self).__init__()

                                    self.yang_name = "protocol"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("redistributed-protocol", ("redistributed_protocol", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.RedistributedProtocol)), ("interface", ("interface", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.Interface))])
                                    self._leafs = OrderedDict([
                                        ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                        ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('auto_summarization', (YLeaf(YType.boolean, 'auto-summarization'), ['bool'])),
                                        ('log_neighbor_changes', (YLeaf(YType.boolean, 'log-neighbor-changes'), ['bool'])),
                                        ('log_neighbor_warnings', (YLeaf(YType.boolean, 'log-neighbor-warnings'), ['bool'])),
                                        ('rib_table_limit_reached', (YLeaf(YType.boolean, 'rib-table-limit-reached'), ['bool'])),
                                        ('outbound_filter_policy', (YLeaf(YType.str, 'outbound-filter-policy'), ['str'])),
                                        ('inbound_filter_policy', (YLeaf(YType.str, 'inbound-filter-policy'), ['str'])),
                                        ('outgoing_candidate_default_flagged', (YLeaf(YType.boolean, 'outgoing-candidate-default-flagged'), ['bool'])),
                                        ('outgoing_candidate_default_policy', (YLeaf(YType.str, 'outgoing-candidate-default-policy'), ['str'])),
                                        ('incoming_candidate_default_flagged', (YLeaf(YType.boolean, 'incoming-candidate-default-flagged'), ['bool'])),
                                        ('incoming_candidate_default_policy', (YLeaf(YType.str, 'incoming-candidate-default-policy'), ['str'])),
                                        ('internal_distance', (YLeaf(YType.uint8, 'internal-distance'), ['int'])),
                                        ('external_distance', (YLeaf(YType.uint8, 'external-distance'), ['int'])),
                                        ('maximum_paths', (YLeaf(YType.uint8, 'maximum-paths'), ['int'])),
                                        ('variance', (YLeaf(YType.uint8, 'variance'), ['int'])),
                                        ('metric_weight_k1', (YLeaf(YType.uint32, 'metric-weight-k1'), ['int'])),
                                        ('metric_weight_k2', (YLeaf(YType.uint32, 'metric-weight-k2'), ['int'])),
                                        ('metric_weight_k3', (YLeaf(YType.uint32, 'metric-weight-k3'), ['int'])),
                                        ('metric_weight_k4', (YLeaf(YType.uint32, 'metric-weight-k4'), ['int'])),
                                        ('metric_weight_k5', (YLeaf(YType.uint32, 'metric-weight-k5'), ['int'])),
                                        ('metric_weight_k6', (YLeaf(YType.uint32, 'metric-weight-k6'), ['int'])),
                                        ('rib_scale', (YLeaf(YType.uint32, 'rib-scale'), ['int'])),
                                        ('metric_version', (YLeaf(YType.enumeration, 'metric-version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdMetricVersion', '')])),
                                        ('metric_maximum_hopcount', (YLeaf(YType.uint32, 'metric-maximum-hopcount'), ['int'])),
                                        ('default_metric_configured', (YLeaf(YType.boolean, 'default-metric-configured'), ['bool'])),
                                        ('default_bandwidth', (YLeaf(YType.uint32, 'default-bandwidth'), ['int'])),
                                        ('default_delay', (YLeaf(YType.uint32, 'default-delay'), ['int'])),
                                        ('default_reliability', (YLeaf(YType.uint32, 'default-reliability'), ['int'])),
                                        ('default_load', (YLeaf(YType.uint32, 'default-load'), ['int'])),
                                        ('default_mtu', (YLeaf(YType.uint32, 'default-mtu'), ['int'])),
                                        ('stub_configured', (YLeaf(YType.boolean, 'stub-configured'), ['bool'])),
                                        ('stub_receive_only', (YLeaf(YType.boolean, 'stub-receive-only'), ['bool'])),
                                        ('stub_allow_connected_routes', (YLeaf(YType.boolean, 'stub-allow-connected-routes'), ['bool'])),
                                        ('stub_allow_static_routes', (YLeaf(YType.boolean, 'stub-allow-static-routes'), ['bool'])),
                                        ('stub_allow_summary_routes', (YLeaf(YType.boolean, 'stub-allow-summary-routes'), ['bool'])),
                                        ('stub_allow_redistributed_routes', (YLeaf(YType.boolean, 'stub-allow-redistributed-routes'), ['bool'])),
                                        ('nsf_enabled', (YLeaf(YType.boolean, 'nsf-enabled'), ['bool'])),
                                        ('nsf_route_hold_time', (YLeaf(YType.uint32, 'nsf-route-hold-time'), ['int'])),
                                        ('nsf_signal_time', (YLeaf(YType.uint32, 'nsf-signal-time'), ['int'])),
                                        ('nsf_converge_time', (YLeaf(YType.uint32, 'nsf-converge-time'), ['int'])),
                                        ('restart_configured', (YLeaf(YType.boolean, 'restart-configured'), ['bool'])),
                                        ('restart_time', (YLeaf(YType.uint32, 'restart-time'), ['int'])),
                                        ('sia_active_time', (YLeaf(YType.uint32, 'sia-active-time'), ['int'])),
                                        ('rib_protocol_id', (YLeaf(YType.uint32, 'rib-protocol-id'), ['int'])),
                                        ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                        ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                        ('ital_activation_received', (YLeaf(YType.boolean, 'ital-activation-received'), ['bool'])),
                                        ('vrf_activated', (YLeaf(YType.boolean, 'vrf-activated'), ['bool'])),
                                        ('up', (YLeaf(YType.boolean, 'up'), ['bool'])),
                                        ('rib_initialized', (YLeaf(YType.boolean, 'rib-initialized'), ['bool'])),
                                        ('rib_converged', (YLeaf(YType.boolean, 'rib-converged'), ['bool'])),
                                        ('rib_converged_reload', (YLeaf(YType.boolean, 'rib-converged-reload'), ['bool'])),
                                        ('socket_request', (YLeaf(YType.boolean, 'socket-request'), ['bool'])),
                                        ('socket_setup', (YLeaf(YType.boolean, 'socket-setup'), ['bool'])),
                                        ('default_vrf', (YLeaf(YType.boolean, 'default-vrf'), ['bool'])),
                                        ('af_enabled', (YLeaf(YType.boolean, 'af-enabled'), ['bool'])),
                                        ('is_passive_default', (YLeaf(YType.boolean, 'is-passive-default'), ['bool'])),
                                        ('configured_items', (YLeaf(YType.uint32, 'configured-items'), ['int'])),
                                        ('af_configured_items', (YLeaf(YType.uint32, 'af-configured-items'), ['int'])),
                                        ('ip_arm_router_id', (YLeaf(YType.uint32, 'ip-arm-router-id'), ['int'])),
                                        ('first_interface_up_address', (YLeaf(YType.uint32, 'first-interface-up-address'), ['int'])),
                                        ('nsf_in_progress', (YLeaf(YType.uint32, 'nsf-in-progress'), ['int'])),
                                        ('rib_table_converged', (YLeaf(YType.uint32, 'rib-table-converged'), ['int'])),
                                    ])
                                    self.afi = None
                                    self.as_number = None
                                    self.router_id = None
                                    self.auto_summarization = None
                                    self.log_neighbor_changes = None
                                    self.log_neighbor_warnings = None
                                    self.rib_table_limit_reached = None
                                    self.outbound_filter_policy = None
                                    self.inbound_filter_policy = None
                                    self.outgoing_candidate_default_flagged = None
                                    self.outgoing_candidate_default_policy = None
                                    self.incoming_candidate_default_flagged = None
                                    self.incoming_candidate_default_policy = None
                                    self.internal_distance = None
                                    self.external_distance = None
                                    self.maximum_paths = None
                                    self.variance = None
                                    self.metric_weight_k1 = None
                                    self.metric_weight_k2 = None
                                    self.metric_weight_k3 = None
                                    self.metric_weight_k4 = None
                                    self.metric_weight_k5 = None
                                    self.metric_weight_k6 = None
                                    self.rib_scale = None
                                    self.metric_version = None
                                    self.metric_maximum_hopcount = None
                                    self.default_metric_configured = None
                                    self.default_bandwidth = None
                                    self.default_delay = None
                                    self.default_reliability = None
                                    self.default_load = None
                                    self.default_mtu = None
                                    self.stub_configured = None
                                    self.stub_receive_only = None
                                    self.stub_allow_connected_routes = None
                                    self.stub_allow_static_routes = None
                                    self.stub_allow_summary_routes = None
                                    self.stub_allow_redistributed_routes = None
                                    self.nsf_enabled = None
                                    self.nsf_route_hold_time = None
                                    self.nsf_signal_time = None
                                    self.nsf_converge_time = None
                                    self.restart_configured = None
                                    self.restart_time = None
                                    self.sia_active_time = None
                                    self.rib_protocol_id = None
                                    self.table_id = None
                                    self.vrf_id = None
                                    self.ital_activation_received = None
                                    self.vrf_activated = None
                                    self.up = None
                                    self.rib_initialized = None
                                    self.rib_converged = None
                                    self.rib_converged_reload = None
                                    self.socket_request = None
                                    self.socket_setup = None
                                    self.default_vrf = None
                                    self.af_enabled = None
                                    self.is_passive_default = None
                                    self.configured_items = None
                                    self.af_configured_items = None
                                    self.ip_arm_router_id = None
                                    self.first_interface_up_address = None
                                    self.nsf_in_progress = None
                                    self.rib_table_converged = None

                                    self.redistributed_protocol = YList(self)
                                    self.interface = YList(self)
                                    self._segment_path = lambda: "protocol"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol, ['afi', 'as_number', 'router_id', 'auto_summarization', 'log_neighbor_changes', 'log_neighbor_warnings', 'rib_table_limit_reached', 'outbound_filter_policy', 'inbound_filter_policy', 'outgoing_candidate_default_flagged', 'outgoing_candidate_default_policy', 'incoming_candidate_default_flagged', 'incoming_candidate_default_policy', 'internal_distance', 'external_distance', 'maximum_paths', 'variance', 'metric_weight_k1', 'metric_weight_k2', 'metric_weight_k3', 'metric_weight_k4', 'metric_weight_k5', 'metric_weight_k6', 'rib_scale', 'metric_version', 'metric_maximum_hopcount', 'default_metric_configured', 'default_bandwidth', 'default_delay', 'default_reliability', 'default_load', 'default_mtu', 'stub_configured', 'stub_receive_only', 'stub_allow_connected_routes', 'stub_allow_static_routes', 'stub_allow_summary_routes', 'stub_allow_redistributed_routes', 'nsf_enabled', 'nsf_route_hold_time', 'nsf_signal_time', 'nsf_converge_time', 'restart_configured', 'restart_time', 'sia_active_time', 'rib_protocol_id', 'table_id', 'vrf_id', 'ital_activation_received', 'vrf_activated', 'up', 'rib_initialized', 'rib_converged', 'rib_converged_reload', 'socket_request', 'socket_setup', 'default_vrf', 'af_enabled', 'is_passive_default', 'configured_items', 'af_configured_items', 'ip_arm_router_id', 'first_interface_up_address', 'nsf_in_progress', 'rib_table_converged'], name, value)


                                class RedistributedProtocol(_Entity_):
                                    """
                                    Redistributed Protocols
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: redistributed_protocol
                                    
                                    	Redistributed Protocol
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: redistributed_protocol_tag
                                    
                                    	Redistributed Protocol tag
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: redristribute_policy
                                    
                                    	Redistribute Filter policy
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: redistribute_protocol_id
                                    
                                    	Redistributed Protocol ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rib_handle
                                    
                                    	Redistributed Protocol handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'eigrp-oper'
                                    _revision = '2018-04-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.RedistributedProtocol, self).__init__()

                                        self.yang_name = "redistributed-protocol"
                                        self.yang_parent_name = "protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                            ('redistributed_protocol', (YLeaf(YType.str, 'redistributed-protocol'), ['str'])),
                                            ('redistributed_protocol_tag', (YLeaf(YType.str, 'redistributed-protocol-tag'), ['str'])),
                                            ('redristribute_policy', (YLeaf(YType.str, 'redristribute-policy'), ['str'])),
                                            ('redistribute_protocol_id', (YLeaf(YType.uint32, 'redistribute-protocol-id'), ['int'])),
                                            ('rib_handle', (YLeaf(YType.uint32, 'rib-handle'), ['int'])),
                                        ])
                                        self.afi = None
                                        self.redistributed_protocol = None
                                        self.redistributed_protocol_tag = None
                                        self.redristribute_policy = None
                                        self.redistribute_protocol_id = None
                                        self.rib_handle = None
                                        self._segment_path = lambda: "redistributed-protocol"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.RedistributedProtocol, ['afi', 'redistributed_protocol', 'redistributed_protocol_tag', 'redristribute_policy', 'redistribute_protocol_id', 'rib_handle'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.RedistributedProtocol']['meta_info']


                                class Interface(_Entity_):
                                    """
                                    Interfaces
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interface
                                    
                                    	Interface
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: outbound_filter_policy
                                    
                                    	Outbound Filter Policy
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: inbound_filter_policy
                                    
                                    	Inbound Filter Policy
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: inactive
                                    
                                    	Interface is DOWN
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: passive_interface
                                    
                                    	Interface is passive
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'eigrp-oper'
                                    _revision = '2018-04-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.Interface, self).__init__()

                                        self.yang_name = "interface"
                                        self.yang_parent_name = "protocol"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                            ('outbound_filter_policy', (YLeaf(YType.str, 'outbound-filter-policy'), ['str'])),
                                            ('inbound_filter_policy', (YLeaf(YType.str, 'inbound-filter-policy'), ['str'])),
                                            ('inactive', (YLeaf(YType.boolean, 'inactive'), ['bool'])),
                                            ('passive_interface', (YLeaf(YType.boolean, 'passive-interface'), ['bool'])),
                                        ])
                                        self.afi = None
                                        self.interface = None
                                        self.outbound_filter_policy = None
                                        self.inbound_filter_policy = None
                                        self.inactive = None
                                        self.passive_interface = None
                                        self._segment_path = lambda: "interface"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.Interface, ['afi', 'interface', 'outbound_filter_policy', 'inbound_filter_policy', 'inactive', 'passive_interface'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol.Interface']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Protocol']['meta_info']


                            class Ases(_Entity_):
                                """
                                List of Autonomous Systems
                                
                                .. attribute:: as_
                                
                                	Operational data for one AS
                                	**type**\: list of  		 :py:class:`As <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'eigrp-oper'
                                _revision = '2018-04-05'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases, self).__init__()

                                    self.yang_name = "ases"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("as", ("as_", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As))])
                                    self._leafs = OrderedDict()

                                    self.as_ = YList(self)
                                    self._segment_path = lambda: "ases"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases, [], name, value)


                                class As(_Entity_):
                                    """
                                    Operational data for one AS
                                    
                                    .. attribute:: asn  (key)
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: static_neighbors
                                    
                                    	EIGRP static neighbors
                                    	**type**\:  :py:class:`StaticNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: topology_routes
                                    
                                    	EIGRP topology table
                                    	**type**\:  :py:class:`TopologyRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eigrp_accounting
                                    
                                    	Accounting info for one VRF AF
                                    	**type**\:  :py:class:`EigrpAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eigrp_traffic
                                    
                                    	Traffic info for one VRF AF
                                    	**type**\:  :py:class:`EigrpTraffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eigrp_topology_summary
                                    
                                    	Topology summary info for one VRF AF
                                    	**type**\:  :py:class:`EigrpTopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: interfaces
                                    
                                    	EIGRP interfaces
                                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eigrp_events
                                    
                                    	Events for a specific VRF AF
                                    	**type**\:  :py:class:`EigrpEvents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbors
                                    
                                    	EIGRP neighbors
                                    	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: eigrp_statistics
                                    
                                    	Statistics for a specific VRF AF
                                    	**type**\:  :py:class:`EigrpStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'eigrp-oper'
                                    _revision = '2018-04-05'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As, self).__init__()

                                        self.yang_name = "as"
                                        self.yang_parent_name = "ases"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['asn']
                                        self._child_classes = OrderedDict([("static-neighbors", ("static_neighbors", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors)), ("topology-routes", ("topology_routes", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes)), ("eigrp-accounting", ("eigrp_accounting", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting)), ("eigrp-traffic", ("eigrp_traffic", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic)), ("eigrp-topology-summary", ("eigrp_topology_summary", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary)), ("interfaces", ("interfaces", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces)), ("eigrp-events", ("eigrp_events", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents)), ("neighbors", ("neighbors", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors)), ("eigrp-statistics", ("eigrp_statistics", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics))])
                                        self._leafs = OrderedDict([
                                            ('asn', (YLeaf(YType.uint32, 'asn'), ['int'])),
                                        ])
                                        self.asn = None

                                        self.static_neighbors = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors()
                                        self.static_neighbors.parent = self
                                        self._children_name_map["static_neighbors"] = "static-neighbors"

                                        self.topology_routes = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes()
                                        self.topology_routes.parent = self
                                        self._children_name_map["topology_routes"] = "topology-routes"

                                        self.eigrp_accounting = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting()
                                        self.eigrp_accounting.parent = self
                                        self._children_name_map["eigrp_accounting"] = "eigrp-accounting"

                                        self.eigrp_traffic = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic()
                                        self.eigrp_traffic.parent = self
                                        self._children_name_map["eigrp_traffic"] = "eigrp-traffic"

                                        self.eigrp_topology_summary = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary()
                                        self.eigrp_topology_summary.parent = self
                                        self._children_name_map["eigrp_topology_summary"] = "eigrp-topology-summary"

                                        self.interfaces = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces()
                                        self.interfaces.parent = self
                                        self._children_name_map["interfaces"] = "interfaces"

                                        self.eigrp_events = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents()
                                        self.eigrp_events.parent = self
                                        self._children_name_map["eigrp_events"] = "eigrp-events"

                                        self.neighbors = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors()
                                        self.neighbors.parent = self
                                        self._children_name_map["neighbors"] = "neighbors"

                                        self.eigrp_statistics = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics()
                                        self.eigrp_statistics.parent = self
                                        self._children_name_map["eigrp_statistics"] = "eigrp-statistics"
                                        self._segment_path = lambda: "as" + "[asn='" + str(self.asn) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As, ['asn'], name, value)


                                    class StaticNeighbors(_Entity_):
                                        """
                                        EIGRP static neighbors
                                        
                                        .. attribute:: static_neighbor
                                        
                                        	Information on one static EIGRP neighbor
                                        	**type**\: list of  		 :py:class:`StaticNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors, self).__init__()

                                            self.yang_name = "static-neighbors"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("static-neighbor", ("static_neighbor", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor))])
                                            self._leafs = OrderedDict()

                                            self.static_neighbor = YList(self)
                                            self._segment_path = lambda: "static-neighbors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors, [], name, value)


                                        class StaticNeighbor(_Entity_):
                                            """
                                            Information on one static EIGRP
                                            neighbor
                                            
                                            .. attribute:: neighbor_address  (key)
                                            
                                            	Neighbor Address
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: source
                                            
                                            	Neighbor address
                                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as_number
                                            
                                            	AS Number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_list
                                            
                                            	Interface Name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor, self).__init__()

                                                self.yang_name = "static-neighbor"
                                                self.yang_parent_name = "static-neighbors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['neighbor_address']
                                                self._child_classes = OrderedDict([("source", ("source", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source))])
                                                self._leafs = OrderedDict([
                                                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                                                    ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                    ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                    ('interface_list', (YLeaf(YType.str, 'interface-list'), ['str'])),
                                                ])
                                                self.neighbor_address = None
                                                self.afi = None
                                                self.as_number = None
                                                self.interface_list = None

                                                self.source = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source()
                                                self.source.parent = self
                                                self._children_name_map["source"] = "source"
                                                self._segment_path = lambda: "static-neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor, ['neighbor_address', 'afi', 'as_number', 'interface_list'], name, value)


                                            class Source(_Entity_):
                                                """
                                                Neighbor address
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 Address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 Address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source, self).__init__()

                                                    self.yang_name = "source"
                                                    self.yang_parent_name = "static-neighbor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "source"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source, ['ipv4_address', 'ipv6_address'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor.Source']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors.StaticNeighbor']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.StaticNeighbors']['meta_info']


                                    class TopologyRoutes(_Entity_):
                                        """
                                        EIGRP topology table
                                        
                                        .. attribute:: topology_route
                                        
                                        	Information about one EIGRP route
                                        	**type**\: list of  		 :py:class:`TopologyRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes, self).__init__()

                                            self.yang_name = "topology-routes"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("topology-route", ("topology_route", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute))])
                                            self._leafs = OrderedDict()

                                            self.topology_route = YList(self)
                                            self._segment_path = lambda: "topology-routes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes, [], name, value)


                                        class TopologyRoute(_Entity_):
                                            """
                                            Information about one EIGRP route
                                            
                                            .. attribute:: prefix
                                            
                                            	IP Prefix
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: prefix_length
                                            
                                            	IP Prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..128
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: prefix_xr
                                            
                                            	IP Prefix/length
                                            	**type**\:  :py:class:`PrefixXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as_number
                                            
                                            	AS Number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: router_id
                                            
                                            	Router ID
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: active
                                            
                                            	Active route
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: successors
                                            
                                            	Successors
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: successors_present
                                            
                                            	Are there successors
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: old_metric
                                            
                                            	Deprecated. Please migrate to use OldMetric64. The value of this object might wrap since the metric value can go up to (2^48 \- 1) in 64\-bit metric mode
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: old_metric64
                                            
                                            	Old metric
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: metric
                                            
                                            	Deprecated. Please migrate to use Metric64. The value of this object might wrap since the metric value can go up to (2^48 \- 1) in 64\-bit metric mode
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: metric64
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: rib_metric
                                            
                                            	Metric downloaded to RIB
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: tag
                                            
                                            	Tag
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: send_flag
                                            
                                            	Send flag
                                            	**type**\:  :py:class:`EigrpBdPathSendFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdPathSendFlag>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: transmit_serial_number
                                            
                                            	Transmit thread Serial Number
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: transmit_refcount
                                            
                                            	Transmit thread refcount
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: transmit_anchored
                                            
                                            	Is Transmit thread anchored
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reply_handles
                                            
                                            	Reply handles used
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: active_time_secs
                                            
                                            	Active time seconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            	**units**\: second
                                            
                                            .. attribute:: active_time_nsecs
                                            
                                            	Active time nanoseconds
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            	**units**\: nanosecond
                                            
                                            .. attribute:: origin
                                            
                                            	Origin
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: retry_count
                                            
                                            	Retry count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: active_stats
                                            
                                            	Active stats flag
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: min_time
                                            
                                            	Active stats min time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: max_time
                                            
                                            	Active stats max time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: average_time
                                            
                                            	Active stats average time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ack_count
                                            
                                            	Active stats active count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: replies
                                            
                                            	Number of replies outstanding
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: route_in_sia
                                            
                                            	Route is SIA
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: sia_reply_handles
                                            
                                            	Reply handles used
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: paths
                                            
                                            	Paths for this route
                                            	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: active_peer
                                            
                                            	Peers yet to respond
                                            	**type**\: list of  		 :py:class:`ActivePeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: sia_peer
                                            
                                            	SIA Peers yet to respond
                                            	**type**\: list of  		 :py:class:`SiaPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute, self).__init__()

                                                self.yang_name = "topology-route"
                                                self.yang_parent_name = "topology-routes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("prefix-xr", ("prefix_xr", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr)), ("paths", ("paths", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths)), ("active-peer", ("active_peer", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer)), ("sia-peer", ("sia_peer", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer))])
                                                self._leafs = OrderedDict([
                                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                                    ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                    ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                                    ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                                                    ('successors', (YLeaf(YType.uint32, 'successors'), ['int'])),
                                                    ('successors_present', (YLeaf(YType.boolean, 'successors-present'), ['bool'])),
                                                    ('old_metric', (YLeaf(YType.uint32, 'old-metric'), ['int'])),
                                                    ('old_metric64', (YLeaf(YType.uint64, 'old-metric64'), ['int'])),
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('metric64', (YLeaf(YType.uint64, 'metric64'), ['int'])),
                                                    ('rib_metric', (YLeaf(YType.uint32, 'rib-metric'), ['int'])),
                                                    ('tag', (YLeaf(YType.uint32, 'tag'), ['int'])),
                                                    ('send_flag', (YLeaf(YType.enumeration, 'send-flag'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdPathSendFlag', '')])),
                                                    ('transmit_serial_number', (YLeaf(YType.uint64, 'transmit-serial-number'), ['int'])),
                                                    ('transmit_refcount', (YLeaf(YType.uint32, 'transmit-refcount'), ['int'])),
                                                    ('transmit_anchored', (YLeaf(YType.boolean, 'transmit-anchored'), ['bool'])),
                                                    ('reply_handles', (YLeaf(YType.uint32, 'reply-handles'), ['int'])),
                                                    ('active_time_secs', (YLeaf(YType.uint32, 'active-time-secs'), ['int'])),
                                                    ('active_time_nsecs', (YLeaf(YType.uint32, 'active-time-nsecs'), ['int'])),
                                                    ('origin', (YLeaf(YType.uint32, 'origin'), ['int'])),
                                                    ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                                                    ('active_stats', (YLeaf(YType.boolean, 'active-stats'), ['bool'])),
                                                    ('min_time', (YLeaf(YType.uint32, 'min-time'), ['int'])),
                                                    ('max_time', (YLeaf(YType.uint32, 'max-time'), ['int'])),
                                                    ('average_time', (YLeaf(YType.uint32, 'average-time'), ['int'])),
                                                    ('ack_count', (YLeaf(YType.uint32, 'ack-count'), ['int'])),
                                                    ('replies', (YLeaf(YType.uint32, 'replies'), ['int'])),
                                                    ('route_in_sia', (YLeaf(YType.boolean, 'route-in-sia'), ['bool'])),
                                                    ('sia_reply_handles', (YLeaf(YType.uint32, 'sia-reply-handles'), ['int'])),
                                                ])
                                                self.prefix = None
                                                self.prefix_length = None
                                                self.afi = None
                                                self.as_number = None
                                                self.router_id = None
                                                self.active = None
                                                self.successors = None
                                                self.successors_present = None
                                                self.old_metric = None
                                                self.old_metric64 = None
                                                self.metric = None
                                                self.metric64 = None
                                                self.rib_metric = None
                                                self.tag = None
                                                self.send_flag = None
                                                self.transmit_serial_number = None
                                                self.transmit_refcount = None
                                                self.transmit_anchored = None
                                                self.reply_handles = None
                                                self.active_time_secs = None
                                                self.active_time_nsecs = None
                                                self.origin = None
                                                self.retry_count = None
                                                self.active_stats = None
                                                self.min_time = None
                                                self.max_time = None
                                                self.average_time = None
                                                self.ack_count = None
                                                self.replies = None
                                                self.route_in_sia = None
                                                self.sia_reply_handles = None

                                                self.prefix_xr = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr()
                                                self.prefix_xr.parent = self
                                                self._children_name_map["prefix_xr"] = "prefix-xr"

                                                self.paths = YList(self)
                                                self.active_peer = YList(self)
                                                self.sia_peer = YList(self)
                                                self._segment_path = lambda: "topology-route"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute, ['prefix', 'prefix_length', 'afi', 'as_number', 'router_id', 'active', 'successors', 'successors_present', 'old_metric', 'old_metric64', 'metric', 'metric64', 'rib_metric', 'tag', 'send_flag', 'transmit_serial_number', 'transmit_refcount', 'transmit_anchored', 'reply_handles', 'active_time_secs', 'active_time_nsecs', 'origin', 'retry_count', 'active_stats', 'min_time', 'max_time', 'average_time', 'ack_count', 'replies', 'route_in_sia', 'sia_reply_handles'], name, value)


                                            class PrefixXr(_Entity_):
                                                """
                                                IP Prefix/length
                                                
                                                .. attribute:: ipv4_prefix
                                                
                                                	IPv4 Prefix
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6_prefix
                                                
                                                	IPv6 Prefix
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: prefix_length
                                                
                                                	Prefix length
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr, self).__init__()

                                                    self.yang_name = "prefix-xr"
                                                    self.yang_parent_name = "topology-route"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                                    ])
                                                    self.ipv4_prefix = None
                                                    self.ipv6_prefix = None
                                                    self.prefix_length = None
                                                    self._segment_path = lambda: "prefix-xr"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr, ['ipv4_prefix', 'ipv6_prefix', 'prefix_length'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.PrefixXr']['meta_info']


                                            class Paths(_Entity_):
                                                """
                                                Paths for this route
                                                
                                                .. attribute:: next_hop_address
                                                
                                                	Nexthop address
                                                	**type**\:  :py:class:`NextHopAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: infosource
                                                
                                                	Source of route
                                                	**type**\:  :py:class:`Infosource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: afi
                                                
                                                	AFI
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: next_hop_present
                                                
                                                	NH flag
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_handle
                                                
                                                	Interface handle
                                                	**type**\: str
                                                
                                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_name
                                                
                                                	Interface name
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: origin
                                                
                                                	Origin of route
                                                	**type**\:  :py:class:`EigrpBdPathOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdPathOrigin>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: send_flag
                                                
                                                	Send flag
                                                	**type**\:  :py:class:`EigrpBdPathSendFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdPathSendFlag>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: reply_outstanding
                                                
                                                	Outstanding reply
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: metric
                                                
                                                	Deprecated. Please migrate to use Metric64. The value of this object might wrap since the metric value can go up to (2^48 \- 1) in 64\-bit metric mode
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: metric64
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: successor_metric
                                                
                                                	Deprecated. Please migrate to use SuccessorMetric64. The value of this object might wrap since the metric value can go up to (2^48 \- 1) in 64\-bit metric mode
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: successor_metric64
                                                
                                                	Successor metric
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: reply_status
                                                
                                                	Reply status
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: sia_status
                                                
                                                	SIA status
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: transmit_serial_number
                                                
                                                	Transmit thread serial number
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: anchored
                                                
                                                	Is Transmit thread anchored
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_path
                                                
                                                	External
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: bandwidth
                                                
                                                	Deprecated. Please migrate to use Bandwidth64
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: bandwidth64
                                                
                                                	Bandwidth
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: delay
                                                
                                                	Deprecated. Please migrate to use Delay64. The value of this object might wrap if it is in picosecond units 
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: delay64
                                                
                                                	Delay
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: delay_unit
                                                
                                                	Delay units
                                                	**type**\:  :py:class:`EigrpBdDelayUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdDelayUnit>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: mtu
                                                
                                                	MTU
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hop_count
                                                
                                                	Hopcount
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: reliability
                                                
                                                	Reliability
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: load
                                                
                                                	Load
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: internal_router_id
                                                
                                                	Router ID
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: internal_tag
                                                
                                                	Internal Tag
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: extended_communities_present
                                                
                                                	Extended communities present
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: extended_communities_length
                                                
                                                	Length of extended communities
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: extended_communities
                                                
                                                	Extended communities
                                                	**type**\: str
                                                
                                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_information_present
                                                
                                                	External information present
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_router_id
                                                
                                                	Router ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_this_system
                                                
                                                	Is it this system
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_as
                                                
                                                	AS Number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_protocol
                                                
                                                	Protocol ID
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: external_tag
                                                
                                                	Tag
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: conditional_default_path
                                                
                                                	Conditional Default flag
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: rib_state
                                                
                                                	State of path in RIB
                                                	**type**\:  :py:class:`EigrpBdPathRibState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdPathRibState>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths, self).__init__()

                                                    self.yang_name = "paths"
                                                    self.yang_parent_name = "topology-route"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("next-hop-address", ("next_hop_address", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress)), ("infosource", ("infosource", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource))])
                                                    self._leafs = OrderedDict([
                                                        ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                        ('next_hop_present', (YLeaf(YType.boolean, 'next-hop-present'), ['bool'])),
                                                        ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                        ('origin', (YLeaf(YType.enumeration, 'origin'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdPathOrigin', '')])),
                                                        ('send_flag', (YLeaf(YType.enumeration, 'send-flag'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdPathSendFlag', '')])),
                                                        ('reply_outstanding', (YLeaf(YType.boolean, 'reply-outstanding'), ['bool'])),
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('metric64', (YLeaf(YType.uint64, 'metric64'), ['int'])),
                                                        ('successor_metric', (YLeaf(YType.uint32, 'successor-metric'), ['int'])),
                                                        ('successor_metric64', (YLeaf(YType.uint64, 'successor-metric64'), ['int'])),
                                                        ('reply_status', (YLeaf(YType.boolean, 'reply-status'), ['bool'])),
                                                        ('sia_status', (YLeaf(YType.boolean, 'sia-status'), ['bool'])),
                                                        ('transmit_serial_number', (YLeaf(YType.uint64, 'transmit-serial-number'), ['int'])),
                                                        ('anchored', (YLeaf(YType.boolean, 'anchored'), ['bool'])),
                                                        ('external_path', (YLeaf(YType.boolean, 'external-path'), ['bool'])),
                                                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                                        ('bandwidth64', (YLeaf(YType.uint64, 'bandwidth64'), ['int'])),
                                                        ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                                        ('delay64', (YLeaf(YType.uint64, 'delay64'), ['int'])),
                                                        ('delay_unit', (YLeaf(YType.enumeration, 'delay-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdDelayUnit', '')])),
                                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                                        ('hop_count', (YLeaf(YType.uint32, 'hop-count'), ['int'])),
                                                        ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                                                        ('load', (YLeaf(YType.uint8, 'load'), ['int'])),
                                                        ('internal_router_id', (YLeaf(YType.str, 'internal-router-id'), ['str'])),
                                                        ('internal_tag', (YLeaf(YType.uint8, 'internal-tag'), ['int'])),
                                                        ('extended_communities_present', (YLeaf(YType.boolean, 'extended-communities-present'), ['bool'])),
                                                        ('extended_communities_length', (YLeaf(YType.uint32, 'extended-communities-length'), ['int'])),
                                                        ('extended_communities', (YLeaf(YType.str, 'extended-communities'), ['str'])),
                                                        ('external_information_present', (YLeaf(YType.boolean, 'external-information-present'), ['bool'])),
                                                        ('external_router_id', (YLeaf(YType.uint32, 'external-router-id'), ['int'])),
                                                        ('external_this_system', (YLeaf(YType.boolean, 'external-this-system'), ['bool'])),
                                                        ('external_as', (YLeaf(YType.uint32, 'external-as'), ['int'])),
                                                        ('external_protocol', (YLeaf(YType.str, 'external-protocol'), ['str'])),
                                                        ('external_metric', (YLeaf(YType.uint32, 'external-metric'), ['int'])),
                                                        ('external_tag', (YLeaf(YType.uint32, 'external-tag'), ['int'])),
                                                        ('conditional_default_path', (YLeaf(YType.boolean, 'conditional-default-path'), ['bool'])),
                                                        ('rib_state', (YLeaf(YType.enumeration, 'rib-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdPathRibState', '')])),
                                                    ])
                                                    self.afi = None
                                                    self.next_hop_present = None
                                                    self.interface_handle = None
                                                    self.interface_name = None
                                                    self.origin = None
                                                    self.send_flag = None
                                                    self.reply_outstanding = None
                                                    self.metric = None
                                                    self.metric64 = None
                                                    self.successor_metric = None
                                                    self.successor_metric64 = None
                                                    self.reply_status = None
                                                    self.sia_status = None
                                                    self.transmit_serial_number = None
                                                    self.anchored = None
                                                    self.external_path = None
                                                    self.bandwidth = None
                                                    self.bandwidth64 = None
                                                    self.delay = None
                                                    self.delay64 = None
                                                    self.delay_unit = None
                                                    self.mtu = None
                                                    self.hop_count = None
                                                    self.reliability = None
                                                    self.load = None
                                                    self.internal_router_id = None
                                                    self.internal_tag = None
                                                    self.extended_communities_present = None
                                                    self.extended_communities_length = None
                                                    self.extended_communities = None
                                                    self.external_information_present = None
                                                    self.external_router_id = None
                                                    self.external_this_system = None
                                                    self.external_as = None
                                                    self.external_protocol = None
                                                    self.external_metric = None
                                                    self.external_tag = None
                                                    self.conditional_default_path = None
                                                    self.rib_state = None

                                                    self.next_hop_address = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress()
                                                    self.next_hop_address.parent = self
                                                    self._children_name_map["next_hop_address"] = "next-hop-address"

                                                    self.infosource = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource()
                                                    self.infosource.parent = self
                                                    self._children_name_map["infosource"] = "infosource"
                                                    self._segment_path = lambda: "paths"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths, ['afi', 'next_hop_present', 'interface_handle', 'interface_name', 'origin', 'send_flag', 'reply_outstanding', 'metric', 'metric64', 'successor_metric', 'successor_metric64', 'reply_status', 'sia_status', 'transmit_serial_number', 'anchored', 'external_path', 'bandwidth', 'bandwidth64', 'delay', 'delay64', 'delay_unit', 'mtu', 'hop_count', 'reliability', 'load', 'internal_router_id', 'internal_tag', 'extended_communities_present', 'extended_communities_length', 'extended_communities', 'external_information_present', 'external_router_id', 'external_this_system', 'external_as', 'external_protocol', 'external_metric', 'external_tag', 'conditional_default_path', 'rib_state'], name, value)


                                                class NextHopAddress(_Entity_):
                                                    """
                                                    Nexthop address
                                                    
                                                    .. attribute:: ipv4_address
                                                    
                                                    	IPv4 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ipv6_address
                                                    
                                                    	IPv6 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'eigrp-oper'
                                                    _revision = '2018-04-05'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress, self).__init__()

                                                        self.yang_name = "next-hop-address"
                                                        self.yang_parent_name = "paths"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                        ])
                                                        self.ipv4_address = None
                                                        self.ipv6_address = None
                                                        self._segment_path = lambda: "next-hop-address"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress, ['ipv4_address', 'ipv6_address'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.NextHopAddress']['meta_info']


                                                class Infosource(_Entity_):
                                                    """
                                                    Source of route
                                                    
                                                    .. attribute:: ipv4_address
                                                    
                                                    	IPv4 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ipv6_address
                                                    
                                                    	IPv6 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'eigrp-oper'
                                                    _revision = '2018-04-05'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource, self).__init__()

                                                        self.yang_name = "infosource"
                                                        self.yang_parent_name = "paths"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                        ])
                                                        self.ipv4_address = None
                                                        self.ipv6_address = None
                                                        self._segment_path = lambda: "infosource"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource, ['ipv4_address', 'ipv6_address'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths.Infosource']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.Paths']['meta_info']


                                            class ActivePeer(_Entity_):
                                                """
                                                Peers yet to respond
                                                
                                                .. attribute:: source
                                                
                                                	Peer Address
                                                	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: peer_available
                                                
                                                	Peer available
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_list
                                                
                                                	Interface name
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: handle_number
                                                
                                                	Handle number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer, self).__init__()

                                                    self.yang_name = "active-peer"
                                                    self.yang_parent_name = "topology-route"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("source", ("source", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source))])
                                                    self._leafs = OrderedDict([
                                                        ('peer_available', (YLeaf(YType.boolean, 'peer-available'), ['bool'])),
                                                        ('interface_list', (YLeaf(YType.str, 'interface-list'), ['str'])),
                                                        ('handle_number', (YLeaf(YType.uint32, 'handle-number'), ['int'])),
                                                    ])
                                                    self.peer_available = None
                                                    self.interface_list = None
                                                    self.handle_number = None

                                                    self.source = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source()
                                                    self.source.parent = self
                                                    self._children_name_map["source"] = "source"
                                                    self._segment_path = lambda: "active-peer"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer, ['peer_available', 'interface_list', 'handle_number'], name, value)


                                                class Source(_Entity_):
                                                    """
                                                    Peer Address
                                                    
                                                    .. attribute:: ipv4_address
                                                    
                                                    	IPv4 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ipv6_address
                                                    
                                                    	IPv6 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'eigrp-oper'
                                                    _revision = '2018-04-05'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source, self).__init__()

                                                        self.yang_name = "source"
                                                        self.yang_parent_name = "active-peer"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                        ])
                                                        self.ipv4_address = None
                                                        self.ipv6_address = None
                                                        self._segment_path = lambda: "source"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source, ['ipv4_address', 'ipv6_address'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer.Source']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.ActivePeer']['meta_info']


                                            class SiaPeer(_Entity_):
                                                """
                                                SIA Peers yet to respond
                                                
                                                .. attribute:: source
                                                
                                                	Peer Address
                                                	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: peer_available
                                                
                                                	Peer available
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interface_list
                                                
                                                	Interface name
                                                	**type**\: str
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: handle_number
                                                
                                                	Handle number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer, self).__init__()

                                                    self.yang_name = "sia-peer"
                                                    self.yang_parent_name = "topology-route"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("source", ("source", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source))])
                                                    self._leafs = OrderedDict([
                                                        ('peer_available', (YLeaf(YType.boolean, 'peer-available'), ['bool'])),
                                                        ('interface_list', (YLeaf(YType.str, 'interface-list'), ['str'])),
                                                        ('handle_number', (YLeaf(YType.uint32, 'handle-number'), ['int'])),
                                                    ])
                                                    self.peer_available = None
                                                    self.interface_list = None
                                                    self.handle_number = None

                                                    self.source = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source()
                                                    self.source.parent = self
                                                    self._children_name_map["source"] = "source"
                                                    self._segment_path = lambda: "sia-peer"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer, ['peer_available', 'interface_list', 'handle_number'], name, value)


                                                class Source(_Entity_):
                                                    """
                                                    Peer Address
                                                    
                                                    .. attribute:: ipv4_address
                                                    
                                                    	IPv4 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ipv6_address
                                                    
                                                    	IPv6 Address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'eigrp-oper'
                                                    _revision = '2018-04-05'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source, self).__init__()

                                                        self.yang_name = "source"
                                                        self.yang_parent_name = "sia-peer"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                        ])
                                                        self.ipv4_address = None
                                                        self.ipv6_address = None
                                                        self._segment_path = lambda: "source"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source, ['ipv4_address', 'ipv6_address'], name, value)

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer.Source']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute.SiaPeer']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes.TopologyRoute']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.TopologyRoutes']['meta_info']


                                    class EigrpAccounting(_Entity_):
                                        """
                                        Accounting info for one VRF AF
                                        
                                        .. attribute:: afi
                                        
                                        	AFI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_number
                                        
                                        	AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: router_id
                                        
                                        	Router ID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregate_count
                                        
                                        	Number of aggregates
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: state
                                        
                                        	Redist state
                                        	**type**\: int
                                        
                                        	**range:** \-128..127
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: redist_prefix_count
                                        
                                        	Redist prefix count
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: restart_count
                                        
                                        	Restart count
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: time_left
                                        
                                        	Time left
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: redist_prefix_present
                                        
                                        	Are there redist'ed prefixes ?
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: peer_statistics
                                        
                                        	Peers and their status
                                        	**type**\: list of  		 :py:class:`PeerStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting, self).__init__()

                                            self.yang_name = "eigrp-accounting"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("peer-statistics", ("peer_statistics", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics))])
                                            self._leafs = OrderedDict([
                                                ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                                ('aggregate_count', (YLeaf(YType.uint32, 'aggregate-count'), ['int'])),
                                                ('state', (YLeaf(YType.int8, 'state'), ['int'])),
                                                ('redist_prefix_count', (YLeaf(YType.uint32, 'redist-prefix-count'), ['int'])),
                                                ('restart_count', (YLeaf(YType.uint32, 'restart-count'), ['int'])),
                                                ('time_left', (YLeaf(YType.uint32, 'time-left'), ['int'])),
                                                ('redist_prefix_present', (YLeaf(YType.boolean, 'redist-prefix-present'), ['bool'])),
                                            ])
                                            self.afi = None
                                            self.as_number = None
                                            self.router_id = None
                                            self.aggregate_count = None
                                            self.state = None
                                            self.redist_prefix_count = None
                                            self.restart_count = None
                                            self.time_left = None
                                            self.redist_prefix_present = None

                                            self.peer_statistics = YList(self)
                                            self._segment_path = lambda: "eigrp-accounting"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting, ['afi', 'as_number', 'router_id', 'aggregate_count', 'state', 'redist_prefix_count', 'restart_count', 'time_left', 'redist_prefix_present'], name, value)


                                        class PeerStatistics(_Entity_):
                                            """
                                            Peers and their status
                                            
                                            .. attribute:: source
                                            
                                            	Source address
                                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: state
                                            
                                            	State
                                            	**type**\: int
                                            
                                            	**range:** \-128..127
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_list
                                            
                                            	Interface name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: peer_prefix_count
                                            
                                            	Peer prefix count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: restart_count
                                            
                                            	Restart count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: time_left
                                            
                                            	Time left
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics, self).__init__()

                                                self.yang_name = "peer-statistics"
                                                self.yang_parent_name = "eigrp-accounting"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("source", ("source", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source))])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                    ('state', (YLeaf(YType.int8, 'state'), ['int'])),
                                                    ('interface_list', (YLeaf(YType.str, 'interface-list'), ['str'])),
                                                    ('peer_prefix_count', (YLeaf(YType.uint32, 'peer-prefix-count'), ['int'])),
                                                    ('restart_count', (YLeaf(YType.uint32, 'restart-count'), ['int'])),
                                                    ('time_left', (YLeaf(YType.uint32, 'time-left'), ['int'])),
                                                ])
                                                self.afi = None
                                                self.state = None
                                                self.interface_list = None
                                                self.peer_prefix_count = None
                                                self.restart_count = None
                                                self.time_left = None

                                                self.source = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source()
                                                self.source.parent = self
                                                self._children_name_map["source"] = "source"
                                                self._segment_path = lambda: "peer-statistics"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics, ['afi', 'state', 'interface_list', 'peer_prefix_count', 'restart_count', 'time_left'], name, value)


                                            class Source(_Entity_):
                                                """
                                                Source address
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 Address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 Address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source, self).__init__()

                                                    self.yang_name = "source"
                                                    self.yang_parent_name = "peer-statistics"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "source"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source, ['ipv4_address', 'ipv6_address'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics.Source']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting.PeerStatistics']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpAccounting']['meta_info']


                                    class EigrpTraffic(_Entity_):
                                        """
                                        Traffic info for one VRF AF
                                        
                                        .. attribute:: afi
                                        
                                        	AFI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_number
                                        
                                        	AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hellos_sent
                                        
                                        	Hellos sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: hellos_received
                                        
                                        	Hellos received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: updates_sent
                                        
                                        	Updates sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: updates_received
                                        
                                        	Updates received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: queries_sent
                                        
                                        	Queries sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: queries_received
                                        
                                        	Queries received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: replies_sent
                                        
                                        	Replies sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: replies_received
                                        
                                        	Replies received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: acks_sent
                                        
                                        	Acks sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: acks_received
                                        
                                        	Acks received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sia_queries_sent
                                        
                                        	SIA Queries sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sia_queries_received
                                        
                                        	SIA Queries received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sia_replies_sent
                                        
                                        	SIA Replies sent
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sia_replies_received
                                        
                                        	SIA Replies received
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: max_queue_depth
                                        
                                        	Maximum queue depth
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: queue_drops
                                        
                                        	Queue drops
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic, self).__init__()

                                            self.yang_name = "eigrp-traffic"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                ('hellos_sent', (YLeaf(YType.uint32, 'hellos-sent'), ['int'])),
                                                ('hellos_received', (YLeaf(YType.uint32, 'hellos-received'), ['int'])),
                                                ('updates_sent', (YLeaf(YType.uint32, 'updates-sent'), ['int'])),
                                                ('updates_received', (YLeaf(YType.uint32, 'updates-received'), ['int'])),
                                                ('queries_sent', (YLeaf(YType.uint32, 'queries-sent'), ['int'])),
                                                ('queries_received', (YLeaf(YType.uint32, 'queries-received'), ['int'])),
                                                ('replies_sent', (YLeaf(YType.uint32, 'replies-sent'), ['int'])),
                                                ('replies_received', (YLeaf(YType.uint32, 'replies-received'), ['int'])),
                                                ('acks_sent', (YLeaf(YType.uint32, 'acks-sent'), ['int'])),
                                                ('acks_received', (YLeaf(YType.uint32, 'acks-received'), ['int'])),
                                                ('sia_queries_sent', (YLeaf(YType.uint32, 'sia-queries-sent'), ['int'])),
                                                ('sia_queries_received', (YLeaf(YType.uint32, 'sia-queries-received'), ['int'])),
                                                ('sia_replies_sent', (YLeaf(YType.uint32, 'sia-replies-sent'), ['int'])),
                                                ('sia_replies_received', (YLeaf(YType.uint32, 'sia-replies-received'), ['int'])),
                                                ('max_queue_depth', (YLeaf(YType.uint32, 'max-queue-depth'), ['int'])),
                                                ('queue_drops', (YLeaf(YType.uint32, 'queue-drops'), ['int'])),
                                            ])
                                            self.afi = None
                                            self.as_number = None
                                            self.hellos_sent = None
                                            self.hellos_received = None
                                            self.updates_sent = None
                                            self.updates_received = None
                                            self.queries_sent = None
                                            self.queries_received = None
                                            self.replies_sent = None
                                            self.replies_received = None
                                            self.acks_sent = None
                                            self.acks_received = None
                                            self.sia_queries_sent = None
                                            self.sia_queries_received = None
                                            self.sia_replies_sent = None
                                            self.sia_replies_received = None
                                            self.max_queue_depth = None
                                            self.queue_drops = None
                                            self._segment_path = lambda: "eigrp-traffic"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic, ['afi', 'as_number', 'hellos_sent', 'hellos_received', 'updates_sent', 'updates_received', 'queries_sent', 'queries_received', 'replies_sent', 'replies_received', 'acks_sent', 'acks_received', 'sia_queries_sent', 'sia_queries_received', 'sia_replies_sent', 'sia_replies_received', 'max_queue_depth', 'queue_drops'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTraffic']['meta_info']


                                    class EigrpTopologySummary(_Entity_):
                                        """
                                        Topology summary info for one VRF AF
                                        
                                        .. attribute:: afi
                                        
                                        	AFI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_number
                                        
                                        	AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: router_id
                                        
                                        	Router ID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: thread_present
                                        
                                        	Is thread present ?
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: transmit_serial_number
                                        
                                        	Thread serial number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: next_serial_number
                                        
                                        	Next serial number
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: route_count
                                        
                                        	Number of routes
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_count
                                        
                                        	Number of paths
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: dummy_count
                                        
                                        	Dummy count
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ddb_name
                                        
                                        	DDB Name
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: interface_count
                                        
                                        	Number of interfaces
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: handles_used
                                        
                                        	Number of handles used
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: active_interface_count
                                        
                                        	Number of active interfaces
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: quiescent
                                        
                                        	Quiescent interfaces
                                        	**type**\: list of  		 :py:class:`Quiescent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary.Quiescent>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary, self).__init__()

                                            self.yang_name = "eigrp-topology-summary"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("quiescent", ("quiescent", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary.Quiescent))])
                                            self._leafs = OrderedDict([
                                                ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                                ('thread_present', (YLeaf(YType.boolean, 'thread-present'), ['bool'])),
                                                ('transmit_serial_number', (YLeaf(YType.uint64, 'transmit-serial-number'), ['int'])),
                                                ('next_serial_number', (YLeaf(YType.uint64, 'next-serial-number'), ['int'])),
                                                ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                                                ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                                                ('dummy_count', (YLeaf(YType.uint32, 'dummy-count'), ['int'])),
                                                ('ddb_name', (YLeaf(YType.str, 'ddb-name'), ['str'])),
                                                ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                                                ('handles_used', (YLeaf(YType.uint32, 'handles-used'), ['int'])),
                                                ('active_interface_count', (YLeaf(YType.uint32, 'active-interface-count'), ['int'])),
                                            ])
                                            self.afi = None
                                            self.as_number = None
                                            self.router_id = None
                                            self.thread_present = None
                                            self.transmit_serial_number = None
                                            self.next_serial_number = None
                                            self.route_count = None
                                            self.path_count = None
                                            self.dummy_count = None
                                            self.ddb_name = None
                                            self.interface_count = None
                                            self.handles_used = None
                                            self.active_interface_count = None

                                            self.quiescent = YList(self)
                                            self._segment_path = lambda: "eigrp-topology-summary"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary, ['afi', 'as_number', 'router_id', 'thread_present', 'transmit_serial_number', 'next_serial_number', 'route_count', 'path_count', 'dummy_count', 'ddb_name', 'interface_count', 'handles_used', 'active_interface_count'], name, value)


                                        class Quiescent(_Entity_):
                                            """
                                            Quiescent interfaces
                                            
                                            .. attribute:: quiescent_interface_list
                                            
                                            	Interface Name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary.Quiescent, self).__init__()

                                                self.yang_name = "quiescent"
                                                self.yang_parent_name = "eigrp-topology-summary"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('quiescent_interface_list', (YLeaf(YType.str, 'quiescent-interface-list'), ['str'])),
                                                ])
                                                self.quiescent_interface_list = None
                                                self._segment_path = lambda: "quiescent"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary.Quiescent, ['quiescent_interface_list'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary.Quiescent']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpTopologySummary']['meta_info']


                                    class Interfaces(_Entity_):
                                        """
                                        EIGRP interfaces
                                        
                                        .. attribute:: interface
                                        
                                        	Information for an EIGRP interface
                                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces, self).__init__()

                                            self.yang_name = "interfaces"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface", ("interface", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface))])
                                            self._leafs = OrderedDict()

                                            self.interface = YList(self)
                                            self._segment_path = lambda: "interfaces"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces, [], name, value)


                                        class Interface(_Entity_):
                                            """
                                            Information for an EIGRP interface
                                            
                                            .. attribute:: interface_name  (key)
                                            
                                            	Interface Name
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as_number
                                            
                                            	AS Number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: peer_count
                                            
                                            	Peer Count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: classic_peer_count
                                            
                                            	Classic Peer Count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: wide_peer_count
                                            
                                            	Wide Peer Count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unreliable_transmits
                                            
                                            	Unreliable transmissions
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reliable_transmits
                                            
                                            	Reliable transmissions
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: total_srtt
                                            
                                            	Total SRTT
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unreliable_send_interval
                                            
                                            	Send interval for Unreliable transmissions
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reliable_send_interval
                                            
                                            	Send interval for Reliable transmissions
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: last_mc_flow_delay
                                            
                                            	Last multicast flow delay
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pending_routes
                                            
                                            	Number of pending routes
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hello_interval
                                            
                                            	Hello interval
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: holdtime
                                            
                                            	Hold time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bfd_enabled
                                            
                                            	BFD enabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bfd_interval
                                            
                                            	BFD interval
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bfd_multiplier
                                            
                                            	BFD multiplier
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: serial_number_present
                                            
                                            	Is serno present
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: transmit_serial_number
                                            
                                            	Thread serial number
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: packetize_pending
                                            
                                            	Packetize Timer pending
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unreliable_multicast_sent
                                            
                                            	Unreliable multicasts sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reliable_multicast_sent
                                            
                                            	Reliable multicasts sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unreliable_unicast_sent
                                            
                                            	Unreliable unicasts sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reliable_unicast_sent
                                            
                                            	Reliable unicasts sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: multicast_exceptions_sent
                                            
                                            	Multicast Exceptions sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: cr_packets_sent
                                            
                                            	CR packets sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: acks_suppressed
                                            
                                            	Suppressed Acks
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: retransmissions_sent
                                            
                                            	Retransmissions sent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: out_of_sequence_received
                                            
                                            	Out\-of\-sequence received
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stub_interface
                                            
                                            	All stub peers
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: next_hop_self_enabled
                                            
                                            	Next\-hop\-self enabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: split_horizon_enabled
                                            
                                            	SplitHorizon enabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: passive_interface
                                            
                                            	Interface is passive
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bandwidth_percent
                                            
                                            	Bandwidth percent
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            	**units**\: percentage
                                            
                                            .. attribute:: site_of_origin_type
                                            
                                            	Site of Origin Type
                                            	**type**\:  :py:class:`EigrpBdSoo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdSoo>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: site_of_origin
                                            
                                            	Site of Origin
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: auth_mode
                                            
                                            	Authentication Mode
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: auth_keychain
                                            
                                            	Authentication Keychain Name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: auth_key_exists
                                            
                                            	Authentication key exists
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: auth_key_md5
                                            
                                            	Authentication key programmed with MD5 algorithm
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: auth_key_id
                                            
                                            	Current active Authentication Key Id
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: total_pkt_recvd
                                            
                                            	Total packets received
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pkt_drop_wrong_kc
                                            
                                            	Packets dropped due to wrong keychain configured
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pkt_drop_no_auth
                                            
                                            	Packets dropped due to missing authentication data
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pkt_drop_invalid_auth
                                            
                                            	Packets dropped due to invalid authentication data
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: pkt_accepted_valid_auth
                                            
                                            	Packets accepted with valid authentication data
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bandwidth
                                            
                                            	Deprecated. Please migrate to use Bandwidth64
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bandwidth64
                                            
                                            	Bandwidth
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: delay
                                            
                                            	Deprecated. Please migrate to use Delay64. The value of this object might wrap if it is in picosecond units
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: delay64
                                            
                                            	Delay
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: delay_unit
                                            
                                            	Delay unit
                                            	**type**\:  :py:class:`EigrpBdDelayUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdDelayUnit>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reliability
                                            
                                            	Reliability
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: load
                                            
                                            	Load
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: mtu
                                            
                                            	MTU
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_bandwidth
                                            
                                            	Deprecated. Please migrate to use ConfiguredBandwidth64
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_bandwidth64
                                            
                                            	Configured bandwidth
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_delay
                                            
                                            	Deprecated. Please migrate to use ConfiguredDelay64. The value of this object might wrap if it is in picosecond units
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_delay64
                                            
                                            	Configured delay
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_delay_unit
                                            
                                            	Configured delay unit
                                            	**type**\:  :py:class:`EigrpBdDelayUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.EigrpBdDelayUnit>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_reliability
                                            
                                            	Configured reliability
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_load
                                            
                                            	Configured load
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_bandwidth_flag
                                            
                                            	Bandwidth configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_delay_flag
                                            
                                            	Delay configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_reliability_flag
                                            
                                            	Reliability configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_load_flag
                                            
                                            	Load configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: up
                                            
                                            	Interface is UP
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: type_supported
                                            
                                            	Interface type is supported
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ital_record_found
                                            
                                            	ITAL Record valid
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured
                                            
                                            	Interface config exists
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: multicast_enabled
                                            
                                            	Requested socket state
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: socket_setup
                                            
                                            	Setup socket state
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: lpts_socket_setup
                                            
                                            	Setup LPTS socket state
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: primary_ipv4_address
                                            
                                            	Primary IPv4 Address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_link_local_addr
                                            
                                            	IPv6 LL Address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: primary_prefix_length
                                            
                                            	Primary prefix length
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_handle
                                            
                                            	Interface Handle
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_type
                                            
                                            	IM Interface Type
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: configured_items
                                            
                                            	Interface Configured Items
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_passive_enabled
                                            
                                            	Passive\-Interface configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_passive_disabled
                                            
                                            	Passive\-Interface disabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: static_neighbor
                                            
                                            	Static Neighbors
                                            	**type**\: list of  		 :py:class:`StaticNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface.StaticNeighbor>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface, self).__init__()

                                                self.yang_name = "interface"
                                                self.yang_parent_name = "interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['interface_name']
                                                self._child_classes = OrderedDict([("static-neighbor", ("static_neighbor", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface.StaticNeighbor))])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                    ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                    ('peer_count', (YLeaf(YType.uint32, 'peer-count'), ['int'])),
                                                    ('classic_peer_count', (YLeaf(YType.uint32, 'classic-peer-count'), ['int'])),
                                                    ('wide_peer_count', (YLeaf(YType.uint32, 'wide-peer-count'), ['int'])),
                                                    ('unreliable_transmits', (YLeaf(YType.uint32, 'unreliable-transmits'), ['int'])),
                                                    ('reliable_transmits', (YLeaf(YType.uint32, 'reliable-transmits'), ['int'])),
                                                    ('total_srtt', (YLeaf(YType.uint32, 'total-srtt'), ['int'])),
                                                    ('unreliable_send_interval', (YLeaf(YType.uint32, 'unreliable-send-interval'), ['int'])),
                                                    ('reliable_send_interval', (YLeaf(YType.uint32, 'reliable-send-interval'), ['int'])),
                                                    ('last_mc_flow_delay', (YLeaf(YType.uint32, 'last-mc-flow-delay'), ['int'])),
                                                    ('pending_routes', (YLeaf(YType.uint32, 'pending-routes'), ['int'])),
                                                    ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                                                    ('holdtime', (YLeaf(YType.uint32, 'holdtime'), ['int'])),
                                                    ('bfd_enabled', (YLeaf(YType.boolean, 'bfd-enabled'), ['bool'])),
                                                    ('bfd_interval', (YLeaf(YType.uint32, 'bfd-interval'), ['int'])),
                                                    ('bfd_multiplier', (YLeaf(YType.uint32, 'bfd-multiplier'), ['int'])),
                                                    ('serial_number_present', (YLeaf(YType.boolean, 'serial-number-present'), ['bool'])),
                                                    ('transmit_serial_number', (YLeaf(YType.uint64, 'transmit-serial-number'), ['int'])),
                                                    ('packetize_pending', (YLeaf(YType.boolean, 'packetize-pending'), ['bool'])),
                                                    ('unreliable_multicast_sent', (YLeaf(YType.uint32, 'unreliable-multicast-sent'), ['int'])),
                                                    ('reliable_multicast_sent', (YLeaf(YType.uint32, 'reliable-multicast-sent'), ['int'])),
                                                    ('unreliable_unicast_sent', (YLeaf(YType.uint32, 'unreliable-unicast-sent'), ['int'])),
                                                    ('reliable_unicast_sent', (YLeaf(YType.uint32, 'reliable-unicast-sent'), ['int'])),
                                                    ('multicast_exceptions_sent', (YLeaf(YType.uint32, 'multicast-exceptions-sent'), ['int'])),
                                                    ('cr_packets_sent', (YLeaf(YType.uint32, 'cr-packets-sent'), ['int'])),
                                                    ('acks_suppressed', (YLeaf(YType.uint32, 'acks-suppressed'), ['int'])),
                                                    ('retransmissions_sent', (YLeaf(YType.uint32, 'retransmissions-sent'), ['int'])),
                                                    ('out_of_sequence_received', (YLeaf(YType.uint32, 'out-of-sequence-received'), ['int'])),
                                                    ('stub_interface', (YLeaf(YType.boolean, 'stub-interface'), ['bool'])),
                                                    ('next_hop_self_enabled', (YLeaf(YType.boolean, 'next-hop-self-enabled'), ['bool'])),
                                                    ('split_horizon_enabled', (YLeaf(YType.boolean, 'split-horizon-enabled'), ['bool'])),
                                                    ('passive_interface', (YLeaf(YType.boolean, 'passive-interface'), ['bool'])),
                                                    ('bandwidth_percent', (YLeaf(YType.uint32, 'bandwidth-percent'), ['int'])),
                                                    ('site_of_origin_type', (YLeaf(YType.enumeration, 'site-of-origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdSoo', '')])),
                                                    ('site_of_origin', (YLeaf(YType.str, 'site-of-origin'), ['str'])),
                                                    ('auth_mode', (YLeaf(YType.uint32, 'auth-mode'), ['int'])),
                                                    ('auth_keychain', (YLeaf(YType.str, 'auth-keychain'), ['str'])),
                                                    ('auth_key_exists', (YLeaf(YType.boolean, 'auth-key-exists'), ['bool'])),
                                                    ('auth_key_md5', (YLeaf(YType.boolean, 'auth-key-md5'), ['bool'])),
                                                    ('auth_key_id', (YLeaf(YType.uint64, 'auth-key-id'), ['int'])),
                                                    ('total_pkt_recvd', (YLeaf(YType.uint32, 'total-pkt-recvd'), ['int'])),
                                                    ('pkt_drop_wrong_kc', (YLeaf(YType.uint32, 'pkt-drop-wrong-kc'), ['int'])),
                                                    ('pkt_drop_no_auth', (YLeaf(YType.uint32, 'pkt-drop-no-auth'), ['int'])),
                                                    ('pkt_drop_invalid_auth', (YLeaf(YType.uint32, 'pkt-drop-invalid-auth'), ['int'])),
                                                    ('pkt_accepted_valid_auth', (YLeaf(YType.uint32, 'pkt-accepted-valid-auth'), ['int'])),
                                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                                    ('bandwidth64', (YLeaf(YType.uint64, 'bandwidth64'), ['int'])),
                                                    ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                                    ('delay64', (YLeaf(YType.uint64, 'delay64'), ['int'])),
                                                    ('delay_unit', (YLeaf(YType.enumeration, 'delay-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdDelayUnit', '')])),
                                                    ('reliability', (YLeaf(YType.uint32, 'reliability'), ['int'])),
                                                    ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                                                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                                    ('configured_bandwidth', (YLeaf(YType.uint32, 'configured-bandwidth'), ['int'])),
                                                    ('configured_bandwidth64', (YLeaf(YType.uint64, 'configured-bandwidth64'), ['int'])),
                                                    ('configured_delay', (YLeaf(YType.uint32, 'configured-delay'), ['int'])),
                                                    ('configured_delay64', (YLeaf(YType.uint64, 'configured-delay64'), ['int'])),
                                                    ('configured_delay_unit', (YLeaf(YType.enumeration, 'configured-delay-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper', 'EigrpBdDelayUnit', '')])),
                                                    ('configured_reliability', (YLeaf(YType.uint32, 'configured-reliability'), ['int'])),
                                                    ('configured_load', (YLeaf(YType.uint32, 'configured-load'), ['int'])),
                                                    ('configured_bandwidth_flag', (YLeaf(YType.boolean, 'configured-bandwidth-flag'), ['bool'])),
                                                    ('configured_delay_flag', (YLeaf(YType.boolean, 'configured-delay-flag'), ['bool'])),
                                                    ('configured_reliability_flag', (YLeaf(YType.boolean, 'configured-reliability-flag'), ['bool'])),
                                                    ('configured_load_flag', (YLeaf(YType.boolean, 'configured-load-flag'), ['bool'])),
                                                    ('up', (YLeaf(YType.boolean, 'up'), ['bool'])),
                                                    ('type_supported', (YLeaf(YType.boolean, 'type-supported'), ['bool'])),
                                                    ('ital_record_found', (YLeaf(YType.boolean, 'ital-record-found'), ['bool'])),
                                                    ('configured', (YLeaf(YType.boolean, 'configured'), ['bool'])),
                                                    ('multicast_enabled', (YLeaf(YType.boolean, 'multicast-enabled'), ['bool'])),
                                                    ('socket_setup', (YLeaf(YType.boolean, 'socket-setup'), ['bool'])),
                                                    ('lpts_socket_setup', (YLeaf(YType.boolean, 'lpts-socket-setup'), ['bool'])),
                                                    ('primary_ipv4_address', (YLeaf(YType.str, 'primary-ipv4-address'), ['str'])),
                                                    ('ipv6_link_local_addr', (YLeaf(YType.str, 'ipv6-link-local-addr'), ['str'])),
                                                    ('primary_prefix_length', (YLeaf(YType.uint32, 'primary-prefix-length'), ['int'])),
                                                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                                    ('interface_type', (YLeaf(YType.uint32, 'interface-type'), ['int'])),
                                                    ('configured_items', (YLeaf(YType.uint32, 'configured-items'), ['int'])),
                                                    ('is_passive_enabled', (YLeaf(YType.boolean, 'is-passive-enabled'), ['bool'])),
                                                    ('is_passive_disabled', (YLeaf(YType.boolean, 'is-passive-disabled'), ['bool'])),
                                                ])
                                                self.interface_name = None
                                                self.afi = None
                                                self.as_number = None
                                                self.peer_count = None
                                                self.classic_peer_count = None
                                                self.wide_peer_count = None
                                                self.unreliable_transmits = None
                                                self.reliable_transmits = None
                                                self.total_srtt = None
                                                self.unreliable_send_interval = None
                                                self.reliable_send_interval = None
                                                self.last_mc_flow_delay = None
                                                self.pending_routes = None
                                                self.hello_interval = None
                                                self.holdtime = None
                                                self.bfd_enabled = None
                                                self.bfd_interval = None
                                                self.bfd_multiplier = None
                                                self.serial_number_present = None
                                                self.transmit_serial_number = None
                                                self.packetize_pending = None
                                                self.unreliable_multicast_sent = None
                                                self.reliable_multicast_sent = None
                                                self.unreliable_unicast_sent = None
                                                self.reliable_unicast_sent = None
                                                self.multicast_exceptions_sent = None
                                                self.cr_packets_sent = None
                                                self.acks_suppressed = None
                                                self.retransmissions_sent = None
                                                self.out_of_sequence_received = None
                                                self.stub_interface = None
                                                self.next_hop_self_enabled = None
                                                self.split_horizon_enabled = None
                                                self.passive_interface = None
                                                self.bandwidth_percent = None
                                                self.site_of_origin_type = None
                                                self.site_of_origin = None
                                                self.auth_mode = None
                                                self.auth_keychain = None
                                                self.auth_key_exists = None
                                                self.auth_key_md5 = None
                                                self.auth_key_id = None
                                                self.total_pkt_recvd = None
                                                self.pkt_drop_wrong_kc = None
                                                self.pkt_drop_no_auth = None
                                                self.pkt_drop_invalid_auth = None
                                                self.pkt_accepted_valid_auth = None
                                                self.bandwidth = None
                                                self.bandwidth64 = None
                                                self.delay = None
                                                self.delay64 = None
                                                self.delay_unit = None
                                                self.reliability = None
                                                self.load = None
                                                self.mtu = None
                                                self.configured_bandwidth = None
                                                self.configured_bandwidth64 = None
                                                self.configured_delay = None
                                                self.configured_delay64 = None
                                                self.configured_delay_unit = None
                                                self.configured_reliability = None
                                                self.configured_load = None
                                                self.configured_bandwidth_flag = None
                                                self.configured_delay_flag = None
                                                self.configured_reliability_flag = None
                                                self.configured_load_flag = None
                                                self.up = None
                                                self.type_supported = None
                                                self.ital_record_found = None
                                                self.configured = None
                                                self.multicast_enabled = None
                                                self.socket_setup = None
                                                self.lpts_socket_setup = None
                                                self.primary_ipv4_address = None
                                                self.ipv6_link_local_addr = None
                                                self.primary_prefix_length = None
                                                self.interface_handle = None
                                                self.interface_type = None
                                                self.configured_items = None
                                                self.is_passive_enabled = None
                                                self.is_passive_disabled = None

                                                self.static_neighbor = YList(self)
                                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface, ['interface_name', 'afi', 'as_number', 'peer_count', 'classic_peer_count', 'wide_peer_count', 'unreliable_transmits', 'reliable_transmits', 'total_srtt', 'unreliable_send_interval', 'reliable_send_interval', 'last_mc_flow_delay', 'pending_routes', 'hello_interval', 'holdtime', 'bfd_enabled', 'bfd_interval', 'bfd_multiplier', 'serial_number_present', 'transmit_serial_number', 'packetize_pending', 'unreliable_multicast_sent', 'reliable_multicast_sent', 'unreliable_unicast_sent', 'reliable_unicast_sent', 'multicast_exceptions_sent', 'cr_packets_sent', 'acks_suppressed', 'retransmissions_sent', 'out_of_sequence_received', 'stub_interface', 'next_hop_self_enabled', 'split_horizon_enabled', 'passive_interface', 'bandwidth_percent', 'site_of_origin_type', 'site_of_origin', 'auth_mode', 'auth_keychain', 'auth_key_exists', 'auth_key_md5', 'auth_key_id', 'total_pkt_recvd', 'pkt_drop_wrong_kc', 'pkt_drop_no_auth', 'pkt_drop_invalid_auth', 'pkt_accepted_valid_auth', 'bandwidth', 'bandwidth64', 'delay', 'delay64', 'delay_unit', 'reliability', 'load', 'mtu', 'configured_bandwidth', 'configured_bandwidth64', 'configured_delay', 'configured_delay64', 'configured_delay_unit', 'configured_reliability', 'configured_load', 'configured_bandwidth_flag', 'configured_delay_flag', 'configured_reliability_flag', 'configured_load_flag', 'up', 'type_supported', 'ital_record_found', 'configured', 'multicast_enabled', 'socket_setup', 'lpts_socket_setup', 'primary_ipv4_address', 'ipv6_link_local_addr', 'primary_prefix_length', 'interface_handle', 'interface_type', 'configured_items', 'is_passive_enabled', 'is_passive_disabled'], name, value)


                                            class StaticNeighbor(_Entity_):
                                                """
                                                Static Neighbors
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 Address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 Address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface.StaticNeighbor, self).__init__()

                                                    self.yang_name = "static-neighbor"
                                                    self.yang_parent_name = "interface"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "static-neighbor"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface.StaticNeighbor, ['ipv4_address', 'ipv6_address'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface.StaticNeighbor']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces.Interface']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Interfaces']['meta_info']


                                    class EigrpEvents(_Entity_):
                                        """
                                        Events for a specific VRF AF
                                        
                                        .. attribute:: afi
                                        
                                        	AFI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_number
                                        
                                        	AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: current_event_index
                                        
                                        	Current event
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: eigrp_start_absolute_seconds
                                        
                                        	Seconds since EIGRP started (absolute)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: eigrp_start_absolute_nanoseconds
                                        
                                        	Seconds since EIGRP started (absolute)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: eigrp_start_relative_seconds
                                        
                                        	Seconds since EIGRP started (relative)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: eigrp_start_relative_nanoseconds
                                        
                                        	Seconds since EIGRP started (relative)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents, self).__init__()

                                            self.yang_name = "eigrp-events"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                ('current_event_index', (YLeaf(YType.uint32, 'current-event-index'), ['int'])),
                                                ('eigrp_start_absolute_seconds', (YLeaf(YType.uint32, 'eigrp-start-absolute-seconds'), ['int'])),
                                                ('eigrp_start_absolute_nanoseconds', (YLeaf(YType.uint32, 'eigrp-start-absolute-nanoseconds'), ['int'])),
                                                ('eigrp_start_relative_seconds', (YLeaf(YType.uint32, 'eigrp-start-relative-seconds'), ['int'])),
                                                ('eigrp_start_relative_nanoseconds', (YLeaf(YType.uint32, 'eigrp-start-relative-nanoseconds'), ['int'])),
                                            ])
                                            self.afi = None
                                            self.as_number = None
                                            self.current_event_index = None
                                            self.eigrp_start_absolute_seconds = None
                                            self.eigrp_start_absolute_nanoseconds = None
                                            self.eigrp_start_relative_seconds = None
                                            self.eigrp_start_relative_nanoseconds = None
                                            self._segment_path = lambda: "eigrp-events"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents, ['afi', 'as_number', 'current_event_index', 'eigrp_start_absolute_seconds', 'eigrp_start_absolute_nanoseconds', 'eigrp_start_relative_seconds', 'eigrp_start_relative_nanoseconds'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpEvents']['meta_info']


                                    class Neighbors(_Entity_):
                                        """
                                        EIGRP neighbors
                                        
                                        .. attribute:: neighbor
                                        
                                        	Information on one EIGRP neighbor
                                        	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors, self).__init__()

                                            self.yang_name = "neighbors"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("neighbor", ("neighbor", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor))])
                                            self._leafs = OrderedDict()

                                            self.neighbor = YList(self)
                                            self._segment_path = lambda: "neighbors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors, [], name, value)


                                        class Neighbor(_Entity_):
                                            """
                                            Information on one EIGRP neighbor
                                            
                                            .. attribute:: neighbor_address  (key)
                                            
                                            	Neighbor Address
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: source
                                            
                                            	Peer address
                                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as_number
                                            
                                            	AS Number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: peer_suspended
                                            
                                            	Is it a suspended peer
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: peer_handle
                                            
                                            	Peer handle
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: interface_list
                                            
                                            	Interface name
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: holdtime
                                            
                                            	Hold time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: uptime
                                            
                                            	UP time (seconds)
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            	**units**\: second
                                            
                                            .. attribute:: srtt
                                            
                                            	Round trip time
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: rto
                                            
                                            	RTO
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: bfd_enabled
                                            
                                            	BFD enabled
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: queue_count
                                            
                                            	Q counts
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: last_sequence_number
                                            
                                            	Last sequence number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: static_neighbor
                                            
                                            	Is it a static neighbor
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: remote_neighbor
                                            
                                            	Is it a remote ucast neighbor
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hop_count
                                            
                                            	Hop count of the static peer
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: restart_configured
                                            
                                            	Is Restart time configured
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: restart_time
                                            
                                            	Restart time (seconds)
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            	**units**\: second
                                            
                                            .. attribute:: last_startup_serial_number
                                            
                                            	Last startup serial number
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ios_major_version
                                            
                                            	IOS Major version
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ios_minor_version
                                            
                                            	IOS Minor version
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: eigrp_major_version
                                            
                                            	EIGRP Major version
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: eigrp_minor_version
                                            
                                            	EIGRP Major version
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: retransmission_count
                                            
                                            	Retransmission count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: retry_count
                                            
                                            	Retry count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: need_init
                                            
                                            	Need EIGRP Init message
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: need_init_ack
                                            
                                            	Need EIGRP InitAck message
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reinitialization_needed
                                            
                                            	Reinitialization needed
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: reinit_start
                                            
                                            	Reinit period
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: peer_prefix_count
                                            
                                            	Prefix count
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stubbed
                                            
                                            	Is it stubbed
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: allow_connected
                                            
                                            	Connected routes accepted
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: allow_static
                                            
                                            	Static routes accepted
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: allow_summaries
                                            
                                            	Summary routes accepted
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: allow_redistributed
                                            
                                            	Redist'ed routes accepted
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: test_handle
                                            
                                            	Test handle flag
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: stubbed_interface
                                            
                                            	Is it stubbed
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: suspended_reset
                                            
                                            	Suspension manually reset
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: suspended_time_left
                                            
                                            	Suspended time left
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: neighbor_queue
                                            
                                            	Neighbor Queue
                                            	**type**\: list of  		 :py:class:`NeighborQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_oper.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.NeighborQueue>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'eigrp-oper'
                                            _revision = '2018-04-05'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor, self).__init__()

                                                self.yang_name = "neighbor"
                                                self.yang_parent_name = "neighbors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['neighbor_address']
                                                self._child_classes = OrderedDict([("source", ("source", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source)), ("neighbor-queue", ("neighbor_queue", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.NeighborQueue))])
                                                self._leafs = OrderedDict([
                                                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                                                    ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                    ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                    ('peer_suspended', (YLeaf(YType.boolean, 'peer-suspended'), ['bool'])),
                                                    ('peer_handle', (YLeaf(YType.uint32, 'peer-handle'), ['int'])),
                                                    ('interface_list', (YLeaf(YType.str, 'interface-list'), ['str'])),
                                                    ('holdtime', (YLeaf(YType.uint32, 'holdtime'), ['int'])),
                                                    ('uptime', (YLeaf(YType.uint32, 'uptime'), ['int'])),
                                                    ('srtt', (YLeaf(YType.uint32, 'srtt'), ['int'])),
                                                    ('rto', (YLeaf(YType.uint32, 'rto'), ['int'])),
                                                    ('bfd_enabled', (YLeaf(YType.boolean, 'bfd-enabled'), ['bool'])),
                                                    ('queue_count', (YLeaf(YType.uint32, 'queue-count'), ['int'])),
                                                    ('last_sequence_number', (YLeaf(YType.uint32, 'last-sequence-number'), ['int'])),
                                                    ('static_neighbor', (YLeaf(YType.boolean, 'static-neighbor'), ['bool'])),
                                                    ('remote_neighbor', (YLeaf(YType.boolean, 'remote-neighbor'), ['bool'])),
                                                    ('hop_count', (YLeaf(YType.uint8, 'hop-count'), ['int'])),
                                                    ('restart_configured', (YLeaf(YType.boolean, 'restart-configured'), ['bool'])),
                                                    ('restart_time', (YLeaf(YType.uint32, 'restart-time'), ['int'])),
                                                    ('last_startup_serial_number', (YLeaf(YType.uint64, 'last-startup-serial-number'), ['int'])),
                                                    ('ios_major_version', (YLeaf(YType.uint8, 'ios-major-version'), ['int'])),
                                                    ('ios_minor_version', (YLeaf(YType.uint8, 'ios-minor-version'), ['int'])),
                                                    ('eigrp_major_version', (YLeaf(YType.uint8, 'eigrp-major-version'), ['int'])),
                                                    ('eigrp_minor_version', (YLeaf(YType.uint8, 'eigrp-minor-version'), ['int'])),
                                                    ('retransmission_count', (YLeaf(YType.uint32, 'retransmission-count'), ['int'])),
                                                    ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                                                    ('need_init', (YLeaf(YType.boolean, 'need-init'), ['bool'])),
                                                    ('need_init_ack', (YLeaf(YType.boolean, 'need-init-ack'), ['bool'])),
                                                    ('reinitialization_needed', (YLeaf(YType.boolean, 'reinitialization-needed'), ['bool'])),
                                                    ('reinit_start', (YLeaf(YType.uint32, 'reinit-start'), ['int'])),
                                                    ('peer_prefix_count', (YLeaf(YType.uint32, 'peer-prefix-count'), ['int'])),
                                                    ('stubbed', (YLeaf(YType.boolean, 'stubbed'), ['bool'])),
                                                    ('allow_connected', (YLeaf(YType.boolean, 'allow-connected'), ['bool'])),
                                                    ('allow_static', (YLeaf(YType.boolean, 'allow-static'), ['bool'])),
                                                    ('allow_summaries', (YLeaf(YType.boolean, 'allow-summaries'), ['bool'])),
                                                    ('allow_redistributed', (YLeaf(YType.boolean, 'allow-redistributed'), ['bool'])),
                                                    ('test_handle', (YLeaf(YType.boolean, 'test-handle'), ['bool'])),
                                                    ('stubbed_interface', (YLeaf(YType.boolean, 'stubbed-interface'), ['bool'])),
                                                    ('suspended_reset', (YLeaf(YType.boolean, 'suspended-reset'), ['bool'])),
                                                    ('suspended_time_left', (YLeaf(YType.uint32, 'suspended-time-left'), ['int'])),
                                                ])
                                                self.neighbor_address = None
                                                self.afi = None
                                                self.as_number = None
                                                self.peer_suspended = None
                                                self.peer_handle = None
                                                self.interface_list = None
                                                self.holdtime = None
                                                self.uptime = None
                                                self.srtt = None
                                                self.rto = None
                                                self.bfd_enabled = None
                                                self.queue_count = None
                                                self.last_sequence_number = None
                                                self.static_neighbor = None
                                                self.remote_neighbor = None
                                                self.hop_count = None
                                                self.restart_configured = None
                                                self.restart_time = None
                                                self.last_startup_serial_number = None
                                                self.ios_major_version = None
                                                self.ios_minor_version = None
                                                self.eigrp_major_version = None
                                                self.eigrp_minor_version = None
                                                self.retransmission_count = None
                                                self.retry_count = None
                                                self.need_init = None
                                                self.need_init_ack = None
                                                self.reinitialization_needed = None
                                                self.reinit_start = None
                                                self.peer_prefix_count = None
                                                self.stubbed = None
                                                self.allow_connected = None
                                                self.allow_static = None
                                                self.allow_summaries = None
                                                self.allow_redistributed = None
                                                self.test_handle = None
                                                self.stubbed_interface = None
                                                self.suspended_reset = None
                                                self.suspended_time_left = None

                                                self.source = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source()
                                                self.source.parent = self
                                                self._children_name_map["source"] = "source"

                                                self.neighbor_queue = YList(self)
                                                self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor, ['neighbor_address', 'afi', 'as_number', 'peer_suspended', 'peer_handle', 'interface_list', 'holdtime', 'uptime', 'srtt', 'rto', 'bfd_enabled', 'queue_count', 'last_sequence_number', 'static_neighbor', 'remote_neighbor', 'hop_count', 'restart_configured', 'restart_time', 'last_startup_serial_number', 'ios_major_version', 'ios_minor_version', 'eigrp_major_version', 'eigrp_minor_version', 'retransmission_count', 'retry_count', 'need_init', 'need_init_ack', 'reinitialization_needed', 'reinit_start', 'peer_prefix_count', 'stubbed', 'allow_connected', 'allow_static', 'allow_summaries', 'allow_redistributed', 'test_handle', 'stubbed_interface', 'suspended_reset', 'suspended_time_left'], name, value)


                                            class Source(_Entity_):
                                                """
                                                Peer address
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 Address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 Address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source, self).__init__()

                                                    self.yang_name = "source"
                                                    self.yang_parent_name = "neighbor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "source"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source, ['ipv4_address', 'ipv6_address'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.Source']['meta_info']


                                            class NeighborQueue(_Entity_):
                                                """
                                                Neighbor Queue
                                                
                                                .. attribute:: operation_code
                                                
                                                	Operation Code
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ack_sequnce_number
                                                
                                                	ACK sequence number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: start_serial_number
                                                
                                                	Starting serial number
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: end_serial_number
                                                
                                                	Ending serial number
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: pregenerated
                                                
                                                	Pregenerated pak
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: packet_length
                                                
                                                	pak len
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: time_sent_flag
                                                
                                                	Has a pak been sent
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: time_sent
                                                
                                                	Time sent
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: init_bit_set
                                                
                                                	Is the init bit set
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: sequenced
                                                
                                                	Is it sequenced
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'eigrp-oper'
                                                _revision = '2018-04-05'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.NeighborQueue, self).__init__()

                                                    self.yang_name = "neighbor-queue"
                                                    self.yang_parent_name = "neighbor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('operation_code', (YLeaf(YType.uint32, 'operation-code'), ['int'])),
                                                        ('ack_sequnce_number', (YLeaf(YType.uint32, 'ack-sequnce-number'), ['int'])),
                                                        ('start_serial_number', (YLeaf(YType.uint64, 'start-serial-number'), ['int'])),
                                                        ('end_serial_number', (YLeaf(YType.uint64, 'end-serial-number'), ['int'])),
                                                        ('pregenerated', (YLeaf(YType.boolean, 'pregenerated'), ['bool'])),
                                                        ('packet_length', (YLeaf(YType.uint32, 'packet-length'), ['int'])),
                                                        ('time_sent_flag', (YLeaf(YType.boolean, 'time-sent-flag'), ['bool'])),
                                                        ('time_sent', (YLeaf(YType.uint32, 'time-sent'), ['int'])),
                                                        ('init_bit_set', (YLeaf(YType.boolean, 'init-bit-set'), ['bool'])),
                                                        ('sequenced', (YLeaf(YType.boolean, 'sequenced'), ['bool'])),
                                                    ])
                                                    self.operation_code = None
                                                    self.ack_sequnce_number = None
                                                    self.start_serial_number = None
                                                    self.end_serial_number = None
                                                    self.pregenerated = None
                                                    self.packet_length = None
                                                    self.time_sent_flag = None
                                                    self.time_sent = None
                                                    self.init_bit_set = None
                                                    self.sequenced = None
                                                    self._segment_path = lambda: "neighbor-queue"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.NeighborQueue, ['operation_code', 'ack_sequnce_number', 'start_serial_number', 'end_serial_number', 'pregenerated', 'packet_length', 'time_sent_flag', 'time_sent', 'init_bit_set', 'sequenced'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor.NeighborQueue']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors.Neighbor']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.Neighbors']['meta_info']


                                    class EigrpStatistics(_Entity_):
                                        """
                                        Statistics for a specific VRF AF
                                        
                                        .. attribute:: afi
                                        
                                        	AFI
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_number
                                        
                                        	AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: configured_interface_count
                                        
                                        	Configured interfaces
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: active_interfaces_count
                                        
                                        	Active interfaces
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: activate_count
                                        
                                        	Activate address family success count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: activate_error
                                        
                                        	Activate address family failure count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: activate_last_error
                                        
                                        	Activate address family last error
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: deactivate_count
                                        
                                        	Deactivate address family success count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: deactivate_error
                                        
                                        	Deactivate address family failure count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: deactivate_last_error
                                        
                                        	Deactivate address family last error
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: socket_set
                                        
                                        	Socket setup success count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: socket_set_error
                                        
                                        	Socket setup failure count
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: sock_set_last_error
                                        
                                        	Socket setup last error
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_in
                                        
                                        	Succeeded RAW packets in
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_in_error
                                        
                                        	Failed RAW packets ln
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_in_last_error
                                        
                                        	RAW packets in last error
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_out
                                        
                                        	Succeeded RAW packets out
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_out_error
                                        
                                        	Failed RAW packets out
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: raw_packet_out_last_error
                                        
                                        	RAW Packets out last error
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'eigrp-oper'
                                        _revision = '2018-04-05'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics, self).__init__()

                                            self.yang_name = "eigrp-statistics"
                                            self.yang_parent_name = "as"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('afi', (YLeaf(YType.uint32, 'afi'), ['int'])),
                                                ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                                ('configured_interface_count', (YLeaf(YType.uint32, 'configured-interface-count'), ['int'])),
                                                ('active_interfaces_count', (YLeaf(YType.uint32, 'active-interfaces-count'), ['int'])),
                                                ('activate_count', (YLeaf(YType.uint64, 'activate-count'), ['int'])),
                                                ('activate_error', (YLeaf(YType.uint64, 'activate-error'), ['int'])),
                                                ('activate_last_error', (YLeaf(YType.int32, 'activate-last-error'), ['int'])),
                                                ('deactivate_count', (YLeaf(YType.uint64, 'deactivate-count'), ['int'])),
                                                ('deactivate_error', (YLeaf(YType.uint64, 'deactivate-error'), ['int'])),
                                                ('deactivate_last_error', (YLeaf(YType.int32, 'deactivate-last-error'), ['int'])),
                                                ('socket_set', (YLeaf(YType.uint64, 'socket-set'), ['int'])),
                                                ('socket_set_error', (YLeaf(YType.uint64, 'socket-set-error'), ['int'])),
                                                ('sock_set_last_error', (YLeaf(YType.int32, 'sock-set-last-error'), ['int'])),
                                                ('raw_packet_in', (YLeaf(YType.uint64, 'raw-packet-in'), ['int'])),
                                                ('raw_packet_in_error', (YLeaf(YType.uint64, 'raw-packet-in-error'), ['int'])),
                                                ('raw_packet_in_last_error', (YLeaf(YType.int32, 'raw-packet-in-last-error'), ['int'])),
                                                ('raw_packet_out', (YLeaf(YType.uint64, 'raw-packet-out'), ['int'])),
                                                ('raw_packet_out_error', (YLeaf(YType.uint64, 'raw-packet-out-error'), ['int'])),
                                                ('raw_packet_out_last_error', (YLeaf(YType.int32, 'raw-packet-out-last-error'), ['int'])),
                                            ])
                                            self.afi = None
                                            self.as_number = None
                                            self.configured_interface_count = None
                                            self.active_interfaces_count = None
                                            self.activate_count = None
                                            self.activate_error = None
                                            self.activate_last_error = None
                                            self.deactivate_count = None
                                            self.deactivate_error = None
                                            self.deactivate_last_error = None
                                            self.socket_set = None
                                            self.socket_set_error = None
                                            self.sock_set_last_error = None
                                            self.raw_packet_in = None
                                            self.raw_packet_in_error = None
                                            self.raw_packet_in_last_error = None
                                            self.raw_packet_out = None
                                            self.raw_packet_out_error = None
                                            self.raw_packet_out_last_error = None
                                            self._segment_path = lambda: "eigrp-statistics"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics, ['afi', 'as_number', 'configured_interface_count', 'active_interfaces_count', 'activate_count', 'activate_error', 'activate_last_error', 'deactivate_count', 'deactivate_error', 'deactivate_last_error', 'socket_set', 'socket_set_error', 'sock_set_last_error', 'raw_packet_in', 'raw_packet_in_error', 'raw_packet_in_last_error', 'raw_packet_out', 'raw_packet_out_error', 'raw_packet_out_last_error'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As.EigrpStatistics']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases.As']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Ases']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                    return meta._meta_table['Eigrp.Processes.Process.Vrfs']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
                return meta._meta_table['Eigrp.Processes.Process']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
            return meta._meta_table['Eigrp.Processes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Eigrp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_oper as meta
        return meta._meta_table['Eigrp']['meta_info']


