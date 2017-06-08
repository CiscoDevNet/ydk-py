""" ietf_ptp_dataset 

This YANG module defines a data model for the configuration
of IEEE 1588\-2008 clocks, and also for retrieval of the state
data of IEEE 1588\-2008 clocks.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DelayMechanismEnumerationEnum(Enum):
    """
    DelayMechanismEnumerationEnum

    The propagation delay measuring option used by the

    port. Values for this enumeration are specified

    by the IEEE 1588 standard exclusively.

    .. data:: E2E = 1

    	The port uses the delay request-response

    	mechanism.

    .. data:: P2P = 2

    	The port uses the peer delay mechanism.

    .. data:: DISABLED = 254

    	The port does not implement any delay

    	mechanism.

    """

    E2E = 1

    P2P = 2

    DISABLED = 254


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
        return meta._meta_table['DelayMechanismEnumerationEnum']


class PortStateEnumerationEnum(Enum):
    """
    PortStateEnumerationEnum

    The current state of the protocol engine associated

    with the port.  Values for this enumeration are specified

    by the IEEE 1588 standard exclusively.

    .. data:: INITIALIZING = 1

    	The port is initializing its data sets, hardware, and

    	communication facilities.

    .. data:: FAULTY = 2

    	The port is in the fault state.

    .. data:: DISABLED = 3

    	The port is disabled, and is not communicating PTP

    	messages (other than possibly PTP management

    	messages).

    .. data:: LISTENING = 4

    	The port is listening for an Announce message.

    .. data:: PRE_MASTER = 5

    	The port is in the pre-master state.

    .. data:: MASTER = 6

    	The port is behaving as a master port.

    .. data:: PASSIVE = 7

    	The port is in the passive state.

    .. data:: UNCALIBRATED = 8

    	A master port has been selected, but the port is still

    	in the uncalibrated state.

    .. data:: SLAVE = 9

    	The port is synchronizing to the selected

    	master port.

    """

    INITIALIZING = 1

    FAULTY = 2

    DISABLED = 3

    LISTENING = 4

    PRE_MASTER = 5

    MASTER = 6

    PASSIVE = 7

    UNCALIBRATED = 8

    SLAVE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
        return meta._meta_table['PortStateEnumerationEnum']



class InstanceList(object):
    """
    List of one or more PTP datasets in the device, one for
    each domain (see IEEE 1588\-2008 subclause 6.3).
    Each PTP dataset represents a distinct instance of
    PTP implementation in the device (i.e. distinct
    Ordinary Clock or Boundary Clock).
    
    .. attribute:: instance_number  <key>
    
    	The instance number of the current PTP instance
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: current_ds
    
    	The current data set of the clock
    	**type**\:   :py:class:`CurrentDs <ydk.models.ietf.ietf_ptp_dataset.InstanceList.CurrentDs>`
    
    .. attribute:: default_ds
    
    	The default data set of the clock
    	**type**\:   :py:class:`DefaultDs <ydk.models.ietf.ietf_ptp_dataset.InstanceList.DefaultDs>`
    
    .. attribute:: parent_ds
    
    	The parent data set of the clock
    	**type**\:   :py:class:`ParentDs <ydk.models.ietf.ietf_ptp_dataset.InstanceList.ParentDs>`
    
    .. attribute:: port_ds_list
    
    	List of port data sets of the clock
    	**type**\: list of    :py:class:`PortDsList <ydk.models.ietf.ietf_ptp_dataset.InstanceList.PortDsList>`
    
    .. attribute:: time_properties_ds
    
    	The timeProperties data set of the clock
    	**type**\:   :py:class:`TimePropertiesDs <ydk.models.ietf.ietf_ptp_dataset.InstanceList.TimePropertiesDs>`
    
    

    """

    _prefix = 'ptp-dataset'
    _revision = '2017-02-08'

    def __init__(self):
        self.instance_number = None
        self.current_ds = InstanceList.CurrentDs()
        self.current_ds.parent = self
        self.default_ds = InstanceList.DefaultDs()
        self.default_ds.parent = self
        self.parent_ds = InstanceList.ParentDs()
        self.parent_ds.parent = self
        self.port_ds_list = YList()
        self.port_ds_list.parent = self
        self.port_ds_list.name = 'port_ds_list'
        self.time_properties_ds = InstanceList.TimePropertiesDs()
        self.time_properties_ds.parent = self


    class DefaultDs(object):
        """
        The default data set of the clock.
        
        .. attribute:: clock_identity
        
        	The clockIdentity of the local clock
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: clock_quality
        
        	The clockQuality of the local clock
        	**type**\:   :py:class:`ClockQuality <ydk.models.ietf.ietf_ptp_dataset.InstanceList.DefaultDs.ClockQuality>`
        
        .. attribute:: domain_number
        
        	The domain number of the current syntonization domain
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: number_ports
        
        	The number of PTP ports on the device
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: priority1
        
        	The priority1 attribute of the local clock
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: priority2
        
        	The priority2 attribute of the local clock. 
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: slave_only
        
        	When set, the clock is a slave\-only clock
        	**type**\:  bool
        
        .. attribute:: two_step_flag
        
        	When set, the clock is a two\-step clock; otherwise, the clock is a one\-step clock
        	**type**\:  bool
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.clock_identity = None
            self.clock_quality = InstanceList.DefaultDs.ClockQuality()
            self.clock_quality.parent = self
            self.domain_number = None
            self.number_ports = None
            self.priority1 = None
            self.priority2 = None
            self.slave_only = None
            self.two_step_flag = None


        class ClockQuality(object):
            """
            The clockQuality of the local clock.
            
            .. attribute:: clock_accuracy
            
            	The clockAccuracy indicates the expected accuracy of the clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_class
            
            	The clockClass denotes the traceability of the time or frequency distributed by the clock
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 248
            
            .. attribute:: offset_scaled_log_variance
            
            	The offsetScaledLogVariance provides an estimate of the variations of the clock from a linear timescale when it is not synchronized to another clock using the protocol
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ptp-dataset'
            _revision = '2017-02-08'

            def __init__(self):
                self.parent = None
                self.clock_accuracy = None
                self.clock_class = None
                self.offset_scaled_log_variance = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ptp-dataset:clock-quality'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.clock_accuracy is not None:
                    return True

                if self.clock_class is not None:
                    return True

                if self.offset_scaled_log_variance is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
                return meta._meta_table['InstanceList.DefaultDs.ClockQuality']['meta_info']

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-ptp-dataset:default-ds'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clock_identity is not None:
                return True

            if self.clock_quality is not None and self.clock_quality._has_data():
                return True

            if self.domain_number is not None:
                return True

            if self.number_ports is not None:
                return True

            if self.priority1 is not None:
                return True

            if self.priority2 is not None:
                return True

            if self.slave_only is not None:
                return True

            if self.two_step_flag is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['InstanceList.DefaultDs']['meta_info']


    class CurrentDs(object):
        """
        The current data set of the clock.
        
        .. attribute:: mean_path_delay
        
        	The current value of the mean propagation time between a master and a slave clock as computed by the slave
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        .. attribute:: offset_from_master
        
        	The current value of the time difference between a master and a slave clock as computed by the slave
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        .. attribute:: steps_removed
        
        	The number of communication paths traversed between the local clock and the grandmaster clock
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 0
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.mean_path_delay = None
            self.offset_from_master = None
            self.steps_removed = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-ptp-dataset:current-ds'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.mean_path_delay is not None:
                return True

            if self.offset_from_master is not None:
                return True

            if self.steps_removed is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['InstanceList.CurrentDs']['meta_info']


    class ParentDs(object):
        """
        The parent data set of the clock.
        
        .. attribute:: grandmaster_clock_quality
        
        	The clockQuality of the grandmaster clock
        	**type**\:   :py:class:`GrandmasterClockQuality <ydk.models.ietf.ietf_ptp_dataset.InstanceList.ParentDs.GrandmasterClockQuality>`
        
        .. attribute:: grandmaster_identity
        
        	The clockIdentity attribute of the grandmaster clock
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: grandmaster_priority1
        
        	The priority1 attribute of the grandmaster clock
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: grandmaster_priority2
        
        	The priority2 attribute of the grandmaster clock
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: observed_parent_clock_phase_change_rate
        
        	An estimate of the parent clock's phase change rate as observed by the slave clock
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: observed_parent_offset_scaled_log_variance
        
        	An estimate of the parent clock's PTP variance as observed by the slave clock
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**default value**\: 0xFFFF
        
        .. attribute:: parent_port_identity
        
        	The portIdentity of the port on the master
        	**type**\:   :py:class:`ParentPortIdentity <ydk.models.ietf.ietf_ptp_dataset.InstanceList.ParentDs.ParentPortIdentity>`
        
        .. attribute:: parent_stats
        
        	When set, the values of observedParentOffsetScaledLogVariance and observedParentClockPhaseChangeRate of parentDS have been measured and are valid
        	**type**\:  bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.grandmaster_clock_quality = InstanceList.ParentDs.GrandmasterClockQuality()
            self.grandmaster_clock_quality.parent = self
            self.grandmaster_identity = None
            self.grandmaster_priority1 = None
            self.grandmaster_priority2 = None
            self.observed_parent_clock_phase_change_rate = None
            self.observed_parent_offset_scaled_log_variance = None
            self.parent_port_identity = InstanceList.ParentDs.ParentPortIdentity()
            self.parent_port_identity.parent = self
            self.parent_stats = None


        class ParentPortIdentity(object):
            """
            The portIdentity of the port on the master
            
            .. attribute:: clock_identity
            
            	Identity of the clock
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: port_number
            
            	Port number
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ptp-dataset'
            _revision = '2017-02-08'

            def __init__(self):
                self.parent = None
                self.clock_identity = None
                self.port_number = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ptp-dataset:parent-port-identity'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.clock_identity is not None:
                    return True

                if self.port_number is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
                return meta._meta_table['InstanceList.ParentDs.ParentPortIdentity']['meta_info']


        class GrandmasterClockQuality(object):
            """
            The clockQuality of the grandmaster clock.
            
            .. attribute:: clock_accuracy
            
            	The clockAccuracy indicates the expected accuracy of the clock
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: clock_class
            
            	The clockClass denotes the traceability of the time or frequency distributed by the clock
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 248
            
            .. attribute:: offset_scaled_log_variance
            
            	The offsetScaledLogVariance provides an estimate of the variations of the clock from a linear timescale when it is not synchronized to another clock using the protocol
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ptp-dataset'
            _revision = '2017-02-08'

            def __init__(self):
                self.parent = None
                self.clock_accuracy = None
                self.clock_class = None
                self.offset_scaled_log_variance = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ptp-dataset:grandmaster-clock-quality'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.clock_accuracy is not None:
                    return True

                if self.clock_class is not None:
                    return True

                if self.offset_scaled_log_variance is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
                return meta._meta_table['InstanceList.ParentDs.GrandmasterClockQuality']['meta_info']

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-ptp-dataset:parent-ds'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.grandmaster_clock_quality is not None and self.grandmaster_clock_quality._has_data():
                return True

            if self.grandmaster_identity is not None:
                return True

            if self.grandmaster_priority1 is not None:
                return True

            if self.grandmaster_priority2 is not None:
                return True

            if self.observed_parent_clock_phase_change_rate is not None:
                return True

            if self.observed_parent_offset_scaled_log_variance is not None:
                return True

            if self.parent_port_identity is not None and self.parent_port_identity._has_data():
                return True

            if self.parent_stats is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['InstanceList.ParentDs']['meta_info']


    class TimePropertiesDs(object):
        """
        The timeProperties data set of the clock.
        
        .. attribute:: current_utc_offset
        
        	The offset between TAI and UTC when the epoch of the PTP system is the PTP epoch, i.e., when ptp\-timescale is TRUE; otherwise, the value has no meaning
        	**type**\:  int
        
        	**range:** \-32768..32767
        
        .. attribute:: current_utc_offset_valid
        
        	When set, the current UTC offset is valid
        	**type**\:  bool
        
        .. attribute:: frequency_traceable
        
        	When set, the frequency determining the timescale is traceable to a primary reference
        	**type**\:  bool
        
        .. attribute:: leap59
        
        	When set, the last minute of the current UTC day contains 59 seconds
        	**type**\:  bool
        
        .. attribute:: leap61
        
        	When set, the last minute of the current UTC day contains 61 seconds
        	**type**\:  bool
        
        .. attribute:: ptp_timescale
        
        	When set, the clock timescale of the grandmaster     clock is PTP; otherwise, the timescale is ARB    (arbitrary)
        	**type**\:  bool
        
        .. attribute:: time_source
        
        	The source of time used by the grandmaster clock
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: time_traceable
        
        	When set, the timescale and the currentUtcOffset are    traceable to a primary reference
        	**type**\:  bool
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.current_utc_offset = None
            self.current_utc_offset_valid = None
            self.frequency_traceable = None
            self.leap59 = None
            self.leap61 = None
            self.ptp_timescale = None
            self.time_source = None
            self.time_traceable = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-ptp-dataset:time-properties-ds'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.current_utc_offset is not None:
                return True

            if self.current_utc_offset_valid is not None:
                return True

            if self.frequency_traceable is not None:
                return True

            if self.leap59 is not None:
                return True

            if self.leap61 is not None:
                return True

            if self.ptp_timescale is not None:
                return True

            if self.time_source is not None:
                return True

            if self.time_traceable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['InstanceList.TimePropertiesDs']['meta_info']


    class PortDsList(object):
        """
        List of port data sets of the clock.
        
        .. attribute:: port_number  <key>
        
        	Refers to the portNumber memer of portDS.portIdentity
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**refers to**\:  :py:class:`port_number <ydk.models.ietf.ietf_ptp_dataset.InstanceList.PortDsList.PortIdentity>`
        
        .. attribute:: announce_receipt_timeout
        
        	The number of announceInterval that have to pass without receipt of an Announce message before the occurrence of the event ANNOUNCE\_RECEIPT\_TIMEOUT\_ EXPIRES
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: delay_mechanism
        
        	The propagation delay measuring option used by the port in computing meanPathDelay
        	**type**\:   :py:class:`DelayMechanismEnumerationEnum <ydk.models.ietf.ietf_ptp_dataset.DelayMechanismEnumerationEnum>`
        
        .. attribute:: log_announce_interval
        
        	The base\-two logarithm of the mean announceInterval (mean time interval between successive Announce messages)
        	**type**\:  int
        
        	**range:** \-128..127
        
        .. attribute:: log_min_delay_req_interval
        
        	The base\-two logarithm of the minDelayReqInterval (the minimum permitted mean time interval between successive Delay\_Req messages)
        	**type**\:  int
        
        	**range:** \-128..127
        
        .. attribute:: log_min_pdelay_req_interval
        
        	The base\-two logarithm of the minPdelayReqInterval (minimum permitted mean time interval between successive Pdelay\_Req messages)
        	**type**\:  int
        
        	**range:** \-128..127
        
        .. attribute:: log_sync_interval
        
        	The base\-two logarithm of the mean SyncInterval for multicast messages.  The rates for unicast transmissions are negotiated separately on a per port basis and are not constrained by this attribute
        	**type**\:  int
        
        	**range:** \-128..127
        
        .. attribute:: peer_mean_path_delay
        
        	An estimate of the current one\-way propagation delay on the link when the delayMechanism is P2P; otherwise, it is zero
        	**type**\:  int
        
        	**range:** \-9223372036854775808..9223372036854775807
        
        	**default value**\: 0
        
        .. attribute:: port_identity
        
        	The portIdentity attribute of the local port
        	**type**\:   :py:class:`PortIdentity <ydk.models.ietf.ietf_ptp_dataset.InstanceList.PortDsList.PortIdentity>`
        
        .. attribute:: port_state
        
        	Current state associated with the port
        	**type**\:   :py:class:`PortStateEnumerationEnum <ydk.models.ietf.ietf_ptp_dataset.PortStateEnumerationEnum>`
        
        	**default value**\: INITIALIZING
        
        .. attribute:: version_number
        
        	The PTP version in use on the port
        	**type**\:  int
        
        	**range:** 0..255
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.port_number = None
            self.announce_receipt_timeout = None
            self.delay_mechanism = None
            self.log_announce_interval = None
            self.log_min_delay_req_interval = None
            self.log_min_pdelay_req_interval = None
            self.log_sync_interval = None
            self.peer_mean_path_delay = None
            self.port_identity = InstanceList.PortDsList.PortIdentity()
            self.port_identity.parent = self
            self.port_state = None
            self.version_number = None


        class PortIdentity(object):
            """
            The portIdentity attribute of the local port.
            
            .. attribute:: clock_identity
            
            	Identity of the clock
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: port_number
            
            	Port number
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ptp-dataset'
            _revision = '2017-02-08'

            def __init__(self):
                self.parent = None
                self.clock_identity = None
                self.port_number = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ptp-dataset:port-identity'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.clock_identity is not None:
                    return True

                if self.port_number is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
                return meta._meta_table['InstanceList.PortDsList.PortIdentity']['meta_info']

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')
            if self.port_number is None:
                raise YPYModelError('Key property port_number is None')

            return self.parent._common_path +'/ietf-ptp-dataset:port-ds-list[ietf-ptp-dataset:port-number = ' + str(self.port_number) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.port_number is not None:
                return True

            if self.announce_receipt_timeout is not None:
                return True

            if self.delay_mechanism is not None:
                return True

            if self.log_announce_interval is not None:
                return True

            if self.log_min_delay_req_interval is not None:
                return True

            if self.log_min_pdelay_req_interval is not None:
                return True

            if self.log_sync_interval is not None:
                return True

            if self.peer_mean_path_delay is not None:
                return True

            if self.port_identity is not None and self.port_identity._has_data():
                return True

            if self.port_state is not None:
                return True

            if self.version_number is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['InstanceList.PortDsList']['meta_info']

    @property
    def _common_path(self):
        if self.instance_number is None:
            raise YPYModelError('Key property instance_number is None')

        return '/ietf-ptp-dataset:instance-list[ietf-ptp-dataset:instance-number = ' + str(self.instance_number) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.instance_number is not None:
            return True

        if self.current_ds is not None and self.current_ds._has_data():
            return True

        if self.default_ds is not None and self.default_ds._has_data():
            return True

        if self.parent_ds is not None and self.parent_ds._has_data():
            return True

        if self.port_ds_list is not None:
            for child_ref in self.port_ds_list:
                if child_ref._has_data():
                    return True

        if self.time_properties_ds is not None and self.time_properties_ds._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
        return meta._meta_table['InstanceList']['meta_info']


class TransparentClockDefaultDs(object):
    """
    The members of the transparentClockDefault Data Set
    
    .. attribute:: clock_identity
    
    	The clockIdentity of the transparent clock
    	**type**\:  str
    
    	**length:** 8
    
    .. attribute:: delay_mechanism
    
    	The propagation delay measuring option used by the transparent clock
    	**type**\:   :py:class:`DelayMechanismEnumerationEnum <ydk.models.ietf.ietf_ptp_dataset.DelayMechanismEnumerationEnum>`
    
    .. attribute:: number_ports
    
    	The number of PTP ports on the device
    	**type**\:  int
    
    	**range:** 0..65535
    
    .. attribute:: primary_domain
    
    	The domainNumber of the primary syntonization domain
    	**type**\:  int
    
    	**range:** 0..255
    
    	**default value**\: 0
    
    

    """

    _prefix = 'ptp-dataset'
    _revision = '2017-02-08'

    def __init__(self):
        self.clock_identity = None
        self.delay_mechanism = None
        self.number_ports = None
        self.primary_domain = None

    @property
    def _common_path(self):

        return '/ietf-ptp-dataset:transparent-clock-default-ds'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.clock_identity is not None:
            return True

        if self.delay_mechanism is not None:
            return True

        if self.number_ports is not None:
            return True

        if self.primary_domain is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
        return meta._meta_table['TransparentClockDefaultDs']['meta_info']


class TransparentClockPortDsList(object):
    """
    List of transparentClockPort data sets
    of the transparent clock.
    
    .. attribute:: port_number  <key>
    
    	Refers to the portNumber memer of transparentClockPortDS.portIdentity
    	**type**\:  int
    
    	**range:** 0..65535
    
    	**refers to**\:  :py:class:`port_number <ydk.models.ietf.ietf_ptp_dataset.TransparentClockPortDsList.PortIdentity>`
    
    .. attribute:: faulty_flag
    
    	When set, the port is faulty
    	**type**\:  bool
    
    	**default value**\: false
    
    .. attribute:: log_min_pdelay_req_interval
    
    	The logarithm to the base 2 of the minPdelayReqInterval (minimum permitted mean time interval between successive Pdelay\_Req messages)
    	**type**\:  int
    
    	**range:** \-128..127
    
    .. attribute:: peer_mean_path_delay
    
    	An estimate of the current one\-way propagation delay on the link when the delayMechanism is P2P; otherwise, it is zero
    	**type**\:  int
    
    	**range:** \-9223372036854775808..9223372036854775807
    
    	**default value**\: 0
    
    .. attribute:: port_identity
    
    	The portIdentity of the local port
    	**type**\:   :py:class:`PortIdentity <ydk.models.ietf.ietf_ptp_dataset.TransparentClockPortDsList.PortIdentity>`
    
    

    """

    _prefix = 'ptp-dataset'
    _revision = '2017-02-08'

    def __init__(self):
        self.port_number = None
        self.faulty_flag = None
        self.log_min_pdelay_req_interval = None
        self.peer_mean_path_delay = None
        self.port_identity = TransparentClockPortDsList.PortIdentity()
        self.port_identity.parent = self


    class PortIdentity(object):
        """
        The portIdentity of the local port.
        
        .. attribute:: clock_identity
        
        	Identity of the clock
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: port_number
        
        	Port number
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'ptp-dataset'
        _revision = '2017-02-08'

        def __init__(self):
            self.parent = None
            self.clock_identity = None
            self.port_number = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-ptp-dataset:port-identity'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.clock_identity is not None:
                return True

            if self.port_number is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
            return meta._meta_table['TransparentClockPortDsList.PortIdentity']['meta_info']

    @property
    def _common_path(self):
        if self.port_number is None:
            raise YPYModelError('Key property port_number is None')

        return '/ietf-ptp-dataset:transparent-clock-port-ds-list[ietf-ptp-dataset:port-number = ' + str(self.port_number) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.port_number is not None:
            return True

        if self.faulty_flag is not None:
            return True

        if self.log_min_pdelay_req_interval is not None:
            return True

        if self.peer_mean_path_delay is not None:
            return True

        if self.port_identity is not None and self.port_identity._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ptp_dataset as meta
        return meta._meta_table['TransparentClockPortDsList']['meta_info']


