""" Cisco_IOS_XR_man_ems_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package operational data.

This module contains definitions
for the following management objects\:
  grpc\: grpc commands

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Grpc(Entity):
    """
    grpc commands
    
    .. attribute:: statistics
    
    	Grpc Statistics
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper.Grpc.Statistics>`
    
    .. attribute:: status
    
    	Grpc Status
    	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper.Grpc.Status>`
    
    

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
        self._child_container_classes = {"statistics" : ("statistics", Grpc.Statistics), "status" : ("status", Grpc.Status)}
        self._child_list_classes = {}

        self.statistics = Grpc.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

        self.status = Grpc.Status()
        self.status.parent = self
        self._children_name_map["status"] = "status"
        self._children_yang_names.add("status")
        self._segment_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc"


    class Statistics(Entity):
        """
        Grpc Statistics
        
        .. attribute:: ct_action_json_req_recv
        
        	CounterForHowManyActionJsonRequests
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_action_json_res_sent
        
        	CounterForHowManyActionJsonResponses
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_req_recv
        
        	CounterCliConfigReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_res_sent
        
        	CounterCliConfigResSent
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_config_req_recv
        
        	CounterForHowManyCommitConfigRequests
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_config_res_sent
        
        	CounterForHowManyCommitConfigResponses
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_replace_req_recv
        
        	CounterCommitReplaceReq
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_commit_replace_res_sent
        
        	CounterCommitReplaceRes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_delete_config_req_recv
        
        	CounterDeleteConfigReq
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_delete_config_res_sent
        
        	CounterDeleteConfigRes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_config_req_recv
        
        	CounterGetConfigReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_config_res_sent
        
        	CounterGetConfigResSent
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_current_session
        
        	CounterGetCurrentSession
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ct_get_oper_req_recv
        
        	CounterGetOperReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_get_oper_res_sent
        
        	CounterGetOperResSent
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_merge_config_req_recv
        
        	CounterMergeConfigReq
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_merge_config_res_sent
        
        	CounterMergeConfigRes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_replace_config_req_recv
        
        	CounterReplaceConfigReq
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_replace_config_res_sent
        
        	CounterReplaceConfigSent
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_show_cmd_txt_req_recv
        
        	CounterShowCmdTxtReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_show_cmd_txt_res_sent
        
        	CounterShowCmdTxtResSent
        	**type**\:  int
        
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
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ct_action_json_req_recv = YLeaf(YType.uint64, "ct-action-json-req-recv")

            self.ct_action_json_res_sent = YLeaf(YType.uint64, "ct-action-json-res-sent")

            self.ct_cli_config_req_recv = YLeaf(YType.uint64, "ct-cli-config-req-recv")

            self.ct_cli_config_res_sent = YLeaf(YType.uint64, "ct-cli-config-res-sent")

            self.ct_commit_config_req_recv = YLeaf(YType.uint64, "ct-commit-config-req-recv")

            self.ct_commit_config_res_sent = YLeaf(YType.uint64, "ct-commit-config-res-sent")

            self.ct_commit_replace_req_recv = YLeaf(YType.uint64, "ct-commit-replace-req-recv")

            self.ct_commit_replace_res_sent = YLeaf(YType.uint64, "ct-commit-replace-res-sent")

            self.ct_delete_config_req_recv = YLeaf(YType.uint64, "ct-delete-config-req-recv")

            self.ct_delete_config_res_sent = YLeaf(YType.uint64, "ct-delete-config-res-sent")

            self.ct_get_config_req_recv = YLeaf(YType.uint64, "ct-get-config-req-recv")

            self.ct_get_config_res_sent = YLeaf(YType.uint64, "ct-get-config-res-sent")

            self.ct_get_current_session = YLeaf(YType.uint32, "ct-get-current-session")

            self.ct_get_oper_req_recv = YLeaf(YType.uint64, "ct-get-oper-req-recv")

            self.ct_get_oper_res_sent = YLeaf(YType.uint64, "ct-get-oper-res-sent")

            self.ct_merge_config_req_recv = YLeaf(YType.uint64, "ct-merge-config-req-recv")

            self.ct_merge_config_res_sent = YLeaf(YType.uint64, "ct-merge-config-res-sent")

            self.ct_replace_config_req_recv = YLeaf(YType.uint64, "ct-replace-config-req-recv")

            self.ct_replace_config_res_sent = YLeaf(YType.uint64, "ct-replace-config-res-sent")

            self.ct_show_cmd_txt_req_recv = YLeaf(YType.uint64, "ct-show-cmd-txt-req-recv")

            self.ct_show_cmd_txt_res_sent = YLeaf(YType.uint64, "ct-show-cmd-txt-res-sent")
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.Statistics, ['ct_action_json_req_recv', 'ct_action_json_res_sent', 'ct_cli_config_req_recv', 'ct_cli_config_res_sent', 'ct_commit_config_req_recv', 'ct_commit_config_res_sent', 'ct_commit_replace_req_recv', 'ct_commit_replace_res_sent', 'ct_delete_config_req_recv', 'ct_delete_config_res_sent', 'ct_get_config_req_recv', 'ct_get_config_res_sent', 'ct_get_current_session', 'ct_get_oper_req_recv', 'ct_get_oper_res_sent', 'ct_merge_config_req_recv', 'ct_merge_config_res_sent', 'ct_replace_config_req_recv', 'ct_replace_config_res_sent', 'ct_show_cmd_txt_req_recv', 'ct_show_cmd_txt_res_sent'], name, value)


    class Status(Entity):
        """
        Grpc Status
        
        .. attribute:: address_family
        
        	AddressFamily
        	**type**\:  str
        
        .. attribute:: listening_port
        
        	ListeningPort
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: max_req_per_user
        
        	MaxReqPerUser
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_req_total
        
        	MaxReqTotal
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: tls
        
        	GRPCTLS
        	**type**\:  str
        
        .. attribute:: transport
        
        	GRPCTransport
        	**type**\:  str
        
        .. attribute:: trustpoint
        
        	GRPCTrustpoint
        	**type**\:  str
        
        .. attribute:: vrf_socket_ns_path
        
        	VrfSocketNamespacePath
        	**type**\:  str
        
        

        """

        _prefix = 'man-ems-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Status, self).__init__()

            self.yang_name = "status"
            self.yang_parent_name = "grpc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.address_family = YLeaf(YType.str, "address-family")

            self.listening_port = YLeaf(YType.int32, "listening-port")

            self.max_req_per_user = YLeaf(YType.uint32, "max-req-per-user")

            self.max_req_total = YLeaf(YType.uint32, "max-req-total")

            self.tls = YLeaf(YType.str, "tls")

            self.transport = YLeaf(YType.str, "transport")

            self.trustpoint = YLeaf(YType.str, "trustpoint")

            self.vrf_socket_ns_path = YLeaf(YType.str, "vrf-socket-ns-path")
            self._segment_path = lambda: "status"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Grpc.Status, ['address_family', 'listening_port', 'max_req_per_user', 'max_req_total', 'tls', 'transport', 'trustpoint', 'vrf_socket_ns_path'], name, value)

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

