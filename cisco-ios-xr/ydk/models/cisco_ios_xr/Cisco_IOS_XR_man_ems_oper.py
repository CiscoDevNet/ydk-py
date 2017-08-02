""" Cisco_IOS_XR_man_ems_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package operational data.

This module contains definitions
for the following management objects\:
  grpc\: grpc commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.statistics = Grpc.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

        self.status = Grpc.Status()
        self.status.parent = self
        self._children_name_map["status"] = "status"
        self._children_yang_names.add("status")


    class Statistics(Entity):
        """
        Grpc Statistics
        
        .. attribute:: address_family
        
        	AddressFamily
        	**type**\:  str
        
        .. attribute:: ct_cli_config_req_recv
        
        	CounterCliConfigReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_res_sent
        
        	CounterCliConfigResSent
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
        
        

        """

        _prefix = 'man-ems-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "grpc"

            self.address_family = YLeaf(YType.str, "address-family")

            self.ct_cli_config_req_recv = YLeaf(YType.uint64, "ct-cli-config-req-recv")

            self.ct_cli_config_res_sent = YLeaf(YType.uint64, "ct-cli-config-res-sent")

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

            self.listening_port = YLeaf(YType.int32, "listening-port")

            self.max_req_per_user = YLeaf(YType.uint32, "max-req-per-user")

            self.max_req_total = YLeaf(YType.uint32, "max-req-total")

            self.tls = YLeaf(YType.str, "tls")

            self.transport = YLeaf(YType.str, "transport")

            self.trustpoint = YLeaf(YType.str, "trustpoint")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address_family",
                            "ct_cli_config_req_recv",
                            "ct_cli_config_res_sent",
                            "ct_commit_replace_req_recv",
                            "ct_commit_replace_res_sent",
                            "ct_delete_config_req_recv",
                            "ct_delete_config_res_sent",
                            "ct_get_config_req_recv",
                            "ct_get_config_res_sent",
                            "ct_get_current_session",
                            "ct_get_oper_req_recv",
                            "ct_get_oper_res_sent",
                            "ct_merge_config_req_recv",
                            "ct_merge_config_res_sent",
                            "ct_replace_config_req_recv",
                            "ct_replace_config_res_sent",
                            "ct_show_cmd_txt_req_recv",
                            "ct_show_cmd_txt_res_sent",
                            "listening_port",
                            "max_req_per_user",
                            "max_req_total",
                            "tls",
                            "transport",
                            "trustpoint") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Grpc.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Grpc.Statistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address_family.is_set or
                self.ct_cli_config_req_recv.is_set or
                self.ct_cli_config_res_sent.is_set or
                self.ct_commit_replace_req_recv.is_set or
                self.ct_commit_replace_res_sent.is_set or
                self.ct_delete_config_req_recv.is_set or
                self.ct_delete_config_res_sent.is_set or
                self.ct_get_config_req_recv.is_set or
                self.ct_get_config_res_sent.is_set or
                self.ct_get_current_session.is_set or
                self.ct_get_oper_req_recv.is_set or
                self.ct_get_oper_res_sent.is_set or
                self.ct_merge_config_req_recv.is_set or
                self.ct_merge_config_res_sent.is_set or
                self.ct_replace_config_req_recv.is_set or
                self.ct_replace_config_res_sent.is_set or
                self.ct_show_cmd_txt_req_recv.is_set or
                self.ct_show_cmd_txt_res_sent.is_set or
                self.listening_port.is_set or
                self.max_req_per_user.is_set or
                self.max_req_total.is_set or
                self.tls.is_set or
                self.transport.is_set or
                self.trustpoint.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address_family.yfilter != YFilter.not_set or
                self.ct_cli_config_req_recv.yfilter != YFilter.not_set or
                self.ct_cli_config_res_sent.yfilter != YFilter.not_set or
                self.ct_commit_replace_req_recv.yfilter != YFilter.not_set or
                self.ct_commit_replace_res_sent.yfilter != YFilter.not_set or
                self.ct_delete_config_req_recv.yfilter != YFilter.not_set or
                self.ct_delete_config_res_sent.yfilter != YFilter.not_set or
                self.ct_get_config_req_recv.yfilter != YFilter.not_set or
                self.ct_get_config_res_sent.yfilter != YFilter.not_set or
                self.ct_get_current_session.yfilter != YFilter.not_set or
                self.ct_get_oper_req_recv.yfilter != YFilter.not_set or
                self.ct_get_oper_res_sent.yfilter != YFilter.not_set or
                self.ct_merge_config_req_recv.yfilter != YFilter.not_set or
                self.ct_merge_config_res_sent.yfilter != YFilter.not_set or
                self.ct_replace_config_req_recv.yfilter != YFilter.not_set or
                self.ct_replace_config_res_sent.yfilter != YFilter.not_set or
                self.ct_show_cmd_txt_req_recv.yfilter != YFilter.not_set or
                self.ct_show_cmd_txt_res_sent.yfilter != YFilter.not_set or
                self.listening_port.yfilter != YFilter.not_set or
                self.max_req_per_user.yfilter != YFilter.not_set or
                self.max_req_total.yfilter != YFilter.not_set or
                self.tls.yfilter != YFilter.not_set or
                self.transport.yfilter != YFilter.not_set or
                self.trustpoint.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address_family.get_name_leafdata())
            if (self.ct_cli_config_req_recv.is_set or self.ct_cli_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_cli_config_req_recv.get_name_leafdata())
            if (self.ct_cli_config_res_sent.is_set or self.ct_cli_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_cli_config_res_sent.get_name_leafdata())
            if (self.ct_commit_replace_req_recv.is_set or self.ct_commit_replace_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_commit_replace_req_recv.get_name_leafdata())
            if (self.ct_commit_replace_res_sent.is_set or self.ct_commit_replace_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_commit_replace_res_sent.get_name_leafdata())
            if (self.ct_delete_config_req_recv.is_set or self.ct_delete_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_delete_config_req_recv.get_name_leafdata())
            if (self.ct_delete_config_res_sent.is_set or self.ct_delete_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_delete_config_res_sent.get_name_leafdata())
            if (self.ct_get_config_req_recv.is_set or self.ct_get_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_config_req_recv.get_name_leafdata())
            if (self.ct_get_config_res_sent.is_set or self.ct_get_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_config_res_sent.get_name_leafdata())
            if (self.ct_get_current_session.is_set or self.ct_get_current_session.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_current_session.get_name_leafdata())
            if (self.ct_get_oper_req_recv.is_set or self.ct_get_oper_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_oper_req_recv.get_name_leafdata())
            if (self.ct_get_oper_res_sent.is_set or self.ct_get_oper_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_oper_res_sent.get_name_leafdata())
            if (self.ct_merge_config_req_recv.is_set or self.ct_merge_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_merge_config_req_recv.get_name_leafdata())
            if (self.ct_merge_config_res_sent.is_set or self.ct_merge_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_merge_config_res_sent.get_name_leafdata())
            if (self.ct_replace_config_req_recv.is_set or self.ct_replace_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_replace_config_req_recv.get_name_leafdata())
            if (self.ct_replace_config_res_sent.is_set or self.ct_replace_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_replace_config_res_sent.get_name_leafdata())
            if (self.ct_show_cmd_txt_req_recv.is_set or self.ct_show_cmd_txt_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_show_cmd_txt_req_recv.get_name_leafdata())
            if (self.ct_show_cmd_txt_res_sent.is_set or self.ct_show_cmd_txt_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_show_cmd_txt_res_sent.get_name_leafdata())
            if (self.listening_port.is_set or self.listening_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.listening_port.get_name_leafdata())
            if (self.max_req_per_user.is_set or self.max_req_per_user.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_req_per_user.get_name_leafdata())
            if (self.max_req_total.is_set or self.max_req_total.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_req_total.get_name_leafdata())
            if (self.tls.is_set or self.tls.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tls.get_name_leafdata())
            if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.transport.get_name_leafdata())
            if (self.trustpoint.is_set or self.trustpoint.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trustpoint.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address-family" or name == "ct-cli-config-req-recv" or name == "ct-cli-config-res-sent" or name == "ct-commit-replace-req-recv" or name == "ct-commit-replace-res-sent" or name == "ct-delete-config-req-recv" or name == "ct-delete-config-res-sent" or name == "ct-get-config-req-recv" or name == "ct-get-config-res-sent" or name == "ct-get-current-session" or name == "ct-get-oper-req-recv" or name == "ct-get-oper-res-sent" or name == "ct-merge-config-req-recv" or name == "ct-merge-config-res-sent" or name == "ct-replace-config-req-recv" or name == "ct-replace-config-res-sent" or name == "ct-show-cmd-txt-req-recv" or name == "ct-show-cmd-txt-res-sent" or name == "listening-port" or name == "max-req-per-user" or name == "max-req-total" or name == "tls" or name == "transport" or name == "trustpoint"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address-family"):
                self.address_family = value
                self.address_family.value_namespace = name_space
                self.address_family.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-cli-config-req-recv"):
                self.ct_cli_config_req_recv = value
                self.ct_cli_config_req_recv.value_namespace = name_space
                self.ct_cli_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-cli-config-res-sent"):
                self.ct_cli_config_res_sent = value
                self.ct_cli_config_res_sent.value_namespace = name_space
                self.ct_cli_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-commit-replace-req-recv"):
                self.ct_commit_replace_req_recv = value
                self.ct_commit_replace_req_recv.value_namespace = name_space
                self.ct_commit_replace_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-commit-replace-res-sent"):
                self.ct_commit_replace_res_sent = value
                self.ct_commit_replace_res_sent.value_namespace = name_space
                self.ct_commit_replace_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-delete-config-req-recv"):
                self.ct_delete_config_req_recv = value
                self.ct_delete_config_req_recv.value_namespace = name_space
                self.ct_delete_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-delete-config-res-sent"):
                self.ct_delete_config_res_sent = value
                self.ct_delete_config_res_sent.value_namespace = name_space
                self.ct_delete_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-config-req-recv"):
                self.ct_get_config_req_recv = value
                self.ct_get_config_req_recv.value_namespace = name_space
                self.ct_get_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-config-res-sent"):
                self.ct_get_config_res_sent = value
                self.ct_get_config_res_sent.value_namespace = name_space
                self.ct_get_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-current-session"):
                self.ct_get_current_session = value
                self.ct_get_current_session.value_namespace = name_space
                self.ct_get_current_session.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-oper-req-recv"):
                self.ct_get_oper_req_recv = value
                self.ct_get_oper_req_recv.value_namespace = name_space
                self.ct_get_oper_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-oper-res-sent"):
                self.ct_get_oper_res_sent = value
                self.ct_get_oper_res_sent.value_namespace = name_space
                self.ct_get_oper_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-merge-config-req-recv"):
                self.ct_merge_config_req_recv = value
                self.ct_merge_config_req_recv.value_namespace = name_space
                self.ct_merge_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-merge-config-res-sent"):
                self.ct_merge_config_res_sent = value
                self.ct_merge_config_res_sent.value_namespace = name_space
                self.ct_merge_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-replace-config-req-recv"):
                self.ct_replace_config_req_recv = value
                self.ct_replace_config_req_recv.value_namespace = name_space
                self.ct_replace_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-replace-config-res-sent"):
                self.ct_replace_config_res_sent = value
                self.ct_replace_config_res_sent.value_namespace = name_space
                self.ct_replace_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-show-cmd-txt-req-recv"):
                self.ct_show_cmd_txt_req_recv = value
                self.ct_show_cmd_txt_req_recv.value_namespace = name_space
                self.ct_show_cmd_txt_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-show-cmd-txt-res-sent"):
                self.ct_show_cmd_txt_res_sent = value
                self.ct_show_cmd_txt_res_sent.value_namespace = name_space
                self.ct_show_cmd_txt_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "listening-port"):
                self.listening_port = value
                self.listening_port.value_namespace = name_space
                self.listening_port.value_namespace_prefix = name_space_prefix
            if(value_path == "max-req-per-user"):
                self.max_req_per_user = value
                self.max_req_per_user.value_namespace = name_space
                self.max_req_per_user.value_namespace_prefix = name_space_prefix
            if(value_path == "max-req-total"):
                self.max_req_total = value
                self.max_req_total.value_namespace = name_space
                self.max_req_total.value_namespace_prefix = name_space_prefix
            if(value_path == "tls"):
                self.tls = value
                self.tls.value_namespace = name_space
                self.tls.value_namespace_prefix = name_space_prefix
            if(value_path == "transport"):
                self.transport = value
                self.transport.value_namespace = name_space
                self.transport.value_namespace_prefix = name_space_prefix
            if(value_path == "trustpoint"):
                self.trustpoint = value
                self.trustpoint.value_namespace = name_space
                self.trustpoint.value_namespace_prefix = name_space_prefix


    class Status(Entity):
        """
        Grpc Status
        
        .. attribute:: address_family
        
        	AddressFamily
        	**type**\:  str
        
        .. attribute:: ct_cli_config_req_recv
        
        	CounterCliConfigReqRecv
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ct_cli_config_res_sent
        
        	CounterCliConfigResSent
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
        
        

        """

        _prefix = 'man-ems-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grpc.Status, self).__init__()

            self.yang_name = "status"
            self.yang_parent_name = "grpc"

            self.address_family = YLeaf(YType.str, "address-family")

            self.ct_cli_config_req_recv = YLeaf(YType.uint64, "ct-cli-config-req-recv")

            self.ct_cli_config_res_sent = YLeaf(YType.uint64, "ct-cli-config-res-sent")

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

            self.listening_port = YLeaf(YType.int32, "listening-port")

            self.max_req_per_user = YLeaf(YType.uint32, "max-req-per-user")

            self.max_req_total = YLeaf(YType.uint32, "max-req-total")

            self.tls = YLeaf(YType.str, "tls")

            self.transport = YLeaf(YType.str, "transport")

            self.trustpoint = YLeaf(YType.str, "trustpoint")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("address_family",
                            "ct_cli_config_req_recv",
                            "ct_cli_config_res_sent",
                            "ct_commit_replace_req_recv",
                            "ct_commit_replace_res_sent",
                            "ct_delete_config_req_recv",
                            "ct_delete_config_res_sent",
                            "ct_get_config_req_recv",
                            "ct_get_config_res_sent",
                            "ct_get_current_session",
                            "ct_get_oper_req_recv",
                            "ct_get_oper_res_sent",
                            "ct_merge_config_req_recv",
                            "ct_merge_config_res_sent",
                            "ct_replace_config_req_recv",
                            "ct_replace_config_res_sent",
                            "ct_show_cmd_txt_req_recv",
                            "ct_show_cmd_txt_res_sent",
                            "listening_port",
                            "max_req_per_user",
                            "max_req_total",
                            "tls",
                            "transport",
                            "trustpoint") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Grpc.Status, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Grpc.Status, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.address_family.is_set or
                self.ct_cli_config_req_recv.is_set or
                self.ct_cli_config_res_sent.is_set or
                self.ct_commit_replace_req_recv.is_set or
                self.ct_commit_replace_res_sent.is_set or
                self.ct_delete_config_req_recv.is_set or
                self.ct_delete_config_res_sent.is_set or
                self.ct_get_config_req_recv.is_set or
                self.ct_get_config_res_sent.is_set or
                self.ct_get_current_session.is_set or
                self.ct_get_oper_req_recv.is_set or
                self.ct_get_oper_res_sent.is_set or
                self.ct_merge_config_req_recv.is_set or
                self.ct_merge_config_res_sent.is_set or
                self.ct_replace_config_req_recv.is_set or
                self.ct_replace_config_res_sent.is_set or
                self.ct_show_cmd_txt_req_recv.is_set or
                self.ct_show_cmd_txt_res_sent.is_set or
                self.listening_port.is_set or
                self.max_req_per_user.is_set or
                self.max_req_total.is_set or
                self.tls.is_set or
                self.transport.is_set or
                self.trustpoint.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.address_family.yfilter != YFilter.not_set or
                self.ct_cli_config_req_recv.yfilter != YFilter.not_set or
                self.ct_cli_config_res_sent.yfilter != YFilter.not_set or
                self.ct_commit_replace_req_recv.yfilter != YFilter.not_set or
                self.ct_commit_replace_res_sent.yfilter != YFilter.not_set or
                self.ct_delete_config_req_recv.yfilter != YFilter.not_set or
                self.ct_delete_config_res_sent.yfilter != YFilter.not_set or
                self.ct_get_config_req_recv.yfilter != YFilter.not_set or
                self.ct_get_config_res_sent.yfilter != YFilter.not_set or
                self.ct_get_current_session.yfilter != YFilter.not_set or
                self.ct_get_oper_req_recv.yfilter != YFilter.not_set or
                self.ct_get_oper_res_sent.yfilter != YFilter.not_set or
                self.ct_merge_config_req_recv.yfilter != YFilter.not_set or
                self.ct_merge_config_res_sent.yfilter != YFilter.not_set or
                self.ct_replace_config_req_recv.yfilter != YFilter.not_set or
                self.ct_replace_config_res_sent.yfilter != YFilter.not_set or
                self.ct_show_cmd_txt_req_recv.yfilter != YFilter.not_set or
                self.ct_show_cmd_txt_res_sent.yfilter != YFilter.not_set or
                self.listening_port.yfilter != YFilter.not_set or
                self.max_req_per_user.yfilter != YFilter.not_set or
                self.max_req_total.yfilter != YFilter.not_set or
                self.tls.yfilter != YFilter.not_set or
                self.transport.yfilter != YFilter.not_set or
                self.trustpoint.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "status" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-ems-oper:grpc/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                leaf_name_data.append(self.address_family.get_name_leafdata())
            if (self.ct_cli_config_req_recv.is_set or self.ct_cli_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_cli_config_req_recv.get_name_leafdata())
            if (self.ct_cli_config_res_sent.is_set or self.ct_cli_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_cli_config_res_sent.get_name_leafdata())
            if (self.ct_commit_replace_req_recv.is_set or self.ct_commit_replace_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_commit_replace_req_recv.get_name_leafdata())
            if (self.ct_commit_replace_res_sent.is_set or self.ct_commit_replace_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_commit_replace_res_sent.get_name_leafdata())
            if (self.ct_delete_config_req_recv.is_set or self.ct_delete_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_delete_config_req_recv.get_name_leafdata())
            if (self.ct_delete_config_res_sent.is_set or self.ct_delete_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_delete_config_res_sent.get_name_leafdata())
            if (self.ct_get_config_req_recv.is_set or self.ct_get_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_config_req_recv.get_name_leafdata())
            if (self.ct_get_config_res_sent.is_set or self.ct_get_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_config_res_sent.get_name_leafdata())
            if (self.ct_get_current_session.is_set or self.ct_get_current_session.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_current_session.get_name_leafdata())
            if (self.ct_get_oper_req_recv.is_set or self.ct_get_oper_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_oper_req_recv.get_name_leafdata())
            if (self.ct_get_oper_res_sent.is_set or self.ct_get_oper_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_get_oper_res_sent.get_name_leafdata())
            if (self.ct_merge_config_req_recv.is_set or self.ct_merge_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_merge_config_req_recv.get_name_leafdata())
            if (self.ct_merge_config_res_sent.is_set or self.ct_merge_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_merge_config_res_sent.get_name_leafdata())
            if (self.ct_replace_config_req_recv.is_set or self.ct_replace_config_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_replace_config_req_recv.get_name_leafdata())
            if (self.ct_replace_config_res_sent.is_set or self.ct_replace_config_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_replace_config_res_sent.get_name_leafdata())
            if (self.ct_show_cmd_txt_req_recv.is_set or self.ct_show_cmd_txt_req_recv.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_show_cmd_txt_req_recv.get_name_leafdata())
            if (self.ct_show_cmd_txt_res_sent.is_set or self.ct_show_cmd_txt_res_sent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ct_show_cmd_txt_res_sent.get_name_leafdata())
            if (self.listening_port.is_set or self.listening_port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.listening_port.get_name_leafdata())
            if (self.max_req_per_user.is_set or self.max_req_per_user.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_req_per_user.get_name_leafdata())
            if (self.max_req_total.is_set or self.max_req_total.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_req_total.get_name_leafdata())
            if (self.tls.is_set or self.tls.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tls.get_name_leafdata())
            if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.transport.get_name_leafdata())
            if (self.trustpoint.is_set or self.trustpoint.yfilter != YFilter.not_set):
                leaf_name_data.append(self.trustpoint.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address-family" or name == "ct-cli-config-req-recv" or name == "ct-cli-config-res-sent" or name == "ct-commit-replace-req-recv" or name == "ct-commit-replace-res-sent" or name == "ct-delete-config-req-recv" or name == "ct-delete-config-res-sent" or name == "ct-get-config-req-recv" or name == "ct-get-config-res-sent" or name == "ct-get-current-session" or name == "ct-get-oper-req-recv" or name == "ct-get-oper-res-sent" or name == "ct-merge-config-req-recv" or name == "ct-merge-config-res-sent" or name == "ct-replace-config-req-recv" or name == "ct-replace-config-res-sent" or name == "ct-show-cmd-txt-req-recv" or name == "ct-show-cmd-txt-res-sent" or name == "listening-port" or name == "max-req-per-user" or name == "max-req-total" or name == "tls" or name == "transport" or name == "trustpoint"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "address-family"):
                self.address_family = value
                self.address_family.value_namespace = name_space
                self.address_family.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-cli-config-req-recv"):
                self.ct_cli_config_req_recv = value
                self.ct_cli_config_req_recv.value_namespace = name_space
                self.ct_cli_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-cli-config-res-sent"):
                self.ct_cli_config_res_sent = value
                self.ct_cli_config_res_sent.value_namespace = name_space
                self.ct_cli_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-commit-replace-req-recv"):
                self.ct_commit_replace_req_recv = value
                self.ct_commit_replace_req_recv.value_namespace = name_space
                self.ct_commit_replace_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-commit-replace-res-sent"):
                self.ct_commit_replace_res_sent = value
                self.ct_commit_replace_res_sent.value_namespace = name_space
                self.ct_commit_replace_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-delete-config-req-recv"):
                self.ct_delete_config_req_recv = value
                self.ct_delete_config_req_recv.value_namespace = name_space
                self.ct_delete_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-delete-config-res-sent"):
                self.ct_delete_config_res_sent = value
                self.ct_delete_config_res_sent.value_namespace = name_space
                self.ct_delete_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-config-req-recv"):
                self.ct_get_config_req_recv = value
                self.ct_get_config_req_recv.value_namespace = name_space
                self.ct_get_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-config-res-sent"):
                self.ct_get_config_res_sent = value
                self.ct_get_config_res_sent.value_namespace = name_space
                self.ct_get_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-current-session"):
                self.ct_get_current_session = value
                self.ct_get_current_session.value_namespace = name_space
                self.ct_get_current_session.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-oper-req-recv"):
                self.ct_get_oper_req_recv = value
                self.ct_get_oper_req_recv.value_namespace = name_space
                self.ct_get_oper_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-get-oper-res-sent"):
                self.ct_get_oper_res_sent = value
                self.ct_get_oper_res_sent.value_namespace = name_space
                self.ct_get_oper_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-merge-config-req-recv"):
                self.ct_merge_config_req_recv = value
                self.ct_merge_config_req_recv.value_namespace = name_space
                self.ct_merge_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-merge-config-res-sent"):
                self.ct_merge_config_res_sent = value
                self.ct_merge_config_res_sent.value_namespace = name_space
                self.ct_merge_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-replace-config-req-recv"):
                self.ct_replace_config_req_recv = value
                self.ct_replace_config_req_recv.value_namespace = name_space
                self.ct_replace_config_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-replace-config-res-sent"):
                self.ct_replace_config_res_sent = value
                self.ct_replace_config_res_sent.value_namespace = name_space
                self.ct_replace_config_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-show-cmd-txt-req-recv"):
                self.ct_show_cmd_txt_req_recv = value
                self.ct_show_cmd_txt_req_recv.value_namespace = name_space
                self.ct_show_cmd_txt_req_recv.value_namespace_prefix = name_space_prefix
            if(value_path == "ct-show-cmd-txt-res-sent"):
                self.ct_show_cmd_txt_res_sent = value
                self.ct_show_cmd_txt_res_sent.value_namespace = name_space
                self.ct_show_cmd_txt_res_sent.value_namespace_prefix = name_space_prefix
            if(value_path == "listening-port"):
                self.listening_port = value
                self.listening_port.value_namespace = name_space
                self.listening_port.value_namespace_prefix = name_space_prefix
            if(value_path == "max-req-per-user"):
                self.max_req_per_user = value
                self.max_req_per_user.value_namespace = name_space
                self.max_req_per_user.value_namespace_prefix = name_space_prefix
            if(value_path == "max-req-total"):
                self.max_req_total = value
                self.max_req_total.value_namespace = name_space
                self.max_req_total.value_namespace_prefix = name_space_prefix
            if(value_path == "tls"):
                self.tls = value
                self.tls.value_namespace = name_space
                self.tls.value_namespace_prefix = name_space_prefix
            if(value_path == "transport"):
                self.transport = value
                self.transport.value_namespace = name_space
                self.transport.value_namespace_prefix = name_space_prefix
            if(value_path == "trustpoint"):
                self.trustpoint = value
                self.trustpoint.value_namespace = name_space
                self.trustpoint.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.statistics is not None and self.statistics.has_data()) or
            (self.status is not None and self.status.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.statistics is not None and self.statistics.has_operation()) or
            (self.status is not None and self.status.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-man-ems-oper:grpc" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = Grpc.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        if (child_yang_name == "status"):
            if (self.status is None):
                self.status = Grpc.Status()
                self.status.parent = self
                self._children_name_map["status"] = "status"
            return self.status

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "statistics" or name == "status"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Grpc()
        return self._top_entity

