""" Cisco_IOS_XR_man_ems_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package operational data.

This module contains definitions
for the following management objects\:
  grpc\: grpc commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Grpc(Entity):
    """
    grpc commands
    
    .. attribute:: statistics
    
    	Grpc Statistics
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper.Grpc.Statistics>`
    
    .. attribute:: status
    
    	Grpc Status
    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper.Grpc.Status>`
    
    

    """

    _prefix = 'man-ems-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Grpc, self).__init__()
        self._top_entity = None

        self.yang_name = "grpc"
        self.yang_parent_name = "Cisco-IOS-XR-man-ems-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("statistics", ("statistics", Grpc.Statistics)), ("status", ("status", Grpc.Status))])
        self._leafs = OrderedDict()

        self.statistics = Grpc.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"

        self.status = Grpc.Status()
        self.status.parent = self
        self._children_name_map["status"] = "status"
        self._segment_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Grpc, [], name, value)


    class Statistics(Entity):
        """
        Grpc Statistics
        
        .. attribute:: ct_show_cmd_txt_req_recv
        
        	CounterShowCmdTxtReqRecv
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_show_cmd_txt_res_sent
        
        	CounterShowCmdTxtResSent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_config_req_recv
        
        	CounterGetConfigReqRecv
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_config_res_sent
        
        	CounterGetConfigResSent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_req_recv
        
        	CounterCliConfigReqRecv
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_res_sent
        
        	CounterCliConfigResSent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_merge_config_req_recv
        
        	CounterMergeConfigReq
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_merge_config_res_sent
        
        	CounterMergeConfigRes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_replace_req_recv
        
        	CounterCommitReplaceReq
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_replace_res_sent
        
        	CounterCommitReplaceRes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_delete_config_req_recv
        
        	CounterDeleteConfigReq
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_delete_config_res_sent
        
        	CounterDeleteConfigRes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_replace_config_req_recv
        
        	CounterReplaceConfigReq
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_replace_config_res_sent
        
        	CounterReplaceConfigSent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_oper_req_recv
        
        	CounterGetOperReqRecv
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_oper_res_sent
        
        	CounterGetOperResSent
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_current_session
        
        	CounterGetCurrentSession
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ct_commit_config_req_recv
        
        	CounterForHowManyCommitConfigRequests
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_config_res_sent
        
        	CounterForHowManyCommitConfigResponses
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_action_json_req_recv
        
        	CounterForHowManyActionJsonRequests
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_action_json_res_sent
        
        	CounterForHowManyActionJsonResponses
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'man-ems-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ct_show_cmd_txt_req_recv', (YLeaf(YType.uint64, 'ct-show-cmd-txt-req-recv'), ['int'])),
                ('ct_show_cmd_txt_res_sent', (YLeaf(YType.uint64, 'ct-show-cmd-txt-res-sent'), ['int'])),
                ('ct_get_config_req_recv', (YLeaf(YType.uint64, 'ct-get-config-req-recv'), ['int'])),
                ('ct_get_config_res_sent', (YLeaf(YType.uint64, 'ct-get-config-res-sent'), ['int'])),
                ('ct_cli_config_req_recv', (YLeaf(YType.uint64, 'ct-cli-config-req-recv'), ['int'])),
                ('ct_cli_config_res_sent', (YLeaf(YType.uint64, 'ct-cli-config-res-sent'), ['int'])),
                ('ct_merge_config_req_recv', (YLeaf(YType.uint64, 'ct-merge-config-req-recv'), ['int'])),
                ('ct_merge_config_res_sent', (YLeaf(YType.uint64, 'ct-merge-config-res-sent'), ['int'])),
                ('ct_commit_replace_req_recv', (YLeaf(YType.uint64, 'ct-commit-replace-req-recv'), ['int'])),
                ('ct_commit_replace_res_sent', (YLeaf(YType.uint64, 'ct-commit-replace-res-sent'), ['int'])),
                ('ct_delete_config_req_recv', (YLeaf(YType.uint64, 'ct-delete-config-req-recv'), ['int'])),
                ('ct_delete_config_res_sent', (YLeaf(YType.uint64, 'ct-delete-config-res-sent'), ['int'])),
                ('ct_replace_config_req_recv', (YLeaf(YType.uint64, 'ct-replace-config-req-recv'), ['int'])),
                ('ct_replace_config_res_sent', (YLeaf(YType.uint64, 'ct-replace-config-res-sent'), ['int'])),
                ('ct_get_oper_req_recv', (YLeaf(YType.uint64, 'ct-get-oper-req-recv'), ['int'])),
                ('ct_get_oper_res_sent', (YLeaf(YType.uint64, 'ct-get-oper-res-sent'), ['int'])),
                ('ct_get_current_session', (YLeaf(YType.uint32, 'ct-get-current-session'), ['int'])),
                ('ct_commit_config_req_recv', (YLeaf(YType.uint64, 'ct-commit-config-req-recv'), ['int'])),
                ('ct_commit_config_res_sent', (YLeaf(YType.uint64, 'ct-commit-config-res-sent'), ['int'])),
                ('ct_action_json_req_recv', (YLeaf(YType.uint64, 'ct-action-json-req-recv'), ['int'])),
                ('ct_action_json_res_sent', (YLeaf(YType.uint64, 'ct-action-json-res-sent'), ['int'])),
            ])
            self.ct_show_cmd_txt_req_recv = None
            self.ct_show_cmd_txt_res_sent = None
            self.ct_get_config_req_recv = None
            self.ct_get_config_res_sent = None
            self.ct_cli_config_req_recv = None
            self.ct_cli_config_res_sent = None
            self.ct_merge_config_req_recv = None
            self.ct_merge_config_res_sent = None
            self.ct_commit_replace_req_recv = None
            self.ct_commit_replace_res_sent = None
            self.ct_delete_config_req_recv = None
            self.ct_delete_config_res_sent = None
            self.ct_replace_config_req_recv = None
            self.ct_replace_config_res_sent = None
            self.ct_get_oper_req_recv = None
            self.ct_get_oper_res_sent = None
            self.ct_get_current_session = None
            self.ct_commit_config_req_recv = None
            self.ct_commit_config_res_sent = None
            self.ct_action_json_req_recv = None
            self.ct_action_json_res_sent = None
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.Statistics, ['ct_show_cmd_txt_req_recv', 'ct_show_cmd_txt_res_sent', 'ct_get_config_req_recv', 'ct_get_config_res_sent', 'ct_cli_config_req_recv', 'ct_cli_config_res_sent', 'ct_merge_config_req_recv', 'ct_merge_config_res_sent', 'ct_commit_replace_req_recv', 'ct_commit_replace_res_sent', 'ct_delete_config_req_recv', 'ct_delete_config_res_sent', 'ct_replace_config_req_recv', 'ct_replace_config_res_sent', 'ct_get_oper_req_recv', 'ct_get_oper_res_sent', 'ct_get_current_session', 'ct_commit_config_req_recv', 'ct_commit_config_res_sent', 'ct_action_json_req_recv', 'ct_action_json_res_sent'], name, value)


    class Status(Entity):
        """
        Grpc Status
        
        .. attribute:: transport
        
        	GRPCTransport
        	**type**\: str
        
        .. attribute:: address_family
        
        	AddressFamily
        	**type**\: str
        
        .. attribute:: tls
        
        	GRPCTLS
        	**type**\: str
        
        .. attribute:: trustpoint
        
        	GRPCTrustpoint
        	**type**\: str
        
        .. attribute:: listening_port
        
        	ListeningPort
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: vrf_socket_ns_path
        
        	VrfSocketNamespacePath
        	**type**\: str
        
        .. attribute:: max_req_per_user
        
        	MaxReqPerUser
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_req_total
        
        	MaxReqTotal
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_streams
        
        	Maximum number of streaming gRPCs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_streams_per_user
        
        	Maximum number of streaming gRPCs per user
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'man-ems-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Status, self).__init__()

            self.yang_name = "status"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('transport', (YLeaf(YType.str, 'transport'), ['str'])),
                ('address_family', (YLeaf(YType.str, 'address-family'), ['str'])),
                ('tls', (YLeaf(YType.str, 'tls'), ['str'])),
                ('trustpoint', (YLeaf(YType.str, 'trustpoint'), ['str'])),
                ('listening_port', (YLeaf(YType.int32, 'listening-port'), ['int'])),
                ('vrf_socket_ns_path', (YLeaf(YType.str, 'vrf-socket-ns-path'), ['str'])),
                ('max_req_per_user', (YLeaf(YType.uint32, 'max-req-per-user'), ['int'])),
                ('max_req_total', (YLeaf(YType.uint32, 'max-req-total'), ['int'])),
                ('max_streams', (YLeaf(YType.uint32, 'max-streams'), ['int'])),
                ('max_streams_per_user', (YLeaf(YType.uint32, 'max-streams-per-user'), ['int'])),
            ])
            self.transport = None
            self.address_family = None
            self.tls = None
            self.trustpoint = None
            self.listening_port = None
            self.vrf_socket_ns_path = None
            self.max_req_per_user = None
            self.max_req_total = None
            self.max_streams = None
            self.max_streams_per_user = None
            self._segment_path = lambda: "status"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.Status, ['transport', 'address_family', 'tls', 'trustpoint', 'listening_port', 'vrf_socket_ns_path', 'max_req_per_user', 'max_req_total', 'max_streams', 'max_streams_per_user'], name, value)

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

