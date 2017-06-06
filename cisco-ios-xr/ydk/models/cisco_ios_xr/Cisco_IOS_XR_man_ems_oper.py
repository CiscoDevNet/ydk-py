""" Cisco_IOS_XR_man_ems_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package operational data.

This module contains definitions
for the following management objects\:
  grpc\: grpc commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Grpc(object):
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
        self.statistics = Grpc.Statistics()
        self.statistics.parent = self
        self.status = Grpc.Status()
        self.status.parent = self


    class Statistics(object):
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
            self.parent = None
            self.address_family = None
            self.ct_cli_config_req_recv = None
            self.ct_cli_config_res_sent = None
            self.ct_commit_replace_req_recv = None
            self.ct_commit_replace_res_sent = None
            self.ct_delete_config_req_recv = None
            self.ct_delete_config_res_sent = None
            self.ct_get_config_req_recv = None
            self.ct_get_config_res_sent = None
            self.ct_get_current_session = None
            self.ct_get_oper_req_recv = None
            self.ct_get_oper_res_sent = None
            self.ct_merge_config_req_recv = None
            self.ct_merge_config_res_sent = None
            self.ct_replace_config_req_recv = None
            self.ct_replace_config_res_sent = None
            self.ct_show_cmd_txt_req_recv = None
            self.ct_show_cmd_txt_res_sent = None
            self.listening_port = None
            self.max_req_per_user = None
            self.max_req_total = None
            self.tls = None
            self.transport = None
            self.trustpoint = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-ems-oper:grpc/Cisco-IOS-XR-man-ems-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.address_family is not None:
                return True

            if self.ct_cli_config_req_recv is not None:
                return True

            if self.ct_cli_config_res_sent is not None:
                return True

            if self.ct_commit_replace_req_recv is not None:
                return True

            if self.ct_commit_replace_res_sent is not None:
                return True

            if self.ct_delete_config_req_recv is not None:
                return True

            if self.ct_delete_config_res_sent is not None:
                return True

            if self.ct_get_config_req_recv is not None:
                return True

            if self.ct_get_config_res_sent is not None:
                return True

            if self.ct_get_current_session is not None:
                return True

            if self.ct_get_oper_req_recv is not None:
                return True

            if self.ct_get_oper_res_sent is not None:
                return True

            if self.ct_merge_config_req_recv is not None:
                return True

            if self.ct_merge_config_res_sent is not None:
                return True

            if self.ct_replace_config_req_recv is not None:
                return True

            if self.ct_replace_config_res_sent is not None:
                return True

            if self.ct_show_cmd_txt_req_recv is not None:
                return True

            if self.ct_show_cmd_txt_res_sent is not None:
                return True

            if self.listening_port is not None:
                return True

            if self.max_req_per_user is not None:
                return True

            if self.max_req_total is not None:
                return True

            if self.tls is not None:
                return True

            if self.transport is not None:
                return True

            if self.trustpoint is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_ems_oper as meta
            return meta._meta_table['Grpc.Statistics']['meta_info']


    class Status(object):
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
            self.parent = None
            self.address_family = None
            self.ct_cli_config_req_recv = None
            self.ct_cli_config_res_sent = None
            self.ct_commit_replace_req_recv = None
            self.ct_commit_replace_res_sent = None
            self.ct_delete_config_req_recv = None
            self.ct_delete_config_res_sent = None
            self.ct_get_config_req_recv = None
            self.ct_get_config_res_sent = None
            self.ct_get_current_session = None
            self.ct_get_oper_req_recv = None
            self.ct_get_oper_res_sent = None
            self.ct_merge_config_req_recv = None
            self.ct_merge_config_res_sent = None
            self.ct_replace_config_req_recv = None
            self.ct_replace_config_res_sent = None
            self.ct_show_cmd_txt_req_recv = None
            self.ct_show_cmd_txt_res_sent = None
            self.listening_port = None
            self.max_req_per_user = None
            self.max_req_total = None
            self.tls = None
            self.transport = None
            self.trustpoint = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-ems-oper:grpc/Cisco-IOS-XR-man-ems-oper:status'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.address_family is not None:
                return True

            if self.ct_cli_config_req_recv is not None:
                return True

            if self.ct_cli_config_res_sent is not None:
                return True

            if self.ct_commit_replace_req_recv is not None:
                return True

            if self.ct_commit_replace_res_sent is not None:
                return True

            if self.ct_delete_config_req_recv is not None:
                return True

            if self.ct_delete_config_res_sent is not None:
                return True

            if self.ct_get_config_req_recv is not None:
                return True

            if self.ct_get_config_res_sent is not None:
                return True

            if self.ct_get_current_session is not None:
                return True

            if self.ct_get_oper_req_recv is not None:
                return True

            if self.ct_get_oper_res_sent is not None:
                return True

            if self.ct_merge_config_req_recv is not None:
                return True

            if self.ct_merge_config_res_sent is not None:
                return True

            if self.ct_replace_config_req_recv is not None:
                return True

            if self.ct_replace_config_res_sent is not None:
                return True

            if self.ct_show_cmd_txt_req_recv is not None:
                return True

            if self.ct_show_cmd_txt_res_sent is not None:
                return True

            if self.listening_port is not None:
                return True

            if self.max_req_per_user is not None:
                return True

            if self.max_req_total is not None:
                return True

            if self.tls is not None:
                return True

            if self.transport is not None:
                return True

            if self.trustpoint is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_ems_oper as meta
            return meta._meta_table['Grpc.Status']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-ems-oper:grpc'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.statistics is not None and self.statistics._has_data():
            return True

        if self.status is not None and self.status._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_ems_oper as meta
        return meta._meta_table['Grpc']['meta_info']


