""" Cisco_IOS_XR_icpe_infra_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package operational data.

This module contains definitions
for the following management objects\:
  nv\-satellite\: Satellite operational information

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IcpeGcoOperControlReason_Enum(Enum):
    """
    IcpeGcoOperControlReason_Enum

    Icpe gco oper control reason

    """

    """

    Unknown error

    """
    ICPE_GCO_OPER_CONTROL_REASON_UNKNOWN_ERROR = 0

    """

    Wrong chassis type

    """
    ICPE_GCO_OPER_CONTROL_REASON_WRONG_CHASSIS_TYPE = 1

    """

    Wrong chassis serial

    """
    ICPE_GCO_OPER_CONTROL_REASON_WRONG_CHASSIS_SERIAL = 2

    """

    Needs to upgrade

    """
    ICPE_GCO_OPER_CONTROL_REASON_NEEDS_TO_UPGRADE = 3

    """

    None

    """
    ICPE_GCO_OPER_CONTROL_REASON_NONE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeGcoOperControlReason_Enum']


class IcpeOperConflict_Enum(Enum):
    """
    IcpeOperConflict_Enum

    Icpe oper conflict

    """

    """

    Not calculated

    """
    ICPE_OPER_CONFLICT_NOT_CALCULATED = 0

    """

    No conflict

    """
    ICPE_OPER_CONFLICT_NO_CONFLICT = 1

    """

    Satellite not configured

    """
    ICPE_OPER_CONFLICT_SATELLITE_NOT_CONFIGURED = 2

    """

    Satellite no type

    """
    ICPE_OPER_CONFLICT_SATELLITE_NO_TYPE = 3

    """

    Satellite id invalid

    """
    ICPE_OPER_CONFLICT_SATELLITE_ID_INVALID = 4

    """

    Satellite no ipv4 addr

    """
    ICPE_OPER_CONFLICT_SATELLITE_NO_IPV4_ADDR = 5

    """

    Satellite conflicting ipv4 addr

    """
    ICPE_OPER_CONFLICT_SATELLITE_CONFLICTING_IPV4_ADDR = 6

    """

    No configured links

    """
    ICPE_OPER_CONFLICT_NO_CONFIGURED_LINKS = 7

    """

    No discovered links

    """
    ICPE_OPER_CONFLICT_NO_DISCOVERED_LINKS = 8

    """

    Invalid ports

    """
    ICPE_OPER_CONFLICT_INVALID_PORTS = 9

    """

    Ports overlap

    """
    ICPE_OPER_CONFLICT_PORTS_OVERLAP = 10

    """

    Waiting for ipv4 addr

    """
    ICPE_OPER_CONFLICT_WAITING_FOR_IPV4_ADDR = 11

    """

    Waiting for VRF

    """
    ICPE_OPER_CONFLICT_WAITING_FOR_VRF = 12

    """

    Different ipv4 addr

    """
    ICPE_OPER_CONFLICT_DIFFERENT_IPV4_ADDR = 13

    """

    Different VRF

    """
    ICPE_OPER_CONFLICT_DIFFERENT_VRF = 14

    """

    Satellite link ipv4 overlap

    """
    ICPE_OPER_CONFLICT_SATELLITE_LINK_IPV4_OVERLAP = 15

    """

    Waiting for ident

    """
    ICPE_OPER_CONFLICT_WAITING_FOR_IDENT = 16

    """

    Multiple ids

    """
    ICPE_OPER_CONFLICT_MULTIPLE_IDS = 17

    """

    Multiple satellites

    """
    ICPE_OPER_CONFLICT_MULTIPLE_SATELLITES = 18

    """

    Ident rejected

    """
    ICPE_OPER_CONFLICT_IDENT_REJECTED = 19

    """

    Interface down

    """
    ICPE_OPER_CONFLICT_INTERFACE_DOWN = 20

    """

    Auto IP unavailable

    """
    ICPE_OPER_CONFLICT_AUTO_IP_UNAVAILABLE = 21

    """

    Satellite auto IP link manual IP

    """
    ICPE_OPER_CONFLICT_SATELLITE_AUTO_IP_LINK_MANUAL_IP = 22

    """

    Link auto IP satellite manual IP

    """
    ICPE_OPER_CONFLICT_LINK_AUTO_IP_SATELLITE_MANUAL_IP = 23

    """

    Serial num mismatch

    """
    ICPE_OPER_CONFLICT_SERIAL_NUM_MISMATCH = 24

    """

    Satellite not identified

    """
    ICPE_OPER_CONFLICT_SATELLITE_NOT_IDENTIFIED = 25

    """

    Satellite unsupported type

    """
    ICPE_OPER_CONFLICT_SATELLITE_UNSUPPORTED_TYPE = 26

    """

    Satellite partition unsupported

    """
    ICPE_OPER_CONFLICT_SATELLITE_PARTITION_UNSUPPORTED = 27

    """

    Satellite no serial number

    """
    ICPE_OPER_CONFLICT_SATELLITE_NO_SERIAL_NUMBER = 28

    """

    Satellite conflicting serial number

    """
    ICPE_OPER_CONFLICT_SATELLITE_CONFLICTING_SERIAL_NUMBER = 29

    """

    Satellite link waiting for arp

    """
    ICPE_OPER_CONFLICT_SATELLITE_LINK_WAITING_FOR_ARP = 30

    """

    Host PE isolated split brain

    """
    ICPE_OPER_CONFLICT_HOST_PE_ISOLATED_SPLIT_BRAIN = 31

    """

    Fabric ICCP group inconsistent

    """
    ICPE_OPER_CONFLICT_FABRIC_ICCP_GROUP_INCONSISTENT = 32

    """

    Invalid ICCP group

    """
    ICPE_OPER_CONFLICT_INVALID_ICCP_GROUP = 33

    """

    Port rejected

    """
    ICPE_OPER_CONFLICT_PORT_REJECTED = 34

    """

    Satellite ICL not supported

    """
    ICPE_OPER_CONFLICT_SATELLITE_ICL_NOT_SUPPORTED = 35

    """

    Multiple serial number

    """
    ICPE_OPER_CONFLICT_MULTIPLE_SERIAL_NUMBER = 36

    """

    Multiple MAC address

    """
    ICPE_OPER_CONFLICT_MULTIPLE_MAC_ADDRESS = 37


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperConflict_Enum']


class IcpeOperDiscdLinkState_Enum(Enum):
    """
    IcpeOperDiscdLinkState_Enum

    Icpe oper discd link state

    """

    """

    Stopped

    """
    ICPE_OPER_DISCD_LINK_STATE_STOPPED = 0

    """

    Probing

    """
    ICPE_OPER_DISCD_LINK_STATE_PROBING = 1

    """

    Configuring

    """
    ICPE_OPER_DISCD_LINK_STATE_CONFIGURING = 2

    """

    Ready

    """
    ICPE_OPER_DISCD_LINK_STATE_READY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperDiscdLinkState_Enum']


class IcpeOperFabricPort_Enum(Enum):
    """
    IcpeOperFabricPort_Enum

    Icpe oper fabric port

    """

    """

    Unknown

    """
    ICPE_OPER_FABRIC_PORT_UNKNOWN = 0

    """

    n v fabric\- gig e

    """
    ICPE_OPER_FABRIC_PORT_N_V_FABRIC_GIG_E = 1

    """

    n v fabric\- ten gig e

    """
    ICPE_OPER_FABRIC_PORT_N_V_FABRIC_TEN_GIG_E = 2

    """

    n v fabric\- hundred gig e

    """
    ICPE_OPER_FABRIC_PORT_N_V_FABRIC_HUNDRED_GIG_E = 3


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperFabricPort_Enum']


class IcpeOperInstallState_Enum(Enum):
    """
    IcpeOperInstallState_Enum

    Icpe oper install state

    """

    """

    Stable

    """
    ICPE_OPER_INSTALL_STATE_STABLE = 0

    """

    Transferring

    """
    ICPE_OPER_INSTALL_STATE_TRANSFERRING = 1

    """

    Transferred

    """
    ICPE_OPER_INSTALL_STATE_TRANSFERRED = 2

    """

    Installing

    """
    ICPE_OPER_INSTALL_STATE_INSTALLING = 3


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperInstallState_Enum']


class IcpeOperPort_Enum(Enum):
    """
    IcpeOperPort_Enum

    Icpe oper port

    """

    """

    Unknown

    """
    ICPE_OPER_PORT_UNKNOWN = 0

    """

    Gigabit ethernet

    """
    ICPE_OPER_PORT_GIGABIT_ETHERNET = 1

    """

    Ten gig e

    """
    ICPE_OPER_PORT_TEN_GIG_E = 2


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperPort_Enum']


class IcpeOperSdacpSessState_Enum(Enum):
    """
    IcpeOperSdacpSessState_Enum

    Icpe oper sdacp sess state

    """

    """

    Not created

    """
    ICPE_OPER_SDACP_SESS_STATE_NOT_CREATED = 0

    """

    Created

    """
    ICPE_OPER_SDACP_SESS_STATE_CREATED = 1

    """

    Authentication not OK

    """
    ICPE_OPER_SDACP_SESS_STATE_AUTHENTICATION_NOT_OK = 2

    """

    Authentication OK

    """
    ICPE_OPER_SDACP_SESS_STATE_AUTHENTICATION_OK = 3

    """

    Version not OK

    """
    ICPE_OPER_SDACP_SESS_STATE_VERSION_NOT_OK = 4

    """

    Up

    """
    ICPE_OPER_SDACP_SESS_STATE_UP = 5

    """

    ISSU

    """
    ICPE_OPER_SDACP_SESS_STATE_ISSU = 6


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperSdacpSessState_Enum']


class IcpeOperVerCheckState_Enum(Enum):
    """
    IcpeOperVerCheckState_Enum

    Icpe oper ver check state

    """

    """

    Unknown

    """
    ICPE_OPER_VER_CHECK_STATE_UNKNOWN = 0

    """

    Not compatible

    """
    ICPE_OPER_VER_CHECK_STATE_NOT_COMPATIBLE = 1

    """

    Current version

    """
    ICPE_OPER_VER_CHECK_STATE_CURRENT_VERSION = 2

    """

    Compatible older

    """
    ICPE_OPER_VER_CHECK_STATE_COMPATIBLE_OLDER = 3

    """

    Compatible newer

    """
    ICPE_OPER_VER_CHECK_STATE_COMPATIBLE_NEWER = 4


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOperVerCheckState_Enum']


class IcpeOpmArbitrationFsmState_Enum(Enum):
    """
    IcpeOpmArbitrationFsmState_Enum

    Icpe opm arbitration fsm state

    """

    """

    Unarbitrated

    """
    ICPE_OPM_ARBITRATION_FSM_STATE_UNARBITRATED = 0

    """

    Waiting

    """
    ICPE_OPM_ARBITRATION_FSM_STATE_WAITING = 1

    """

    Arbitrating

    """
    ICPE_OPM_ARBITRATION_FSM_STATE_ARBITRATING = 2

    """

    Arbitrated

    """
    ICPE_OPM_ARBITRATION_FSM_STATE_ARBITRATED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmArbitrationFsmState_Enum']


class IcpeOpmAuthFsmState_Enum(Enum):
    """
    IcpeOpmAuthFsmState_Enum

    Icpe opm auth fsm state

    """

    """

    Unauth

    """
    ICPE_OPM_AUTH_FSM_STATE_UNAUTH = 0

    """

    Waiting

    """
    ICPE_OPM_AUTH_FSM_STATE_WAITING = 1

    """

    Waiting for auth

    """
    ICPE_OPM_AUTH_FSM_STATE_WAITING_FOR_AUTH = 2

    """

    Waiting for reply

    """
    ICPE_OPM_AUTH_FSM_STATE_WAITING_FOR_REPLY = 3

    """

    Authed

    """
    ICPE_OPM_AUTH_FSM_STATE_AUTHED = 4


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmAuthFsmState_Enum']


class IcpeOpmChanFsmState_Enum(Enum):
    """
    IcpeOpmChanFsmState_Enum

    Icpe opm chan fsm state

    """

    """

    Down

    """
    ICPE_OPM_CHAN_FSM_STATE_DOWN = 0

    """

    Closed

    """
    ICPE_OPM_CHAN_FSM_STATE_CLOSED = 1

    """

    Opening

    """
    ICPE_OPM_CHAN_FSM_STATE_OPENING = 2

    """

    Opened

    """
    ICPE_OPM_CHAN_FSM_STATE_OPENED = 3

    """

    Open

    """
    ICPE_OPM_CHAN_FSM_STATE_OPEN = 4


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmChanFsmState_Enum']


class IcpeOpmController_Enum(Enum):
    """
    IcpeOpmController_Enum

    Icpe opm controller

    """

    """

    Unknown

    """
    ICPE_OPM_CONTROLLER_UNKNOWN = 0

    """

    Primary

    """
    ICPE_OPM_CONTROLLER_PRIMARY = 1

    """

    Secondary

    """
    ICPE_OPM_CONTROLLER_SECONDARY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmController_Enum']


class IcpeOpmResyncFsmState_Enum(Enum):
    """
    IcpeOpmResyncFsmState_Enum

    Icpe opm resync fsm state

    """

    """

    Not open

    """
    ICPE_OPM_RESYNC_FSM_STATE_NOT_OPEN = 0

    """

    Stable

    """
    ICPE_OPM_RESYNC_FSM_STATE_STABLE = 1

    """

    In resync

    """
    ICPE_OPM_RESYNC_FSM_STATE_IN_RESYNC = 2

    """

    Queued

    """
    ICPE_OPM_RESYNC_FSM_STATE_QUEUED = 3

    """

    Resync req

    """
    ICPE_OPM_RESYNC_FSM_STATE_RESYNC_REQ = 4


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmResyncFsmState_Enum']


class IcpeOpmSessState_Enum(Enum):
    """
    IcpeOpmSessState_Enum

    Icpe opm sess state

    """

    """

    Disconnected

    """
    ICPE_OPM_SESS_STATE_DISCONNECTED = 0

    """

    Connecting

    """
    ICPE_OPM_SESS_STATE_CONNECTING = 1

    """

    Authenticating

    """
    ICPE_OPM_SESS_STATE_AUTHENTICATING = 2

    """

    Arbitrating

    """
    ICPE_OPM_SESS_STATE_ARBITRATING = 3

    """

    Waiting for resyncs

    """
    ICPE_OPM_SESS_STATE_WAITING_FOR_RESYNCS = 4

    """

    Connected

    """
    ICPE_OPM_SESS_STATE_CONNECTED = 5


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmSessState_Enum']


class IcpeOpmSyncFsmState_Enum(Enum):
    """
    IcpeOpmSyncFsmState_Enum

    Icpe opm sync fsm state

    """

    """

    Split brain

    """
    ICPE_OPM_SYNC_FSM_STATE_SPLIT_BRAIN = 0

    """

    Waiting

    """
    ICPE_OPM_SYNC_FSM_STATE_WAITING = 1

    """

    Whole brain

    """
    ICPE_OPM_SYNC_FSM_STATE_WHOLE_BRAIN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmSyncFsmState_Enum']


class IcpeOpmTransportState_Enum(Enum):
    """
    IcpeOpmTransportState_Enum

    Icpe opm transport state

    """

    """

    Disconnected

    """
    ICPE_OPM_TRANSPORT_STATE_DISCONNECTED = 0

    """

    ICCP unavailable

    """
    ICPE_OPM_TRANSPORT_STATE_ICCP_UNAVAILABLE = 1

    """

    No member present

    """
    ICPE_OPM_TRANSPORT_STATE_NO_MEMBER_PRESENT = 2

    """

    Member down

    """
    ICPE_OPM_TRANSPORT_STATE_MEMBER_DOWN = 3

    """

    Member not reachable

    """
    ICPE_OPM_TRANSPORT_STATE_MEMBER_NOT_REACHABLE = 4

    """

    Waiting for app connect

    """
    ICPE_OPM_TRANSPORT_STATE_WAITING_FOR_APP_CONNECT = 5

    """

    Waiting for app connect response

    """
    ICPE_OPM_TRANSPORT_STATE_WAITING_FOR_APP_CONNECT_RESPONSE = 6

    """

    Connected

    """
    ICPE_OPM_TRANSPORT_STATE_CONNECTED = 7


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpmTransportState_Enum']


class IcpeOpticalSyncState_Enum(Enum):
    """
    IcpeOpticalSyncState_Enum

    Icpe optical sync state

    """

    """

    Unknown

    """
    ICPE_OPTICAL_SYNC_STATE_UNKNOWN = 0

    """

    Syncing

    """
    ICPE_OPTICAL_SYNC_STATE_SYNCING = 1

    """

    Synced

    """
    ICPE_OPTICAL_SYNC_STATE_SYNCED = 2

    """

    Not connected

    """
    ICPE_OPTICAL_SYNC_STATE_NOT_CONNECTED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['IcpeOpticalSyncState_Enum']



class NvSatellite(object):
    """
    Satellite operational information
    
    .. attribute:: install_op_statuses
    
    	Detailed breakdown of install status table
    	**type**\: :py:class:`InstallOpStatuses <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses>`
    
    .. attribute:: install_progresses
    
    	Current percentage of install table
    	**type**\: :py:class:`InstallProgresses <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses>`
    
    .. attribute:: install_statuses
    
    	Detailed breakdown of install status table
    	**type**\: :py:class:`InstallStatuses <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses>`
    
    .. attribute:: reload_statuses
    
    	Detailed breakdown of reload status table
    	**type**\: :py:class:`ReloadStatuses <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses>`
    
    .. attribute:: satellite_statuses
    
    	Satellite status information table
    	**type**\: :py:class:`SatelliteStatuses <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses>`
    
    .. attribute:: satellite_topologies
    
    	Satellite Topology Information table
    	**type**\: :py:class:`SatelliteTopologies <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies>`
    
    .. attribute:: sdacp_redundancies
    
    	nV Satellite Redundancy Protocol Information table
    	**type**\: :py:class:`SdacpRedundancies <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies>`
    
    

    """

    _prefix = 'icpe-infra-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.install_op_statuses = NvSatellite.InstallOpStatuses()
        self.install_op_statuses.parent = self
        self.install_progresses = NvSatellite.InstallProgresses()
        self.install_progresses.parent = self
        self.install_statuses = NvSatellite.InstallStatuses()
        self.install_statuses.parent = self
        self.reload_statuses = NvSatellite.ReloadStatuses()
        self.reload_statuses.parent = self
        self.satellite_statuses = NvSatellite.SatelliteStatuses()
        self.satellite_statuses.parent = self
        self.satellite_topologies = NvSatellite.SatelliteTopologies()
        self.satellite_topologies.parent = self
        self.sdacp_redundancies = NvSatellite.SdacpRedundancies()
        self.sdacp_redundancies.parent = self


    class InstallOpStatuses(object):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_op_status
        
        	Detailed breakdown of install status
        	**type**\: list of :py:class:`InstallOpStatus <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallOpStatuses.InstallOpStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_op_status = YList()
            self.install_op_status.parent = self
            self.install_op_status.name = 'install_op_status'


        class InstallOpStatus(object):
            """
            Detailed breakdown of install status
            
            .. attribute:: operation_id
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operation_id_xr
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.operation_id = None
                self.operation_id_xr = None
                self.satellite_range = None
                self.sats_activate_aborted = []
                self.sats_activate_failed = []
                self.sats_activating = []
                self.sats_completed = []
                self.sats_no_operation = []
                self.sats_not_initiated = []
                self.sats_transfer_aborted = []
                self.sats_transfer_failed = []
                self.sats_transferring = []

            @property
            def _common_path(self):
                if self.operation_id is None:
                    raise YPYDataValidationError('Key property operation_id is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-op-statuses/Cisco-IOS-XR-icpe-infra-oper:install-op-status[Cisco-IOS-XR-icpe-infra-oper:operation-id = ' + str(self.operation_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.operation_id is not None:
                    return True

                if self.operation_id_xr is not None:
                    return True

                if self.satellite_range is not None:
                    return True

                if self.sats_activate_aborted is not None:
                    for child in self.sats_activate_aborted:
                        if child is not None:
                            return True

                if self.sats_activate_failed is not None:
                    for child in self.sats_activate_failed:
                        if child is not None:
                            return True

                if self.sats_activating is not None:
                    for child in self.sats_activating:
                        if child is not None:
                            return True

                if self.sats_completed is not None:
                    for child in self.sats_completed:
                        if child is not None:
                            return True

                if self.sats_no_operation is not None:
                    for child in self.sats_no_operation:
                        if child is not None:
                            return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_transfer_aborted is not None:
                    for child in self.sats_transfer_aborted:
                        if child is not None:
                            return True

                if self.sats_transfer_failed is not None:
                    for child in self.sats_transfer_failed:
                        if child is not None:
                            return True

                if self.sats_transferring is not None:
                    for child in self.sats_transferring:
                        if child is not None:
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallOpStatuses.InstallOpStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-op-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.install_op_status is not None:
                for child_ref in self.install_op_status:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallOpStatuses']['meta_info']


    class InstallProgresses(object):
        """
        Current percentage of install table
        
        .. attribute:: install_progress
        
        	Current percentage of install
        	**type**\: list of :py:class:`InstallProgress <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallProgresses.InstallProgress>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_progress = YList()
            self.install_progress.parent = self
            self.install_progress.name = 'install_progress'


        class InstallProgress(object):
            """
            Current percentage of install
            
            .. attribute:: progress_percentage
            
            	Progress percentage
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: progress_percentage_xr
            
            	Progress percentage
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: satellite_count
            
            	Satellite count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.progress_percentage = None
                self.progress_percentage_xr = None
                self.satellite_count = None

            @property
            def _common_path(self):
                if self.progress_percentage is None:
                    raise YPYDataValidationError('Key property progress_percentage is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-progresses/Cisco-IOS-XR-icpe-infra-oper:install-progress[Cisco-IOS-XR-icpe-infra-oper:progress-percentage = ' + str(self.progress_percentage) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.progress_percentage is not None:
                    return True

                if self.progress_percentage_xr is not None:
                    return True

                if self.satellite_count is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallProgresses.InstallProgress']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-progresses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.install_progress is not None:
                for child_ref in self.install_progress:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallProgresses']['meta_info']


    class InstallStatuses(object):
        """
        Detailed breakdown of install status table
        
        .. attribute:: install_status
        
        	Detailed breakdown of install status
        	**type**\: list of :py:class:`InstallStatus <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.InstallStatuses.InstallStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.install_status = YList()
            self.install_status.parent = self
            self.install_status.name = 'install_status'


        class InstallStatus(object):
            """
            Detailed breakdown of install status
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: operation_id
            
            	Operation ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_range_xr
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_activate_aborted
            
            	Sats activate aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activate_failed
            
            	Sats activate failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_activating
            
            	Sats activating
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_completed
            
            	Sats completed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_no_operation
            
            	Sats no operation
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_aborted
            
            	Sats transfer aborted
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transfer_failed
            
            	Sats transfer failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_transferring
            
            	Sats transferring
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.satellite_range = None
                self.operation_id = None
                self.satellite_range_xr = None
                self.sats_activate_aborted = []
                self.sats_activate_failed = []
                self.sats_activating = []
                self.sats_completed = []
                self.sats_no_operation = []
                self.sats_not_initiated = []
                self.sats_transfer_aborted = []
                self.sats_transfer_failed = []
                self.sats_transferring = []

            @property
            def _common_path(self):
                if self.satellite_range is None:
                    raise YPYDataValidationError('Key property satellite_range is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-statuses/Cisco-IOS-XR-icpe-infra-oper:install-status[Cisco-IOS-XR-icpe-infra-oper:satellite-range = ' + str(self.satellite_range) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.satellite_range is not None:
                    return True

                if self.operation_id is not None:
                    return True

                if self.satellite_range_xr is not None:
                    return True

                if self.sats_activate_aborted is not None:
                    for child in self.sats_activate_aborted:
                        if child is not None:
                            return True

                if self.sats_activate_failed is not None:
                    for child in self.sats_activate_failed:
                        if child is not None:
                            return True

                if self.sats_activating is not None:
                    for child in self.sats_activating:
                        if child is not None:
                            return True

                if self.sats_completed is not None:
                    for child in self.sats_completed:
                        if child is not None:
                            return True

                if self.sats_no_operation is not None:
                    for child in self.sats_no_operation:
                        if child is not None:
                            return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_transfer_aborted is not None:
                    for child in self.sats_transfer_aborted:
                        if child is not None:
                            return True

                if self.sats_transfer_failed is not None:
                    for child in self.sats_transfer_failed:
                        if child is not None:
                            return True

                if self.sats_transferring is not None:
                    for child in self.sats_transferring:
                        if child is not None:
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.InstallStatuses.InstallStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:install-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.install_status is not None:
                for child_ref in self.install_status:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.InstallStatuses']['meta_info']


    class ReloadStatuses(object):
        """
        Detailed breakdown of reload status table
        
        .. attribute:: reload_status
        
        	Detailed breakdown of reload status
        	**type**\: list of :py:class:`ReloadStatus <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.ReloadStatuses.ReloadStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.reload_status = YList()
            self.reload_status.parent = self
            self.reload_status.name = 'reload_status'


        class ReloadStatus(object):
            """
            Detailed breakdown of reload status
            
            .. attribute:: satellite_range
            
            	Satellite range
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: satellite_range_xr
            
            	Satellite range
            	**type**\: str
            
            .. attribute:: sats_not_initiated
            
            	Sats not initiated
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reload_failed
            
            	Sats reload failed
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloaded
            
            	Sats reloaded
            	**type**\: list of int
            
            	**range:** 0..65535
            
            .. attribute:: sats_reloading
            
            	Sats reloading
            	**type**\: list of int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.satellite_range = None
                self.satellite_range_xr = None
                self.sats_not_initiated = []
                self.sats_reload_failed = []
                self.sats_reloaded = []
                self.sats_reloading = []

            @property
            def _common_path(self):
                if self.satellite_range is None:
                    raise YPYDataValidationError('Key property satellite_range is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-statuses/Cisco-IOS-XR-icpe-infra-oper:reload-status[Cisco-IOS-XR-icpe-infra-oper:satellite-range = ' + str(self.satellite_range) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.satellite_range is not None:
                    return True

                if self.satellite_range_xr is not None:
                    return True

                if self.sats_not_initiated is not None:
                    for child in self.sats_not_initiated:
                        if child is not None:
                            return True

                if self.sats_reload_failed is not None:
                    for child in self.sats_reload_failed:
                        if child is not None:
                            return True

                if self.sats_reloaded is not None:
                    for child in self.sats_reloaded:
                        if child is not None:
                            return True

                if self.sats_reloading is not None:
                    for child in self.sats_reloading:
                        if child is not None:
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.ReloadStatuses.ReloadStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:reload-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.reload_status is not None:
                for child_ref in self.reload_status:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.ReloadStatuses']['meta_info']


    class SatelliteStatuses(object):
        """
        Satellite status information table
        
        .. attribute:: satellite_status
        
        	Satellite status information
        	**type**\: list of :py:class:`SatelliteStatus <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.satellite_status = YList()
            self.satellite_status.parent = self
            self.satellite_status.name = 'satellite_status'


        class SatelliteStatus(object):
            """
            Satellite status information
            
            .. attribute:: satellite_id
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: candidate_fabric_ports
            
            	Candidate Fabric Ports on this Satellite
            	**type**\: :py:class:`CandidateFabricPorts <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts>`
            
            .. attribute:: cfgd_timeout
            
            	Cfgd timeout
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: configured_link
            
            	Configured Links on this Satellite table
            	**type**\: list of :py:class:`ConfiguredLink <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink>`
            
            .. attribute:: configured_serial_number
            
            	Configured serial number
            	**type**\: str
            
            .. attribute:: configured_serial_number_present
            
            	Configured serial number present
            	**type**\: bool
            
            .. attribute:: conflict_context
            
            	Conflict context
            	**type**\: str
            
            .. attribute:: conflict_reason
            
            	Conflict reason
            	**type**\: :py:class:`IcpeOperConflict_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict_Enum>`
            
            .. attribute:: description
            
            	Description
            	**type**\: str
            
            .. attribute:: description_present
            
            	Description present
            	**type**\: bool
            
            .. attribute:: ethernet_fabric_supported
            
            	Ethernet fabric supported
            	**type**\: bool
            
            .. attribute:: host_treating_as_active
            
            	Host treating as active
            	**type**\: bool
            
            .. attribute:: install_state
            
            	Install state
            	**type**\: :py:class:`IcpeOperInstallState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperInstallState_Enum>`
            
            .. attribute:: ip_address
            
            	IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ip_address_auto
            
            	IP address auto
            	**type**\: bool
            
            .. attribute:: ip_address_present
            
            	IP address present
            	**type**\: bool
            
            .. attribute:: ipv6_address
            
            	IPV6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address_present
            
            	IPV6 address present
            	**type**\: bool
            
            .. attribute:: mac_address
            
            	MAC address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mac_address_present
            
            	MAC address present
            	**type**\: bool
            
            .. attribute:: optical_status
            
            	Optical Satellite Status
            	**type**\: :py:class:`OpticalStatus <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus>`
            
            .. attribute:: optical_supported
            
            	Optical supported
            	**type**\: bool
            
            .. attribute:: password
            
            	Password
            	**type**\: str
            
            .. attribute:: password_error
            
            	Password error
            	**type**\: str
            
            .. attribute:: received_host_name
            
            	Received hostname
            	**type**\: str
            
            .. attribute:: received_serial_number
            
            	Received serial number
            	**type**\: str
            
            .. attribute:: received_serial_number_present
            
            	Received serial number present
            	**type**\: bool
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: redundancy_out_of_sync_timestamp
            
            	Timestamp
            	**type**\: :py:class:`RedundancyOutOfSyncTimestamp <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp>`
            
            .. attribute:: remote_version
            
            	Remote version
            	**type**\: list of str
            
            .. attribute:: remote_version_present
            
            	Remote version present
            	**type**\: bool
            
            .. attribute:: satellite_id_xr
            
            	Satellite ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: satellite_treating_as_active
            
            	Satellite treating as active
            	**type**\: bool
            
            .. attribute:: sdacp_session_failure_reason
            
            	SDACP session failure reason
            	**type**\: :py:class:`IcpeGcoOperControlReason_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeGcoOperControlReason_Enum>`
            
            .. attribute:: sdacp_session_state
            
            	SDACP session state
            	**type**\: :py:class:`IcpeOperSdacpSessState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperSdacpSessState_Enum>`
            
            .. attribute:: type
            
            	Type
            	**type**\: str
            
            .. attribute:: version_check_state
            
            	Version check state
            	**type**\: :py:class:`IcpeOperVerCheckState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperVerCheckState_Enum>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: vrfid
            
            	VRFID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.satellite_id = None
                self.candidate_fabric_ports = NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts()
                self.candidate_fabric_ports.parent = self
                self.cfgd_timeout = None
                self.configured_link = YList()
                self.configured_link.parent = self
                self.configured_link.name = 'configured_link'
                self.configured_serial_number = None
                self.configured_serial_number_present = None
                self.conflict_context = None
                self.conflict_reason = None
                self.description = None
                self.description_present = None
                self.ethernet_fabric_supported = None
                self.host_treating_as_active = None
                self.install_state = None
                self.ip_address = None
                self.ip_address_auto = None
                self.ip_address_present = None
                self.ipv6_address = None
                self.ipv6_address_present = None
                self.mac_address = None
                self.mac_address_present = None
                self.optical_status = NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus()
                self.optical_status.parent = self
                self.optical_supported = None
                self.password = None
                self.password_error = None
                self.received_host_name = None
                self.received_serial_number = None
                self.received_serial_number_present = None
                self.redundancy_iccp_group = None
                self.redundancy_out_of_sync_timestamp = NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp()
                self.redundancy_out_of_sync_timestamp.parent = self
                self.remote_version = []
                self.remote_version_present = None
                self.satellite_id_xr = None
                self.satellite_treating_as_active = None
                self.sdacp_session_failure_reason = None
                self.sdacp_session_state = None
                self.type = None
                self.version_check_state = None
                self.vrf_name = None
                self.vrfid = None


            class CandidateFabricPorts(object):
                """
                Candidate Fabric Ports on this Satellite
                
                .. attribute:: channel_up
                
                	Channel up
                	**type**\: bool
                
                .. attribute:: configured_port
                
                	Configured Candidate Fabric Ports table
                	**type**\: list of :py:class:`ConfiguredPort <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort>`
                
                .. attribute:: current_port
                
                	Current Candidate Fabric Ports on this Satellite table
                	**type**\: list of :py:class:`CurrentPort <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort>`
                
                .. attribute:: error_string
                
                	Error string
                	**type**\: str
                
                .. attribute:: out_of_sync
                
                	Out of sync
                	**type**\: bool
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.channel_up = None
                    self.configured_port = YList()
                    self.configured_port.parent = self
                    self.configured_port.name = 'configured_port'
                    self.current_port = YList()
                    self.current_port.parent = self
                    self.current_port.name = 'current_port'
                    self.error_string = None
                    self.out_of_sync = None


                class ConfiguredPort(object):
                    """
                    Configured Candidate Fabric Ports table
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\: :py:class:`IcpeOperFabricPort_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort_Enum>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: valid
                    
                    	Valid
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.port = None
                        self.port_type = None
                        self.slot = None
                        self.subslot = None
                        self.valid = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:configured-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        if self.valid is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.ConfiguredPort']['meta_info']


                class CurrentPort(object):
                    """
                    Current Candidate Fabric Ports on this Satellite
                    table
                    
                    .. attribute:: permanent
                    
                    	Permanent
                    	**type**\: bool
                    
                    .. attribute:: port
                    
                    	Port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\: :py:class:`IcpeOperFabricPort_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperFabricPort_Enum>`
                    
                    .. attribute:: requested
                    
                    	Requested
                    	**type**\: bool
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.permanent = None
                        self.port = None
                        self.port_type = None
                        self.requested = None
                        self.slot = None
                        self.subslot = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:current-port'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.permanent is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.requested is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts.CurrentPort']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:candidate-fabric-ports'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.channel_up is not None:
                        return True

                    if self.configured_port is not None:
                        for child_ref in self.configured_port:
                            if child_ref._has_data():
                                return True

                    if self.current_port is not None:
                        for child_ref in self.current_port:
                            if child_ref._has_data():
                                return True

                    if self.error_string is not None:
                        return True

                    if self.out_of_sync is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.CandidateFabricPorts']['meta_info']


            class ConfiguredLink(object):
                """
                Configured Links on this Satellite table
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\: str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\: :py:class:`IcpeOperConflict_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict_Enum>`
                
                .. attribute:: discovered_link
                
                	Discovered Links table
                	**type**\: list of :py:class:`DiscoveredLink <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink>`
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: ip_address
                
                	IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ip_address_auto
                
                	IP address auto
                	**type**\: bool
                
                .. attribute:: min_links_satisfied
                
                	Min links satisfied
                	**type**\: bool
                
                .. attribute:: minimum_preferred_links
                
                	Minimum preferred links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_active_links
                
                	Number active links
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_range
                
                	Port ranges table
                	**type**\: list of :py:class:`PortRange <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange>`
                
                .. attribute:: vrf_id
                
                	VRF ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_id_present
                
                	VRF ID present
                	**type**\: bool
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.conflict_context = None
                    self.conflict_reason = None
                    self.discovered_link = YList()
                    self.discovered_link.parent = self
                    self.discovered_link.name = 'discovered_link'
                    self.interface_handle = None
                    self.ip_address = None
                    self.ip_address_auto = None
                    self.min_links_satisfied = None
                    self.minimum_preferred_links = None
                    self.number_active_links = None
                    self.port_range = YList()
                    self.port_range.parent = self
                    self.port_range.name = 'port_range'
                    self.vrf_id = None
                    self.vrf_id_present = None


                class DiscoveredLink(object):
                    """
                    Discovered Links table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\: str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\: :py:class:`IcpeOperConflict_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict_Enum>`
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: state
                    
                    	State
                    	**type**\: :py:class:`IcpeOperDiscdLinkState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperDiscdLinkState_Enum>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.conflict_context = None
                        self.conflict_reason = None
                        self.interface_handle = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:discovered-link'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.conflict_context is not None:
                            return True

                        if self.conflict_reason is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.DiscoveredLink']['meta_info']


                class PortRange(object):
                    """
                    Port ranges table
                    
                    .. attribute:: conflict_context
                    
                    	Conflict context
                    	**type**\: str
                    
                    .. attribute:: conflict_reason
                    
                    	Conflict reason
                    	**type**\: :py:class:`IcpeOperConflict_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict_Enum>`
                    
                    .. attribute:: high_port
                    
                    	High port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: low_port
                    
                    	Low port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port_type
                    
                    	Port type
                    	**type**\: :py:class:`IcpeOperPort_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperPort_Enum>`
                    
                    .. attribute:: slot
                    
                    	Slot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: subslot
                    
                    	Subslot
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.conflict_context = None
                        self.conflict_reason = None
                        self.high_port = None
                        self.low_port = None
                        self.port_type = None
                        self.slot = None
                        self.subslot = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:port-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.conflict_context is not None:
                            return True

                        if self.conflict_reason is not None:
                            return True

                        if self.high_port is not None:
                            return True

                        if self.low_port is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.slot is not None:
                            return True

                        if self.subslot is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink.PortRange']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:configured-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.conflict_context is not None:
                        return True

                    if self.conflict_reason is not None:
                        return True

                    if self.discovered_link is not None:
                        for child_ref in self.discovered_link:
                            if child_ref._has_data():
                                return True

                    if self.interface_handle is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.ip_address_auto is not None:
                        return True

                    if self.min_links_satisfied is not None:
                        return True

                    if self.minimum_preferred_links is not None:
                        return True

                    if self.number_active_links is not None:
                        return True

                    if self.port_range is not None:
                        for child_ref in self.port_range:
                            if child_ref._has_data():
                                return True

                    if self.vrf_id is not None:
                        return True

                    if self.vrf_id_present is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.ConfiguredLink']['meta_info']


            class OpticalStatus(object):
                """
                Optical Satellite Status
                
                .. attribute:: application
                
                	Application State table
                	**type**\: list of :py:class:`Application <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application>`
                
                .. attribute:: chassis_sync_state
                
                	Chassis sync state
                	**type**\: :py:class:`IcpeOpticalSyncState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState_Enum>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.application = YList()
                    self.application.parent = self
                    self.application.name = 'application'
                    self.chassis_sync_state = None


                class Application(object):
                    """
                    Application State table
                    
                    .. attribute:: name
                    
                    	Name
                    	**type**\: str
                    
                    .. attribute:: sync_state
                    
                    	Sync state
                    	**type**\: :py:class:`IcpeOpticalSyncState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpticalSyncState_Enum>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.sync_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:application'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.name is not None:
                            return True

                        if self.sync_state is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus.Application']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:optical-status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.application is not None:
                        for child_ref in self.application:
                            if child_ref._has_data():
                                return True

                    if self.chassis_sync_state is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.OpticalStatus']['meta_info']


            class RedundancyOutOfSyncTimestamp(object):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nanoseconds = None
                    self.seconds = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:redundancy-out-of-sync-timestamp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.nanoseconds is not None:
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus.RedundancyOutOfSyncTimestamp']['meta_info']

            @property
            def _common_path(self):
                if self.satellite_id is None:
                    raise YPYDataValidationError('Key property satellite_id is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-statuses/Cisco-IOS-XR-icpe-infra-oper:satellite-status[Cisco-IOS-XR-icpe-infra-oper:satellite-id = ' + str(self.satellite_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.satellite_id is not None:
                    return True

                if self.candidate_fabric_ports is not None and self.candidate_fabric_ports._has_data():
                    return True

                if self.candidate_fabric_ports is not None and self.candidate_fabric_ports.is_presence():
                    return True

                if self.cfgd_timeout is not None:
                    return True

                if self.configured_link is not None:
                    for child_ref in self.configured_link:
                        if child_ref._has_data():
                            return True

                if self.configured_serial_number is not None:
                    return True

                if self.configured_serial_number_present is not None:
                    return True

                if self.conflict_context is not None:
                    return True

                if self.conflict_reason is not None:
                    return True

                if self.description is not None:
                    return True

                if self.description_present is not None:
                    return True

                if self.ethernet_fabric_supported is not None:
                    return True

                if self.host_treating_as_active is not None:
                    return True

                if self.install_state is not None:
                    return True

                if self.ip_address is not None:
                    return True

                if self.ip_address_auto is not None:
                    return True

                if self.ip_address_present is not None:
                    return True

                if self.ipv6_address is not None:
                    return True

                if self.ipv6_address_present is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.mac_address_present is not None:
                    return True

                if self.optical_status is not None and self.optical_status._has_data():
                    return True

                if self.optical_status is not None and self.optical_status.is_presence():
                    return True

                if self.optical_supported is not None:
                    return True

                if self.password is not None:
                    return True

                if self.password_error is not None:
                    return True

                if self.received_host_name is not None:
                    return True

                if self.received_serial_number is not None:
                    return True

                if self.received_serial_number_present is not None:
                    return True

                if self.redundancy_iccp_group is not None:
                    return True

                if self.redundancy_out_of_sync_timestamp is not None and self.redundancy_out_of_sync_timestamp._has_data():
                    return True

                if self.redundancy_out_of_sync_timestamp is not None and self.redundancy_out_of_sync_timestamp.is_presence():
                    return True

                if self.remote_version is not None:
                    for child in self.remote_version:
                        if child is not None:
                            return True

                if self.remote_version_present is not None:
                    return True

                if self.satellite_id_xr is not None:
                    return True

                if self.satellite_treating_as_active is not None:
                    return True

                if self.sdacp_session_failure_reason is not None:
                    return True

                if self.sdacp_session_state is not None:
                    return True

                if self.type is not None:
                    return True

                if self.version_check_state is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrfid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SatelliteStatuses.SatelliteStatus']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-statuses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.satellite_status is not None:
                for child_ref in self.satellite_status:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SatelliteStatuses']['meta_info']


    class SatelliteTopologies(object):
        """
        Satellite Topology Information table
        
        .. attribute:: satellite_topology
        
        	Satellite Topology Information
        	**type**\: list of :py:class:`SatelliteTopology <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.satellite_topology = YList()
            self.satellite_topology.parent = self
            self.satellite_topology.name = 'satellite_topology'


        class SatelliteTopology(object):
            """
            Satellite Topology Information
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: discovered_link
            
            	Discovered Links table
            	**type**\: list of :py:class:`DiscoveredLink <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink>`
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\: str
            
            .. attribute:: is_physical
            
            	Is physical
            	**type**\: bool
            
            .. attribute:: redundancy_iccp_group
            
            	Redundancy ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ring_whole
            
            	Ring whole
            	**type**\: bool
            
            .. attribute:: satellite
            
            	Satellite table
            	**type**\: list of :py:class:`Satellite <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.discovered_link = YList()
                self.discovered_link.parent = self
                self.discovered_link.name = 'discovered_link'
                self.interface_handle = None
                self.interface_name_xr = None
                self.is_physical = None
                self.redundancy_iccp_group = None
                self.ring_whole = None
                self.satellite = YList()
                self.satellite.parent = self
                self.satellite.name = 'satellite'


            class DiscoveredLink(object):
                """
                Discovered Links table
                
                .. attribute:: discovery_running
                
                	Discovery running
                	**type**\: bool
                
                .. attribute:: interface_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\: str
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.discovery_running = None
                    self.interface_handle = None
                    self.interface_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:discovered-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.discovery_running is not None:
                        return True

                    if self.interface_handle is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.DiscoveredLink']['meta_info']


            class Satellite(object):
                """
                Satellite table
                
                .. attribute:: configured
                
                	Configured
                	**type**\: bool
                
                .. attribute:: conflict_context
                
                	Conflict context
                	**type**\: str
                
                .. attribute:: conflict_reason
                
                	Conflict reason
                	**type**\: :py:class:`IcpeOperConflict_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOperConflict_Enum>`
                
                .. attribute:: display_name
                
                	Display name
                	**type**\: str
                
                .. attribute:: fabric_link
                
                	Local Satellite Fabric Link table
                	**type**\: list of :py:class:`FabricLink <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink>`
                
                .. attribute:: mac_address
                
                	MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: num_hops
                
                	Num hops
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: received_serial_number
                
                	Received serial number
                	**type**\: str
                
                .. attribute:: received_serial_number_present
                
                	Received serial number present
                	**type**\: bool
                
                .. attribute:: satellite_id
                
                	Satellite ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Type
                	**type**\: str
                
                .. attribute:: vlan_id
                
                	VLAN ID
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.configured = None
                    self.conflict_context = None
                    self.conflict_reason = None
                    self.display_name = None
                    self.fabric_link = YList()
                    self.fabric_link.parent = self
                    self.fabric_link.name = 'fabric_link'
                    self.mac_address = None
                    self.num_hops = None
                    self.received_serial_number = None
                    self.received_serial_number_present = None
                    self.satellite_id = None
                    self.type = None
                    self.vlan_id = None


                class FabricLink(object):
                    """
                    Local Satellite Fabric Link table
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\: bool
                    
                    .. attribute:: display_name
                    
                    	Display name
                    	**type**\: str
                    
                    .. attribute:: icl_id
                    
                    	ICL ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: obsolete
                    
                    	Obsolete
                    	**type**\: bool
                    
                    .. attribute:: redundant
                    
                    	Redundant
                    	**type**\: bool
                    
                    .. attribute:: remote_device
                    
                    	Remote Device table
                    	**type**\: list of :py:class:`RemoteDevice <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice>`
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active = None
                        self.display_name = None
                        self.icl_id = None
                        self.interface_name = None
                        self.obsolete = None
                        self.redundant = None
                        self.remote_device = YList()
                        self.remote_device.parent = self
                        self.remote_device.name = 'remote_device'


                    class RemoteDevice(object):
                        """
                        Remote Device table
                        
                        .. attribute:: icl_id
                        
                        	ICL ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: str
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: remote_is_local_host
                        
                        	Remote is local host
                        	**type**\: bool
                        
                        .. attribute:: remote_is_satellite
                        
                        	Remote is satellite
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'icpe-infra-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.icl_id = None
                            self.interface_handle = None
                            self.interface_name = None
                            self.mac_address = None
                            self.remote_is_local_host = None
                            self.remote_is_satellite = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:remote-device'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.icl_id is not None:
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.remote_is_local_host is not None:
                                return True

                            if self.remote_is_satellite is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                            return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink.RemoteDevice']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:fabric-link'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.active is not None:
                            return True

                        if self.display_name is not None:
                            return True

                        if self.icl_id is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.obsolete is not None:
                            return True

                        if self.redundant is not None:
                            return True

                        if self.remote_device is not None:
                            for child_ref in self.remote_device:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite.FabricLink']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:satellite'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.configured is not None:
                        return True

                    if self.conflict_context is not None:
                        return True

                    if self.conflict_reason is not None:
                        return True

                    if self.display_name is not None:
                        return True

                    if self.fabric_link is not None:
                        for child_ref in self.fabric_link:
                            if child_ref._has_data():
                                return True

                    if self.mac_address is not None:
                        return True

                    if self.num_hops is not None:
                        return True

                    if self.received_serial_number is not None:
                        return True

                    if self.received_serial_number_present is not None:
                        return True

                    if self.satellite_id is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.vlan_id is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology.Satellite']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-topologies/Cisco-IOS-XR-icpe-infra-oper:satellite-topology[Cisco-IOS-XR-icpe-infra-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_name is not None:
                    return True

                if self.discovered_link is not None:
                    for child_ref in self.discovered_link:
                        if child_ref._has_data():
                            return True

                if self.interface_handle is not None:
                    return True

                if self.interface_name_xr is not None:
                    return True

                if self.is_physical is not None:
                    return True

                if self.redundancy_iccp_group is not None:
                    return True

                if self.ring_whole is not None:
                    return True

                if self.satellite is not None:
                    for child_ref in self.satellite:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SatelliteTopologies.SatelliteTopology']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:satellite-topologies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.satellite_topology is not None:
                for child_ref in self.satellite_topology:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SatelliteTopologies']['meta_info']


    class SdacpRedundancies(object):
        """
        nV Satellite Redundancy Protocol Information
        table
        
        .. attribute:: sdacp_redundancy
        
        	nV Satellite Redundancy Protocol Information
        	**type**\: list of :py:class:`SdacpRedundancy <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy>`
        
        

        """

        _prefix = 'icpe-infra-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.sdacp_redundancy = YList()
            self.sdacp_redundancy.parent = self
            self.sdacp_redundancy.name = 'sdacp_redundancy'


        class SdacpRedundancy(object):
            """
            nV Satellite Redundancy Protocol Information
            
            .. attribute:: iccp_group
            
            	ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: arbitration_state
            
            	Arbitration state
            	**type**\: :py:class:`IcpeOpmArbitrationFsmState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmArbitrationFsmState_Enum>`
            
            .. attribute:: authentication_state
            
            	Authentication state
            	**type**\: :py:class:`IcpeOpmAuthFsmState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmAuthFsmState_Enum>`
            
            .. attribute:: channel
            
            	Channels on this session table
            	**type**\: list of :py:class:`Channel <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel>`
            
            .. attribute:: iccp_group_xr
            
            	ICCP group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: isolated
            
            	Isolated
            	**type**\: bool
            
            .. attribute:: primacy
            
            	Primacy
            	**type**\: :py:class:`IcpeOpmController_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmController_Enum>`
            
            .. attribute:: protocol_state
            
            	Protocol state
            	**type**\: :py:class:`IcpeOpmSessState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSessState_Enum>`
            
            .. attribute:: protocol_state_timestamp
            
            	Timestamp
            	**type**\: :py:class:`ProtocolStateTimestamp <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp>`
            
            .. attribute:: synchronization_state
            
            	Synchronization state
            	**type**\: :py:class:`IcpeOpmSyncFsmState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmSyncFsmState_Enum>`
            
            .. attribute:: system_mac
            
            	System MAC
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: transport_state
            
            	Transport state
            	**type**\: :py:class:`IcpeOpmTransportState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmTransportState_Enum>`
            
            

            """

            _prefix = 'icpe-infra-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.iccp_group = None
                self.arbitration_state = None
                self.authentication_state = None
                self.channel = YList()
                self.channel.parent = self
                self.channel.name = 'channel'
                self.iccp_group_xr = None
                self.isolated = None
                self.primacy = None
                self.protocol_state = None
                self.protocol_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp()
                self.protocol_state_timestamp.parent = self
                self.synchronization_state = None
                self.system_mac = None
                self.transport_state = None


            class Channel(object):
                """
                Channels on this session table
                
                .. attribute:: chan_state
                
                	Chan state
                	**type**\: :py:class:`IcpeOpmChanFsmState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmChanFsmState_Enum>`
                
                .. attribute:: channel_id
                
                	Channel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: channel_state_timestamp
                
                	Timestamp
                	**type**\: :py:class:`ChannelStateTimestamp <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp>`
                
                .. attribute:: control_messages_received
                
                	Control messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: control_messages_sent
                
                	Control messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_received
                
                	Normal messages received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: normal_messages_sent
                
                	Normal messages sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: resync_state
                
                	Resync state
                	**type**\: :py:class:`IcpeOpmResyncFsmState_Enum <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.IcpeOpmResyncFsmState_Enum>`
                
                .. attribute:: resync_state_timestamp
                
                	Timestamp
                	**type**\: :py:class:`ResyncStateTimestamp <ydk.models.icpe.Cisco_IOS_XR_icpe_infra_oper.NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp>`
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.chan_state = None
                    self.channel_id = None
                    self.channel_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp()
                    self.channel_state_timestamp.parent = self
                    self.control_messages_received = None
                    self.control_messages_sent = None
                    self.normal_messages_received = None
                    self.normal_messages_sent = None
                    self.resync_state = None
                    self.resync_state_timestamp = NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp()
                    self.resync_state_timestamp.parent = self


                class ChannelStateTimestamp(object):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:channel-state-timestamp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ChannelStateTimestamp']['meta_info']


                class ResyncStateTimestamp(object):
                    """
                    Timestamp
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'icpe-infra-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.nanoseconds = None
                        self.seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:resync-state-timestamp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.nanoseconds is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                        return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel.ResyncStateTimestamp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:channel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.chan_state is not None:
                        return True

                    if self.channel_id is not None:
                        return True

                    if self.channel_state_timestamp is not None and self.channel_state_timestamp._has_data():
                        return True

                    if self.channel_state_timestamp is not None and self.channel_state_timestamp.is_presence():
                        return True

                    if self.control_messages_received is not None:
                        return True

                    if self.control_messages_sent is not None:
                        return True

                    if self.normal_messages_received is not None:
                        return True

                    if self.normal_messages_sent is not None:
                        return True

                    if self.resync_state is not None:
                        return True

                    if self.resync_state_timestamp is not None and self.resync_state_timestamp._has_data():
                        return True

                    if self.resync_state_timestamp is not None and self.resync_state_timestamp.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.Channel']['meta_info']


            class ProtocolStateTimestamp(object):
                """
                Timestamp
                
                .. attribute:: nanoseconds
                
                	Nanoseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds
                
                	Seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'icpe-infra-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nanoseconds = None
                    self.seconds = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-oper:protocol-state-timestamp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.nanoseconds is not None:
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                    return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy.ProtocolStateTimestamp']['meta_info']

            @property
            def _common_path(self):
                if self.iccp_group is None:
                    raise YPYDataValidationError('Key property iccp_group is None')

                return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancies/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancy[Cisco-IOS-XR-icpe-infra-oper:iccp-group = ' + str(self.iccp_group) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.iccp_group is not None:
                    return True

                if self.arbitration_state is not None:
                    return True

                if self.authentication_state is not None:
                    return True

                if self.channel is not None:
                    for child_ref in self.channel:
                        if child_ref._has_data():
                            return True

                if self.iccp_group_xr is not None:
                    return True

                if self.isolated is not None:
                    return True

                if self.primacy is not None:
                    return True

                if self.protocol_state is not None:
                    return True

                if self.protocol_state_timestamp is not None and self.protocol_state_timestamp._has_data():
                    return True

                if self.protocol_state_timestamp is not None and self.protocol_state_timestamp.is_presence():
                    return True

                if self.synchronization_state is not None:
                    return True

                if self.system_mac is not None:
                    return True

                if self.transport_state is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
                return meta._meta_table['NvSatellite.SdacpRedundancies.SdacpRedundancy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite/Cisco-IOS-XR-icpe-infra-oper:sdacp-redundancies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sdacp_redundancy is not None:
                for child_ref in self.sdacp_redundancy:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
            return meta._meta_table['NvSatellite.SdacpRedundancies']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-icpe-infra-oper:nv-satellite'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.install_op_statuses is not None and self.install_op_statuses._has_data():
            return True

        if self.install_op_statuses is not None and self.install_op_statuses.is_presence():
            return True

        if self.install_progresses is not None and self.install_progresses._has_data():
            return True

        if self.install_progresses is not None and self.install_progresses.is_presence():
            return True

        if self.install_statuses is not None and self.install_statuses._has_data():
            return True

        if self.install_statuses is not None and self.install_statuses.is_presence():
            return True

        if self.reload_statuses is not None and self.reload_statuses._has_data():
            return True

        if self.reload_statuses is not None and self.reload_statuses.is_presence():
            return True

        if self.satellite_statuses is not None and self.satellite_statuses._has_data():
            return True

        if self.satellite_statuses is not None and self.satellite_statuses.is_presence():
            return True

        if self.satellite_topologies is not None and self.satellite_topologies._has_data():
            return True

        if self.satellite_topologies is not None and self.satellite_topologies.is_presence():
            return True

        if self.sdacp_redundancies is not None and self.sdacp_redundancies._has_data():
            return True

        if self.sdacp_redundancies is not None and self.sdacp_redundancies.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.icpe._meta import _Cisco_IOS_XR_icpe_infra_oper as meta
        return meta._meta_table['NvSatellite']['meta_info']


