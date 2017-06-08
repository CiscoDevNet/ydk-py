""" ietf_conn_oam 

This YANG module defines the generic configuration,
statistics and rpc for connection oriented OAM
to be used within IETF in a protocol indpendent manner.
Functional level abstraction is indendent
with YANG modeling. It is assumed that each protocol
maps corresponding abstracts to its native format.
Each protocol may extend the YANG model defined
here to include protocol specific extensions

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IdentifierFormatIdentity(object):
    """
    Identifier\-format identity can be augmented to define other
    format identifiers used in MEP\-ID etc
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['IdentifierFormatIdentity']['meta_info']


class TechnologyTypesIdentity(object):
    """
    This is the base identy of technology types which are
    TRILL,MPLS\-TP,vpls etc
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['TechnologyTypesIdentity']['meta_info']


class NameFormatIdentity(object):
    """
    This defines the name format, IEEE 8021ag CFM defines varying
    styles of names. It is expected name format as an identity ref
    to be extended with new types.
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['NameFormatIdentity']['meta_info']


class CommandSubTypeIdentity(object):
    """
    Defines different rpc command subtypes,
    e.g rfc6905 trill OAM, this is optional for most cases
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['CommandSubTypeIdentity']['meta_info']


class DefectTypesIdentity(object):
    """
    Defines different defect types, e.g. remote rdi,
    mis\-connection defect, loss of continuity
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['DefectTypesIdentity']['meta_info']


class Domains(object):
    """
    Contains configuration related data. Within the container
    is list of fault domains. Wihin each domian has List of MA.
    
    .. attribute:: domain
    
    	Define the list of Domains within the IETF\-OAM
    	**type**\: list of    :py:class:`Domain <ydk.models.ietf.ietf_conn_oam.Domains.Domain>`
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        self.domain = YList()
        self.domain.parent = self
        self.domain.name = 'domain'


    class Domain(object):
        """
        Define the list of Domains within the IETF\-OAM
        
        .. attribute:: md_name_string  <key>
        
        	Defines the generic administrative maintenance domain name
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: technology  <key>
        
        	Defines the technology
        	**type**\:   :py:class:`TechnologyTypesIdentity <ydk.models.ietf.ietf_conn_oam.TechnologyTypesIdentity>`
        
        	**mandatory**\: True
        
        .. attribute:: mas
        
        	This container defines MA, within that have multiple MA and within MA have MEP
        	**type**\:   :py:class:`Mas <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas>`
        
        .. attribute:: md_level
        
        	Defines the MD\-Level
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: md_name_format
        
        	Name format
        	**type**\:   :py:class:`NameFormatIdentity <ydk.models.ietf.ietf_conn_oam.NameFormatIdentity>`
        
        .. attribute:: md_name_null
        
        	MD name Null
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.md_name_string = None
            self.technology = None
            self.mas = Domains.Domain.Mas()
            self.mas.parent = self
            self.md_level = None
            self.md_name_format = None
            self.md_name_null = None


        class Mas(object):
            """
            This container defines MA, within that have multiple MA
            and within MA have MEP
            
            .. attribute:: ma
            
            	Maintenance Association list
            	**type**\: list of    :py:class:`Ma <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma>`
            
            

            """

            _prefix = 'goam'
            _revision = '2017-02-10'

            def __init__(self):
                self.parent = None
                self.ma = YList()
                self.ma.parent = self
                self.ma.name = 'ma'


            class Ma(object):
                """
                Maintenance Association list
                
                .. attribute:: ma_name_string  <key>
                
                	MA name string
                	**type**\:  str
                
                .. attribute:: cc_enable
                
                	Indicate whether the CC enable
                	**type**\:  bool
                
                .. attribute:: context_null
                
                	There is no context define
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cos_id
                
                	Class of service
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: ma_name_format
                
                	Ma name format
                	**type**\:   :py:class:`NameFormatIdentity <ydk.models.ietf.ietf_conn_oam.NameFormatIdentity>`
                
                .. attribute:: ma_name_null
                
                	Empty
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: mep
                
                	Contain list of MEPS
                	**type**\: list of    :py:class:`Mep <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep>`
                
                .. attribute:: mip
                
                	List for MIP
                	**type**\: list of    :py:class:`Mip <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mip>`
                
                

                """

                _prefix = 'goam'
                _revision = '2017-02-10'

                def __init__(self):
                    self.parent = None
                    self.ma_name_string = None
                    self.cc_enable = None
                    self.context_null = None
                    self.cos_id = None
                    self.ma_name_format = None
                    self.ma_name_null = None
                    self.mep = YList()
                    self.mep.parent = self
                    self.mep.name = 'mep'
                    self.mip = YList()
                    self.mip.parent = self
                    self.mip.name = 'mip'


                class Mep(object):
                    """
                    Contain list of MEPS
                    
                    .. attribute:: mep_name  <key>
                    
                    	Generic administrative name of the MEP
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: cc_enable
                    
                    	Indicate whether the CC enable
                    	**type**\:  bool
                    
                    .. attribute:: cos_id
                    
                    	Class of service
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mac_address
                    
                    	MAC Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mep_id_format
                    
                    	MEP ID format
                    	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
                    
                    .. attribute:: mep_id_int
                    
                    	MEP ID in integer format
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: session
                    
                    	Monitoring session to/from a particular remote MEP. Depending on the protocol, this could represent CC messages received from a single remote MEP (if the protocol uses multicast CCs) or a target to which unicast echo request CCs are sent and from which responses are received (if the protocol uses a unicast request/response mechanism)
                    	**type**\: list of    :py:class:`Session <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep.Session>`
                    
                    

                    """

                    _prefix = 'goam'
                    _revision = '2017-02-10'

                    def __init__(self):
                        self.parent = None
                        self.mep_name = None
                        self.cc_enable = None
                        self.cos_id = None
                        self.ipv4_address = None
                        self.ipv6_address = None
                        self.mac_address = None
                        self.mep_id_format = None
                        self.mep_id_int = None
                        self.session = YList()
                        self.session.parent = self
                        self.session.name = 'session'


                    class Session(object):
                        """
                        Monitoring session to/from a particular remote MEP.
                        Depending on the protocol, this could represent CC
                        messages received from a single remote MEP (if the
                        protocol uses multicast CCs) or a target to which
                        unicast echo request CCs are sent and from which
                        responses are received (if the protocol uses a
                        unicast request/response mechanism).
                        
                        .. attribute:: session_cookie  <key>
                        
                        	Cookie to identify different sessions, when there are multiple remote MEPs or multiple sessions to the same remote MEP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cos_id
                        
                        	Class of service
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: destination_mep
                        
                        	Destination MEP
                        	**type**\:   :py:class:`DestinationMep <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep.Session.DestinationMep>`
                        
                        .. attribute:: destination_mep_address
                        
                        	Destination MEP Address
                        	**type**\:   :py:class:`DestinationMepAddress <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress>`
                        
                        

                        """

                        _prefix = 'goam'
                        _revision = '2017-02-10'

                        def __init__(self):
                            self.parent = None
                            self.session_cookie = None
                            self.cos_id = None
                            self.destination_mep = Domains.Domain.Mas.Ma.Mep.Session.DestinationMep()
                            self.destination_mep.parent = self
                            self.destination_mep_address = Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress()
                            self.destination_mep_address.parent = self


                        class DestinationMep(object):
                            """
                            Destination MEP
                            
                            .. attribute:: mep_id_format
                            
                            	MEP ID format
                            	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
                            
                            .. attribute:: mep_id_int
                            
                            	MEP ID in integer format
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'goam'
                            _revision = '2017-02-10'

                            def __init__(self):
                                self.parent = None
                                self.mep_id_format = None
                                self.mep_id_int = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-conn-oam:destination-mep'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mep_id_format is not None:
                                    return True

                                if self.mep_id_int is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                                return meta._meta_table['Domains.Domain.Mas.Ma.Mep.Session.DestinationMep']['meta_info']


                        class DestinationMepAddress(object):
                            """
                            Destination MEP Address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 Address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mac_address
                            
                            	MAC Address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'goam'
                            _revision = '2017-02-10'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.mac_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-conn-oam:destination-mep-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.mac_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                                return meta._meta_table['Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.session_cookie is None:
                                raise YPYModelError('Key property session_cookie is None')

                            return self.parent._common_path +'/ietf-conn-oam:session[ietf-conn-oam:session-cookie = ' + str(self.session_cookie) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.session_cookie is not None:
                                return True

                            if self.cos_id is not None:
                                return True

                            if self.destination_mep is not None and self.destination_mep._has_data():
                                return True

                            if self.destination_mep_address is not None and self.destination_mep_address._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_conn_oam as meta
                            return meta._meta_table['Domains.Domain.Mas.Ma.Mep.Session']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.mep_name is None:
                            raise YPYModelError('Key property mep_name is None')

                        return self.parent._common_path +'/ietf-conn-oam:MEP[ietf-conn-oam:mep-name = ' + str(self.mep_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mep_name is not None:
                            return True

                        if self.cc_enable is not None:
                            return True

                        if self.cos_id is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv6_address is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        if self.mep_id_format is not None:
                            return True

                        if self.mep_id_int is not None:
                            return True

                        if self.session is not None:
                            for child_ref in self.session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_conn_oam as meta
                        return meta._meta_table['Domains.Domain.Mas.Ma.Mep']['meta_info']


                class Mip(object):
                    """
                    List for MIP
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: level
                    
                    	Configure a level of maintenance intermediate point (MIP) for the interface. The MIP level range is 0 to 7
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: mac_address
                    
                    	MAC Address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'goam'
                    _revision = '2017-02-10'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.ipv4_address = None
                        self.ipv6_address = None
                        self.level = None
                        self.mac_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/ietf-conn-oam:MIP[ietf-conn-oam:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv6_address is not None:
                            return True

                        if self.level is not None:
                            return True

                        if self.mac_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_conn_oam as meta
                        return meta._meta_table['Domains.Domain.Mas.Ma.Mip']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ma_name_string is None:
                        raise YPYModelError('Key property ma_name_string is None')

                    return self.parent._common_path +'/ietf-conn-oam:MA[ietf-conn-oam:MA-name-string = ' + str(self.ma_name_string) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ma_name_string is not None:
                        return True

                    if self.cc_enable is not None:
                        return True

                    if self.context_null is not None:
                        return True

                    if self.cos_id is not None:
                        return True

                    if self.ma_name_format is not None:
                        return True

                    if self.ma_name_null is not None:
                        return True

                    if self.mep is not None:
                        for child_ref in self.mep:
                            if child_ref._has_data():
                                return True

                    if self.mip is not None:
                        for child_ref in self.mip:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_conn_oam as meta
                    return meta._meta_table['Domains.Domain.Mas.Ma']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-conn-oam:MAs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ma is not None:
                    for child_ref in self.ma:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                return meta._meta_table['Domains.Domain.Mas']['meta_info']

        @property
        def _common_path(self):
            if self.md_name_string is None:
                raise YPYModelError('Key property md_name_string is None')
            if self.technology is None:
                raise YPYModelError('Key property technology is None')

            return '/ietf-conn-oam:domains/ietf-conn-oam:domain[ietf-conn-oam:MD-name-string = ' + str(self.md_name_string) + '][ietf-conn-oam:technology = ' + str(self.technology) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.md_name_string is not None:
                return True

            if self.technology is not None:
                return True

            if self.mas is not None and self.mas._has_data():
                return True

            if self.md_level is not None:
                return True

            if self.md_name_format is not None:
                return True

            if self.md_name_null is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['Domains.Domain']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-conn-oam:domains'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.domain is not None:
            for child_ref in self.domain:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['Domains']['meta_info']


class ContinuityCheckRpc(object):
    """
    Generates continuity\-check as per RFC7276 Table 4.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_conn_oam.ContinuityCheckRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_conn_oam.ContinuityCheckRpc.Output>`
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        self.input = ContinuityCheckRpc.Input()
        self.input.parent = self
        self.output = ContinuityCheckRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: cc_transmit_interval
        
        	Interval between echo requests
        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: cos_id
        
        	Class of service
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: count
        
        	Number of continuity\-check message to send
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 3
        
        .. attribute:: destination_mep
        
        	Destination MEP
        	**type**\:   :py:class:`DestinationMep <ydk.models.ietf.ietf_conn_oam.ContinuityCheckRpc.Input.DestinationMep>`
        
        .. attribute:: ip_ttl
        
        	Time to live
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 255
        
        .. attribute:: ma_name_string
        
        	Indicate which MA is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`ma_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma>`
        
        	**mandatory**\: True
        
        .. attribute:: md_name_string
        
        	Indicate which MD is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`md_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain>`
        
        	**mandatory**\: True
        
        .. attribute:: mpls_ttl
        
        	Time to live. When an IP packet is imposed with a label, the IP TTL value is first decremented then copied into the MPLS TTL. As each LSR the MPLS frame's TTL is decremented.This behavior can be modified with no mpls ip ttl. When a MPLS label is popped, the MPLS TTL value is decremented then copied in the IP TTL field. If the MPLS TTL value is great than IP TTL, that values is not copied over. This is to prevent a possible condition of forwarding loop and TTL never reaching 0. When two MPLS labels are swapped, decrement by 1 and copy over the result into the new label. When a new MPLS labels is pushed, decrement by 1 and copy over the result into the new label. When a new MPLS labels is popped, decrement by 1 and copy over the result into the label below.[RFC3443]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: packet_size
        
        	Size of continuity\-check packets, in octets
        	**type**\:  int
        
        	**range:** 0..10000
        
        	**default value**\: 64
        
        .. attribute:: source_mep
        
        	Source MEP
        	**type**\:  str
        
        	**refers to**\:  :py:class:`mep_name <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep>`
        
        .. attribute:: sub_type
        
        	Defines different command types
        	**type**\:   :py:class:`CommandSubTypeIdentity <ydk.models.ietf.ietf_conn_oam.CommandSubTypeIdentity>`
        
        .. attribute:: technology
        
        	The technology
        	**type**\:   :py:class:`TechnologyTypesIdentity <ydk.models.ietf.ietf_conn_oam.TechnologyTypesIdentity>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.cc_transmit_interval = None
            self.cos_id = None
            self.count = None
            self.destination_mep = ContinuityCheckRpc.Input.DestinationMep()
            self.destination_mep.parent = self
            self.ip_ttl = None
            self.ma_name_string = None
            self.md_name_string = None
            self.mpls_ttl = None
            self.packet_size = None
            self.source_mep = None
            self.sub_type = None
            self.technology = None


        class DestinationMep(object):
            """
            Destination MEP
            
            .. attribute:: ipv4_address
            
            	IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address
            
            	IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: mac_address
            
            	MAC Address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mep_id_format
            
            	MEP ID format
            	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
            
            .. attribute:: mep_id_int
            
            	MEP ID in integer format
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'goam'
            _revision = '2017-02-10'

            def __init__(self):
                self.parent = None
                self.ipv4_address = None
                self.ipv6_address = None
                self.mac_address = None
                self.mep_id_format = None
                self.mep_id_int = None

            @property
            def _common_path(self):

                return '/ietf-conn-oam:continuity-check/ietf-conn-oam:input/ietf-conn-oam:destination-mep'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4_address is not None:
                    return True

                if self.ipv6_address is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.mep_id_format is not None:
                    return True

                if self.mep_id_int is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                return meta._meta_table['ContinuityCheckRpc.Input.DestinationMep']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-conn-oam:continuity-check/ietf-conn-oam:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.cc_transmit_interval is not None:
                return True

            if self.cos_id is not None:
                return True

            if self.count is not None:
                return True

            if self.destination_mep is not None and self.destination_mep._has_data():
                return True

            if self.ip_ttl is not None:
                return True

            if self.ma_name_string is not None:
                return True

            if self.md_name_string is not None:
                return True

            if self.mpls_ttl is not None:
                return True

            if self.packet_size is not None:
                return True

            if self.source_mep is not None:
                return True

            if self.sub_type is not None:
                return True

            if self.technology is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['ContinuityCheckRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: monitor_null
        
        	There is no monitoring statistics to be defined
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.monitor_null = None

        @property
        def _common_path(self):

            return '/ietf-conn-oam:continuity-check/ietf-conn-oam:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.monitor_null is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['ContinuityCheckRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-conn-oam:continuity-check'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['ContinuityCheckRpc']['meta_info']


class ContinuityVerificationRpc(object):
    """
    Generates continuity\-verification as per RFC7276 Table 4.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_conn_oam.ContinuityVerificationRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_conn_oam.ContinuityVerificationRpc.Output>`
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        self.input = ContinuityVerificationRpc.Input()
        self.input.parent = self
        self.output = ContinuityVerificationRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: cos_id
        
        	Class of service
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: count
        
        	Number of continuity\-verification message to send
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 3
        
        .. attribute:: destination_mep
        
        	Destination MEP
        	**type**\:   :py:class:`DestinationMep <ydk.models.ietf.ietf_conn_oam.ContinuityVerificationRpc.Input.DestinationMep>`
        
        .. attribute:: interval
        
        	Interval between echo requests
        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: ip_ttl
        
        	Time to live
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 255
        
        .. attribute:: ma_name_string
        
        	Indicate which MA is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`ma_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma>`
        
        	**mandatory**\: True
        
        .. attribute:: md_name_string
        
        	Indicate which MD is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`md_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain>`
        
        	**mandatory**\: True
        
        .. attribute:: mpls_ttl
        
        	Time to live. When an IP packet is imposed with a label, the IP TTL value is first decremented then copied into the MPLS TTL. As each LSR the MPLS frame's TTL is decremented.This behavior can be modified with no mpls ip ttl. When a MPLS label is popped, the MPLS TTL value is decremented then copied in the IP TTL field. If the MPLS TTL value is great than IP TTL, that values is not copied over. This is to prevent a possible condition of forwarding loop and TTL never reaching 0. When two MPLS labels are swapped, decrement by 1 and copy over the result into the new label. When a new MPLS labels is pushed, decrement by 1 and copy over the result into the new label. When a new MPLS labels is popped, decrement by 1 and copy over the result into the label below.[RFC3443]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: packet_size
        
        	Size of continuity\-verification packets, in octets
        	**type**\:  int
        
        	**range:** 64..10000
        
        	**default value**\: 64
        
        .. attribute:: source_mep
        
        	Source MEP
        	**type**\:  str
        
        	**refers to**\:  :py:class:`mep_name <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep>`
        
        .. attribute:: sub_type
        
        	Defines different command types
        	**type**\:   :py:class:`CommandSubTypeIdentity <ydk.models.ietf.ietf_conn_oam.CommandSubTypeIdentity>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.cos_id = None
            self.count = None
            self.destination_mep = ContinuityVerificationRpc.Input.DestinationMep()
            self.destination_mep.parent = self
            self.interval = None
            self.ip_ttl = None
            self.ma_name_string = None
            self.md_name_string = None
            self.mpls_ttl = None
            self.packet_size = None
            self.source_mep = None
            self.sub_type = None


        class DestinationMep(object):
            """
            Destination MEP
            
            .. attribute:: ipv4_address
            
            	IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address
            
            	IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: mac_address
            
            	MAC Address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mep_id_format
            
            	MEP ID format
            	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
            
            .. attribute:: mep_id_int
            
            	MEP ID in integer format
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'goam'
            _revision = '2017-02-10'

            def __init__(self):
                self.parent = None
                self.ipv4_address = None
                self.ipv6_address = None
                self.mac_address = None
                self.mep_id_format = None
                self.mep_id_int = None

            @property
            def _common_path(self):

                return '/ietf-conn-oam:continuity-verification/ietf-conn-oam:input/ietf-conn-oam:destination-mep'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4_address is not None:
                    return True

                if self.ipv6_address is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.mep_id_format is not None:
                    return True

                if self.mep_id_int is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                return meta._meta_table['ContinuityVerificationRpc.Input.DestinationMep']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-conn-oam:continuity-verification/ietf-conn-oam:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.cos_id is not None:
                return True

            if self.count is not None:
                return True

            if self.destination_mep is not None and self.destination_mep._has_data():
                return True

            if self.interval is not None:
                return True

            if self.ip_ttl is not None:
                return True

            if self.ma_name_string is not None:
                return True

            if self.md_name_string is not None:
                return True

            if self.mpls_ttl is not None:
                return True

            if self.packet_size is not None:
                return True

            if self.source_mep is not None:
                return True

            if self.sub_type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['ContinuityVerificationRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: monitor_null
        
        	There is no monitoring statistics to be defined
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.monitor_null = None

        @property
        def _common_path(self):

            return '/ietf-conn-oam:continuity-verification/ietf-conn-oam:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.monitor_null is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['ContinuityVerificationRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-conn-oam:continuity-verification'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['ContinuityVerificationRpc']['meta_info']


class TracerouteRpc(object):
    """
    Generates Traceroute or Path Trace and return response.
    Referencing RFC7276 for common Toolset name, for
    MPLS\-TP OAM it's Route Tracing, and for TRILL OAM It's
    Path Tracing tool. Starts with TTL of one and increment
    by one at each hop. Untill destination reached or TTL
    reach max value
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Output>`
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        self.input = TracerouteRpc.Input()
        self.input.parent = self
        self.output = TracerouteRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: command_sub_type
        
        	Defines different command types
        	**type**\:   :py:class:`CommandSubTypeIdentity <ydk.models.ietf.ietf_conn_oam.CommandSubTypeIdentity>`
        
        .. attribute:: cos_id
        
        	Class of service
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: count
        
        	Number of traceroute probes to send.  In protocols where a separate message is sent at each TTL, this is the number of packets to send at each TTL
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**default value**\: 1
        
        .. attribute:: destination_mep
        
        	Destination MEP
        	**type**\:   :py:class:`DestinationMep <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Input.DestinationMep>`
        
        .. attribute:: interval
        
        	Interval between echo requests
        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        .. attribute:: ip_ttl
        
        	Time to live
        	**type**\:  int
        
        	**range:** 0..255
        
        	**default value**\: 255
        
        .. attribute:: ma_name_string
        
        	Indicate which MA is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`ma_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma>`
        
        	**mandatory**\: True
        
        .. attribute:: md_name_string
        
        	Indicate which MD is seeing the defect
        	**type**\:  str
        
        	**refers to**\:  :py:class:`md_name_string <ydk.models.ietf.ietf_conn_oam.Domains.Domain>`
        
        	**mandatory**\: True
        
        .. attribute:: mpls_ttl
        
        	Time to live. When an IP packet is imposed with a label, the IP TTL value is first decremented then copied into the MPLS TTL. As each LSR the MPLS frame's TTL is decremented.This behavior can be modified with no mpls ip ttl. When a MPLS label is popped, the MPLS TTL value is decremented then copied in the IP TTL field. If the MPLS TTL value is great than IP TTL, that values is not copied over. This is to prevent a possible condition of forwarding loop and TTL never reaching 0. When two MPLS labels are swapped, decrement by 1 and copy over the result into the new label. When a new MPLS labels is pushed, decrement by 1 and copy over the result into the new label. When a new MPLS labels is popped, decrement by 1 and copy over the result into the label below.[RFC3443]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: source_mep
        
        	Source MEP
        	**type**\:  str
        
        	**refers to**\:  :py:class:`mep_name <ydk.models.ietf.ietf_conn_oam.Domains.Domain.Mas.Ma.Mep>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.command_sub_type = None
            self.cos_id = None
            self.count = None
            self.destination_mep = TracerouteRpc.Input.DestinationMep()
            self.destination_mep.parent = self
            self.interval = None
            self.ip_ttl = None
            self.ma_name_string = None
            self.md_name_string = None
            self.mpls_ttl = None
            self.source_mep = None


        class DestinationMep(object):
            """
            Destination MEP
            
            .. attribute:: ipv4_address
            
            	IPv4 Address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6_address
            
            	IPv6 Address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: mac_address
            
            	MAC Address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: mep_id_format
            
            	MEP ID format
            	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
            
            .. attribute:: mep_id_int
            
            	MEP ID in integer format
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'goam'
            _revision = '2017-02-10'

            def __init__(self):
                self.parent = None
                self.ipv4_address = None
                self.ipv6_address = None
                self.mac_address = None
                self.mep_id_format = None
                self.mep_id_int = None

            @property
            def _common_path(self):

                return '/ietf-conn-oam:traceroute/ietf-conn-oam:input/ietf-conn-oam:destination-mep'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ipv4_address is not None:
                    return True

                if self.ipv6_address is not None:
                    return True

                if self.mac_address is not None:
                    return True

                if self.mep_id_format is not None:
                    return True

                if self.mep_id_int is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                return meta._meta_table['TracerouteRpc.Input.DestinationMep']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-conn-oam:traceroute/ietf-conn-oam:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.command_sub_type is not None:
                return True

            if self.cos_id is not None:
                return True

            if self.count is not None:
                return True

            if self.destination_mep is not None and self.destination_mep._has_data():
                return True

            if self.interval is not None:
                return True

            if self.ip_ttl is not None:
                return True

            if self.ma_name_string is not None:
                return True

            if self.md_name_string is not None:
                return True

            if self.mpls_ttl is not None:
                return True

            if self.source_mep is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['TracerouteRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: response
        
        	List of response
        	**type**\: list of    :py:class:`Response <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Output.Response>`
        
        

        """

        _prefix = 'goam'
        _revision = '2017-02-10'

        def __init__(self):
            self.parent = None
            self.response = YList()
            self.response.parent = self
            self.response.name = 'response'


        class Response(object):
            """
            List of response.
            
            .. attribute:: response_index  <key>
            
            	Arbitrary index for the response.  In protocols that guarantee there is only a single response at each TTL , the TTL can be used as the response index
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: destination_mep
            
            	MEP from which the response has been received
            	**type**\:   :py:class:`DestinationMep <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Output.Response.DestinationMep>`
            
            .. attribute:: ip_ttl
            
            	Time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 255
            
            .. attribute:: mip
            
            	MIP responding with traceroute
            	**type**\:   :py:class:`Mip <ydk.models.ietf.ietf_conn_oam.TracerouteRpc.Output.Response.Mip>`
            
            .. attribute:: monitor_null
            
            	There is no monitoring statistics to be defined
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mpls_ttl
            
            	Time to live. When an IP packet is imposed with a label, the IP TTL value is first decremented then copied into the MPLS TTL. As each LSR the MPLS frame's TTL is decremented.This behavior can be modified with no mpls ip ttl. When a MPLS label is popped, the MPLS TTL value is decremented then copied in the IP TTL field. If the MPLS TTL value is great than IP TTL, that values is not copied over. This is to prevent a possible condition of forwarding loop and TTL never reaching 0. When two MPLS labels are swapped, decrement by 1 and copy over the result into the new label. When a new MPLS labels is pushed, decrement by 1 and copy over the result into the new label. When a new MPLS labels is popped, decrement by 1 and copy over the result into the label below.[RFC3443]
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'goam'
            _revision = '2017-02-10'

            def __init__(self):
                self.parent = None
                self.response_index = None
                self.destination_mep = TracerouteRpc.Output.Response.DestinationMep()
                self.destination_mep.parent = self
                self.ip_ttl = None
                self.mip = TracerouteRpc.Output.Response.Mip()
                self.mip.parent = self
                self.monitor_null = None
                self.mpls_ttl = None


            class DestinationMep(object):
                """
                MEP from which the response has been received
                
                .. attribute:: ipv4_address
                
                	IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mep_id_format
                
                	MEP ID format
                	**type**\:   :py:class:`IdentifierFormatIdentity <ydk.models.ietf.ietf_conn_oam.IdentifierFormatIdentity>`
                
                .. attribute:: mep_id_int
                
                	MEP ID in integer format
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'goam'
                _revision = '2017-02-10'

                def __init__(self):
                    self.parent = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.mac_address = None
                    self.mep_id_format = None
                    self.mep_id_int = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-conn-oam:destination-mep'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ipv4_address is not None:
                        return True

                    if self.ipv6_address is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.mep_id_format is not None:
                        return True

                    if self.mep_id_int is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_conn_oam as meta
                    return meta._meta_table['TracerouteRpc.Output.Response.DestinationMep']['meta_info']


            class Mip(object):
                """
                MIP responding with traceroute
                
                .. attribute:: interface
                
                	MIP interface
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: ipv4_address
                
                	IPv4 Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 Address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'goam'
                _revision = '2017-02-10'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.mac_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-conn-oam:mip'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interface is not None:
                        return True

                    if self.ipv4_address is not None:
                        return True

                    if self.ipv6_address is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_conn_oam as meta
                    return meta._meta_table['TracerouteRpc.Output.Response.Mip']['meta_info']

            @property
            def _common_path(self):
                if self.response_index is None:
                    raise YPYModelError('Key property response_index is None')

                return '/ietf-conn-oam:traceroute/ietf-conn-oam:output/ietf-conn-oam:response[ietf-conn-oam:response-index = ' + str(self.response_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.response_index is not None:
                    return True

                if self.destination_mep is not None and self.destination_mep._has_data():
                    return True

                if self.ip_ttl is not None:
                    return True

                if self.mip is not None and self.mip._has_data():
                    return True

                if self.monitor_null is not None:
                    return True

                if self.mpls_ttl is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_conn_oam as meta
                return meta._meta_table['TracerouteRpc.Output.Response']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-conn-oam:traceroute/ietf-conn-oam:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.response is not None:
                for child_ref in self.response:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_conn_oam as meta
            return meta._meta_table['TracerouteRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-conn-oam:traceroute'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['TracerouteRpc']['meta_info']


class NameFormatNullIdentity(NameFormatIdentity):
    """
    Defines name format as null
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        NameFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['NameFormatNullIdentity']['meta_info']


class OnDemandIdentity(CommandSubTypeIdentity):
    """
    On demand activation \- indicates that the tool is activated
    manually to detect a specific anomaly.
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        CommandSubTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['OnDemandIdentity']['meta_info']


class InvalidOamDefectIdentity(DefectTypesIdentity):
    """
    Indicates that one or more invalid OAM messages has been
    received and that 3.5 times that OAM message transmission
    interval has not yet expired.
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        DefectTypesIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['InvalidOamDefectIdentity']['meta_info']


class IdentifierFormatIntegerIdentity(IdentifierFormatIdentity):
    """
    Defines identifier\-format to be integer
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        IdentifierFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['IdentifierFormatIntegerIdentity']['meta_info']


class LossOfContinuityIdentity(DefectTypesIdentity):
    """
    If no proactive CC OAM packets from the source
    MEP (and in the case of CV, this includes the
    requirement to have the expected globally unique
    Source MEP identifier) are received within the interval. 
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        DefectTypesIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['LossOfContinuityIdentity']['meta_info']


class RemoteMepDefectIdentity(DefectTypesIdentity):
    """
    Indicates that one or more of the remote MEPs is
    reporting a failure 
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        DefectTypesIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['RemoteMepDefectIdentity']['meta_info']


class RdiIdentity(DefectTypesIdentity):
    """
    Indicates the aggregate health of the remote MEPs. 
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        DefectTypesIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['RdiIdentity']['meta_info']


class CrossConnectDefectIdentity(DefectTypesIdentity):
    """
    Indicates that one or more cross\-connect defect
    (for example, a service ID does not match the VLAN.)
    messages has been received and that 3.5 times that OAM message
    transmission interval has not yet expired.
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        DefectTypesIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['CrossConnectDefectIdentity']['meta_info']


class ProactiveIdentity(CommandSubTypeIdentity):
    """
    Proactive activation \- indicates that the tool is activated on a
    continual basis, where messages are sent periodically, and errors
    are detected when a certain number of expected messages are not
    received.
    
    

    """

    _prefix = 'goam'
    _revision = '2017-02-10'

    def __init__(self):
        CommandSubTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_conn_oam as meta
        return meta._meta_table['ProactiveIdentity']['meta_info']


