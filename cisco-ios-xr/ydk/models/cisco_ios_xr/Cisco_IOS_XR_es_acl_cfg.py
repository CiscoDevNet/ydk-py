""" Cisco_IOS_XR_es_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package configuration.

This module contains definitions
for the following management objects\:
  es\-acl\: Layer 2 ACL configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EsAclGrantEnumEnum(Enum):
    """
    EsAclGrantEnumEnum

    ES acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = 0

    permit = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
        return meta._meta_table['EsAclGrantEnumEnum']



class EsAcl(object):
    """
    Layer 2 ACL configuration data
    
    .. attribute:: accesses
    
    	Table of access lists
    	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses>`
    
    

    """

    _prefix = 'es-acl-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.accesses = EsAcl.Accesses()
        self.accesses.parent = self


    class Accesses(object):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access>`
        
        

        """

        _prefix = 'es-acl-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.access = YList()
            self.access.parent = self
            self.access.name = 'access'


        class Access(object):
            """
            An ACL
            
            .. attribute:: name  <key>
            
            	Name of the access list
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of access list entries
            	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'es-acl-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.access_list_entries = EsAcl.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self


            class AccessListEntries(object):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'es-acl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_list_entry = YList()
                    self.access_list_entry.parent = self
                    self.access_list_entry.name = 'access_list_entry'


                class AccessListEntry(object):
                    """
                    An ACL entry; either a description (remark)
                    or anAccess List Entry to match against
                    
                    .. attribute:: sequence_number  <key>
                    
                    	Sequence number of access list entry
                    	**type**\:  int
                    
                    	**range:** 1..2147483646
                    
                    .. attribute:: capture
                    
                    	Enable capture
                    	**type**\:  bool
                    
                    .. attribute:: cos
                    
                    	COS value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: dei
                    
                    	DEI bit
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:   :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: ether_type_number
                    
                    	Ethernet type Number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the ACE
                    	**type**\:   :py:class:`EsAclGrantEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAclGrantEnumEnum>`
                    
                    .. attribute:: inner_cos
                    
                    	Inner COS value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: inner_dei
                    
                    	Inner DEI bit
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: inner_vlan1
                    
                    	Inner VLAN ID/range lower limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: inner_vlan2
                    
                    	Inner VLAN ID range higher limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: log_option
                    
                    	Whether and how to log matches against this entry
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the access list
                    	**type**\:  str
                    
                    .. attribute:: sequence_str
                    
                    	Sequence String for the ace
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:   :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: vlan1
                    
                    	VLAN ID/range lower limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vlan2
                    
                    	VLAN ID range higher limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'es-acl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sequence_number = None
                        self.capture = None
                        self.cos = None
                        self.dei = None
                        self.destination_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self.ether_type_number = None
                        self.grant = None
                        self.inner_cos = None
                        self.inner_dei = None
                        self.inner_vlan1 = None
                        self.inner_vlan2 = None
                        self.log_option = None
                        self.remark = None
                        self.sequence_str = None
                        self.source_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self.vlan1 = None
                        self.vlan2 = None


                    class SourceNetwork(object):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source address to match, leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source address (if specified), leave unspecified for no wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.source_address = None
                            self.source_wild_card_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-es-acl-cfg:source-network'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source_address is not None:
                                return True

                            if self.source_wild_card_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
                            return meta._meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info']


                    class DestinationNetwork(object):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination address to match (if a protocol was specified), leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination address (if specified), leave unspecified for no wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.destination_address = None
                            self.destination_wild_card_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-es-acl-cfg:destination-network'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.destination_address is not None:
                                return True

                            if self.destination_wild_card_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
                            return meta._meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.sequence_number is None:
                            raise YPYModelError('Key property sequence_number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-es-acl-cfg:access-list-entry[Cisco-IOS-XR-es-acl-cfg:sequence-number = ' + str(self.sequence_number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sequence_number is not None:
                            return True

                        if self.capture is not None:
                            return True

                        if self.cos is not None:
                            return True

                        if self.dei is not None:
                            return True

                        if self.destination_network is not None and self.destination_network._has_data():
                            return True

                        if self.ether_type_number is not None:
                            return True

                        if self.grant is not None:
                            return True

                        if self.inner_cos is not None:
                            return True

                        if self.inner_dei is not None:
                            return True

                        if self.inner_vlan1 is not None:
                            return True

                        if self.inner_vlan2 is not None:
                            return True

                        if self.log_option is not None:
                            return True

                        if self.remark is not None:
                            return True

                        if self.sequence_str is not None:
                            return True

                        if self.source_network is not None and self.source_network._has_data():
                            return True

                        if self.vlan1 is not None:
                            return True

                        if self.vlan2 is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
                        return meta._meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-es-acl-cfg:access-list-entries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_list_entry is not None:
                        for child_ref in self.access_list_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
                    return meta._meta_table['EsAcl.Accesses.Access.AccessListEntries']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-es-acl-cfg:es-acl/Cisco-IOS-XR-es-acl-cfg:accesses/Cisco-IOS-XR-es-acl-cfg:access[Cisco-IOS-XR-es-acl-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.access_list_entries is not None and self.access_list_entries._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
                return meta._meta_table['EsAcl.Accesses.Access']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-es-acl-cfg:es-acl/Cisco-IOS-XR-es-acl-cfg:accesses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.access is not None:
                for child_ref in self.access:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
            return meta._meta_table['EsAcl.Accesses']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-es-acl-cfg:es-acl'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.accesses is not None and self.accesses._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_es_acl_cfg as meta
        return meta._meta_table['EsAcl']['meta_info']


