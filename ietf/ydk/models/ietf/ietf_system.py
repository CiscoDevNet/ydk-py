""" ietf_system 

This module contains a collection of YANG definitions for the
configuration and identification of some common system
properties within a device containing a NETCONF server.  This
includes data node definitions for system identification,
time\-of\-day management, user management, DNS resolver
configuration, and some protocol operations for system
management.
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC 7317; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AuthenticationMethodIdentity(object):
    """
    Base identity for user authentication methods.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['AuthenticationMethodIdentity']['meta_info']


class RadiusAuthenticationTypeIdentity(object):
    """
    Base identity for RADIUS authentication types.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['RadiusAuthenticationTypeIdentity']['meta_info']


class System(object):
    """
    System group configuration.
    
    .. attribute:: authentication
    
    	The authentication configuration subtree
    	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_system.System.Authentication>`
    
    .. attribute:: clock
    
    	Configuration of the system date and time properties
    	**type**\:   :py:class:`Clock <ydk.models.ietf.ietf_system.System.Clock>`
    
    .. attribute:: contact
    
    	The administrator contact information for the system. A server implementation MAY map this leaf to the sysContact MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and sysContact.  The definition of such a mechanism is outside the scope of this document
    	**type**\:  str
    
    .. attribute:: dns_resolver
    
    	Configuration of the DNS resolver
    	**type**\:   :py:class:`DnsResolver <ydk.models.ietf.ietf_system.System.DnsResolver>`
    
    .. attribute:: hostname
    
    	The name of the host.  This name can be a single domain label or the fully qualified domain name of the host
    	**type**\:  str
    
    	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
    
    .. attribute:: location
    
    	The system location. A server implementation MAY map this leaf to the sysLocation MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and sysLocation.  The definition of such a mechanism is outside the scope of this document
    	**type**\:  str
    
    .. attribute:: ntp
    
    	Configuration of the NTP client
    	**type**\:   :py:class:`Ntp <ydk.models.ietf.ietf_system.System.Ntp>`
    
    	**presence node**\: True
    
    .. attribute:: radius
    
    	Configuration of the RADIUS client
    	**type**\:   :py:class:`Radius <ydk.models.ietf.ietf_system.System.Radius>`
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        self.authentication = System.Authentication()
        self.authentication.parent = self
        self.clock = System.Clock()
        self.clock.parent = self
        self.contact = None
        self.dns_resolver = System.DnsResolver()
        self.dns_resolver.parent = self
        self.hostname = None
        self.location = None
        self.ntp = None
        self.radius = System.Radius()
        self.radius.parent = self


    class Clock(object):
        """
        Configuration of the system date and time properties.
        
        .. attribute:: timezone_name
        
        	The TZ database name to use for the system, such as 'Europe/Stockholm'
        	**type**\:  str
        
        .. attribute:: timezone_utc_offset
        
        	The number of minutes to add to UTC time to identify the time zone for this system.  For example, 'UTC \- 8\:00 hours' would be represented as '\-480'. Note that automatic daylight saving time adjustment is not provided if this object is used
        	**type**\:  int
        
        	**range:** \-1500..1500
        
        	**units**\: minutes
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.timezone_name = None
            self.timezone_utc_offset = None

        @property
        def _common_path(self):

            return '/ietf-system:system/ietf-system:clock'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.timezone_name is not None:
                return True

            if self.timezone_utc_offset is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['System.Clock']['meta_info']


    class Ntp(object):
        """
        Configuration of the NTP client.
        
        .. attribute:: enabled
        
        	Indicates that the system should attempt to synchronize the system clock with an NTP server from the 'ntp/server' list
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: server
        
        	List of NTP servers to use for system clock synchronization.  If '/system/ntp/enabled' is 'true', then the system will attempt to contact and utilize the specified NTP servers
        	**type**\: list of    :py:class:`Server <ydk.models.ietf.ietf_system.System.Ntp.Server>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.enabled = None
            self.server = YList()
            self.server.parent = self
            self.server.name = 'server'


        class Server(object):
            """
            List of NTP servers to use for system clock
            synchronization.  If '/system/ntp/enabled'
            is 'true', then the system will attempt to
            contact and utilize the specified NTP servers.
            
            .. attribute:: name  <key>
            
            	An arbitrary name for the NTP server
            	**type**\:  str
            
            .. attribute:: association_type
            
            	The desired association type for this NTP server
            	**type**\:   :py:class:`AssociationTypeEnum <ydk.models.ietf.ietf_system.System.Ntp.Server.AssociationTypeEnum>`
            
            	**default value**\: server
            
            .. attribute:: iburst
            
            	Indicates whether this server should enable burst synchronization or not
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: prefer
            
            	Indicates whether this server should be preferred or not
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: udp
            
            	Contains UDP\-specific configuration parameters for NTP
            	**type**\:   :py:class:`Udp <ydk.models.ietf.ietf_system.System.Ntp.Server.Udp>`
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.name = None
                self.association_type = None
                self.iburst = None
                self.prefer = None
                self.udp = System.Ntp.Server.Udp()
                self.udp.parent = self

            class AssociationTypeEnum(Enum):
                """
                AssociationTypeEnum

                The desired association type for this NTP server.

                .. data:: server = 0

                	Use client association mode.  This device

                	will not provide synchronization to the

                	configured NTP server.

                .. data:: peer = 1

                	Use symmetric active association mode.

                	This device may provide synchronization

                	to the configured NTP server.

                .. data:: pool = 2

                	Use client association mode with one or

                	more of the NTP servers found by DNS

                	resolution of the domain name given by

                	the 'address' leaf.  This device will not

                	provide synchronization to the servers.

                """

                server = 0

                peer = 1

                pool = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_system as meta
                    return meta._meta_table['System.Ntp.Server.AssociationTypeEnum']



            class Udp(object):
                """
                Contains UDP\-specific configuration parameters
                for NTP.
                
                .. attribute:: address
                
                	The address of the NTP server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                
                ----
                	**type**\:  str
                
                	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	The port number of the NTP server
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 123
                
                

                """

                _prefix = 'sys'
                _revision = '2014-08-06'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.port = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-system:udp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_system as meta
                    return meta._meta_table['System.Ntp.Server.Udp']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-system:system/ietf-system:ntp/ietf-system:server[ietf-system:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.association_type is not None:
                    return True

                if self.iburst is not None:
                    return True

                if self.prefer is not None:
                    return True

                if self.udp is not None and self.udp._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.Ntp.Server']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-system:system/ietf-system:ntp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.enabled is not None:
                return True

            if self.server is not None:
                for child_ref in self.server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['System.Ntp']['meta_info']


    class DnsResolver(object):
        """
        Configuration of the DNS resolver.
        
        .. attribute:: options
        
        	Resolver options.  The set of available options has been limited to those that are generally available across different resolver implementations and generally useful
        	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_system.System.DnsResolver.Options>`
        
        .. attribute:: search
        
        	An ordered list of domains to search when resolving a host name
        	**type**\:  list of str
        
        	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
        
        .. attribute:: server
        
        	List of the DNS servers that the resolver should query. When the resolver is invoked by a calling application, it sends the query to the first name server in this list.  If no response has been received within 'timeout' seconds, the resolver continues with the next server in the list. If no response is received from any server, the resolver continues with the first server again.  When the resolver has traversed the list 'attempts' times without receiving any response, it gives up and returns an error to the calling application. Implementations MAY limit the number of entries in this list
        	**type**\: list of    :py:class:`Server <ydk.models.ietf.ietf_system.System.DnsResolver.Server>`
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.options = System.DnsResolver.Options()
            self.options.parent = self
            self.search = YLeafList()
            self.search.parent = self
            self.search.name = 'search'
            self.server = YList()
            self.server.parent = self
            self.server.name = 'server'


        class Server(object):
            """
            List of the DNS servers that the resolver should query.
            When the resolver is invoked by a calling application, it
            sends the query to the first name server in this list.  If
            no response has been received within 'timeout' seconds,
            the resolver continues with the next server in the list.
            If no response is received from any server, the resolver
            continues with the first server again.  When the resolver
            has traversed the list 'attempts' times without receiving
            any response, it gives up and returns an error to the
            calling application.
            Implementations MAY limit the number of entries in this
            list.
            
            .. attribute:: name  <key>
            
            	An arbitrary name for the DNS server
            	**type**\:  str
            
            .. attribute:: udp_and_tcp
            
            	Contains UDP\- and TCP\-specific configuration parameters for DNS
            	**type**\:   :py:class:`UdpAndTcp <ydk.models.ietf.ietf_system.System.DnsResolver.Server.UdpAndTcp>`
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.name = None
                self.udp_and_tcp = System.DnsResolver.Server.UdpAndTcp()
                self.udp_and_tcp.parent = self


            class UdpAndTcp(object):
                """
                Contains UDP\- and TCP\-specific configuration
                parameters for DNS.
                
                .. attribute:: address
                
                	The address of the DNS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	The UDP and TCP port number of the DNS server
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 53
                
                

                """

                _prefix = 'sys'
                _revision = '2014-08-06'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.port = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-system:udp-and-tcp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_system as meta
                    return meta._meta_table['System.DnsResolver.Server.UdpAndTcp']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-system:system/ietf-system:dns-resolver/ietf-system:server[ietf-system:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.udp_and_tcp is not None and self.udp_and_tcp._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.DnsResolver.Server']['meta_info']


        class Options(object):
            """
            Resolver options.  The set of available options has been
            limited to those that are generally available across
            different resolver implementations and generally useful.
            
            .. attribute:: attempts
            
            	The number of times the resolver will send a query to all of its name servers before giving up and returning an error to the calling application
            	**type**\:  int
            
            	**range:** 1..255
            
            	**default value**\: 2
            
            .. attribute:: timeout
            
            	The amount of time the resolver will wait for a response from each remote name server before retrying the query via a different name server
            	**type**\:  int
            
            	**range:** 1..255
            
            	**units**\: seconds
            
            	**default value**\: 5
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.attempts = None
                self.timeout = None

            @property
            def _common_path(self):

                return '/ietf-system:system/ietf-system:dns-resolver/ietf-system:options'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.attempts is not None:
                    return True

                if self.timeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.DnsResolver.Options']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-system:system/ietf-system:dns-resolver'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.options is not None and self.options._has_data():
                return True

            if self.search is not None:
                for child in self.search:
                    if child is not None:
                        return True

            if self.server is not None:
                for child_ref in self.server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['System.DnsResolver']['meta_info']


    class Radius(object):
        """
        Configuration of the RADIUS client.
        
        .. attribute:: options
        
        	RADIUS client options
        	**type**\:   :py:class:`Options <ydk.models.ietf.ietf_system.System.Radius.Options>`
        
        .. attribute:: server
        
        	List of RADIUS servers used by the device. When the RADIUS client is invoked by a calling application, it sends the query to the first server in this list.  If no response has been received within 'timeout' seconds, the client continues with the next server in the list.  If no response is received from any server, the client continues with the first server again. When the client has traversed the list 'attempts' times without receiving any response, it gives up and returns an error to the calling application
        	**type**\: list of    :py:class:`Server <ydk.models.ietf.ietf_system.System.Radius.Server>`
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.options = System.Radius.Options()
            self.options.parent = self
            self.server = YList()
            self.server.parent = self
            self.server.name = 'server'


        class Server(object):
            """
            List of RADIUS servers used by the device.
            When the RADIUS client is invoked by a calling
            application, it sends the query to the first server in
            this list.  If no response has been received within
            'timeout' seconds, the client continues with the next
            server in the list.  If no response is received from any
            server, the client continues with the first server again.
            When the client has traversed the list 'attempts' times
            without receiving any response, it gives up and returns an
            error to the calling application.
            
            .. attribute:: name  <key>
            
            	An arbitrary name for the RADIUS server
            	**type**\:  str
            
            .. attribute:: authentication_type
            
            	The authentication type requested from the RADIUS server
            	**type**\:   :py:class:`RadiusAuthenticationTypeIdentity <ydk.models.ietf.ietf_system.RadiusAuthenticationTypeIdentity>`
            
            	**default value**\: radius-pap
            
            .. attribute:: udp
            
            	Contains UDP\-specific configuration parameters for RADIUS
            	**type**\:   :py:class:`Udp <ydk.models.ietf.ietf_system.System.Radius.Server.Udp>`
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.name = None
                self.authentication_type = None
                self.udp = System.Radius.Server.Udp()
                self.udp.parent = self


            class Udp(object):
                """
                Contains UDP\-specific configuration parameters
                for RADIUS.
                
                .. attribute:: address
                
                	The address of the RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                
                ----
                	**type**\:  str
                
                	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: authentication_port
                
                	The port number of the RADIUS server
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**default value**\: 1812
                
                .. attribute:: shared_secret
                
                	The shared secret, which is known to both the RADIUS client and server
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'sys'
                _revision = '2014-08-06'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.authentication_port = None
                    self.shared_secret = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-system:udp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.authentication_port is not None:
                        return True

                    if self.shared_secret is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_system as meta
                    return meta._meta_table['System.Radius.Server.Udp']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-system:system/ietf-system:radius/ietf-system:server[ietf-system:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.authentication_type is not None:
                    return True

                if self.udp is not None and self.udp._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.Radius.Server']['meta_info']


        class Options(object):
            """
            RADIUS client options.
            
            .. attribute:: attempts
            
            	The number of times the device will send a query to all of its RADIUS servers before giving up
            	**type**\:  int
            
            	**range:** 1..255
            
            	**default value**\: 2
            
            .. attribute:: timeout
            
            	The number of seconds the device will wait for a response from each RADIUS server before trying with a different server
            	**type**\:  int
            
            	**range:** 1..255
            
            	**units**\: seconds
            
            	**default value**\: 5
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.attempts = None
                self.timeout = None

            @property
            def _common_path(self):

                return '/ietf-system:system/ietf-system:radius/ietf-system:options'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.attempts is not None:
                    return True

                if self.timeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.Radius.Options']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-system:system/ietf-system:radius'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.options is not None and self.options._has_data():
                return True

            if self.server is not None:
                for child_ref in self.server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['System.Radius']['meta_info']


    class Authentication(object):
        """
        The authentication configuration subtree.
        
        .. attribute:: user
        
        	The list of local users configured on this device
        	**type**\: list of    :py:class:`User <ydk.models.ietf.ietf_system.System.Authentication.User>`
        
        .. attribute:: user_authentication_order
        
        	When the device authenticates a user with a password, it tries the authentication methods in this leaf\-list in order.  If authentication with one method fails, the next method is used.  If no method succeeds, the user is denied access. An empty user\-authentication\-order leaf\-list still allows authentication of users using mechanisms that do not involve a password. If the 'radius\-authentication' feature is advertised by the NETCONF server, the 'radius' identity can be added to this list. If the 'local\-users' feature is advertised by the NETCONF server, the 'local\-users' identity can be added to this list
        	**type**\:  
        		list of  
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.user = YList()
            self.user.parent = self
            self.user.name = 'user'
            self.user_authentication_order = YLeafList()
            self.user_authentication_order.parent = self
            self.user_authentication_order.name = 'user_authentication_order'


        class User(object):
            """
            The list of local users configured on this device.
            
            .. attribute:: name  <key>
            
            	The user name string identifying this entry
            	**type**\:  str
            
            .. attribute:: authorized_key
            
            	A list of public SSH keys for this user.  These keys are allowed for SSH authentication, as described in RFC 4253
            	**type**\: list of    :py:class:`AuthorizedKey <ydk.models.ietf.ietf_system.System.Authentication.User.AuthorizedKey>`
            
            .. attribute:: password
            
            	The password for this entry
            	**type**\:  str
            
            	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
            
            

            """

            _prefix = 'sys'
            _revision = '2014-08-06'

            def __init__(self):
                self.parent = None
                self.name = None
                self.authorized_key = YList()
                self.authorized_key.parent = self
                self.authorized_key.name = 'authorized_key'
                self.password = None


            class AuthorizedKey(object):
                """
                A list of public SSH keys for this user.  These keys
                are allowed for SSH authentication, as described in
                RFC 4253.
                
                .. attribute:: name  <key>
                
                	An arbitrary name for the SSH key
                	**type**\:  str
                
                .. attribute:: algorithm
                
                	The public key algorithm name for this SSH key. Valid values are the values in the IANA 'Secure Shell (SSH) Protocol Parameters' registry, Public Key Algorithm Names
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: key_data
                
                	The binary public key data for this SSH key, as specified by RFC 4253, Section 6.6, i.e.\:   string    certificate or public key format             identifier   byte[n]   key/certificate data
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'sys'
                _revision = '2014-08-06'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.algorithm = None
                    self.key_data = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-system:authorized-key[ietf-system:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.algorithm is not None:
                        return True

                    if self.key_data is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_system as meta
                    return meta._meta_table['System.Authentication.User.AuthorizedKey']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-system:system/ietf-system:authentication/ietf-system:user[ietf-system:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.authorized_key is not None:
                    for child_ref in self.authorized_key:
                        if child_ref._has_data():
                            return True

                if self.password is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_system as meta
                return meta._meta_table['System.Authentication.User']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-system:system/ietf-system:authentication'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.user is not None:
                for child_ref in self.user:
                    if child_ref._has_data():
                        return True

            if self.user_authentication_order is not None:
                for child_ref in self.user_authentication_order:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['System.Authentication']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-system:system'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.authentication is not None and self.authentication._has_data():
            return True

        if self.clock is not None and self.clock._has_data():
            return True

        if self.contact is not None:
            return True

        if self.dns_resolver is not None and self.dns_resolver._has_data():
            return True

        if self.hostname is not None:
            return True

        if self.location is not None:
            return True

        if self.ntp is not None and self.ntp._has_data():
            return True

        if self.radius is not None and self.radius._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['System']['meta_info']


class SystemState(object):
    """
    System group operational state.
    
    .. attribute:: clock
    
    	Monitoring of the system date and time properties
    	**type**\:   :py:class:`Clock <ydk.models.ietf.ietf_system.SystemState.Clock>`
    
    .. attribute:: platform
    
    	Contains vendor\-specific information for identifying the system platform and operating system
    	**type**\:   :py:class:`Platform <ydk.models.ietf.ietf_system.SystemState.Platform>`
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        self.clock = SystemState.Clock()
        self.clock.parent = self
        self.platform = SystemState.Platform()
        self.platform.parent = self


    class Platform(object):
        """
        Contains vendor\-specific information for
        identifying the system platform and operating system.
        
        .. attribute:: machine
        
        	A vendor\-specific identifier string representing the hardware in use
        	**type**\:  str
        
        .. attribute:: os_name
        
        	The name of the operating system in use \- for example, 'Linux'
        	**type**\:  str
        
        .. attribute:: os_release
        
        	The current release level of the operating system in use.  This string MAY indicate the OS source code revision
        	**type**\:  str
        
        .. attribute:: os_version
        
        	The current version level of the operating system in use.  This string MAY indicate the specific OS build date and target variant information
        	**type**\:  str
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.machine = None
            self.os_name = None
            self.os_release = None
            self.os_version = None

        @property
        def _common_path(self):

            return '/ietf-system:system-state/ietf-system:platform'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.machine is not None:
                return True

            if self.os_name is not None:
                return True

            if self.os_release is not None:
                return True

            if self.os_version is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['SystemState.Platform']['meta_info']


    class Clock(object):
        """
        Monitoring of the system date and time properties.
        
        .. attribute:: boot_datetime
        
        	The system date and time when the system last restarted
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: current_datetime
        
        	The current system date and time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.boot_datetime = None
            self.current_datetime = None

        @property
        def _common_path(self):

            return '/ietf-system:system-state/ietf-system:clock'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.boot_datetime is not None:
                return True

            if self.current_datetime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['SystemState.Clock']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-system:system-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.clock is not None and self.clock._has_data():
            return True

        if self.platform is not None and self.platform._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['SystemState']['meta_info']


class SetCurrentDatetimeRpc(object):
    """
    Set the /system\-state/clock/current\-datetime leaf
    to the specified value.
    If the system is using NTP (i.e., /system/ntp/enabled
    is set to 'true'), then this operation will fail with
    error\-tag 'operation\-failed' and error\-app\-tag value of
    'ntp\-active'.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_system.SetCurrentDatetimeRpc.Input>`
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        self.input = SetCurrentDatetimeRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: current_datetime
        
        	The current system date and time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sys'
        _revision = '2014-08-06'

        def __init__(self):
            self.parent = None
            self.current_datetime = None

        @property
        def _common_path(self):

            return '/ietf-system:set-current-datetime/ietf-system:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.current_datetime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_system as meta
            return meta._meta_table['SetCurrentDatetimeRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-system:set-current-datetime'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['SetCurrentDatetimeRpc']['meta_info']


class SystemRestartRpc(object):
    """
    Request that the entire system be restarted immediately.
    A server SHOULD send an rpc reply to the client before
    restarting the system.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/ietf-system:system-restart'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['SystemRestartRpc']['meta_info']


class SystemShutdownRpc(object):
    """
    Request that the entire system be shut down immediately.
    A server SHOULD send an rpc reply to the client before
    shutting down the system.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/ietf-system:system-shutdown'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['SystemShutdownRpc']['meta_info']


class LocalUsersIdentity(AuthenticationMethodIdentity):
    """
    Indicates password\-based authentication of locally
    configured users.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        AuthenticationMethodIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['LocalUsersIdentity']['meta_info']


class RadiusPapIdentity(RadiusAuthenticationTypeIdentity):
    """
    The device requests Password Authentication Protocol (PAP)
    authentication from the RADIUS server.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        RadiusAuthenticationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['RadiusPapIdentity']['meta_info']


class RadiusChapIdentity(RadiusAuthenticationTypeIdentity):
    """
    The device requests Challenge Handshake Authentication
    Protocol (CHAP) authentication from the RADIUS server.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        RadiusAuthenticationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['RadiusChapIdentity']['meta_info']


class RadiusIdentity(AuthenticationMethodIdentity):
    """
    Indicates user authentication using RADIUS.
    
    

    """

    _prefix = 'sys'
    _revision = '2014-08-06'

    def __init__(self):
        AuthenticationMethodIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_system as meta
        return meta._meta_table['RadiusIdentity']['meta_info']


