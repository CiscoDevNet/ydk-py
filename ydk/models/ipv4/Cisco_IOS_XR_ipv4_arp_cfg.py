""" Cisco_IOS_XR_ipv4_arp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-arp package configuration.

This module contains definitions
for the following management objects\:
  arp\: ARP configuraiton
  arpgmp\: arpgmp
  arp\-redundancy\: arp redundancy

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ArpEncapEnum(Enum):
    """
    ArpEncapEnum

    Arp encap

    .. data:: ARPA = 1

    	Encapsulation type ARPA

    .. data:: SRP = 4

    	Encapsulation type SRP

    .. data:: SRPA = 5

    	Encapsulation type SRPA

    .. data:: SRPB = 6

    	Encapsulation type SRPB

    """

    ARPA = 1

    SRP = 4

    SRPA = 5

    SRPB = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
        return meta._meta_table['ArpEncapEnum']


class ArpEntryEnum(Enum):
    """
    ArpEntryEnum

    Arp entry

    .. data:: STATIC = 0

    	Static ARP entry type

    .. data:: ALIAS = 1

    	Alias ARP entry type

    """

    STATIC = 0

    ALIAS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
        return meta._meta_table['ArpEntryEnum']



class Arp(object):
    """
    ARP configuraiton
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for arp packets
    	**type**\: int
    
    	**range:** 0..7
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for arp packets
    	**type**\: int
    
    	**range:** 0..7
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.inner_cos = None
        self.outer_cos = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-arp-cfg:arp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.inner_cos is not None:
            return True

        if self.outer_cos is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
        return meta._meta_table['Arp']['meta_info']


class Arpgmp(object):
    """
    arpgmp
    
    .. attribute:: vrf
    
    	Per VRF configuration, for the default VRF use 'default'
    	**type**\: list of :py:class:`Vrf <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf>`
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.vrf = YList()
        self.vrf.parent = self
        self.vrf.name = 'vrf'


    class Vrf(object):
        """
        Per VRF configuration, for the default VRF use
        'default'
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: entries
        
        	ARP static and alias entry configuration
        	**type**\: :py:class:`Entries <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries>`
        
        

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf_name = None
            self.entries = Arpgmp.Vrf.Entries()
            self.entries.parent = self


        class Entries(object):
            """
            ARP static and alias entry configuration
            
            .. attribute:: entry
            
            	ARP static and alias entry configuration item
            	**type**\: list of :py:class:`Entry <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries.Entry>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.entry = YList()
                self.entry.parent = self
                self.entry.name = 'entry'


            class Entry(object):
                """
                ARP static and alias entry configuration item
                
                .. attribute:: address  <key>
                
                	IP Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: encapsulation
                
                	Encapsulation type
                	**type**\: :py:class:`ArpEncapEnum <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpEncapEnum>`
                
                .. attribute:: entry_type
                
                	Entry type
                	**type**\: :py:class:`ArpEntryEnum <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpEntryEnum>`
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.mac_address = None
                    self.encapsulation = None
                    self.entry_type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.address is None:
                        raise YPYDataValidationError('Key property address is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:entry[Cisco-IOS-XR-ipv4-arp-cfg:address = ' + str(self.address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.encapsulation is not None:
                        return True

                    if self.entry_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                    return meta._meta_table['Arpgmp.Vrf.Entries.Entry']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:entries'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.entry is not None:
                    for child_ref in self.entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                return meta._meta_table['Arpgmp.Vrf.Entries']['meta_info']

        @property
        def _common_path(self):
            if self.vrf_name is None:
                raise YPYDataValidationError('Key property vrf_name is None')

            return '/Cisco-IOS-XR-ipv4-arp-cfg:arpgmp/Cisco-IOS-XR-ipv4-arp-cfg:vrf[Cisco-IOS-XR-ipv4-arp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vrf_name is not None:
                return True

            if self.entries is not None and self.entries._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
            return meta._meta_table['Arpgmp.Vrf']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-arp-cfg:arpgmp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.vrf is not None:
            for child_ref in self.vrf:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
        return meta._meta_table['Arpgmp']['meta_info']


class ArpRedundancy(object):
    """
    arp redundancy
    
    .. attribute:: redundancy
    
    	Configure parameter for ARP Geo redundancy
    	**type**\: :py:class:`Redundancy <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy>`
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.redundancy = None


    class Redundancy(object):
        """
        Configure parameter for ARP Geo redundancy
        
        .. attribute:: groups
        
        	Table of Group
        	**type**\: :py:class:`Groups <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        .. attribute:: enable
        
        	Enable Configure parameter for ARP Geo redundancy. Deletion of this object also causes deletion of all associated objects under ArpRedundancy
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.groups = ArpRedundancy.Redundancy.Groups()
            self.groups.parent = self
            self.enable = None


        class Groups(object):
            """
            Table of Group
            
            .. attribute:: group
            
            	None
            	**type**\: list of :py:class:`Group <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
                """
                None
                
                .. attribute:: group_id  <key>
                
                	Group ID
                	**type**\: int
                
                	**range:** 1..32
                
                .. attribute:: peers
                
                	Table of Peer
                	**type**\: :py:class:`Peers <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers>`
                
                .. attribute:: interface_list
                
                	List of Interfaces for this Group
                	**type**\: :py:class:`InterfaceList <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList>`
                
                .. attribute:: source_interface
                
                	Interface name
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_id = None
                    self.peers = ArpRedundancy.Redundancy.Groups.Group.Peers()
                    self.peers.parent = self
                    self.interface_list = None
                    self.source_interface = None


                class Peers(object):
                    """
                    Table of Peer
                    
                    .. attribute:: peer
                    
                    	None
                    	**type**\: list of :py:class:`Peer <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers.Peer>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.peer = YList()
                        self.peer.parent = self
                        self.peer.name = 'peer'


                    class Peer(object):
                        """
                        None
                        
                        .. attribute:: prefix_string  <key>
                        
                        	Neighbor IPv4 address
                        	**type**\: one of the below types:
                        
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefix_string = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.prefix_string is None:
                                raise YPYDataValidationError('Key property prefix_string is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:peer[Cisco-IOS-XR-ipv4-arp-cfg:prefix-string = ' + str(self.prefix_string) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_string is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                            return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers.Peer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:peers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.peer is not None:
                            for child_ref in self.peer:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                        return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers']['meta_info']


                class InterfaceList(object):
                    """
                    List of Interfaces for this Group
                    
                    .. attribute:: interfaces
                    
                    	Table of Interface
                    	**type**\: :py:class:`Interfaces <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: enable
                    
                    	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interfaces = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces()
                        self.interfaces.parent = self
                        self.enable = None


                    class Interfaces(object):
                        """
                        Table of Interface
                        
                        .. attribute:: interface
                        
                        	Interface for this Group
                        	**type**\: list of :py:class:`Interface <ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface = YList()
                            self.interface.parent = self
                            self.interface.name = 'interface'


                        class Interface(object):
                            """
                            Interface for this Group
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: interface_id
                            
                            	Interface Id for the interface
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'ipv4-arp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.interface_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYDataValidationError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:interface[Cisco-IOS-XR-ipv4-arp-cfg:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.interface_name is not None:
                                    return True

                                if self.interface_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                                return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface is not None:
                                for child_ref in self.interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                            return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-arp-cfg:interface-list'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                        return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList']['meta_info']

                @property
                def _common_path(self):
                    if self.group_id is None:
                        raise YPYDataValidationError('Key property group_id is None')

                    return '/Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/Cisco-IOS-XR-ipv4-arp-cfg:redundancy/Cisco-IOS-XR-ipv4-arp-cfg:groups/Cisco-IOS-XR-ipv4-arp-cfg:group[Cisco-IOS-XR-ipv4-arp-cfg:group-id = ' + str(self.group_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.group_id is not None:
                        return True

                    if self.peers is not None and self.peers._has_data():
                        return True

                    if self.interface_list is not None and self.interface_list._has_data():
                        return True

                    if self.source_interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                    return meta._meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/Cisco-IOS-XR-ipv4-arp-cfg:redundancy/Cisco-IOS-XR-ipv4-arp-cfg:groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
                return meta._meta_table['ArpRedundancy.Redundancy.Groups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/Cisco-IOS-XR-ipv4-arp-cfg:redundancy'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.groups is not None and self.groups._has_data():
                return True

            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
            return meta._meta_table['ArpRedundancy.Redundancy']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.redundancy is not None and self.redundancy._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_arp_cfg as meta
        return meta._meta_table['ArpRedundancy']['meta_info']


