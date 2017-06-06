""" Cisco_IOS_XR_subscriber_srg_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-srg package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-redundancy\-manager\: Subscriber Redundancy Manager
    information
  subscriber\-redundancy\-agent\: subscriber redundancy agent

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SrgPeerStatusEnum(Enum):
    """
    SrgPeerStatusEnum

    SRG Peer Status

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgPeerStatusEnum']


class SrgShowCompEnum(Enum):
    """
    SrgShowCompEnum

    SRG Components

    .. data:: srga = 0

    	SRG Agent

    .. data:: dhcpv4 = 1

    	DHCPv4

    .. data:: dhcpv6 = 2

    	DHCPv6

    .. data:: pppoe = 3

    	PPPoE

    .. data:: ppp = 4

    	PPP

    .. data:: l2tp = 5

    	L2TP

    .. data:: iedge = 6

    	iEdge

    """

    srga = 0

    dhcpv4 = 1

    dhcpv6 = 2

    pppoe = 3

    ppp = 4

    l2tp = 5

    iedge = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowCompEnum']


class SrgShowImRoleEnum(Enum):
    """
    SrgShowImRoleEnum

    SRG Interface Management Role

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowImRoleEnum']


class SrgShowRoleEnum(Enum):
    """
    SrgShowRoleEnum

    SRG Role

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowRoleEnum']


class SrgShowSessionErrorEnum(Enum):
    """
    SrgShowSessionErrorEnum

    SRG Session Error Operation

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowSessionErrorEnum']


class SrgShowSessionOperationEnum(Enum):
    """
    SrgShowSessionOperationEnum

    SRG Session Operation

    .. data:: none = 0

    	No Operation

    .. data:: update = 1

    	SRG Session Update Operation

    .. data:: delete = 2

    	SRG Session Delete Operation

    .. data:: in_sync = 3

    	SRG Session In Sync

    """

    none = 0

    update = 1

    delete = 2

    in_sync = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowSessionOperationEnum']


class SrgShowSlaveModeEnum(Enum):
    """
    SrgShowSlaveModeEnum

    SRG Slave Mode

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowSlaveModeEnum']


class SrgShowSoReasonEnum(Enum):
    """
    SrgShowSoReasonEnum

    Subscriber Redundancy Switchover Reason

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

    .. data:: srg_show_so_reason_max = 5

    	Unknown Switchover Reason

    """

    internal = 0

    admin = 1

    peer_up = 2

    peer_down = 3

    object_tracking_status_change = 4

    srg_show_so_reason_max = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SrgShowSoReasonEnum']



class SubscriberRedundancyManager(object):
    """
    Subscriber Redundancy Manager information
    
    .. attribute:: groups
    
    	Subscriber Redundancy Manager group table
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups>`
    
    .. attribute:: interfaces
    
    	Subscriber Redundancy Manager interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces>`
    
    .. attribute:: summary
    
    	Subscriber redundancy manager summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Summary>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.groups = SubscriberRedundancyManager.Groups()
        self.groups.parent = self
        self.interfaces = SubscriberRedundancyManager.Interfaces()
        self.interfaces.parent = self
        self.summary = SubscriberRedundancyManager.Summary()
        self.summary.parent = self


    class Groups(object):
        """
        Subscriber Redundancy Manager group table
        
        .. attribute:: group
        
        	Subscriber redundancy manager group
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Groups.Group>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            Subscriber redundancy manager group
            
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
            	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
            
            .. attribute:: role
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRoleEnum>`
            
            .. attribute:: slave_mode
            
            	Slave Mode
            	**type**\:   :py:class:`SrgShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveModeEnum>`
            
            .. attribute:: virtual_mac_address
            
            	Virtual MAC Address
            	**type**\:  str
            
            .. attribute:: virtual_mac_address_disable
            
            	Virtual MAC Address Disable
            	**type**\:  bool
            
            

            """

            _prefix = 'subscriber-srg-oper'
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
                self.virtual_mac_address = None
                self.virtual_mac_address_disable = None

            @property
            def _common_path(self):
                if self.group is None:
                    raise YPYModelError('Key property group is None')

                return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/Cisco-IOS-XR-subscriber-srg-oper:groups/Cisco-IOS-XR-subscriber-srg-oper:group[Cisco-IOS-XR-subscriber-srg-oper:group = ' + str(self.group) + ']'

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

                if self.virtual_mac_address is not None:
                    return True

                if self.virtual_mac_address_disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                return meta._meta_table['SubscriberRedundancyManager.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/Cisco-IOS-XR-subscriber-srg-oper:groups'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
            return meta._meta_table['SubscriberRedundancyManager.Groups']['meta_info']


    class Summary(object):
        """
        Subscriber redundancy manager summary
        
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
        	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
        
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
        	**type**\:   :py:class:`SrgShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveModeEnum>`
        
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

        _prefix = 'subscriber-srg-oper'
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

            return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/Cisco-IOS-XR-subscriber-srg-oper:summary'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
            return meta._meta_table['SubscriberRedundancyManager.Summary']['meta_info']


    class Interfaces(object):
        """
        Subscriber Redundancy Manager interface table
        
        .. attribute:: interface
        
        	Subscriber redundancy manager interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyManager.Interfaces.Interface>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Subscriber redundancy manager interface
            
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
            
            	SRG Role
            	**type**\:   :py:class:`SrgShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRoleEnum>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
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

                return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/Cisco-IOS-XR-subscriber-srg-oper:interfaces/Cisco-IOS-XR-subscriber-srg-oper:interface[Cisco-IOS-XR-subscriber-srg-oper:interface = ' + str(self.interface) + ']'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                return meta._meta_table['SubscriberRedundancyManager.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager/Cisco-IOS-XR-subscriber-srg-oper:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
            return meta._meta_table['SubscriberRedundancyManager.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-manager'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SubscriberRedundancyManager']['meta_info']


class SubscriberRedundancyAgent(object):
    """
    subscriber redundancy agent
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes>`
    
    

    """

    _prefix = 'subscriber-srg-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = SubscriberRedundancyAgent.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-srg-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: group_id_xr
            
            	Data for particular subscriber group session
            	**type**\:   :py:class:`GroupIdXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr>`
            
            .. attribute:: group_ids
            
            	Data for particular subscriber group 
            	**type**\:   :py:class:`GroupIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds>`
            
            .. attribute:: group_summaries
            
            	Subscriber data for a particular node
            	**type**\:   :py:class:`GroupSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries>`
            
            .. attribute:: interfaces
            
            	List of interfaces
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'subscriber-srg-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.group_id_xr = SubscriberRedundancyAgent.Nodes.Node.GroupIdXr()
                self.group_id_xr.parent = self
                self.group_ids = SubscriberRedundancyAgent.Nodes.Node.GroupIds()
                self.group_ids.parent = self
                self.group_summaries = SubscriberRedundancyAgent.Nodes.Node.GroupSummaries()
                self.group_summaries.parent = self
                self.interfaces = SubscriberRedundancyAgent.Nodes.Node.Interfaces()
                self.interfaces.parent = self


            class GroupIdXr(object):
                """
                Data for particular subscriber group session
                
                .. attribute:: group_id
                
                	Group id for subscriber group session
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
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
                    
                    .. attribute:: inner_vlan
                    
                    	Inner VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    .. attribute:: l2tp_tunnel_id
                    
                    	L2TP Tunnel local ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: negative_acknowledgement_update_all
                    
                    	Negative Acknowledgement Update Flag is Set
                    	**type**\:  bool
                    
                    .. attribute:: outer_vlan
                    
                    	Outer VLAN Information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe_session_id
                    
                    	PPPoE Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: role_master
                    
                    	Master Role is Set
                    	**type**\:  bool
                    
                    .. attribute:: session_detailed_information
                    
                    	More Session Information
                    	**type**\: list of    :py:class:`SessionDetailedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation>`
                    
                    .. attribute:: session_mac_address
                    
                    	Session MAC Address
                    	**type**\:  str
                    
                    .. attribute:: session_sync_error_information
                    
                    	Session Synchroniation Error Information
                    	**type**\: list of    :py:class:`SessionSyncErrorInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation>`
                    
                    .. attribute:: valid_mac_address
                    
                    	Holds a Valid MAC Address
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.group_id_xr = None
                        self.inner_vlan = None
                        self.interface_name = None
                        self.l2tp_tunnel_id = None
                        self.negative_acknowledgement_update_all = None
                        self.outer_vlan = None
                        self.pppoe_session_id = None
                        self.role_master = None
                        self.session_detailed_information = YList()
                        self.session_detailed_information.parent = self
                        self.session_detailed_information.name = 'session_detailed_information'
                        self.session_mac_address = None
                        self.session_sync_error_information = YList()
                        self.session_sync_error_information.parent = self
                        self.session_sync_error_information.name = 'session_sync_error_information'
                        self.valid_mac_address = None


                    class SessionDetailedInformation(object):
                        """
                        More Session Information
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SrgShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowCompEnum>`
                        
                        .. attribute:: marked_for_cleanup
                        
                        	Marked For Cleanup
                        	**type**\:  bool
                        
                        .. attribute:: marked_for_sweeping
                        
                        	Marked For Sweeping
                        	**type**\:  bool
                        
                        .. attribute:: operation
                        
                        	Operation Code
                        	**type**\:   :py:class:`SrgShowSessionOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionOperationEnum>`
                        
                        .. attribute:: tx_list_queue_fail
                        
                        	Tx List Queue Failed
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:session-detailed-information'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation']['meta_info']


                    class SessionSyncErrorInformation(object):
                        """
                        Session Synchroniation Error Information
                        
                        .. attribute:: last_error_code
                        
                        	Last Error Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_error_type
                        
                        	Last Error Type
                        	**type**\:   :py:class:`SrgShowSessionErrorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSessionErrorEnum>`
                        
                        .. attribute:: sync_error_count
                        
                        	No. of Errors occured during Synchronization
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:session-sync-error-information'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-id[Cisco-IOS-XR-subscriber-srg-oper:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.group_id_xr is not None:
                            return True

                        if self.inner_vlan is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.l2tp_tunnel_id is not None:
                            return True

                        if self.negative_acknowledgement_update_all is not None:
                            return True

                        if self.outer_vlan is not None:
                            return True

                        if self.pppoe_session_id is not None:
                            return True

                        if self.role_master is not None:
                            return True

                        if self.session_detailed_information is not None:
                            for child_ref in self.session_detailed_information:
                                if child_ref._has_data():
                                    return True

                        if self.session_mac_address is not None:
                            return True

                        if self.session_sync_error_information is not None:
                            for child_ref in self.session_sync_error_information:
                                if child_ref._has_data():
                                    return True

                        if self.valid_mac_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                        return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-id-xr'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                    return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info']


            class Interfaces(object):
                """
                List of interfaces
                
                .. attribute:: interface
                
                	Specify interface name
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
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
                    	**type**\: list of    :py:class:`ClientStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus>`
                    
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
                    	**type**\:   :py:class:`InterfaceOper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper>`
                    
                    .. attribute:: interface_status
                    
                    	Interface Status
                    	**type**\:   :py:class:`InterfaceStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus>`
                    
                    .. attribute:: interface_synchronization_id
                    
                    	Interface Sync ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRoleEnum>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
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
                        self.interface_oper = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper()
                        self.interface_oper.parent = self
                        self.interface_status = SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus()
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

                        _prefix = 'subscriber-srg-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:interface-oper'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper']['meta_info']


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

                        _prefix = 'subscriber-srg-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:interface-status'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus']['meta_info']


                    class ClientStatus(object):
                        """
                        Interface status for each client
                        
                        .. attribute:: component
                        
                        	Component
                        	**type**\:   :py:class:`SrgShowCompEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowCompEnum>`
                        
                        .. attribute:: session_count
                        
                        	session count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_show_idb_client_eoms_pending
                        
                        	SRG SHOW IDB CLIENT EOMS PENDING
                        	**type**\:  bool
                        
                        .. attribute:: srg_show_idb_client_sync_eod_pending
                        
                        	SRG SHOW IDB CLIENT SYNC EOD PENDING
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'subscriber-srg-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.component = None
                            self.session_count = None
                            self.srg_show_idb_client_eoms_pending = None
                            self.srg_show_idb_client_sync_eod_pending = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:client-status'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.component is not None:
                                return True

                            if self.session_count is not None:
                                return True

                            if self.srg_show_idb_client_eoms_pending is not None:
                                return True

                            if self.srg_show_idb_client_sync_eod_pending is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:interface[Cisco-IOS-XR-subscriber-srg-oper:interface = ' + str(self.interface) + ']'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                        return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                    return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces']['meta_info']


            class GroupSummaries(object):
                """
                Subscriber data for a particular node
                
                .. attribute:: group_summary
                
                	Subscriber redundancy agent group summary
                	**type**\: list of    :py:class:`GroupSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_summary = YList()
                    self.group_summary.parent = self
                    self.group_summary.name = 'group_summary'


                class GroupSummary(object):
                    """
                    Subscriber redundancy agent group summary
                    
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
                    	**type**\:   :py:class:`SrgPeerStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatusEnum>`
                    
                    .. attribute:: pending_add_session_count
                    
                    	Pending Session Count for Synchornization
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: preferred_role
                    
                    	Preferred Role
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
                    .. attribute:: role
                    
                    	SRG Role
                    	**type**\:   :py:class:`SrgShowImRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowImRoleEnum>`
                    
                    .. attribute:: session_count
                    
                    	Session Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: slave_mode
                    
                    	Slave Mode
                    	**type**\:   :py:class:`SrgShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveModeEnum>`
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-summary[Cisco-IOS-XR-subscriber-srg-oper:group-id = ' + str(self.group_id) + ']'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                        return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-summaries'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                    return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info']


            class GroupIds(object):
                """
                Data for particular subscriber group 
                
                .. attribute:: group_id
                
                	Group id for subscriber group
                	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId>`
                
                

                """

                _prefix = 'subscriber-srg-oper'
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
                    
                    .. attribute:: core_tracking_object_name
                    
                    	Core Object Tracking Name
                    	**type**\:  str
                    
                    .. attribute:: core_tracking_object_status
                    
                    	Core Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: current_role
                    
                    	Current Role
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
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
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
                    .. attribute:: interface
                    
                    	Interface List
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface>`
                    
                    .. attribute:: interface_count
                    
                    	No. of Configured Interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2tp_source_ip
                    
                    	L2TP Souce IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: last_switchover_reason
                    
                    	Last Switchover Reason
                    	**type**\:   :py:class:`SrgShowSoReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSoReasonEnum>`
                    
                    .. attribute:: last_switchover_time
                    
                    	Last Switchover time
                    	**type**\:  str
                    
                    .. attribute:: negotiating_role
                    
                    	Negotiating Role
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
                    .. attribute:: object_tracking_status
                    
                    	Object Tracking Status (Enabled/Disabled)
                    	**type**\:  bool
                    
                    .. attribute:: peer_current_role
                    
                    	Peer Current Role
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
                    .. attribute:: peer_init_role
                    
                    	Peer Preferred Init Role
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
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
                    	**type**\:   :py:class:`SrgShowRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowRoleEnum>`
                    
                    .. attribute:: peer_object_tracking_status
                    
                    	Peer Object Tracking Status
                    	**type**\:  bool
                    
                    .. attribute:: peer_status
                    
                    	Peer Status
                    	**type**\:   :py:class:`SrgPeerStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgPeerStatusEnum>`
                    
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
                    	**type**\:   :py:class:`SrgShowSlaveModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper.SrgShowSlaveModeEnum>`
                    
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
                    
                    .. attribute:: tunnel_count
                    
                    	Tunnel Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: virtual_mac_address
                    
                    	Virtual MAC Address
                    	**type**\:  str
                    
                    .. attribute:: virtual_mac_address_disable
                    
                    	Virtual MAC Address Disable
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'subscriber-srg-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.access_tracking_object_name = None
                        self.access_tracking_object_status = None
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
                        self.l2tp_source_ip = None
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
                        self.tunnel_count = None
                        self.virtual_mac_address = None
                        self.virtual_mac_address_disable = None


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

                        _prefix = 'subscriber-srg-oper'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:interface'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                            return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-id[Cisco-IOS-XR-subscriber-srg-oper:group-id = ' + str(self.group_id) + ']'

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

                        if self.l2tp_source_ip is not None:
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

                        if self.tunnel_count is not None:
                            return True

                        if self.virtual_mac_address is not None:
                            return True

                        if self.virtual_mac_address_disable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                        return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-srg-oper:group-ids'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                    return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/Cisco-IOS-XR-subscriber-srg-oper:nodes/Cisco-IOS-XR-subscriber-srg-oper:node[Cisco-IOS-XR-subscriber-srg-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.group_id_xr is not None and self.group_id_xr._has_data():
                    return True

                if self.group_ids is not None and self.group_ids._has_data():
                    return True

                if self.group_summaries is not None and self.group_summaries._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
                return meta._meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent/Cisco-IOS-XR-subscriber-srg-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
            return meta._meta_table['SubscriberRedundancyAgent.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-srg-oper:subscriber-redundancy-agent'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_srg_oper as meta
        return meta._meta_table['SubscriberRedundancyAgent']['meta_info']


