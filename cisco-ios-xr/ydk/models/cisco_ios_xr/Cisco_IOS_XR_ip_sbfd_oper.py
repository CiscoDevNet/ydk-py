""" Cisco_IOS_XR_ip_sbfd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-sbfd package operational data.

This module contains definitions
for the following management objects\:
  sbfd\: Seamless BFD (S\-BFD) operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BfdAfId(Enum):
    """
    BfdAfId (Enum Class)

    Bfd af id

    .. data:: bfd_af_id_none = 0

    	No Address

    .. data:: bfd_af_id_ipv4 = 2

    	IPv4 AFI

    .. data:: bfd_af_id_ipv6 = 10

    	IPv6 AFI

    """

    bfd_af_id_none = Enum.YLeaf(0, "bfd-af-id-none")

    bfd_af_id_ipv4 = Enum.YLeaf(2, "bfd-af-id-ipv4")

    bfd_af_id_ipv6 = Enum.YLeaf(10, "bfd-af-id-ipv6")


class SbfdAddressFamily(Enum):
    """
    SbfdAddressFamily (Enum Class)

    Sbfd address family

    .. data:: ipv4 = 1

    	ipv4

    .. data:: ipv6 = 2

    	ipv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")



class Sbfd(Entity):
    """
    Seamless BFD (S\-BFD) operational data
    
    .. attribute:: target_identifier
    
    	Target\-identifier information
    	**type**\:  :py:class:`TargetIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier>`
    
    

    """

    _prefix = 'ip-sbfd-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(Sbfd, self).__init__()
        self._top_entity = None

        self.yang_name = "sbfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-sbfd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("target-identifier", ("target_identifier", Sbfd.TargetIdentifier))])
        self._leafs = OrderedDict()

        self.target_identifier = Sbfd.TargetIdentifier()
        self.target_identifier.parent = self
        self._children_name_map["target_identifier"] = "target-identifier"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sbfd, [], name, value)


    class TargetIdentifier(Entity):
        """
        Target\-identifier information
        
        .. attribute:: remote_vrfs
        
        	SBFD remote discriminator data
        	**type**\:  :py:class:`RemoteVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs>`
        
        .. attribute:: local_vrfs
        
        	SBFD local discriminator  data
        	**type**\:  :py:class:`LocalVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs>`
        
        

        """

        _prefix = 'ip-sbfd-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sbfd.TargetIdentifier, self).__init__()

            self.yang_name = "target-identifier"
            self.yang_parent_name = "sbfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("remote-vrfs", ("remote_vrfs", Sbfd.TargetIdentifier.RemoteVrfs)), ("local-vrfs", ("local_vrfs", Sbfd.TargetIdentifier.LocalVrfs))])
            self._leafs = OrderedDict()

            self.remote_vrfs = Sbfd.TargetIdentifier.RemoteVrfs()
            self.remote_vrfs.parent = self
            self._children_name_map["remote_vrfs"] = "remote-vrfs"

            self.local_vrfs = Sbfd.TargetIdentifier.LocalVrfs()
            self.local_vrfs.parent = self
            self._children_name_map["local_vrfs"] = "local-vrfs"
            self._segment_path = lambda: "target-identifier"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sbfd.TargetIdentifier, [], name, value)


        class RemoteVrfs(Entity):
            """
            SBFD remote discriminator data
            
            .. attribute:: remote_vrf
            
            	Table of remote discriminator data per VRF
            	**type**\: list of  		 :py:class:`RemoteVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sbfd.TargetIdentifier.RemoteVrfs, self).__init__()

                self.yang_name = "remote-vrfs"
                self.yang_parent_name = "target-identifier"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("remote-vrf", ("remote_vrf", Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf))])
                self._leafs = OrderedDict()

                self.remote_vrf = YList(self)
                self._segment_path = lambda: "remote-vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.TargetIdentifier.RemoteVrfs, [], name, value)


            class RemoteVrf(Entity):
                """
                Table of remote discriminator data per VRF
                
                .. attribute:: vrf_name  (key)
                
                	VRF name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: remote_discriminator
                
                	SBFD remote discriminator 
                	**type**\: list of  		 :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf, self).__init__()

                    self.yang_name = "remote-vrf"
                    self.yang_parent_name = "remote-vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([("remote-discriminator", ("remote_discriminator", Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.vrf_name = None

                    self.remote_discriminator = YList(self)
                    self._segment_path = lambda: "remote-vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/remote-vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf, ['vrf_name'], name, value)


                class RemoteDiscriminator(Entity):
                    """
                    SBFD remote discriminator 
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: remote_discriminator
                    
                    	Remote Discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address
                    
                    	Address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\:  :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress>`
                    
                    .. attribute:: tid_type
                    
                    	Target identifier for sbfd
                    	**type**\:  :py:class:`SbfdAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.SbfdAddressFamily>`
                    
                    .. attribute:: discr
                    
                    	Remote discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\: str
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "remote-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ip-address", ("ip_address", Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('remote_discriminator', (YLeaf(YType.uint32, 'remote-discriminator'), ['int'])),
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('tid_type', (YLeaf(YType.enumeration, 'tid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'SbfdAddressFamily', '')])),
                            ('discr', (YLeaf(YType.uint32, 'discr'), ['int'])),
                            ('vrf_name_xr', (YLeaf(YType.str, 'vrf-name-xr'), ['str'])),
                            ('status', (YLeaf(YType.str, 'status'), ['str'])),
                            ('discr_src', (YLeaf(YType.str, 'discr-src'), ['str'])),
                        ])
                        self.vrf_name = None
                        self.remote_discriminator = None
                        self.address = None
                        self.tid_type = None
                        self.discr = None
                        self.vrf_name_xr = None
                        self.status = None
                        self.discr_src = None

                        self.ip_address = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress()
                        self.ip_address.parent = self
                        self._children_name_map["ip_address"] = "ip-address"
                        self._segment_path = lambda: "remote-discriminator"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator, ['vrf_name', 'remote_discriminator', 'address', 'tid_type', 'discr', 'vrf_name_xr', 'status', 'discr_src'], name, value)


                    class IpAddress(Entity):
                        """
                        IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:  :py:class:`BfdAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.BfdAfId>`
                        
                        .. attribute:: dummy
                        
                        	No Address
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-sbfd-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress, self).__init__()

                            self.yang_name = "ip-address"
                            self.yang_parent_name = "remote-discriminator"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'BfdAfId', '')])),
                                ('dummy', (YLeaf(YType.uint8, 'dummy'), ['int'])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.afi = None
                            self.dummy = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "ip-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress, ['afi', 'dummy', 'ipv4', 'ipv6'], name, value)


        class LocalVrfs(Entity):
            """
            SBFD local discriminator  data
            
            .. attribute:: local_vrf
            
            	Table of local discriminator data per VRF
            	**type**\: list of  		 :py:class:`LocalVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sbfd.TargetIdentifier.LocalVrfs, self).__init__()

                self.yang_name = "local-vrfs"
                self.yang_parent_name = "target-identifier"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("local-vrf", ("local_vrf", Sbfd.TargetIdentifier.LocalVrfs.LocalVrf))])
                self._leafs = OrderedDict()

                self.local_vrf = YList(self)
                self._segment_path = lambda: "local-vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.TargetIdentifier.LocalVrfs, [], name, value)


            class LocalVrf(Entity):
                """
                Table of local discriminator data per VRF
                
                .. attribute:: vrf_name  (key)
                
                	VRF name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: local_discriminator
                
                	SBFD local discriminator 
                	**type**\: list of  		 :py:class:`LocalDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf, self).__init__()

                    self.yang_name = "local-vrf"
                    self.yang_parent_name = "local-vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([("local-discriminator", ("local_discriminator", Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator))])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.vrf_name = None

                    self.local_discriminator = YList(self)
                    self._segment_path = lambda: "local-vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/local-vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf, ['vrf_name'], name, value)


                class LocalDiscriminator(Entity):
                    """
                    SBFD local discriminator 
                    
                    .. attribute:: local_discriminator
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: discr
                    
                    	Local discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: flags
                    
                    	MODE name
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\: str
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator, self).__init__()

                        self.yang_name = "local-discriminator"
                        self.yang_parent_name = "local-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('local_discriminator', (YLeaf(YType.uint32, 'local-discriminator'), ['int'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('discr', (YLeaf(YType.uint32, 'discr'), ['int'])),
                            ('vrf_name_xr', (YLeaf(YType.str, 'vrf-name-xr'), ['str'])),
                            ('flags', (YLeaf(YType.str, 'flags'), ['str'])),
                            ('status', (YLeaf(YType.str, 'status'), ['str'])),
                            ('discr_src', (YLeaf(YType.str, 'discr-src'), ['str'])),
                        ])
                        self.local_discriminator = None
                        self.vrf_name = None
                        self.discr = None
                        self.vrf_name_xr = None
                        self.flags = None
                        self.status = None
                        self.discr_src = None
                        self._segment_path = lambda: "local-discriminator"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator, ['local_discriminator', 'vrf_name', 'discr', 'vrf_name_xr', 'flags', 'status', 'discr_src'], name, value)

    def clone_ptr(self):
        self._top_entity = Sbfd()
        return self._top_entity

