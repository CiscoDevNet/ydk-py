""" Cisco_IOS_XR_lpts_pre_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pifib\: lpts pre\-ifib data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LptsPifibEnum(Enum):
    """
    LptsPifibEnum

    Lpts pifib

    .. data:: isis = 0

    	ISIS packets

    .. data:: ipv4_frag = 1

    	IPv4 fragmented packets

    .. data:: ipv4_echo = 2

    	IPv4 ICMP Echo packets

    .. data:: ipv4_any = 3

    	All IPv4 packets

    .. data:: ipv6_frag = 4

    	IPv6 fragmented packets

    .. data:: ipv6_echo = 5

    	IPv6 ICMP Echo packets

    .. data:: ipv6_nd = 6

    	IPv6 ND packets

    .. data:: ipv6_any = 7

    	All IPv6 packets

    .. data:: bfd_any = 8

    	BFD packets

    .. data:: all = 9

    	All packets

    """

    isis = 0

    ipv4_frag = 1

    ipv4_echo = 2

    ipv4_any = 3

    ipv6_frag = 4

    ipv6_echo = 5

    ipv6_nd = 6

    ipv6_any = 7

    bfd_any = 8

    all = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
        return meta._meta_table['LptsPifibEnum']



class LptsPifib(object):
    """
    lpts pre\-ifib data
    
    .. attribute:: nodes
    
    	List of Pre\-ifib Nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes>`
    
    

    """

    _prefix = 'lpts-pre-ifib-oper'
    _revision = '2016-02-22'

    def __init__(self):
        self.nodes = LptsPifib.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of Pre\-ifib Nodes
        
        .. attribute:: node
        
        	Pre\-ifib data for particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node>`
        
        

        """

        _prefix = 'lpts-pre-ifib-oper'
        _revision = '2016-02-22'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Pre\-ifib data for particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: hardware
            
            	Hardware specific
            	**type**\:   :py:class:`Hardware <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware>`
            
            .. attribute:: type_values
            
            	Type specific
            	**type**\:   :py:class:`TypeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.TypeValues>`
            
            

            """

            _prefix = 'lpts-pre-ifib-oper'
            _revision = '2016-02-22'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.hardware = LptsPifib.Nodes.Node.Hardware()
                self.hardware.parent = self
                self.type_values = LptsPifib.Nodes.Node.TypeValues()
                self.type_values.parent = self


            class TypeValues(object):
                """
                Type specific
                
                .. attribute:: type_value
                
                	pifib types
                	**type**\: list of    :py:class:`TypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.TypeValues.TypeValue>`
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    self.parent = None
                    self.type_value = YList()
                    self.type_value.parent = self
                    self.type_value.name = 'type_value'


                class TypeValue(object):
                    """
                    pifib types
                    
                    .. attribute:: pifib_type  <key>
                    
                    	Type value
                    	**type**\:   :py:class:`LptsPifibEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifibEnum>`
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.pifib_type = None
                        self.entry = YList()
                        self.entry.parent = self
                        self.entry.name = 'entry'


                    class Entry(object):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  <key>
                        
                        	Single Pre\-ifib entry
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: accepts
                        
                        	Packets matched to accept
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: deliver_list_long
                        
                        	Deliver List Long Format
                        	**type**\:  str
                        
                        .. attribute:: deliver_list_short
                        
                        	Deliver List Short Format
                        	**type**\:  str
                        
                        .. attribute:: destination_addr
                        
                        	Destination IP Address
                        	**type**\:  str
                        
                        .. attribute:: destination_type
                        
                        	Destination Key Type
                        	**type**\:  str
                        
                        .. attribute:: destination_value
                        
                        	Destination Port/ICMP Type/IGMP Type
                        	**type**\:  str
                        
                        .. attribute:: drops
                        
                        	Packets matched for drop
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\:  str
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\:  str
                        
                        .. attribute:: local_flag
                        
                        	Local Flag
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: opcode
                        
                        	Opcode
                        	**type**\:  str
                        
                        .. attribute:: pifib_program_time
                        
                        	Creation or Update Time
                        	**type**\:  str
                        
                        .. attribute:: pifib_type
                        
                        	sub Pre\-IFIB type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\:  str
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\:  str
                        
                        .. attribute:: stale
                        
                        	Is Stale
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.entry = None
                            self.accepts = None
                            self.deliver_list_long = None
                            self.deliver_list_short = None
                            self.destination_addr = None
                            self.destination_type = None
                            self.destination_value = None
                            self.drops = None
                            self.flow_type = None
                            self.intf_handle = None
                            self.intf_name = None
                            self.is_fgid = None
                            self.is_frag = None
                            self.is_syn = None
                            self.l3protocol = None
                            self.l4protocol = None
                            self.listener_tag = None
                            self.local_flag = None
                            self.min_ttl = None
                            self.opcode = None
                            self.pifib_program_time = None
                            self.pifib_type = None
                            self.source_addr = None
                            self.source_port = None
                            self.stale = None
                            self.vid = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.entry is None:
                                raise YPYModelError('Key property entry is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-oper:entry[Cisco-IOS-XR-lpts-pre-ifib-oper:entry = ' + str(self.entry) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.entry is not None:
                                return True

                            if self.accepts is not None:
                                return True

                            if self.deliver_list_long is not None:
                                return True

                            if self.deliver_list_short is not None:
                                return True

                            if self.destination_addr is not None:
                                return True

                            if self.destination_type is not None:
                                return True

                            if self.destination_value is not None:
                                return True

                            if self.drops is not None:
                                return True

                            if self.flow_type is not None:
                                return True

                            if self.intf_handle is not None:
                                return True

                            if self.intf_name is not None:
                                return True

                            if self.is_fgid is not None:
                                return True

                            if self.is_frag is not None:
                                return True

                            if self.is_syn is not None:
                                return True

                            if self.l3protocol is not None:
                                return True

                            if self.l4protocol is not None:
                                return True

                            if self.listener_tag is not None:
                                return True

                            if self.local_flag is not None:
                                return True

                            if self.min_ttl is not None:
                                return True

                            if self.opcode is not None:
                                return True

                            if self.pifib_program_time is not None:
                                return True

                            if self.pifib_type is not None:
                                return True

                            if self.source_addr is not None:
                                return True

                            if self.source_port is not None:
                                return True

                            if self.stale is not None:
                                return True

                            if self.vid is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pifib_type is None:
                            raise YPYModelError('Key property pifib_type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-oper:type-value[Cisco-IOS-XR-lpts-pre-ifib-oper:pifib-type = ' + str(self.pifib_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pifib_type is not None:
                            return True

                        if self.entry is not None:
                            for child_ref in self.entry:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.TypeValues.TypeValue']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-oper:type-values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.type_value is not None:
                        for child_ref in self.type_value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib.Nodes.Node.TypeValues']['meta_info']


            class Hardware(object):
                """
                Hardware specific
                
                .. attribute:: bfd
                
                	Bfd details
                	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.Bfd>`
                
                .. attribute:: index_entries
                
                	Hardware Entry options
                	**type**\:   :py:class:`IndexEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.IndexEntries>`
                
                .. attribute:: police
                
                	Police details
                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.Police>`
                
                .. attribute:: static_police
                
                	Static Police details
                	**type**\:   :py:class:`StaticPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.StaticPolice>`
                
                .. attribute:: statistics
                
                	Hardware Entry type
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.Statistics>`
                
                .. attribute:: usage_entries
                
                	Usage Table options
                	**type**\:   :py:class:`UsageEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.UsageEntries>`
                
                

                """

                _prefix = 'platform-pifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    self.parent = None
                    self.bfd = LptsPifib.Nodes.Node.Hardware.Bfd()
                    self.bfd.parent = self
                    self.index_entries = LptsPifib.Nodes.Node.Hardware.IndexEntries()
                    self.index_entries.parent = self
                    self.police = LptsPifib.Nodes.Node.Hardware.Police()
                    self.police.parent = self
                    self.static_police = LptsPifib.Nodes.Node.Hardware.StaticPolice()
                    self.static_police.parent = self
                    self.statistics = LptsPifib.Nodes.Node.Hardware.Statistics()
                    self.statistics.parent = self
                    self.usage_entries = LptsPifib.Nodes.Node.Hardware.UsageEntries()
                    self.usage_entries.parent = self


                class UsageEntries(object):
                    """
                    Usage Table options
                    
                    .. attribute:: usage_entry
                    
                    	Usage details
                    	**type**\: list of    :py:class:`UsageEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.usage_entry = YList()
                        self.usage_entry.parent = self
                        self.usage_entry.name = 'usage_entry'


                    class UsageEntry(object):
                        """
                        Usage details
                        
                        .. attribute:: region_id  <key>
                        
                        	Region ID
                        	**type**\:   :py:class:`UsageAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper.UsageAddressFamilyEnum>`
                        
                        .. attribute:: usage_info
                        
                        	Per TCAM type usage info
                        	**type**\: list of    :py:class:`UsageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo>`
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.region_id = None
                            self.usage_info = YList()
                            self.usage_info.parent = self
                            self.usage_info.name = 'usage_info'


                        class UsageInfo(object):
                            """
                            Per TCAM type usage info
                            
                            .. attribute:: pipe_id
                            
                            	Pipe ID
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region
                            
                            	Region Type
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region_id
                            
                            	Region ID
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: size
                            
                            	Maximum Number of Entries in the Region
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used Number of Entries in the Region
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.pipe_id = None
                                self.region = None
                                self.region_id = None
                                self.size = None
                                self.used = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:usage-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.pipe_id is not None:
                                    return True

                                if self.region is not None:
                                    return True

                                if self.region_id is not None:
                                    return True

                                if self.size is not None:
                                    return True

                                if self.used is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.region_id is None:
                                raise YPYModelError('Key property region_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:usage-entry[Cisco-IOS-XR-platform-pifib-oper:region-id = ' + str(self.region_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.region_id is not None:
                                return True

                            if self.usage_info is not None:
                                for child_ref in self.usage_info:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:usage-entries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.usage_entry is not None:
                            for child_ref in self.usage_entry:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries']['meta_info']


                class Police(object):
                    """
                    Police details
                    
                    .. attribute:: police_info
                    
                    	Per flow type police info
                    	**type**\: list of    :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.police_info = YList()
                        self.police_info.parent = self
                        self.police_info.name = 'police_info'


                    class PoliceInfo(object):
                        """
                        Per flow type police info
                        
                        .. attribute:: accepted_stats
                        
                        	accepted stats
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: acl_config
                        
                        	acl config
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: acl_str
                        
                        	acl str
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: avgrate
                        
                        	avgrate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: avgrate_type
                        
                        	avgrate type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: burst
                        
                        	burst
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dropped_stats
                        
                        	dropped stats
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: iptos_value
                        
                        	iptos value
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policer
                        
                        	policer
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: static_avgrate
                        
                        	static avgrate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.accepted_stats = None
                            self.acl_config = None
                            self.acl_str = None
                            self.avgrate = None
                            self.avgrate_type = None
                            self.burst = None
                            self.change_type = None
                            self.dropped_stats = None
                            self.iptos_value = None
                            self.policer = None
                            self.static_avgrate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:police-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.accepted_stats is not None:
                                return True

                            if self.acl_config is not None:
                                return True

                            if self.acl_str is not None:
                                return True

                            if self.avgrate is not None:
                                return True

                            if self.avgrate_type is not None:
                                return True

                            if self.burst is not None:
                                return True

                            if self.change_type is not None:
                                return True

                            if self.dropped_stats is not None:
                                return True

                            if self.iptos_value is not None:
                                return True

                            if self.policer is not None:
                                return True

                            if self.static_avgrate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:police'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.police_info is not None:
                            for child_ref in self.police_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.Police']['meta_info']


                class StaticPolice(object):
                    """
                    Static Police details
                    
                    .. attribute:: static_info
                    
                    	Per punt reason info
                    	**type**\: list of    :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.static_info = YList()
                        self.static_info.parent = self
                        self.static_info.name = 'static_info'


                    class StaticInfo(object):
                        """
                        Per punt reason info
                        
                        .. attribute:: accepted
                        
                        	accepted
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: burst_rate
                        
                        	burst rate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: dropped
                        
                        	dropped
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_rate
                        
                        	flow rate
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punt_reason
                        
                        	punt reason
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: punt_reason_string
                        
                        	punt reason string
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: sid
                        
                        	sid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.accepted = None
                            self.burst_rate = None
                            self.change_type = None
                            self.dropped = None
                            self.flow_rate = None
                            self.punt_reason = None
                            self.punt_reason_string = None
                            self.sid = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:static-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.accepted is not None:
                                return True

                            if self.burst_rate is not None:
                                return True

                            if self.change_type is not None:
                                return True

                            if self.dropped is not None:
                                return True

                            if self.flow_rate is not None:
                                return True

                            if self.punt_reason is not None:
                                return True

                            if self.punt_reason_string is not None:
                                return True

                            if self.sid is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:static-police'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.static_info is not None:
                            for child_ref in self.static_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.StaticPolice']['meta_info']


                class Bfd(object):
                    """
                    Bfd details
                    
                    .. attribute:: bfd_entry_info
                    
                    	Per bfd disc entry info
                    	**type**\: list of    :py:class:`BfdEntryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.bfd_entry_info = YList()
                        self.bfd_entry_info.parent = self
                        self.bfd_entry_info.name = 'bfd_entry_info'


                    class BfdEntryInfo(object):
                        """
                        Per bfd disc entry info
                        
                        .. attribute:: fgid_or_vqi
                        
                        	fgid or vqi
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: index
                        
                        	index
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_mcast
                        
                        	is mcast
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_valid
                        
                        	is valid
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policer_id
                        
                        	policer id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.fgid_or_vqi = None
                            self.index = None
                            self.is_mcast = None
                            self.is_valid = None
                            self.policer_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:bfd-entry-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.fgid_or_vqi is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.is_mcast is not None:
                                return True

                            if self.is_valid is not None:
                                return True

                            if self.policer_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:bfd'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bfd_entry_info is not None:
                            for child_ref in self.bfd_entry_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.Bfd']['meta_info']


                class Statistics(object):
                    """
                    Hardware Entry type
                    
                    .. attribute:: accepted
                    
                    	Deleted\-entry accepted packets counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_ts
                    
                    	Statistics clear timestamp
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dropped
                    
                    	Deleted\-entry dropped packets counter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: no_stats_mem_err
                    
                    	No statistics memory error
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.accepted = None
                        self.clear_ts = None
                        self.dropped = None
                        self.no_stats_mem_err = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accepted is not None:
                            return True

                        if self.clear_ts is not None:
                            return True

                        if self.dropped is not None:
                            return True

                        if self.no_stats_mem_err is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.Statistics']['meta_info']


                class IndexEntries(object):
                    """
                    Hardware Entry options
                    
                    .. attribute:: index_entry
                    
                    	Entry options
                    	**type**\: list of    :py:class:`IndexEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        self.parent = None
                        self.index_entry = YList()
                        self.index_entry.parent = self
                        self.index_entry.name = 'index_entry'


                    class IndexEntry(object):
                        """
                        Entry options
                        
                        .. attribute:: index  <key>
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: acl_str
                        
                        	Acl name
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: action
                        
                        	Action
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: action_string
                        
                        	Action String
                        	**type**\:  str
                        
                        .. attribute:: cir
                        
                        	Committed Information Rate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: entry_ptr
                        
                        	ptr to ifib\_entry\_st
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: entry_shadow_ptr
                        
                        	ptr to ifib\_entry\_shadow\_st
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fgid_or_sfp
                        
                        	fabric group id or swith fabric port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hw_info
                        
                        	Per pipe type hardware info
                        	**type**\: list of    :py:class:`HwInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo>`
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_optimized
                        
                        	Is optimized or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_uidb_opt_bit
                        
                        	Is uidb set for optimized entry or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_vrf
                        
                        	Is VRF or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: list_node_ptr
                        
                        	ptr to dlqueue list node
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: local_addr
                        
                        	Local IP Address
                        	**type**\:  str
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_prefix_len
                        
                        	Local Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lookup_priority
                        
                        	Lookup priority
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: no_stats
                        
                        	Stats not available
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: num_retries
                        
                        	retries count
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: num_tm_entries
                        
                        	Number of TCAM entries used
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: policer_avgrate
                        
                        	Policer avg. rate limit
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policer_burst
                        
                        	Policer burst
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: priority
                        
                        	Flow priority or COS
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rack_id
                        
                        	Remote racknum if remote
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote IP Address
                        	**type**\:  str
                        
                        .. attribute:: remote_fgid
                        
                        	Remote FGID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_prefix_len
                        
                        	Remote Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_rack
                        
                        	Is entry remote or not
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: retry_fail_cause
                        
                        	failure cause
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rslot
                        
                        	Remote slotnum if remote
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid
                        
                        	Stream ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	state of pifib entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: storage_priority
                        
                        	Storage priority
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: u_len
                        
                        	Union Key Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: u_type
                        
                        	Union Key Type
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: u_value
                        
                        	Remote Port/ICMP Type/IGMP Type
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: uidb_index
                        
                        	Interface uidb index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.acl_str = None
                            self.action = None
                            self.action_string = None
                            self.cir = None
                            self.entry_ptr = None
                            self.entry_shadow_ptr = None
                            self.fgid_or_sfp = None
                            self.flow_type = None
                            self.hw_info = YList()
                            self.hw_info.parent = self
                            self.hw_info.name = 'hw_info'
                            self.intf_handle = None
                            self.intf_name = None
                            self.is_fgid = None
                            self.is_frag = None
                            self.is_optimized = None
                            self.is_syn = None
                            self.is_uidb_opt_bit = None
                            self.is_vrf = None
                            self.l3protocol = None
                            self.l4protocol = None
                            self.list_node_ptr = None
                            self.listener_tag = None
                            self.local_addr = None
                            self.local_port = None
                            self.local_prefix_len = None
                            self.lookup_priority = None
                            self.min_ttl = None
                            self.no_stats = None
                            self.num_retries = None
                            self.num_tm_entries = None
                            self.policer_avgrate = None
                            self.policer_burst = None
                            self.priority = None
                            self.rack_id = None
                            self.remote_addr = None
                            self.remote_fgid = None
                            self.remote_prefix_len = None
                            self.remote_rack = None
                            self.retry_fail_cause = None
                            self.rslot = None
                            self.sid = None
                            self.state = None
                            self.storage_priority = None
                            self.u_len = None
                            self.u_type = None
                            self.u_value = None
                            self.uidb_index = None
                            self.vrf_id = None


                        class HwInfo(object):
                            """
                            Per pipe type hardware info
                            
                            .. attribute:: accepted
                            
                            	Accepted Packets Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped
                            
                            	Dropped Packets Counter
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policer
                            
                            	Policer Pointer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sort_start_offset
                            
                            	Relative position in sorting order
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: stats_ptr
                            
                            	Stats Pointer
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tm_start_offset
                            
                            	Relative position in TCAM
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                self.parent = None
                                self.accepted = None
                                self.dropped = None
                                self.policer = None
                                self.sort_start_offset = None
                                self.stats_ptr = None
                                self.tm_start_offset = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:hw-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.accepted is not None:
                                    return True

                                if self.dropped is not None:
                                    return True

                                if self.policer is not None:
                                    return True

                                if self.sort_start_offset is not None:
                                    return True

                                if self.stats_ptr is not None:
                                    return True

                                if self.tm_start_offset is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                                return meta._meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:index-entry[Cisco-IOS-XR-platform-pifib-oper:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.acl_str is not None:
                                return True

                            if self.action is not None:
                                return True

                            if self.action_string is not None:
                                return True

                            if self.cir is not None:
                                return True

                            if self.entry_ptr is not None:
                                return True

                            if self.entry_shadow_ptr is not None:
                                return True

                            if self.fgid_or_sfp is not None:
                                return True

                            if self.flow_type is not None:
                                return True

                            if self.hw_info is not None:
                                for child_ref in self.hw_info:
                                    if child_ref._has_data():
                                        return True

                            if self.intf_handle is not None:
                                return True

                            if self.intf_name is not None:
                                return True

                            if self.is_fgid is not None:
                                return True

                            if self.is_frag is not None:
                                return True

                            if self.is_optimized is not None:
                                return True

                            if self.is_syn is not None:
                                return True

                            if self.is_uidb_opt_bit is not None:
                                return True

                            if self.is_vrf is not None:
                                return True

                            if self.l3protocol is not None:
                                return True

                            if self.l4protocol is not None:
                                return True

                            if self.list_node_ptr is not None:
                                return True

                            if self.listener_tag is not None:
                                return True

                            if self.local_addr is not None:
                                return True

                            if self.local_port is not None:
                                return True

                            if self.local_prefix_len is not None:
                                return True

                            if self.lookup_priority is not None:
                                return True

                            if self.min_ttl is not None:
                                return True

                            if self.no_stats is not None:
                                return True

                            if self.num_retries is not None:
                                return True

                            if self.num_tm_entries is not None:
                                return True

                            if self.policer_avgrate is not None:
                                return True

                            if self.policer_burst is not None:
                                return True

                            if self.priority is not None:
                                return True

                            if self.rack_id is not None:
                                return True

                            if self.remote_addr is not None:
                                return True

                            if self.remote_fgid is not None:
                                return True

                            if self.remote_prefix_len is not None:
                                return True

                            if self.remote_rack is not None:
                                return True

                            if self.retry_fail_cause is not None:
                                return True

                            if self.rslot is not None:
                                return True

                            if self.sid is not None:
                                return True

                            if self.state is not None:
                                return True

                            if self.storage_priority is not None:
                                return True

                            if self.u_len is not None:
                                return True

                            if self.u_type is not None:
                                return True

                            if self.u_value is not None:
                                return True

                            if self.uidb_index is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                            return meta._meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:index-entries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.index_entry is not None:
                            for child_ref in self.index_entry:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                        return meta._meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-platform-pifib-oper:hardware'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd is not None and self.bfd._has_data():
                        return True

                    if self.index_entries is not None and self.index_entries._has_data():
                        return True

                    if self.police is not None and self.police._has_data():
                        return True

                    if self.static_police is not None and self.static_police._has_data():
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    if self.usage_entries is not None and self.usage_entries._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                    return meta._meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/Cisco-IOS-XR-lpts-pre-ifib-oper:nodes/Cisco-IOS-XR-lpts-pre-ifib-oper:node[Cisco-IOS-XR-lpts-pre-ifib-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.hardware is not None and self.hardware._has_data():
                    return True

                if self.type_values is not None and self.type_values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
                return meta._meta_table['LptsPifib.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/Cisco-IOS-XR-lpts-pre-ifib-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
            return meta._meta_table['LptsPifib.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_oper as meta
        return meta._meta_table['LptsPifib']['meta_info']


