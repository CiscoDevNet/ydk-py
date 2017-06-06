""" Cisco_IOS_XR_infra_serg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-serg package operational data.

This module contains definitions
for the following management objects\:
  session\-redundancy\-manager\: Session Redundancy Manager
    information
  session\-redundancy\-agent\: session redundancy agent

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SergPeerStatusEnum(Enum):
    """
    SergPeerStatusEnum

    SERG Peer Status

    .. data:: not_configured = 0

    	Peer not configured

    .. data:: initialize = 1

    	Peer initialization

    .. data:: retry = 2

    	Peer retry pending

    .. data:: connect = 3

    	Connection in Progress

    .. data:: listen = 4

    	Listening in Progress

    .. data:: registration = 5

    	Awaiting Registration from Peer

    .. data:: cleanup = 6

    	Peer cleanup in progress

    .. data:: connected = 7

    	Peer Connected

    .. data:: established = 8

    	Peer Established

    """

    not_configured = 0

    initialize = 1

    retry = 2

    connect = 3

    listen = 4

    registration = 5

    cleanup = 6

    connected = 7

    established = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergPeerStatusEnum']


class SergShowCompEnum(Enum):
    """
    SergShowCompEnum

    SERG Components

    .. data:: serga = 0

    	SERG Agent

    .. data:: ipv6nd = 1

    	IPv6ND

    .. data:: dhcpv6 = 2

    	DHCPv6

    """

    serga = 0

    ipv6nd = 1

    dhcpv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowCompEnum']


class SergShowImRoleEnum(Enum):
    """
    SergShowImRoleEnum

    SERG Interface Management Role

    .. data:: none = 0

    	Not Determined

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = 0

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowImRoleEnum']


class SergShowMemEnum(Enum):
    """
    SergShowMemEnum

    SERG Memory Manager type

    .. data:: standard = 0

    	Standard type

    .. data:: chunk = 1

    	Chunk type

    .. data:: edm = 2

    	EDM type

    .. data:: string = 3

    	String type

    .. data:: static = 4

    	Static type

    .. data:: unknown = 5

    	Unknown type

    """

    standard = 0

    chunk = 1

    edm = 2

    string = 3

    static = 4

    unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowMemEnum']


class SergShowRoleEnum(Enum):
    """
    SergShowRoleEnum

    SERG Role

    .. data:: none = 0

    	Not Configured

    .. data:: master = 1

    	Master Role

    .. data:: slave = 2

    	Slave Role

    """

    none = 0

    master = 1

    slave = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowRoleEnum']


class SergShowSessionErrorEnum(Enum):
    """
    SergShowSessionErrorEnum

    SERG Session Error Operation

    .. data:: none = 0

    	Invalid Error

    .. data:: hard = 1

    	Hard Error

    .. data:: soft = 2

    	Soft Error

    """

    none = 0

    hard = 1

    soft = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowSessionErrorEnum']


class SergShowSessionOperationEnum(Enum):
    """
    SergShowSessionOperationEnum

    SERG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SERG Session Update Operation

    .. data:: delete = 2

    	SERG Session Delete Operation

    .. data:: in_sync = 3

    	SERG Session In Sync

    """

    none = 0

    update = 1

    delete = 2

    in_sync = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowSessionOperationEnum']


class SergShowSlaveModeEnum(Enum):
    """
    SergShowSlaveModeEnum

    SERG Slave Mode

    .. data:: none = 0

    	Not Configured

    .. data:: warm = 1

    	Warm Modem

    .. data:: hot = 2

    	Hot Mode

    """

    none = 0

    warm = 1

    hot = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowSlaveModeEnum']


class SergShowSoReasonEnum(Enum):
    """
    SergShowSoReasonEnum

    Session Redundancy Switchover Reason

    .. data:: internal = 0

    	SwitchOver for Internal Reason

    .. data:: admin = 1

    	SwitchOver for Admin

    .. data:: peer_up = 2

    	SwitchOver for Peer UP

    .. data:: peer_down = 3

    	SwitchOver for Peer Down

    .. data:: object_tracking_status_change = 4

    	SwitchOver for Object Tracking status change

    .. data:: serg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = 0

    admin = 1

    peer_up = 2

    peer_down = 3

    object_tracking_status_change = 4

    serg_show_so_reason_max = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SergShowSoReasonEnum']



class SessionRedundancyManager(object):
    """
    Session Redundancy Manager information
    
    .. attribute:: groups
    
    	Session Redundancy Manager group table
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups>`
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces>`
    
    .. attribute:: summary
    
    	Session redundancy manager summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Summary>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.groups = SessionRedundancyManager.Groups()
        self.groups.parent = self
        self.interfaces = SessionRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self.summary = SessionRedundancyManager.Summary()
        self.summary.parent = self


    class Interfaces(object):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	interface redundancy manager interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            interface redundancy manager interface
            
            .. attribute:: interface  <key>
            
            	Interface
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: forward_referenced
            
            	Forward Referenced
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_mapping_id
            
            	Interface Mapping ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name
            
            	Interface Name
            	**type**\:  str
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:   :py:class:`SergShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRoleEnum>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = None
                self.forward_referenced = None
                self.group_id = None
                self.interface_mapping_id = None
                self.interface_name = None
                self.role = None

            @property
            def _common_path(self):
                if self.interface is None:
                    raise YPYModelError('Key property interface is None')

                return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/Cisco-IOS-XR-infra-serg-oper:interfaces/Cisco-IOS-XR-infra-serg-oper:interface[Cisco-IOS-XR-infra-serg-oper:interface = ' + str(self.interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    return True

                if self.forward_referenced is not None:
                    return True

                if self.group_id is not None:
                    return True

                if self.interface_mapping_id is not None:
                    return True

                if self.interface_name is not None:
                    return True

                if self.role is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                return meta._meta_table['SessionRedundancyManager.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/Cisco-IOS-XR-infra-serg-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
            return meta._meta_table['SessionRedundancyManager.Interfaces']['meta_info']


    class Groups(object):
        """
        Session Redundancy Manager group table
        
        .. attribute:: group
        
        	Session redundancy manager group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            Session redundancy manager group
            
            .. attribute:: group  <key>
            
            	Group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: description
            
            	Group Description
            	**type**\:  str
            
            .. attribute:: disabled
            
            	Disabled by Config
            	**type**\:  bool
            
            .. attribute:: group_id
            
            	Group ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Interface Count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_name
            
            	Node Information
            	**type**\:  str
            
            .. attribute:: object_tracking_status
            
            	Object Tracking Status (Enabled/Disabled)
            	**type**\:  bool
            
            .. attribute:: peer_ipv4_address
            
            	Peer IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_ipv6_address
            
            	Peer IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: preferred_role
            
            	Preferred Role
            	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
            
            .. attribute:: role
            
            	SERG Role
            	**type**\:   :py:class:`SergShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRoleEnum>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:   :py:class:`SergShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveModeEnum>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group = None
                self.description = None
                self.disabled = None
                self.group_id = None
                self.interface_count = None
                self.node_name = None
                self.object_tracking_status = None
                self.peer_ipv4_address = None
                self.peer_ipv6_address = None
                self.preferred_role = None
                self.role = None
                self.slave_mode = None

            @property
            def _common_path(self):
                if self.group is None:
                    raise YPYModelError('Key property group is None')

                return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/Cisco-IOS-XR-infra-serg-oper:groups/Cisco-IOS-XR-infra-serg-oper:group[Cisco-IOS-XR-infra-serg-oper:group = ' + str(self.group) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.group is not None:
                    return True

                if self.description is not None:
                    return True

                if self.disabled is not None:
                    return True

                if self.group_id is not None:
                    return True

                if self.interface_count is not None:
                    return True

                if self.node_name is not None:
                    return True

                if self.object_tracking_status is not None:
                    return True

                if self.peer_ipv4_address is not None:
                    return True

                if self.peer_ipv6_address is not None:
                    return True

                if self.preferred_role is not None:
                    return True

                if self.role is not None:
                    return True

                if self.slave_mode is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                return meta._meta_table['SessionRedundancyManager.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/Cisco-IOS-XR-infra-serg-oper:groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.group is not None:
                for child_ref in self.group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
            return meta._meta_table['SessionRedundancyManager.Groups']['meta_info']


    class Summary(object):
        """
        Session redundancy manager summary
        
        .. attribute:: active_state
        
        	Process Active State
        	**type**\:  bool
        
        .. attribute:: disabled
        
        	Disabled by Config
        	**type**\:  bool
        
        .. attribute:: disabled_group_count
        
        	No. of Disabled Groups by Config
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: group_count
        
        	No. of Configured Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: hold_timer
        
        	Switch Over Hold Time
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_count
        
        	No. of Configured Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_group_count
        
        	No. of Master/Active Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_interface_count
        
        	No. of Master/Active Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: preferred_role
        
        	Preferred Role
        	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
        
        .. attribute:: slave_group_count
        
        	No. of Slave Groups
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_interface_count
        
        	No. of Slave Interfaces
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: slave_mode
        
        	Slave Mode
        	**type**\:   :py:class:`SergShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveModeEnum>`
        
        .. attribute:: source_interface_ipv4_address
        
        	Source Interface IPv4 Address
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_ipv6_address
        
        	Source Interface IPv6 Address
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: source_interface_name
        
        	Source Interface Name
        	**type**\:  str
        
        .. attribute:: vrf_name
        
        	VRF Name
        	**type**\:  str
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.active_state = None
            self.disabled = None
            self.disabled_group_count = None
            self.group_count = None
            self.hold_timer = None
            self.interface_count = None
            self.master_group_count = None
            self.master_interface_count = None
            self.preferred_role = None
            self.slave_group_count = None
            self.slave_interface_count = None
            self.slave_mode = None
            self.source_interface_ipv4_address = None
            self.source_interface_ipv6_address = None
            self.source_interface_name = None
            self.vrf_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager/Cisco-IOS-XR-infra-serg-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.active_state is not None:
                return True

            if self.disabled is not None:
                return True

            if self.disabled_group_count is not None:
                return True

            if self.group_count is not None:
                return True

            if self.hold_timer is not None:
                return True

            if self.interface_count is not None:
                return True

            if self.master_group_count is not None:
                return True

            if self.master_interface_count is not None:
                return True

            if self.preferred_role is not None:
                return True

            if self.slave_group_count is not None:
                return True

            if self.slave_interface_count is not None:
                return True

            if self.slave_mode is not None:
                return True

            if self.source_interface_ipv4_address is not None:
                return True

            if self.source_interface_ipv6_address is not None:
                return True

            if self.source_interface_name is not None:
                return True

            if self.vrf_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
            return meta._meta_table['SessionRedundancyManager.Summary']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.groups is not None and self.groups._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SessionRedundancyManager']['meta_info']


class SessionRedundancyAgent(object):
    """
    session redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which session data is collected
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'infra-serg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = SessionRedundancyAgent.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes for which session data is
        collected
        
        .. attribute:: node
        
        	Session data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'infra-serg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Session data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_ids
            
            	Stats Client
            	**type**\:   :py:class:`ClientIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds>`
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:   :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: group_summaries
            
            	Session data for a particular node
            	**type**\:   :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces>`
            
            .. attribute:: memory
            
            	Show Memory
            	**type**\:   :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory>`
            
            .. attribute:: stats_global
            
            	Stats Global
            	**type**\:   :py:class:`StatsGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal>`
            
            

            """

            _prefix = 'infra-serg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.client_ids = SessionRedundancyAgent.Nodes.Node.ClientIds()
                self.client_ids.parent = self
                self.group_id_xr = SessionRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self.group_ids = SessionRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self.group_summaries = SessionRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self.interfaces = SessionRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.memory = SessionRedundancyAgent.Nodes.Node.Memory()
                self.memory.parent = self
                self.stats_global = SessionRedundancyAgent.Nodes.Node.StatsGlobal()
                self.stats_global.parent = self


            class GroupIdXr(object):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_id = YList()
                    self.group_id.parent = self
                    self.group_id.name = 'group_id'


                class GroupId(object):
                    """
                    Group id for subscriber group session
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: key_index
                    
                    	Key index
                    	**type**\:  str
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\:  bool
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\:  bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of    :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of    :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.group_id_xr = None
                        self.interface_name = None
                        self.key_index = None
                        self.negative_acknowledgement_update_all = None
                        self.role_master = None
                        self.session_detailed_information = YList()
                        self.session_detailed_information.parent = self
                        self.session_detailed_information.name = 'session_detailed_information'
                        self.session_sync_error_information = YList()
                        self.session_sync_error_information.parent = self
                        self.session_sync_error_information.name = 'session_sync_error_information'


                    class SessionDetailedInformation(object):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowCompEnum>`
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\:  bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\:  bool
                        
                        .. attribute:: operation
                        
                        	Operation Code
                        	**type**\:   :py:class:`SergShowSessionOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionOperationEnum>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.component = None
                            self.marked_for_cleanup = None
                            self.marked_for_sweeping = None
                            self.operation = None
                            self.tx_list_queue_fail = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:session-detailed-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.component is not None:
                                return True

                            if self.marked_for_cleanup is not None:
                                return True

                            if self.marked_for_sweeping is not None:
                                return True

                            if self.operation is not None:
                                return True

                            if self.tx_list_queue_fail is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation']['meta_info']


                    class SessionSyncErrorInformation(object):
                        """
                        Session Synchroniation Error Information
                        
                        .. attribute:: last_error_code
                        
                        	Last Error Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_error_type
                        
                        	Last Error Type
                        	**type**\:   :py:class:`SergShowSessionErrorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSessionErrorEnum>`
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.last_error_code = None
                            self.last_error_type = None
                            self.sync_error_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:session-sync-error-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.last_error_code is not None:
                                return True

                            if self.last_error_type is not None:
                                return True

                            if self.sync_error_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-id[Cisco-IOS-XR-infra-serg-oper:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.group_id_xr is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.key_index is not None:
                            return True

                        if self.negative_acknowledgement_update_all is not None:
                            return True

                        if self.role_master is not None:
                            return True

                        if self.session_detailed_information is not None:
                            for child_ref in self.session_detailed_information:
                                if child_ref._has_data():
                                    return True

                        if self.session_sync_error_information is not None:
                            for child_ref in self.session_sync_error_information:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-id-xr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group_id is not None:
                        for child_ref in self.group_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info']


            class ClientIds(object):
                """
                Stats Client
                
                .. attribute:: client_id
                
                	Specify stats client
                	**type**\: list of    :py:class:`ClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_id = YList()
                    self.client_id.parent = self
                    self.client_id.name = 'client_id'


                class ClientId(object):
                    """
                    Specify stats client
                    
                    .. attribute:: stats_client_id  <key>
                    
                    	Client Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: clean_call_back
                    
                    	CleanCallBack
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_replay_all_count
                    
                    	LastReplayAllCount
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_not_ok
                    
                    	TxListActiveNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_active_ok
                    
                    	TxListActiveOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_not_ok
                    
                    	TxListClearAllAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_all_add_ok
                    
                    	TxListClearAllAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_not_ok
                    
                    	TxListClearSelectedAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clear_selected_add_ok
                    
                    	TxListClearSelectedAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_cleanup
                    
                    	TxListClientCleanup
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_connection_down
                    
                    	TxListClientConnectionDown
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_de_registration
                    
                    	TxListClientDeRegistration
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_not_ok
                    
                    	TxListClientRegistrationNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_client_registration_ok
                    
                    	TxListClientRegistrationOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_not_ok
                    
                    	TxListDeActiveNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_de_active_ok
                    
                    	TxListDeActiveOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_ok
                    
                    	TxListEncodeSessionSessionOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_session_session_partial_write
                    
                    	TxListEncodeSessionSessionPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_not_ok
                    
                    	TxListEndOfDownloadAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_download_add_ok
                    
                    	TxListEndOfDownloadAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_not_ok
                    
                    	TxListEndOfMessageAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_end_of_message_add_ok
                    
                    	TxListEndOfMessageAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_all
                    
                    	TxListReceiveCommandReplayAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_command_replay_selected
                    
                    	TxListReceiveCommandReplaySelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_all
                    
                    	TxListReceiveSessionSessionClearAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_clear_selected
                    
                    	TxListReceiveSessionSessionClearSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_invalid
                    
                    	TxListReceiveSessionSessionDeleteInValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_delete_valid
                    
                    	TxListReceiveSessionSessionDeleteValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_all
                    
                    	TxListReceiveSessionSessionEODAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eod_selected
                    
                    	TxListReceiveSessionSessionEODSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_eoms
                    
                    	TxListReceiveSessionSessionEOMS
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack
                    
                    	TxListReceiveSessionSessionNegAck
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_neg_ack_not_ok
                    
                    	TxListReceiveSessionSessionNegAckNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_all
                    
                    	TxListReceiveSessionSessionSODAll
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_sod_selected
                    
                    	TxListReceiveSessionSessionSODSelected
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_invalid
                    
                    	TxListReceiveSessionSessionUpdateInValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_receive_session_session_update_valid
                    
                    	TxListReceiveSessionSessionUpdateValid
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_not_ok
                    
                    	TxListReplayAllAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_all_add_ok
                    
                    	TxListReplayAllAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_not_ok
                    
                    	TxListReplaySelectedAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_replay_selected_add_ok
                    
                    	TxListReplaySelectedAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_not_ok
                    
                    	TxListSessionSessionAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_add_ok
                    
                    	TxListSessionSessionAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_delete
                    
                    	TxListSessionSessionDelete
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_not_ok
                    
                    	TxListSessionSessionUpdateNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_session_session_update_ok
                    
                    	TxListSessionSessionUpdateOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_start_of_download_add_not_ok
                    
                    	TxListStartOfDownloadAddNotOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_start_of_download_add_ok
                    
                    	TxListStartOfDownloadAddOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.stats_client_id = None
                        self.clean_call_back = None
                        self.last_replay_all_count = None
                        self.tx_list_active_not_ok = None
                        self.tx_list_active_ok = None
                        self.tx_list_clear_all_add_not_ok = None
                        self.tx_list_clear_all_add_ok = None
                        self.tx_list_clear_selected_add_not_ok = None
                        self.tx_list_clear_selected_add_ok = None
                        self.tx_list_client_cleanup = None
                        self.tx_list_client_connection_down = None
                        self.tx_list_client_de_registration = None
                        self.tx_list_client_registration_not_ok = None
                        self.tx_list_client_registration_ok = None
                        self.tx_list_de_active_not_ok = None
                        self.tx_list_de_active_ok = None
                        self.tx_list_encode_session_session_ok = None
                        self.tx_list_encode_session_session_partial_write = None
                        self.tx_list_end_of_download_add_not_ok = None
                        self.tx_list_end_of_download_add_ok = None
                        self.tx_list_end_of_message_add_not_ok = None
                        self.tx_list_end_of_message_add_ok = None
                        self.tx_list_receive_command_replay_all = None
                        self.tx_list_receive_command_replay_selected = None
                        self.tx_list_receive_session_session_clear_all = None
                        self.tx_list_receive_session_session_clear_selected = None
                        self.tx_list_receive_session_session_delete_invalid = None
                        self.tx_list_receive_session_session_delete_valid = None
                        self.tx_list_receive_session_session_eod_all = None
                        self.tx_list_receive_session_session_eod_selected = None
                        self.tx_list_receive_session_session_eoms = None
                        self.tx_list_receive_session_session_neg_ack = None
                        self.tx_list_receive_session_session_neg_ack_not_ok = None
                        self.tx_list_receive_session_session_sod_all = None
                        self.tx_list_receive_session_session_sod_selected = None
                        self.tx_list_receive_session_session_update_invalid = None
                        self.tx_list_receive_session_session_update_valid = None
                        self.tx_list_replay_all_add_not_ok = None
                        self.tx_list_replay_all_add_ok = None
                        self.tx_list_replay_selected_add_not_ok = None
                        self.tx_list_replay_selected_add_ok = None
                        self.tx_list_session_session_add_not_ok = None
                        self.tx_list_session_session_add_ok = None
                        self.tx_list_session_session_delete = None
                        self.tx_list_session_session_update_not_ok = None
                        self.tx_list_session_session_update_ok = None
                        self.tx_list_start_of_download_add_not_ok = None
                        self.tx_list_start_of_download_add_ok = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.stats_client_id is None:
                            raise YPYModelError('Key property stats_client_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:client-id[Cisco-IOS-XR-infra-serg-oper:stats-client-id = ' + str(self.stats_client_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.stats_client_id is not None:
                            return True

                        if self.clean_call_back is not None:
                            return True

                        if self.last_replay_all_count is not None:
                            return True

                        if self.tx_list_active_not_ok is not None:
                            return True

                        if self.tx_list_active_ok is not None:
                            return True

                        if self.tx_list_clear_all_add_not_ok is not None:
                            return True

                        if self.tx_list_clear_all_add_ok is not None:
                            return True

                        if self.tx_list_clear_selected_add_not_ok is not None:
                            return True

                        if self.tx_list_clear_selected_add_ok is not None:
                            return True

                        if self.tx_list_client_cleanup is not None:
                            return True

                        if self.tx_list_client_connection_down is not None:
                            return True

                        if self.tx_list_client_de_registration is not None:
                            return True

                        if self.tx_list_client_registration_not_ok is not None:
                            return True

                        if self.tx_list_client_registration_ok is not None:
                            return True

                        if self.tx_list_de_active_not_ok is not None:
                            return True

                        if self.tx_list_de_active_ok is not None:
                            return True

                        if self.tx_list_encode_session_session_ok is not None:
                            return True

                        if self.tx_list_encode_session_session_partial_write is not None:
                            return True

                        if self.tx_list_end_of_download_add_not_ok is not None:
                            return True

                        if self.tx_list_end_of_download_add_ok is not None:
                            return True

                        if self.tx_list_end_of_message_add_not_ok is not None:
                            return True

                        if self.tx_list_end_of_message_add_ok is not None:
                            return True

                        if self.tx_list_receive_command_replay_all is not None:
                            return True

                        if self.tx_list_receive_command_replay_selected is not None:
                            return True

                        if self.tx_list_receive_session_session_clear_all is not None:
                            return True

                        if self.tx_list_receive_session_session_clear_selected is not None:
                            return True

                        if self.tx_list_receive_session_session_delete_invalid is not None:
                            return True

                        if self.tx_list_receive_session_session_delete_valid is not None:
                            return True

                        if self.tx_list_receive_session_session_eod_all is not None:
                            return True

                        if self.tx_list_receive_session_session_eod_selected is not None:
                            return True

                        if self.tx_list_receive_session_session_eoms is not None:
                            return True

                        if self.tx_list_receive_session_session_neg_ack is not None:
                            return True

                        if self.tx_list_receive_session_session_neg_ack_not_ok is not None:
                            return True

                        if self.tx_list_receive_session_session_sod_all is not None:
                            return True

                        if self.tx_list_receive_session_session_sod_selected is not None:
                            return True

                        if self.tx_list_receive_session_session_update_invalid is not None:
                            return True

                        if self.tx_list_receive_session_session_update_valid is not None:
                            return True

                        if self.tx_list_replay_all_add_not_ok is not None:
                            return True

                        if self.tx_list_replay_all_add_ok is not None:
                            return True

                        if self.tx_list_replay_selected_add_not_ok is not None:
                            return True

                        if self.tx_list_replay_selected_add_ok is not None:
                            return True

                        if self.tx_list_session_session_add_not_ok is not None:
                            return True

                        if self.tx_list_session_session_add_ok is not None:
                            return True

                        if self.tx_list_session_session_delete is not None:
                            return True

                        if self.tx_list_session_session_update_not_ok is not None:
                            return True

                        if self.tx_list_session_session_update_ok is not None:
                            return True

                        if self.tx_list_start_of_download_add_not_ok is not None:
                            return True

                        if self.tx_list_start_of_download_add_ok is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:client-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client_id is not None:
                        for child_ref in self.client_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.ClientIds']['meta_info']


            class Memory(object):
                """
                Show Memory
                
                .. attribute:: edm_memory_info
                
                	EDM Memory Info
                	**type**\: list of    :py:class:`EdmMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo>`
                
                .. attribute:: memory_info
                
                	Memory Info
                	**type**\: list of    :py:class:`MemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo>`
                
                .. attribute:: string_memory_info
                
                	String Memory Info
                	**type**\: list of    :py:class:`StringMemoryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.edm_memory_info = YList()
                    self.edm_memory_info.parent = self
                    self.edm_memory_info.name = 'edm_memory_info'
                    self.memory_info = YList()
                    self.memory_info.parent = self
                    self.memory_info.name = 'memory_info'
                    self.string_memory_info = YList()
                    self.string_memory_info.parent = self
                    self.string_memory_info.name = 'string_memory_info'


                class MemoryInfo(object):
                    """
                    Memory Info
                    
                    .. attribute:: alloc_count
                    
                    	Allocated count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: alloc_fails
                    
                    	Allocation Fails
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_count
                    
                    	Current Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: freed_count
                    
                    	Freed Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: memory_type
                    
                    	Memory Type
                    	**type**\:   :py:class:`SergShowMemEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowMemEnum>`
                    
                    .. attribute:: size
                    
                    	Size of the datastructure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: structure_name
                    
                    	Structure Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.alloc_count = None
                        self.alloc_fails = None
                        self.current_count = None
                        self.freed_count = None
                        self.memory_type = None
                        self.size = None
                        self.structure_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:memory-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.alloc_count is not None:
                            return True

                        if self.alloc_fails is not None:
                            return True

                        if self.current_count is not None:
                            return True

                        if self.freed_count is not None:
                            return True

                        if self.memory_type is not None:
                            return True

                        if self.size is not None:
                            return True

                        if self.structure_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo']['meta_info']


                class EdmMemoryInfo(object):
                    """
                    EDM Memory Info
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.failure = None
                        self.size = None
                        self.success = None
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:edm-memory-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.failure is not None:
                            return True

                        if self.size is not None:
                            return True

                        if self.success is not None:
                            return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo']['meta_info']


                class StringMemoryInfo(object):
                    """
                    String Memory Info
                    
                    .. attribute:: failure
                    
                    	Cache\-hit failure
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Size of the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Cache\-hit success
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	Total request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.failure = None
                        self.size = None
                        self.success = None
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:string-memory-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.failure is not None:
                            return True

                        if self.size is not None:
                            return True

                        if self.success is not None:
                            return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:memory'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.edm_memory_info is not None:
                        for child_ref in self.edm_memory_info:
                            if child_ref._has_data():
                                return True

                    if self.memory_info is not None:
                        for child_ref in self.memory_info:
                            if child_ref._has_data():
                                return True

                    if self.string_memory_info is not None:
                        for child_ref in self.string_memory_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Memory']['meta_info']


            class GroupIds(object):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_id = YList()
                    self.group_id.parent = self
                    self.group_id.name = 'group_id'


                class GroupId(object):
                    """
                    Group id for subscriber group
                    
                    .. attribute:: group_id  <key>
                    
                    	Group Id
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: access_tracking_object_name
                    
                    	Access Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: access_tracking_object_status
                    
                    	Access Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: client_session_count
                    
                    	Client Session Count
                    	**type**\: list of    :py:class:`ClientSessionCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount>`
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: description
                    
                    	Group Description
                    	**type**\:  str
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_timer
                    
                    	Switch Over Hold Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_role
                    
                    	Preferred Init Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:   :py:class:`SergShowSoReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSoReasonEnum>`
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\:  str
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_last_down_time
                    
                    	Last Down time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_negotiation_time
                    
                    	Last Negotiation time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_last_up_time
                    
                    	Last UP time of Peer
                    	**type**\:  str
                    
                    .. attribute:: peer_negotiating_role
                    
                    	Peer Negotiating Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SergPeerStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatusEnum>`
                    
                    .. attribute:: pending_session_delete_count
                    
                    	Pending Session Delete Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_session_update_count
                    
                    	Pending Session Update Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: revertive_timer
                    
                    	Revertive timer for SWO back
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SergShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveModeEnum>`
                    
                    .. attribute:: slave_update_failure_count
                    
                    	Slave Session update fail count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_count
                    
                    	Switchover Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: switchover_hold_time
                    
                    	Switchover Hold Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: switchover_revert_time
                    
                    	Switchover Revert Time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.access_tracking_object_name = None
                        self.access_tracking_object_status = None
                        self.client_session_count = YList()
                        self.client_session_count.parent = self
                        self.client_session_count.name = 'client_session_count'
                        self.core_tracking_object_name = None
                        self.core_tracking_object_status = None
                        self.current_role = None
                        self.description = None
                        self.disabled = None
                        self.group_id_xr = None
                        self.hold_timer = None
                        self.init_role = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'
                        self.interface_count = None
                        self.last_switchover_reason = None
                        self.last_switchover_time = None
                        self.negotiating_role = None
                        self.object_tracking_status = None
                        self.peer_current_role = None
                        self.peer_init_role = None
                        self.peer_ipv4_address = None
                        self.peer_ipv6_address = None
                        self.peer_last_down_time = None
                        self.peer_last_negotiation_time = None
                        self.peer_last_up_time = None
                        self.peer_negotiating_role = None
                        self.peer_object_tracking_status = None
                        self.peer_status = None
                        self.pending_session_delete_count = None
                        self.pending_session_update_count = None
                        self.revertive_timer = None
                        self.session_count = None
                        self.slave_mode = None
                        self.slave_update_failure_count = None
                        self.switchover_count = None
                        self.switchover_hold_time = None
                        self.switchover_revert_time = None


                    class ClientSessionCount(object):
                        """
                        Client Session Count
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowCompEnum>`
                        
                        .. attribute:: session_count
                        
                        	Session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.component = None
                            self.session_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:client-session-count'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.component is not None:
                                return True

                            if self.session_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount']['meta_info']


                    class Interface(object):
                        """
                        Interface List
                        
                        .. attribute:: forward_referenced
                        
                        	Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: interface_synchronization_id
                        
                        	Interface Synchronization ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_count
                        
                        	Session Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.forward_referenced = None
                            self.interface_name = None
                            self.interface_synchronization_id = None
                            self.session_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:interface'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.forward_referenced is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.interface_synchronization_id is not None:
                                return True

                            if self.session_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-id[Cisco-IOS-XR-infra-serg-oper:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.access_tracking_object_name is not None:
                            return True

                        if self.access_tracking_object_status is not None:
                            return True

                        if self.client_session_count is not None:
                            for child_ref in self.client_session_count:
                                if child_ref._has_data():
                                    return True

                        if self.core_tracking_object_name is not None:
                            return True

                        if self.core_tracking_object_status is not None:
                            return True

                        if self.current_role is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.disabled is not None:
                            return True

                        if self.group_id_xr is not None:
                            return True

                        if self.hold_timer is not None:
                            return True

                        if self.init_role is not None:
                            return True

                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        if self.interface_count is not None:
                            return True

                        if self.last_switchover_reason is not None:
                            return True

                        if self.last_switchover_time is not None:
                            return True

                        if self.negotiating_role is not None:
                            return True

                        if self.object_tracking_status is not None:
                            return True

                        if self.peer_current_role is not None:
                            return True

                        if self.peer_init_role is not None:
                            return True

                        if self.peer_ipv4_address is not None:
                            return True

                        if self.peer_ipv6_address is not None:
                            return True

                        if self.peer_last_down_time is not None:
                            return True

                        if self.peer_last_negotiation_time is not None:
                            return True

                        if self.peer_last_up_time is not None:
                            return True

                        if self.peer_negotiating_role is not None:
                            return True

                        if self.peer_object_tracking_status is not None:
                            return True

                        if self.peer_status is not None:
                            return True

                        if self.pending_session_delete_count is not None:
                            return True

                        if self.pending_session_update_count is not None:
                            return True

                        if self.revertive_timer is not None:
                            return True

                        if self.session_count is not None:
                            return True

                        if self.slave_mode is not None:
                            return True

                        if self.slave_update_failure_count is not None:
                            return True

                        if self.switchover_count is not None:
                            return True

                        if self.switchover_hold_time is not None:
                            return True

                        if self.switchover_revert_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group_id is not None:
                        for child_ref in self.group_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds']['meta_info']


            class Interfaces(object):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Specify interface name
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: client_status
                    
                    	Interface status for each client
                    	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
                    .. attribute:: forward_referenced
                    
                    	Forward Referenced
                    	**type**\:  bool
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_attribute_update_error_count
                    
                    	Interface Attribute Update Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_add_error_count
                    
                    	Interface Caps Add Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_caps_remove_error_count
                    
                    	Interface Caps Remove Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_disable_error_count
                    
                    	Interface Disable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_enable_error_count
                    
                    	Interface Enable Error Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: interface_oper
                    
                    	Interface Batch Operation
                    	**type**\:   :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:   :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:   :py:class:`SergShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRoleEnum>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.client_status = YList()
                        self.client_status.parent = self
                        self.client_status.name = 'client_status'
                        self.forward_referenced = None
                        self.group_id = None
                        self.interface_attribute_update_error_count = None
                        self.interface_caps_add_error_count = None
                        self.interface_caps_remove_error_count = None
                        self.interface_disable_error_count = None
                        self.interface_enable_error_count = None
                        self.interface_name = None
                        self.interface_oper = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self.interface_status = SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
                        self.interface_status.parent = self
                        self.interface_synchronization_id = None
                        self.role = None
                        self.session_count = None


                    class InterfaceOper(object):
                        """
                        Interface Batch Operation
                        
                        .. attribute:: idb_oper_attr_update
                        
                        	Operational Attribute Update
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_add
                        
                        	Operational Caps Add
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_caps_remove
                        
                        	Operational Caps Remove
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_disable
                        
                        	Operational Registration Disabled
                        	**type**\:  bool
                        
                        .. attribute:: idb_oper_reg_enable
                        
                        	Operational Registration Enabled
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.idb_oper_attr_update = None
                            self.idb_oper_caps_add = None
                            self.idb_oper_caps_remove = None
                            self.idb_oper_reg_disable = None
                            self.idb_oper_reg_enable = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:interface-oper'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.idb_oper_attr_update is not None:
                                return True

                            if self.idb_oper_caps_add is not None:
                                return True

                            if self.idb_oper_caps_remove is not None:
                                return True

                            if self.idb_oper_reg_disable is not None:
                                return True

                            if self.idb_oper_reg_enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper']['meta_info']


                    class InterfaceStatus(object):
                        """
                        Interface Status
                        
                        .. attribute:: idb_client_eoms_pending
                        
                        	Interface Client EOMS Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_caps_added
                        
                        	Interface State Caps Added
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_fwd_ref
                        
                        	Interface Forward Referenced
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_owned_re_source
                        
                        	Interface State Owned Resource
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_caps_rem
                        
                        	Interface Caps Remove Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_p_end_reg_disable
                        
                        	Interface Registration Disable Pending
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_registered
                        
                        	Interface State Registered
                        	**type**\:  bool
                        
                        .. attribute:: idb_state_stale
                        
                        	Interface State Stale
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.idb_client_eoms_pending = None
                            self.idb_state_caps_added = None
                            self.idb_state_fwd_ref = None
                            self.idb_state_owned_re_source = None
                            self.idb_state_p_end_caps_rem = None
                            self.idb_state_p_end_reg_disable = None
                            self.idb_state_registered = None
                            self.idb_state_stale = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:interface-status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.idb_client_eoms_pending is not None:
                                return True

                            if self.idb_state_caps_added is not None:
                                return True

                            if self.idb_state_fwd_ref is not None:
                                return True

                            if self.idb_state_owned_re_source is not None:
                                return True

                            if self.idb_state_p_end_caps_rem is not None:
                                return True

                            if self.idb_state_p_end_reg_disable is not None:
                                return True

                            if self.idb_state_registered is not None:
                                return True

                            if self.idb_state_stale is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus']['meta_info']


                    class ClientStatus(object):
                        """
                        Interface status for each client
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SergShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowCompEnum>`
                        
                        .. attribute:: serg_show_idb_client_eoms_pending
                        
                        	SERG SHOW IDB CLIENT EOMS PENDING
                        	**type**\:  bool
                        
                        .. attribute:: serg_show_idb_client_sync_eod_pending
                        
                        	SERG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\:  bool
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-serg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.component = None
                            self.serg_show_idb_client_eoms_pending = None
                            self.serg_show_idb_client_sync_eod_pending = None
                            self.session_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:client-status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.component is not None:
                                return True

                            if self.serg_show_idb_client_eoms_pending is not None:
                                return True

                            if self.serg_show_idb_client_sync_eod_pending is not None:
                                return True

                            if self.session_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                            return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:interface[Cisco-IOS-XR-infra-serg-oper:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.client_status is not None:
                            for child_ref in self.client_status:
                                if child_ref._has_data():
                                    return True

                        if self.forward_referenced is not None:
                            return True

                        if self.group_id is not None:
                            return True

                        if self.interface_attribute_update_error_count is not None:
                            return True

                        if self.interface_caps_add_error_count is not None:
                            return True

                        if self.interface_caps_remove_error_count is not None:
                            return True

                        if self.interface_disable_error_count is not None:
                            return True

                        if self.interface_enable_error_count is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.interface_oper is not None and self.interface_oper._has_data():
                            return True

                        if self.interface_status is not None and self.interface_status._has_data():
                            return True

                        if self.interface_synchronization_id is not None:
                            return True

                        if self.role is not None:
                            return True

                        if self.session_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces']['meta_info']


            class StatsGlobal(object):
                """
                Stats Global
                
                .. attribute:: client_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\:  str
                
                .. attribute:: client_status
                
                	Client Status
                	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus>`
                
                .. attribute:: intf_status_statistics
                
                	intf status statistics
                	**type**\:   :py:class:`IntfStatusStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics>`
                
                .. attribute:: opaque_memory_status
                
                	Opaque memory Stats
                	**type**\: list of    :py:class:`OpaqueMemoryStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus>`
                
                .. attribute:: peer_action_timer
                
                	Value in Seconds to trigger the peer actions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peer_init_sync_time_stamp
                
                	Synchronization TimeStamp
                	**type**\:  str
                
                .. attribute:: redundancy_role
                
                	Redundancy Role
                	**type**\:  str
                
                .. attribute:: restart_client_sync_in_progress
                
                	Restart Client Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: restart_peer_sync_in_progress
                
                	Restart Peer Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: retry_timer_remaining
                
                	Value in Seconds to trigger the retry
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: source_interface_ipv4_address
                
                	Source Interface IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_interface_ipv6_address
                
                	Source Interface IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_interface_name
                
                	Source Interface Name
                	**type**\:  str
                
                .. attribute:: sync_in_progress
                
                	Sync In Progress Flag
                	**type**\:  bool
                
                .. attribute:: tx_list_client_connection_down
                
                	TxListClientConnectionDown
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_connection_up
                
                	TxListClientConnectionUp
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_de_registration_invalid
                
                	TxListClientDeRegistrationInvalid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_message_call_back
                
                	TxListClientMessageCallBack
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_peer_done
                
                	TxListClientPeerDone
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_invalid
                
                	TxListClientReceiveCommandInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_command_valid
                
                	TxListClientReceiveCommandValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_invalid
                
                	TxListClientReceiveInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_session_invalid
                
                	TxListClientReceiveSessionSessionInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_session_sessionvalid
                
                	TxListClientReceiveSessionSessionValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_receive_valid
                
                	TxListClientReceiveValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_client_registration_invalid
                
                	TxListClientRegistrationInvalid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_over_tcp_status
                
                	TCP TxList Statistics
                	**type**\: list of    :py:class:`TxListOverTcpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus>`
                
                .. attribute:: tx_list_peer_cmd_connection_down_not_ok
                
                	TxListPeerCmdConnectionDownNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_cmd_connection_up_not_ok
                
                	TxListPeerCmdConnectionUpNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_de_registration_invalid
                
                	TxListPeerDeRegistrationInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_done
                
                	TxListPeerDone
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_invalid
                
                	TxListPeerMessageCallBackInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_message_call_back_valid
                
                	TxListPeerMessageCallBackValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_registration_invalid
                
                	TxListPeerRegistrationInValid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_down_not_ok
                
                	TxListPeerSessionConnectionDownNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_session_connection_up_not_ok
                
                	TxListPeerSessionConnectionUpNotOk
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_peer_timer_handler
                
                	TxListPeerTimerHandler
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tx_list_statistics
                
                	tx list statistics
                	**type**\:   :py:class:`TxListStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics>`
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\:  str
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client_init_sync_time_stamp = None
                    self.client_status = YList()
                    self.client_status.parent = self
                    self.client_status.name = 'client_status'
                    self.intf_status_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics()
                    self.intf_status_statistics.parent = self
                    self.opaque_memory_status = YList()
                    self.opaque_memory_status.parent = self
                    self.opaque_memory_status.name = 'opaque_memory_status'
                    self.peer_action_timer = None
                    self.peer_init_sync_time_stamp = None
                    self.redundancy_role = None
                    self.restart_client_sync_in_progress = None
                    self.restart_peer_sync_in_progress = None
                    self.retry_timer_remaining = None
                    self.source_interface_ipv4_address = None
                    self.source_interface_ipv6_address = None
                    self.source_interface_name = None
                    self.sync_in_progress = None
                    self.tx_list_client_connection_down = None
                    self.tx_list_client_connection_up = None
                    self.tx_list_client_de_registration_invalid = None
                    self.tx_list_client_message_call_back = None
                    self.tx_list_client_peer_done = None
                    self.tx_list_client_receive_command_invalid = None
                    self.tx_list_client_receive_command_valid = None
                    self.tx_list_client_receive_invalid = None
                    self.tx_list_client_receive_session_session_invalid = None
                    self.tx_list_client_receive_session_sessionvalid = None
                    self.tx_list_client_receive_valid = None
                    self.tx_list_client_registration_invalid = None
                    self.tx_list_over_tcp_status = YList()
                    self.tx_list_over_tcp_status.parent = self
                    self.tx_list_over_tcp_status.name = 'tx_list_over_tcp_status'
                    self.tx_list_peer_cmd_connection_down_not_ok = None
                    self.tx_list_peer_cmd_connection_up_not_ok = None
                    self.tx_list_peer_de_registration_invalid = None
                    self.tx_list_peer_done = None
                    self.tx_list_peer_message_call_back_invalid = None
                    self.tx_list_peer_message_call_back_valid = None
                    self.tx_list_peer_registration_invalid = None
                    self.tx_list_peer_session_connection_down_not_ok = None
                    self.tx_list_peer_session_connection_up_not_ok = None
                    self.tx_list_peer_timer_handler = None
                    self.tx_list_statistics = SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics()
                    self.tx_list_statistics.parent = self
                    self.vrf_name = None


                class IntfStatusStatistics(object):
                    """
                    intf status statistics
                    
                    .. attribute:: grp_bound_cnt
                    
                    	No. of interface bound to a group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: non_stale_cnt
                    
                    	No. of non stale interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_caps_rem_cnt
                    
                    	No. of interfaces pending caps remove
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_other_batch_oper_cnt
                    
                    	No. of interfaces pending for other (except unreg/caps rem) batch oper
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pend_reg_disable_cnt
                    
                    	No. of interfaces pending red disable
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.grp_bound_cnt = None
                        self.non_stale_cnt = None
                        self.pend_caps_rem_cnt = None
                        self.pend_other_batch_oper_cnt = None
                        self.pend_reg_disable_cnt = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:intf-status-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.grp_bound_cnt is not None:
                            return True

                        if self.non_stale_cnt is not None:
                            return True

                        if self.pend_caps_rem_cnt is not None:
                            return True

                        if self.pend_other_batch_oper_cnt is not None:
                            return True

                        if self.pend_reg_disable_cnt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics']['meta_info']


                class TxListStatistics(object):
                    """
                    tx list statistics
                    
                    .. attribute:: tx_list_clean_command
                    
                    	TxListCleanCommand
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_marker
                    
                    	TxListCleanMarker
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_clean_negotiation
                    
                    	TxListCleanNegotiation
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_ok
                    
                    	TxListEncodeCommandOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_command_partial_write
                    
                    	TxListEncodeCommandPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_marker_ok
                    
                    	TxListEncodeMarkerOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_marker_partial_write
                    
                    	TxListEncodeMarkerPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_ok
                    
                    	TxListEncodeNegotiationOk
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_list_encode_negotiation_partial_write
                    
                    	TxListEncodeNegotiationPartialWrite
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tx_list_clean_command = None
                        self.tx_list_clean_marker = None
                        self.tx_list_clean_negotiation = None
                        self.tx_list_encode_command_ok = None
                        self.tx_list_encode_command_partial_write = None
                        self.tx_list_encode_marker_ok = None
                        self.tx_list_encode_marker_partial_write = None
                        self.tx_list_encode_negotiation_ok = None
                        self.tx_list_encode_negotiation_partial_write = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:tx-list-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.tx_list_clean_command is not None:
                            return True

                        if self.tx_list_clean_marker is not None:
                            return True

                        if self.tx_list_clean_negotiation is not None:
                            return True

                        if self.tx_list_encode_command_ok is not None:
                            return True

                        if self.tx_list_encode_command_partial_write is not None:
                            return True

                        if self.tx_list_encode_marker_ok is not None:
                            return True

                        if self.tx_list_encode_marker_partial_write is not None:
                            return True

                        if self.tx_list_encode_negotiation_ok is not None:
                            return True

                        if self.tx_list_encode_negotiation_partial_write is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics']['meta_info']


                class ClientStatus(object):
                    """
                    Client Status
                    
                    .. attribute:: clean_up_timer_remaining
                    
                    	Value in Seconds to trigger the client cleanup
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: client_connection_status
                    
                    	ClientConnectionStatus
                    	**type**\:  bool
                    
                    .. attribute:: client_initialization_synchronization_pending
                    
                    	ClientInitializationSynchronizationPending
                    	**type**\:  bool
                    
                    .. attribute:: client_synchronization_end_of_download_pending
                    
                    	ClientSynchronizationEndOfDownloadPending
                    	**type**\:  bool
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:   :py:class:`SergShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowCompEnum>`
                    
                    .. attribute:: down_time_stamp
                    
                    	DownTimeStamp
                    	**type**\:  str
                    
                    .. attribute:: up_time_stamp
                    
                    	UpTimeStamp
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.clean_up_timer_remaining = None
                        self.client_connection_status = None
                        self.client_initialization_synchronization_pending = None
                        self.client_synchronization_end_of_download_pending = None
                        self.component = None
                        self.down_time_stamp = None
                        self.up_time_stamp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:client-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.clean_up_timer_remaining is not None:
                            return True

                        if self.client_connection_status is not None:
                            return True

                        if self.client_initialization_synchronization_pending is not None:
                            return True

                        if self.client_synchronization_end_of_download_pending is not None:
                            return True

                        if self.component is not None:
                            return True

                        if self.down_time_stamp is not None:
                            return True

                        if self.up_time_stamp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus']['meta_info']


                class OpaqueMemoryStatus(object):
                    """
                    Opaque memory Stats
                    
                    .. attribute:: component
                    
                    	Component
                    	**type**\:   :py:class:`SergShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowCompEnum>`
                    
                    .. attribute:: opaque_data_size
                    
                    	Current Opaque Data Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_high_size
                    
                    	High Watermark of Opaque Data Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opaque_size
                    
                    	Current Opaque Memory Size for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_count
                    
                    	Session count for each component
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.component = None
                        self.opaque_data_size = None
                        self.opaque_high_size = None
                        self.opaque_size = None
                        self.session_count = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:opaque-memory-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.component is not None:
                            return True

                        if self.opaque_data_size is not None:
                            return True

                        if self.opaque_high_size is not None:
                            return True

                        if self.opaque_size is not None:
                            return True

                        if self.session_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus']['meta_info']


                class TxListOverTcpStatus(object):
                    """
                    TCP TxList Statistics
                    
                    .. attribute:: accept_count
                    
                    	Socket Accept Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_socket_count
                    
                    	Active Socket Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: blocked_connect_count
                    
                    	Blocked Socket Connect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: buffer_cache_hit
                    
                    	Buffer Cache Hit Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_cache_miss
                    
                    	Buffer Cache Miss Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_freed_count
                    
                    	Buffer Free Count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: buffer_full_occurence_count
                    
                    	Buffer Full on Write Occurence Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_received
                    
                    	Bytes Received Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes Sent Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: connect_count
                    
                    	Socket Connect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_retry_count
                    
                    	Socket Connect Retry Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_received_message_size
                    
                    	Maximum Size of Received Message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_requested_buffer_size
                    
                    	Maximum Size of Requested Buffer
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: maximum_sent_message_size
                    
                    	Maximum Size of Sent Message
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_bytes_count
                    
                    	Partial Message Memory Move Byte Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mem_move_message_count
                    
                    	Partial Message Memory Move Occurence Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_received
                    
                    	Message Received Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_sent
                    
                    	Message Sent Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_pause_count
                    
                    	Peer Pause Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: remote_node_down_count
                    
                    	Remote Peer DisConnect Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_read_count
                    
                    	Socket Read Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_write_count
                    
                    	Socket Write Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.accept_count = None
                        self.active_socket_count = None
                        self.blocked_connect_count = None
                        self.buffer_cache_hit = None
                        self.buffer_cache_miss = None
                        self.buffer_freed_count = None
                        self.buffer_full_occurence_count = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.connect_count = None
                        self.connect_retry_count = None
                        self.maximum_received_message_size = None
                        self.maximum_requested_buffer_size = None
                        self.maximum_sent_message_size = None
                        self.mem_move_bytes_count = None
                        self.mem_move_message_count = None
                        self.messages_received = None
                        self.messages_sent = None
                        self.peer_pause_count = None
                        self.remote_node_down_count = None
                        self.socket_read_count = None
                        self.socket_write_count = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:tx-list-over-tcp-status'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accept_count is not None:
                            return True

                        if self.active_socket_count is not None:
                            return True

                        if self.blocked_connect_count is not None:
                            return True

                        if self.buffer_cache_hit is not None:
                            return True

                        if self.buffer_cache_miss is not None:
                            return True

                        if self.buffer_freed_count is not None:
                            return True

                        if self.buffer_full_occurence_count is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.connect_count is not None:
                            return True

                        if self.connect_retry_count is not None:
                            return True

                        if self.maximum_received_message_size is not None:
                            return True

                        if self.maximum_requested_buffer_size is not None:
                            return True

                        if self.maximum_sent_message_size is not None:
                            return True

                        if self.mem_move_bytes_count is not None:
                            return True

                        if self.mem_move_message_count is not None:
                            return True

                        if self.messages_received is not None:
                            return True

                        if self.messages_sent is not None:
                            return True

                        if self.peer_pause_count is not None:
                            return True

                        if self.remote_node_down_count is not None:
                            return True

                        if self.socket_read_count is not None:
                            return True

                        if self.socket_write_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:stats-global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.client_init_sync_time_stamp is not None:
                        return True

                    if self.client_status is not None:
                        for child_ref in self.client_status:
                            if child_ref._has_data():
                                return True

                    if self.intf_status_statistics is not None and self.intf_status_statistics._has_data():
                        return True

                    if self.opaque_memory_status is not None:
                        for child_ref in self.opaque_memory_status:
                            if child_ref._has_data():
                                return True

                    if self.peer_action_timer is not None:
                        return True

                    if self.peer_init_sync_time_stamp is not None:
                        return True

                    if self.redundancy_role is not None:
                        return True

                    if self.restart_client_sync_in_progress is not None:
                        return True

                    if self.restart_peer_sync_in_progress is not None:
                        return True

                    if self.retry_timer_remaining is not None:
                        return True

                    if self.source_interface_ipv4_address is not None:
                        return True

                    if self.source_interface_ipv6_address is not None:
                        return True

                    if self.source_interface_name is not None:
                        return True

                    if self.sync_in_progress is not None:
                        return True

                    if self.tx_list_client_connection_down is not None:
                        return True

                    if self.tx_list_client_connection_up is not None:
                        return True

                    if self.tx_list_client_de_registration_invalid is not None:
                        return True

                    if self.tx_list_client_message_call_back is not None:
                        return True

                    if self.tx_list_client_peer_done is not None:
                        return True

                    if self.tx_list_client_receive_command_invalid is not None:
                        return True

                    if self.tx_list_client_receive_command_valid is not None:
                        return True

                    if self.tx_list_client_receive_invalid is not None:
                        return True

                    if self.tx_list_client_receive_session_session_invalid is not None:
                        return True

                    if self.tx_list_client_receive_session_sessionvalid is not None:
                        return True

                    if self.tx_list_client_receive_valid is not None:
                        return True

                    if self.tx_list_client_registration_invalid is not None:
                        return True

                    if self.tx_list_over_tcp_status is not None:
                        for child_ref in self.tx_list_over_tcp_status:
                            if child_ref._has_data():
                                return True

                    if self.tx_list_peer_cmd_connection_down_not_ok is not None:
                        return True

                    if self.tx_list_peer_cmd_connection_up_not_ok is not None:
                        return True

                    if self.tx_list_peer_de_registration_invalid is not None:
                        return True

                    if self.tx_list_peer_done is not None:
                        return True

                    if self.tx_list_peer_message_call_back_invalid is not None:
                        return True

                    if self.tx_list_peer_message_call_back_valid is not None:
                        return True

                    if self.tx_list_peer_registration_invalid is not None:
                        return True

                    if self.tx_list_peer_session_connection_down_not_ok is not None:
                        return True

                    if self.tx_list_peer_session_connection_up_not_ok is not None:
                        return True

                    if self.tx_list_peer_timer_handler is not None:
                        return True

                    if self.tx_list_statistics is not None and self.tx_list_statistics._has_data():
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']


            class GroupSummaries(object):
                """
                Session data for a particular node
                
                .. attribute:: group_summary
                
                	Session redundancy agent group summary
                	**type**\: list of    :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'infra-serg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_summary = YList()
                    self.group_summary.parent = self
                    self.group_summary.name = 'group_summary'


                class GroupSummary(object):
                    """
                    Session redundancy agent group summary
                    
                    .. attribute:: group_id  <key>
                    
                    	GroupId
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: disabled
                    
                    	Disabled by Config
                    	**type**\:  bool
                    
                    .. attribute:: group_id_xr
                    
                    	Group ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	Interface Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_ipv4_address
                    
                    	Peer IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_ipv6_address
                    
                    	Peer IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SergPeerStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergPeerStatusEnum>`
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:   :py:class:`SergShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowRoleEnum>`
                    
                    .. attribute:: role
                    
                    	SERG Role
                    	**type**\:   :py:class:`SergShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowImRoleEnum>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SergShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper.SergShowSlaveModeEnum>`
                    
                    

                    """

                    _prefix = 'infra-serg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.disabled = None
                        self.group_id_xr = None
                        self.interface_count = None
                        self.object_tracking_status = None
                        self.peer_ipv4_address = None
                        self.peer_ipv6_address = None
                        self.peer_status = None
                        self.pending_add_session_count = None
                        self.preferred_role = None
                        self.role = None
                        self.session_count = None
                        self.slave_mode = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-summary[Cisco-IOS-XR-infra-serg-oper:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.disabled is not None:
                            return True

                        if self.group_id_xr is not None:
                            return True

                        if self.interface_count is not None:
                            return True

                        if self.object_tracking_status is not None:
                            return True

                        if self.peer_ipv4_address is not None:
                            return True

                        if self.peer_ipv6_address is not None:
                            return True

                        if self.peer_status is not None:
                            return True

                        if self.pending_add_session_count is not None:
                            return True

                        if self.preferred_role is not None:
                            return True

                        if self.role is not None:
                            return True

                        if self.session_count is not None:
                            return True

                        if self.slave_mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                        return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-serg-oper:group-summaries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group_summary is not None:
                        for child_ref in self.group_summary:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                    return meta._meta_table['SessionRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/Cisco-IOS-XR-infra-serg-oper:nodes/Cisco-IOS-XR-infra-serg-oper:node[Cisco-IOS-XR-infra-serg-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.client_ids is not None and self.client_ids._has_data():
                    return True

                if self.group_id_xr is not None and self.group_id_xr._has_data():
                    return True

                if self.group_ids is not None and self.group_ids._has_data():
                    return True

                if self.group_summaries is not None and self.group_summaries._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.memory is not None and self.memory._has_data():
                    return True

                if self.stats_global is not None and self.stats_global._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
                return meta._meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent/Cisco-IOS-XR-infra-serg-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
            return meta._meta_table['SessionRedundancyAgent.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-serg-oper:session-redundancy-agent'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_serg_oper as meta
        return meta._meta_table['SessionRedundancyAgent']['meta_info']


