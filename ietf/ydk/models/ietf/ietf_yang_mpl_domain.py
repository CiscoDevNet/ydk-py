""" ietf_yang_mpl_domain 

This module contains information about the state of the MPL domain.

Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Domain(object):
    """
    High level container containing the choice statement.
    
    .. attribute:: mpl_domain
    
    	The entries describe the MPL domains, the associated Multicast addresses and interfaces
    	**type**\:   :py:class:`MplDomain <ydk.models.ietf.ietf_yang_mpl_domain.Domain.MplDomain>`
    
    .. attribute:: mpl_single
    
    	For small devices list of MC addresses for single interface and domain
    	**type**\:   :py:class:`MplSingle <ydk.models.ietf.ietf_yang_mpl_domain.Domain.MplSingle>`
    
    

    """

    _prefix = 'mpl'
    _revision = '2016-10-25'

    def __init__(self):
        self.mpl_domain = Domain.MplDomain()
        self.mpl_domain.parent = self
        self.mpl_single = Domain.MplSingle()
        self.mpl_single.parent = self


    class MplDomain(object):
        """
        The entries describe the MPL domains, the associated
        Multicast addresses and interfaces.
        
        .. attribute:: addresses
        
        	The entries describe the interfaces enabled with the specified MC address
        	**type**\: list of    :py:class:`Addresses <ydk.models.ietf.ietf_yang_mpl_domain.Domain.MplDomain.Addresses>`
        
        .. attribute:: domains
        
        	The entries describe a given domain identified with domainID and the associated Multicast addresses
        	**type**\: list of    :py:class:`Domains <ydk.models.ietf.ietf_yang_mpl_domain.Domain.MplDomain.Domains>`
        
        

        """

        _prefix = 'mpl'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.addresses = YList()
            self.addresses.parent = self
            self.addresses.name = 'addresses'
            self.domains = YList()
            self.domains.parent = self
            self.domains.name = 'domains'


        class Domains(object):
            """
            The entries describe a given domain identified with
            domainID and the associated Multicast addresses.
            
            .. attribute:: domainid  <key>
            
            	Entry uniquely identifies the domain in the forwarder
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mclist
            
            	List of associated IPv6 Addresses
            	**type**\:  list of str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'mpl'
            _revision = '2016-10-25'

            def __init__(self):
                self.parent = None
                self.domainid = None
                self.mclist = YLeafList()
                self.mclist.parent = self
                self.mclist.name = 'mclist'

            @property
            def _common_path(self):
                if self.domainid is None:
                    raise YPYModelError('Key property domainid is None')

                return '/ietf-yang-mpl-domain:domain/ietf-yang-mpl-domain:mpl-domain/ietf-yang-mpl-domain:domains[ietf-yang-mpl-domain:domainID = ' + str(self.domainid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.domainid is not None:
                    return True

                if self.mclist is not None:
                    for child in self.mclist:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_yang_mpl_domain as meta
                return meta._meta_table['Domain.MplDomain.Domains']['meta_info']


        class Addresses(object):
            """
            The entries describe the interfaces enabled
            with the specified MC address.
            
            .. attribute:: mcaddress  <key>
            
            	MC address belonging to a MPL domain
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interfaces
            
            	List of names of interfaces enabled for this Multicast address. Interface name is defined in [RFC6206]
            	**type**\:  list of str
            
            

            """

            _prefix = 'mpl'
            _revision = '2016-10-25'

            def __init__(self):
                self.parent = None
                self.mcaddress = None
                self.interfaces = YLeafList()
                self.interfaces.parent = self
                self.interfaces.name = 'interfaces'

            @property
            def _common_path(self):
                if self.mcaddress is None:
                    raise YPYModelError('Key property mcaddress is None')

                return '/ietf-yang-mpl-domain:domain/ietf-yang-mpl-domain:mpl-domain/ietf-yang-mpl-domain:addresses[ietf-yang-mpl-domain:MCaddress = ' + str(self.mcaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.mcaddress is not None:
                    return True

                if self.interfaces is not None:
                    for child in self.interfaces:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_yang_mpl_domain as meta
                return meta._meta_table['Domain.MplDomain.Addresses']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-yang-mpl-domain:domain/ietf-yang-mpl-domain:mpl-domain'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.addresses is not None:
                for child_ref in self.addresses:
                    if child_ref._has_data():
                        return True

            if self.domains is not None:
                for child_ref in self.domains:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_yang_mpl_domain as meta
            return meta._meta_table['Domain.MplDomain']['meta_info']


    class MplSingle(object):
        """
        For small devices list of MC addresses for single
        interface and domain.
        
        .. attribute:: mcaddresses
        
        	list of MC addresses belonging to one single domain and interface
        	**type**\:  list of str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'mpl'
        _revision = '2016-10-25'

        def __init__(self):
            self.parent = None
            self.mcaddresses = YLeafList()
            self.mcaddresses.parent = self
            self.mcaddresses.name = 'mcaddresses'

        @property
        def _common_path(self):

            return '/ietf-yang-mpl-domain:domain/ietf-yang-mpl-domain:mpl-single'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.mcaddresses is not None:
                for child in self.mcaddresses:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_yang_mpl_domain as meta
            return meta._meta_table['Domain.MplSingle']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-yang-mpl-domain:domain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.mpl_domain is not None and self.mpl_domain._has_data():
            return True

        if self.mpl_single is not None and self.mpl_single._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_yang_mpl_domain as meta
        return meta._meta_table['Domain']['meta_info']


