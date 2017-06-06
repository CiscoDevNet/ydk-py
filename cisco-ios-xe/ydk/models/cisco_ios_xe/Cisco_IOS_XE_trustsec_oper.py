""" Cisco_IOS_XE_trustsec_oper 

This module contains a collection of YANG definitions for monitoring
Cisco Trustsec operational information on Role based permissions,
IP\-SGT bindings and SXP connections.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CtsOdmBindingSourceEnum(Enum):
    """
    CtsOdmBindingSourceEnum

    Binding Source enumeration

    .. data:: default = 0

    	Default Security Group Tag binding value in this device

    	for the given IP-Address.

    .. data:: from_vlan = 1

    	Security Group Tag binding value in this device for the given

    	IP-Address is learned from a VLAN.

    .. data:: from_cli = 2

    	Security Group Tag binding value in this device

    	for the given

    	IP-Address is configure from CLI (Command Line

    	Inteface).

    .. data:: from_l3if = 3

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned from a

    	L3 (Layer 3) interface

    .. data:: from_cfp = 4

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned via SXP

    	binding exchange protocol.

    .. data:: from_ip_arp = 5

    	Security Group Tag binding value in this

    	device for the given

    	IP-Address is learned via IP-ARP protocol.

    .. data:: from_local = 6

    	Security Group Tag binding value in this device

    	for the given 

    	IP-Address is learned locally.

    .. data:: from_sgt_caching = 7

    	Security Group Tag binding value in this device

    	for the given

    	IP-Address is learned via Security Group Tag

    	caching from datapath.

    .. data:: from_cli_hi = 8

    	Security Group Tag binding value in this device

    	for the given 

    	IP-Address is configured from CLI-high priority.

    """

    default = 0

    from_vlan = 1

    from_cli = 2

    from_l3if = 3

    from_cfp = 4

    from_ip_arp = 5

    from_local = 6

    from_sgt_caching = 7

    from_cli_hi = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
        return meta._meta_table['CtsOdmBindingSourceEnum']


class SxpConModeEnum(Enum):
    """
    SxpConModeEnum

    SXP Connection mode

    .. data:: con_mode_invalid = 0

    	SXP Connection mode is Invalid

    .. data:: con_mode_speaker = 1

    	SXP Connection mode is Speaker

    .. data:: con_mode_listener = 2

    	SXP Connection mode is Listener

    .. data:: con_mode_both = 3

    	SXP Connection mode is Both (Speaker and Listener)

    """

    con_mode_invalid = 0

    con_mode_speaker = 1

    con_mode_listener = 2

    con_mode_both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
        return meta._meta_table['SxpConModeEnum']


class SxpConStateEnum(Enum):
    """
    SxpConStateEnum

    SXP Connection state

    .. data:: state_off = 0

    	SXP Connection state is OFF

    .. data:: state_pending_on = 1

    	SXP Connection state is Pending-On

    .. data:: state_on = 2

    	SXP Connection state is ON

    .. data:: state_delete_hold_down = 3

    	SXP Connection state is Delete-Hold-Down

    .. data:: state_not_applicable = 4

    	SXP Connection state is Not-Applicable

    """

    state_off = 0

    state_pending_on = 1

    state_on = 2

    state_delete_hold_down = 3

    state_not_applicable = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
        return meta._meta_table['SxpConStateEnum']



class TrustsecState(object):
    """
    This is top level container for Cisco Trusted Security
    solution operational data.
    It can have Security Group Tag binding information for
    the given IP\-Address, Role based permissions between a
    Source Security Group Tag and a Destination Security
    Group, SXP Connection information for a given peer
    IP\-Address in this device.
    
    .. attribute:: cts_rolebased_policies
    
    	Role based permissions between a Source Security Group and a Destination Security Group are configured by the administrator in the Identity Services Engine or in the Device
    	**type**\:   :py:class:`CtsRolebasedPolicies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies>`
    
    .. attribute:: cts_rolebased_sgtmaps
    
    	Security Group Tag value corresponding to an IP\-Address  in the given VRF instance in this device
    	**type**\:   :py:class:`CtsRolebasedSgtmaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps>`
    
    .. attribute:: cts_sxp_connections
    
    	Trustsec SXP connection is used between Cisco devices to propagate Security Group Tags from one device to  another device. One of the device will be in Speaker  mode or Listener mode or both the devices can be in both the connection modes
    	**type**\:   :py:class:`CtsSxpConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections>`
    
    

    """

    _prefix = 'trustsec-ios-xe-oper'
    _revision = '2017-02-27'

    def __init__(self):
        self.cts_rolebased_policies = TrustsecState.CtsRolebasedPolicies()
        self.cts_rolebased_policies.parent = self
        self.cts_rolebased_sgtmaps = TrustsecState.CtsRolebasedSgtmaps()
        self.cts_rolebased_sgtmaps.parent = self
        self.cts_sxp_connections = TrustsecState.CtsSxpConnections()
        self.cts_sxp_connections.parent = self


    class CtsRolebasedSgtmaps(object):
        """
        Security Group Tag value corresponding to an IP\-Address 
        in the given VRF instance in this device.
        
        .. attribute:: cts_rolebased_sgtmap
        
        	Security Group Tag is assigned for an IP\-Address based on the user permissions and authorization  level as configured by the network administrator in Identity Service Engine server or in the device locally
        	**type**\: list of    :py:class:`CtsRolebasedSgtmap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-27'

        def __init__(self):
            self.parent = None
            self.cts_rolebased_sgtmap = YList()
            self.cts_rolebased_sgtmap.parent = self
            self.cts_rolebased_sgtmap.name = 'cts_rolebased_sgtmap'


        class CtsRolebasedSgtmap(object):
            """
            Security Group Tag is assigned for an IP\-Address
            based on the user permissions and authorization 
            level as configured by the network administrator
            in Identity Service Engine server or in the
            device locally
            
            .. attribute:: ip  <key>
            
            	IP\-Prefix information to find its corresponding Secure Group Tag. Only IPv4 prefix information is  supported currently to get the Security Group Tag binding in this device
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	VRF\-Name to find the Security Group Tag for the  corresponding IP\-Address in this VRF instance. Only default VRF is supported  currently which is indicated by (empty string)
            	**type**\:  str
            
            .. attribute:: sgt
            
            	Security Group Tag value corresponding to the given IP\-Address
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: source
            
            	Source information via which the Security  Group Tag binding was learned in this device
            	**type**\:   :py:class:`CtsOdmBindingSourceEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.CtsOdmBindingSourceEnum>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-27'

            def __init__(self):
                self.parent = None
                self.ip = None
                self.vrf_name = None
                self.sgt = None
                self.source = None

            @property
            def _common_path(self):
                if self.ip is None:
                    raise YPYModelError('Key property ip is None')
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-rolebased-sgtmaps/Cisco-IOS-XE-trustsec-oper:cts-rolebased-sgtmap[Cisco-IOS-XE-trustsec-oper:ip = ' + str(self.ip) + '][Cisco-IOS-XE-trustsec-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ip is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.sgt is not None:
                    return True

                if self.source is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
                return meta._meta_table['TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-rolebased-sgtmaps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cts_rolebased_sgtmap is not None:
                for child_ref in self.cts_rolebased_sgtmap:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
            return meta._meta_table['TrustsecState.CtsRolebasedSgtmaps']['meta_info']


    class CtsRolebasedPolicies(object):
        """
        Role based permissions between a Source Security Group
        and a Destination Security Group are configured by the
        administrator in the Identity Services Engine or in the
        Device
        
        .. attribute:: cts_rolebased_policy
        
        	Role based permissions between a Source Security Group and a Destination Security Group can be retrieved from the device using a Security Group Tag and Destination Group Tag value
        	**type**\: list of    :py:class:`CtsRolebasedPolicy <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-27'

        def __init__(self):
            self.parent = None
            self.cts_rolebased_policy = YList()
            self.cts_rolebased_policy.parent = self
            self.cts_rolebased_policy.name = 'cts_rolebased_policy'


        class CtsRolebasedPolicy(object):
            """
            Role based permissions between a Source Security Group
            and a Destination Security Group can be retrieved from
            the device using a Security Group Tag and Destination
            Group Tag value.
            
            .. attribute:: src_sgt  <key>
            
            	Source Security Group Tag number. This value must be in the  inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dst_sgt  <key>
            
            	Destination Security Tag number. This value must be in the  inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hardware_deny_count
            
            	Number of packets that have been denied in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_monitor_count
            
            	Number of packets that have been monitored in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_permit_count
            
            	Number of packets that have been permitted in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_updated_time
            
            	Indicates the time when the Role based permissions  between a Source Security Group and a Destination  Security Group was modified or updated last. The  value will be represented as date and time   corresponding to the local time zone of the  Identify Services Engine when the Role based   permissions was modified or updated  last
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: monitor_mode
            
            	Indicates the monitor mode status between the Source Security Group and Destination Security Group is currently enabled or disabled. This will be TRUE if monitor mode is enabled and FALSE if it is disabled
            	**type**\:  bool
            
            .. attribute:: num_of_sgacl
            
            	Number of Security Group Access Control Lists that are currently applied between the Source Security Group and the Destination Security Group. This should match the number of Security Group Access Control List names in sgacl\-name
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: policy_life_time
            
            	Duration of the Role based permissions that are applied    between a Source Security Group and a Destination Security Group. The duration is represented in seconds
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: sgacl_name
            
            	List of Security Group Access Control List names separated by semi\-colon(;)
            	**type**\:  str
            
            .. attribute:: software_deny_count
            
            	Number of packets that have been denied in the  software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_monitor_count
            
            	Number of packets that have been monitored in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_permit_count
            
            	Number of packets that have been permitted in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_deny_count
            
            	Total number of packets that have been denied by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets denied in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_permit_count
            
            	Total number of packets that have been permitted by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets allowed in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-27'

            def __init__(self):
                self.parent = None
                self.src_sgt = None
                self.dst_sgt = None
                self.hardware_deny_count = None
                self.hardware_monitor_count = None
                self.hardware_permit_count = None
                self.last_updated_time = None
                self.monitor_mode = None
                self.num_of_sgacl = None
                self.policy_life_time = None
                self.sgacl_name = None
                self.software_deny_count = None
                self.software_monitor_count = None
                self.software_permit_count = None
                self.total_deny_count = None
                self.total_permit_count = None

            @property
            def _common_path(self):
                if self.src_sgt is None:
                    raise YPYModelError('Key property src_sgt is None')
                if self.dst_sgt is None:
                    raise YPYModelError('Key property dst_sgt is None')

                return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-rolebased-policies/Cisco-IOS-XE-trustsec-oper:cts-rolebased-policy[Cisco-IOS-XE-trustsec-oper:src-sgt = ' + str(self.src_sgt) + '][Cisco-IOS-XE-trustsec-oper:dst-sgt = ' + str(self.dst_sgt) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.src_sgt is not None:
                    return True

                if self.dst_sgt is not None:
                    return True

                if self.hardware_deny_count is not None:
                    return True

                if self.hardware_monitor_count is not None:
                    return True

                if self.hardware_permit_count is not None:
                    return True

                if self.last_updated_time is not None:
                    return True

                if self.monitor_mode is not None:
                    return True

                if self.num_of_sgacl is not None:
                    return True

                if self.policy_life_time is not None:
                    return True

                if self.sgacl_name is not None:
                    return True

                if self.software_deny_count is not None:
                    return True

                if self.software_monitor_count is not None:
                    return True

                if self.software_permit_count is not None:
                    return True

                if self.total_deny_count is not None:
                    return True

                if self.total_permit_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
                return meta._meta_table['TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-rolebased-policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cts_rolebased_policy is not None:
                for child_ref in self.cts_rolebased_policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
            return meta._meta_table['TrustsecState.CtsRolebasedPolicies']['meta_info']


    class CtsSxpConnections(object):
        """
        Trustsec SXP connection is used between Cisco devices
        to propagate Security Group Tags from one device to 
        another device. One of the device will be in Speaker 
        mode or Listener mode or both the devices can be in
        both the connection modes.
        
        .. attribute:: cts_sxp_connection
        
        	Trustsec SXP connection information from a device can be retrieved with the SXP connection peer IP address. Only IPv4 address as Peer IP and default VRF instance in device is supported currently
        	**type**\: list of    :py:class:`CtsSxpConnection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections.CtsSxpConnection>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-27'

        def __init__(self):
            self.parent = None
            self.cts_sxp_connection = YList()
            self.cts_sxp_connection.parent = self
            self.cts_sxp_connection.name = 'cts_sxp_connection'


        class CtsSxpConnection(object):
            """
            Trustsec SXP connection information from a device
            can be retrieved with the SXP connection peer IP
            address. Only IPv4 address as Peer IP and default
            VRF instance in device is supported currently
            
            .. attribute:: peer_ip  <key>
            
            	IP\-Address information of the peer of an SXP connection in this device. Only IPv4 address is currently supported
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	vrf\-name string of the VRF instance in this device, to which the peer of an SXP connection Belongs to. Only default VRF is supported currently which is indicated by empty string
            	**type**\:  str
            
            .. attribute:: listener_duration
            
            	Duration of the SXP listener of the SXP connection in this device. This information is valid Only if the local mode of the SXP connection is Listener
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: listener_state
            
            	SXP listener state information of the SXP  connection in this device. This information is valid only if the local mode of the SXP connection in the device is Listener
            	**type**\:   :py:class:`SxpConStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConStateEnum>`
            
            .. attribute:: local_mode
            
            	SXP connection mode of this device for the SXP connection with the given peer
            	**type**\:   :py:class:`SxpConModeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConModeEnum>`
            
            .. attribute:: source_ip
            
            	Source IP\-Address of the SXP connection in this device for the given peer IP\-Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: speaker_duration
            
            	Duration of the SXP speaker of the SXP connection in this device. This information is valid only if the local mode of the SXP connection is Speaker
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: speaker_state
            
            	SXP speaker state information of the SXP connection in this device. This information is valid only if the local mode of the SXP connection in this device is Speaker
            	**type**\:   :py:class:`SxpConStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConStateEnum>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-27'

            def __init__(self):
                self.parent = None
                self.peer_ip = None
                self.vrf_name = None
                self.listener_duration = None
                self.listener_state = None
                self.local_mode = None
                self.source_ip = None
                self.speaker_duration = None
                self.speaker_state = None

            @property
            def _common_path(self):
                if self.peer_ip is None:
                    raise YPYModelError('Key property peer_ip is None')
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-sxp-connections/Cisco-IOS-XE-trustsec-oper:cts-sxp-connection[Cisco-IOS-XE-trustsec-oper:peer-ip = ' + str(self.peer_ip) + '][Cisco-IOS-XE-trustsec-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.peer_ip is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.listener_duration is not None:
                    return True

                if self.listener_state is not None:
                    return True

                if self.local_mode is not None:
                    return True

                if self.source_ip is not None:
                    return True

                if self.speaker_duration is not None:
                    return True

                if self.speaker_state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
                return meta._meta_table['TrustsecState.CtsSxpConnections.CtsSxpConnection']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-trustsec-oper:trustsec-state/Cisco-IOS-XE-trustsec-oper:cts-sxp-connections'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cts_sxp_connection is not None:
                for child_ref in self.cts_sxp_connection:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
            return meta._meta_table['TrustsecState.CtsSxpConnections']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-trustsec-oper:trustsec-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cts_rolebased_policies is not None and self.cts_rolebased_policies._has_data():
            return True

        if self.cts_rolebased_sgtmaps is not None and self.cts_rolebased_sgtmaps._has_data():
            return True

        if self.cts_sxp_connections is not None and self.cts_sxp_connections._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_trustsec_oper as meta
        return meta._meta_table['TrustsecState']['meta_info']


