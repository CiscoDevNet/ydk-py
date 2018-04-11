""" Cisco_IOS_XR_asr9k_ptp_pd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-ptp\-pd package operational data.

This module contains definitions
for the following management objects\:
  platform\-ptp\: PTP PD operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PlatformPtp(Entity):
    """
    PTP PD operational data
    
    .. attribute:: platform_ptp_servo
    
    	PTP PD Servo information
    	**type**\:  :py:class:`PlatformPtpServo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo>`
    
    

    """

    _prefix = 'asr9k-ptp-pd-oper'
    _revision = '2017-03-16'

    def __init__(self):
        super(PlatformPtp, self).__init__()
        self._top_entity = None

        self.yang_name = "platform-ptp"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-ptp-pd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("platform-ptp-servo", ("platform_ptp_servo", PlatformPtp.PlatformPtpServo))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.platform_ptp_servo = PlatformPtp.PlatformPtpServo()
        self.platform_ptp_servo.parent = self
        self._children_name_map["platform_ptp_servo"] = "platform-ptp-servo"
        self._children_yang_names.add("platform-ptp-servo")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp"


    class PlatformPtpServo(Entity):
        """
        PTP PD Servo information
        
        .. attribute:: last_set_time
        
        	last input of setTime
        	**type**\:  :py:class:`LastSetTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.LastSetTime>`
        
        .. attribute:: last_received_t1
        
        	last T1 timestamp reveiced
        	**type**\:  :py:class:`LastReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.LastReceivedT1>`
        
        .. attribute:: last_received_t2
        
        	last T2 timestamp reveiced
        	**type**\:  :py:class:`LastReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.LastReceivedT2>`
        
        .. attribute:: last_received_t3
        
        	last T3 timestamp reveiced
        	**type**\:  :py:class:`LastReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.LastReceivedT3>`
        
        .. attribute:: last_received_t4
        
        	last T4 timestamp reveiced
        	**type**\:  :py:class:`LastReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.LastReceivedT4>`
        
        .. attribute:: pre_received_t1
        
        	pre T1 timestamp reveiced
        	**type**\:  :py:class:`PreReceivedT1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.PreReceivedT1>`
        
        .. attribute:: pre_received_t2
        
        	pre T2 timestamp reveiced
        	**type**\:  :py:class:`PreReceivedT2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.PreReceivedT2>`
        
        .. attribute:: pre_received_t3
        
        	pre T3 timestamp reveiced
        	**type**\:  :py:class:`PreReceivedT3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.PreReceivedT3>`
        
        .. attribute:: pre_received_t4
        
        	pre T4 timestamp reveiced
        	**type**\:  :py:class:`PreReceivedT4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ptp_pd_oper.PlatformPtp.PlatformPtpServo.PreReceivedT4>`
        
        .. attribute:: lock_status
        
        	lock status of device
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: running
        
        	running status of apr
        	**type**\: bool
        
        .. attribute:: device_status
        
        	status of device
        	**type**\: str
        
        	**length:** 0..50
        
        .. attribute:: log_level
        
        	log level of apr
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: phase_accuracy_last
        
        	 last phase alignment accuracy
        	**type**\: int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        .. attribute:: num_sync_timestamp
        
        	number of sync timestamp reveiced
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_delay_timestamp
        
        	number of delay timestamp reveiced
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_set_time
        
        	number of setTime() been called
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_step_time
        
        	number of stepTime() been called
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_adjust_freq
        
        	number of adjustFreq() been called
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_adjust_freq_time
        
        	number of adjustFreqTime() been called
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: last_adjust_freq
        
        	last input of adjustFreq
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: last_step_time
        
        	last input of stepTime
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: num_discard_sync_timestamp
        
        	number of sync timestamp discarded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_discard_delay_timestamp
        
        	number of delay timestamp discarded
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: flagof_last_set_time
        
        	last input flag of setTime
        	**type**\: bool
        
        .. attribute:: offset_from_master
        
        	Time Offset From Master
        	**type**\: int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        .. attribute:: mean_path_delay
        
        	Mean Path Delay
        	**type**\: int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        

        """

        _prefix = 'asr9k-ptp-pd-oper'
        _revision = '2017-03-16'

        def __init__(self):
            super(PlatformPtp.PlatformPtpServo, self).__init__()

            self.yang_name = "platform-ptp-servo"
            self.yang_parent_name = "platform-ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("last-set-time", ("last_set_time", PlatformPtp.PlatformPtpServo.LastSetTime)), ("last-received-t1", ("last_received_t1", PlatformPtp.PlatformPtpServo.LastReceivedT1)), ("last-received-t2", ("last_received_t2", PlatformPtp.PlatformPtpServo.LastReceivedT2)), ("last-received-t3", ("last_received_t3", PlatformPtp.PlatformPtpServo.LastReceivedT3)), ("last-received-t4", ("last_received_t4", PlatformPtp.PlatformPtpServo.LastReceivedT4)), ("pre-received-t1", ("pre_received_t1", PlatformPtp.PlatformPtpServo.PreReceivedT1)), ("pre-received-t2", ("pre_received_t2", PlatformPtp.PlatformPtpServo.PreReceivedT2)), ("pre-received-t3", ("pre_received_t3", PlatformPtp.PlatformPtpServo.PreReceivedT3)), ("pre-received-t4", ("pre_received_t4", PlatformPtp.PlatformPtpServo.PreReceivedT4))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lock_status', YLeaf(YType.uint16, 'lock-status')),
                ('running', YLeaf(YType.boolean, 'running')),
                ('device_status', YLeaf(YType.str, 'device-status')),
                ('log_level', YLeaf(YType.uint16, 'log-level')),
                ('phase_accuracy_last', YLeaf(YType.int64, 'phase-accuracy-last')),
                ('num_sync_timestamp', YLeaf(YType.uint32, 'num-sync-timestamp')),
                ('num_delay_timestamp', YLeaf(YType.uint32, 'num-delay-timestamp')),
                ('num_set_time', YLeaf(YType.uint32, 'num-set-time')),
                ('num_step_time', YLeaf(YType.uint32, 'num-step-time')),
                ('num_adjust_freq', YLeaf(YType.uint32, 'num-adjust-freq')),
                ('num_adjust_freq_time', YLeaf(YType.uint32, 'num-adjust-freq-time')),
                ('last_adjust_freq', YLeaf(YType.int32, 'last-adjust-freq')),
                ('last_step_time', YLeaf(YType.int32, 'last-step-time')),
                ('num_discard_sync_timestamp', YLeaf(YType.uint32, 'num-discard-sync-timestamp')),
                ('num_discard_delay_timestamp', YLeaf(YType.uint32, 'num-discard-delay-timestamp')),
                ('flagof_last_set_time', YLeaf(YType.boolean, 'flagof-last-set-time')),
                ('offset_from_master', YLeaf(YType.int64, 'offset-from-master')),
                ('mean_path_delay', YLeaf(YType.int64, 'mean-path-delay')),
            ])
            self.lock_status = None
            self.running = None
            self.device_status = None
            self.log_level = None
            self.phase_accuracy_last = None
            self.num_sync_timestamp = None
            self.num_delay_timestamp = None
            self.num_set_time = None
            self.num_step_time = None
            self.num_adjust_freq = None
            self.num_adjust_freq_time = None
            self.last_adjust_freq = None
            self.last_step_time = None
            self.num_discard_sync_timestamp = None
            self.num_discard_delay_timestamp = None
            self.flagof_last_set_time = None
            self.offset_from_master = None
            self.mean_path_delay = None

            self.last_set_time = PlatformPtp.PlatformPtpServo.LastSetTime()
            self.last_set_time.parent = self
            self._children_name_map["last_set_time"] = "last-set-time"
            self._children_yang_names.add("last-set-time")

            self.last_received_t1 = PlatformPtp.PlatformPtpServo.LastReceivedT1()
            self.last_received_t1.parent = self
            self._children_name_map["last_received_t1"] = "last-received-t1"
            self._children_yang_names.add("last-received-t1")

            self.last_received_t2 = PlatformPtp.PlatformPtpServo.LastReceivedT2()
            self.last_received_t2.parent = self
            self._children_name_map["last_received_t2"] = "last-received-t2"
            self._children_yang_names.add("last-received-t2")

            self.last_received_t3 = PlatformPtp.PlatformPtpServo.LastReceivedT3()
            self.last_received_t3.parent = self
            self._children_name_map["last_received_t3"] = "last-received-t3"
            self._children_yang_names.add("last-received-t3")

            self.last_received_t4 = PlatformPtp.PlatformPtpServo.LastReceivedT4()
            self.last_received_t4.parent = self
            self._children_name_map["last_received_t4"] = "last-received-t4"
            self._children_yang_names.add("last-received-t4")

            self.pre_received_t1 = PlatformPtp.PlatformPtpServo.PreReceivedT1()
            self.pre_received_t1.parent = self
            self._children_name_map["pre_received_t1"] = "pre-received-t1"
            self._children_yang_names.add("pre-received-t1")

            self.pre_received_t2 = PlatformPtp.PlatformPtpServo.PreReceivedT2()
            self.pre_received_t2.parent = self
            self._children_name_map["pre_received_t2"] = "pre-received-t2"
            self._children_yang_names.add("pre-received-t2")

            self.pre_received_t3 = PlatformPtp.PlatformPtpServo.PreReceivedT3()
            self.pre_received_t3.parent = self
            self._children_name_map["pre_received_t3"] = "pre-received-t3"
            self._children_yang_names.add("pre-received-t3")

            self.pre_received_t4 = PlatformPtp.PlatformPtpServo.PreReceivedT4()
            self.pre_received_t4.parent = self
            self._children_name_map["pre_received_t4"] = "pre-received-t4"
            self._children_yang_names.add("pre-received-t4")
            self._segment_path = lambda: "platform-ptp-servo"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PlatformPtp.PlatformPtpServo, ['lock_status', 'running', 'device_status', 'log_level', 'phase_accuracy_last', 'num_sync_timestamp', 'num_delay_timestamp', 'num_set_time', 'num_step_time', 'num_adjust_freq', 'num_adjust_freq_time', 'last_adjust_freq', 'last_step_time', 'num_discard_sync_timestamp', 'num_discard_delay_timestamp', 'flagof_last_set_time', 'offset_from_master', 'mean_path_delay'], name, value)


        class LastSetTime(Entity):
            """
            last input of setTime
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.LastSetTime, self).__init__()

                self.yang_name = "last-set-time"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "last-set-time"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.LastSetTime, ['second', 'nano_second'], name, value)


        class LastReceivedT1(Entity):
            """
            last T1 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.LastReceivedT1, self).__init__()

                self.yang_name = "last-received-t1"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "last-received-t1"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.LastReceivedT1, ['second', 'nano_second'], name, value)


        class LastReceivedT2(Entity):
            """
            last T2 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.LastReceivedT2, self).__init__()

                self.yang_name = "last-received-t2"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "last-received-t2"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.LastReceivedT2, ['second', 'nano_second'], name, value)


        class LastReceivedT3(Entity):
            """
            last T3 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.LastReceivedT3, self).__init__()

                self.yang_name = "last-received-t3"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "last-received-t3"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.LastReceivedT3, ['second', 'nano_second'], name, value)


        class LastReceivedT4(Entity):
            """
            last T4 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.LastReceivedT4, self).__init__()

                self.yang_name = "last-received-t4"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "last-received-t4"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.LastReceivedT4, ['second', 'nano_second'], name, value)


        class PreReceivedT1(Entity):
            """
            pre T1 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.PreReceivedT1, self).__init__()

                self.yang_name = "pre-received-t1"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "pre-received-t1"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.PreReceivedT1, ['second', 'nano_second'], name, value)


        class PreReceivedT2(Entity):
            """
            pre T2 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.PreReceivedT2, self).__init__()

                self.yang_name = "pre-received-t2"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "pre-received-t2"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.PreReceivedT2, ['second', 'nano_second'], name, value)


        class PreReceivedT3(Entity):
            """
            pre T3 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.PreReceivedT3, self).__init__()

                self.yang_name = "pre-received-t3"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "pre-received-t3"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.PreReceivedT3, ['second', 'nano_second'], name, value)


        class PreReceivedT4(Entity):
            """
            pre T4 timestamp reveiced
            
            .. attribute:: second
            
            	value of second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nano_second
            
            	value of nano second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'asr9k-ptp-pd-oper'
            _revision = '2017-03-16'

            def __init__(self):
                super(PlatformPtp.PlatformPtpServo.PreReceivedT4, self).__init__()

                self.yang_name = "pre-received-t4"
                self.yang_parent_name = "platform-ptp-servo"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('second', YLeaf(YType.uint32, 'second')),
                    ('nano_second', YLeaf(YType.uint32, 'nano-second')),
                ])
                self.second = None
                self.nano_second = None
                self._segment_path = lambda: "pre-received-t4"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-oper:platform-ptp/platform-ptp-servo/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PlatformPtp.PlatformPtpServo.PreReceivedT4, ['second', 'nano_second'], name, value)

    def clone_ptr(self):
        self._top_entity = PlatformPtp()
        return self._top_entity

