""" Cisco_IOS_XR_ip_sbfd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-sbfd package operational data.

This module contains definitions
for the following management objects\:
  sbfd\: Seamless BFD (S\-BFD) operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BfdAfIdEnum(Enum):
    """
    BfdAfIdEnum

    Bfd af id

    .. data:: bfd_af_id_none = 0

    	No Address

    .. data:: bfd_af_id_ipv4 = 2

    	IPv4 AFI

    .. data:: bfd_af_id_ipv6 = 10

    	IPv6 AFI

    """

    bfd_af_id_none = 0

    bfd_af_id_ipv4 = 2

    bfd_af_id_ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
        return meta._meta_table['BfdAfIdEnum']


class SbfdAddressFamilyEnum(Enum):
    """
    SbfdAddressFamilyEnum

    Sbfd address family

    .. data:: ipv4 = 1

    	ipv4

    .. data:: ipv6 = 2

    	ipv6

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
        return meta._meta_table['SbfdAddressFamilyEnum']



class Sbfd(object):
    """
    Seamless BFD (S\-BFD) operational data
    
    .. attribute:: target_identifier
    
    	Target\-identifier information
    	**type**\:   :py:class:`TargetIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier>`
    
    

    """

    _prefix = 'ip-sbfd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.target_identifier = Sbfd.TargetIdentifier()
        self.target_identifier.parent = self


    class TargetIdentifier(object):
        """
        Target\-identifier information
        
        .. attribute:: local_vrfs
        
        	SBFD local discriminator  data
        	**type**\:   :py:class:`LocalVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs>`
        
        .. attribute:: remote_vrfs
        
        	SBFD remote discriminator data
        	**type**\:   :py:class:`RemoteVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs>`
        
        

        """

        _prefix = 'ip-sbfd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.local_vrfs = Sbfd.TargetIdentifier.LocalVrfs()
            self.local_vrfs.parent = self
            self.remote_vrfs = Sbfd.TargetIdentifier.RemoteVrfs()
            self.remote_vrfs.parent = self


        class RemoteVrfs(object):
            """
            SBFD remote discriminator data
            
            .. attribute:: remote_vrf
            
            	Table of remote discriminator data per VRF
            	**type**\: list of    :py:class:`RemoteVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.remote_vrf = YList()
                self.remote_vrf.parent = self
                self.remote_vrf.name = 'remote_vrf'


            class RemoteVrf(object):
                """
                Table of remote discriminator data per VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: remote_discriminator
                
                	SBFD remote discriminator 
                	**type**\: list of    :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.remote_discriminator = YList()
                    self.remote_discriminator.parent = self
                    self.remote_discriminator.name = 'remote_discriminator'


                class RemoteDiscriminator(object):
                    """
                    SBFD remote discriminator 
                    
                    .. attribute:: address
                    
                    	Address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: discr
                    
                    	Remote discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\:   :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress>`
                    
                    .. attribute:: remote_discriminator
                    
                    	Remote Discriminator
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\:  str
                    
                    .. attribute:: tid_type
                    
                    	Target identifier for sbfd
                    	**type**\:   :py:class:`SbfdAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.SbfdAddressFamilyEnum>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.discr = None
                        self.discr_src = None
                        self.ip_address = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress()
                        self.ip_address.parent = self
                        self.remote_discriminator = None
                        self.status = None
                        self.tid_type = None
                        self.vrf_name = None
                        self.vrf_name_xr = None


                    class IpAddress(object):
                        """
                        IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:   :py:class:`BfdAfIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.BfdAfIdEnum>`
                        
                        .. attribute:: dummy
                        
                        	No Address
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-sbfd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.afi = None
                            self.dummy = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-sbfd-oper:ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.afi is not None:
                                return True

                            if self.dummy is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                            return meta._meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-sbfd-oper:remote-discriminator'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        if self.discr is not None:
                            return True

                        if self.discr_src is not None:
                            return True

                        if self.ip_address is not None and self.ip_address._has_data():
                            return True

                        if self.remote_discriminator is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.tid_type is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        if self.vrf_name_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                        return meta._meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd/Cisco-IOS-XR-ip-sbfd-oper:target-identifier/Cisco-IOS-XR-ip-sbfd-oper:remote-vrfs/Cisco-IOS-XR-ip-sbfd-oper:remote-vrf[Cisco-IOS-XR-ip-sbfd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.remote_discriminator is not None:
                        for child_ref in self.remote_discriminator:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                    return meta._meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd/Cisco-IOS-XR-ip-sbfd-oper:target-identifier/Cisco-IOS-XR-ip-sbfd-oper:remote-vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.remote_vrf is not None:
                    for child_ref in self.remote_vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                return meta._meta_table['Sbfd.TargetIdentifier.RemoteVrfs']['meta_info']


        class LocalVrfs(object):
            """
            SBFD local discriminator  data
            
            .. attribute:: local_vrf
            
            	Table of local discriminator data per VRF
            	**type**\: list of    :py:class:`LocalVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.local_vrf = YList()
                self.local_vrf.parent = self
                self.local_vrf.name = 'local_vrf'


            class LocalVrf(object):
                """
                Table of local discriminator data per VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: local_discriminator
                
                	SBFD local discriminator 
                	**type**\: list of    :py:class:`LocalDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.local_discriminator = YList()
                    self.local_discriminator.parent = self
                    self.local_discriminator.name = 'local_discriminator'


                class LocalDiscriminator(object):
                    """
                    SBFD local discriminator 
                    
                    .. attribute:: discr
                    
                    	Local discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\:  str
                    
                    .. attribute:: flags
                    
                    	MODE name
                    	**type**\:  str
                    
                    .. attribute:: local_discriminator
                    
                    	Local discriminator
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.discr = None
                        self.discr_src = None
                        self.flags = None
                        self.local_discriminator = None
                        self.status = None
                        self.vrf_name = None
                        self.vrf_name_xr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-sbfd-oper:local-discriminator'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.discr is not None:
                            return True

                        if self.discr_src is not None:
                            return True

                        if self.flags is not None:
                            return True

                        if self.local_discriminator is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        if self.vrf_name_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                        return meta._meta_table['Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd/Cisco-IOS-XR-ip-sbfd-oper:target-identifier/Cisco-IOS-XR-ip-sbfd-oper:local-vrfs/Cisco-IOS-XR-ip-sbfd-oper:local-vrf[Cisco-IOS-XR-ip-sbfd-oper:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.local_discriminator is not None:
                        for child_ref in self.local_discriminator:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                    return meta._meta_table['Sbfd.TargetIdentifier.LocalVrfs.LocalVrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd/Cisco-IOS-XR-ip-sbfd-oper:target-identifier/Cisco-IOS-XR-ip-sbfd-oper:local-vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_vrf is not None:
                    for child_ref in self.local_vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
                return meta._meta_table['Sbfd.TargetIdentifier.LocalVrfs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd/Cisco-IOS-XR-ip-sbfd-oper:target-identifier'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.local_vrfs is not None and self.local_vrfs._has_data():
                return True

            if self.remote_vrfs is not None and self.remote_vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
            return meta._meta_table['Sbfd.TargetIdentifier']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-sbfd-oper:sbfd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.target_identifier is not None and self.target_identifier._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_sbfd_oper as meta
        return meta._meta_table['Sbfd']['meta_info']


