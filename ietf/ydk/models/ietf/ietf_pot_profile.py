""" ietf_pot_profile 

This module contains a collection of YANG
definitions for proof of transit configuration
parameters. The model is meant for proof of
transit and is targeted for communicating the
POT\-profile between a controller and nodes
participating in proof of transit.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PotProfiles(object):
    """
    A group of proof of transit profiles.
    
    .. attribute:: pot_profile_set
    
    	Set of proof of transit profiles that group parameters required to classify and compute proof of transit metadata at a node
    	**type**\: list of    :py:class:`PotProfileSet <ydk.models.ietf.ietf_pot_profile.PotProfiles.PotProfileSet>`
    
    

    """

    _prefix = 'ietf-pot-profile'
    _revision = '2016-06-15'

    def __init__(self):
        self.pot_profile_set = YList()
        self.pot_profile_set.parent = self
        self.pot_profile_set.name = 'pot_profile_set'


    class PotProfileSet(object):
        """
        Set of proof of transit profiles that group parameters
        required to classify and compute proof of transit
        metadata at a node
        
        .. attribute:: pot_profile_name  <key>
        
        	Unique identifier for each proof of transit profile
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: active_profile_index
        
        	Proof of transit profile index that is currently active. Will be set in the first hop of the path or chain. Other nodes will not use this field
        	**type**\:  int
        
        	**range:** 0..1
        
        .. attribute:: pot_profile_list
        
        	A set of pot profiles
        	**type**\: list of    :py:class:`PotProfileList <ydk.models.ietf.ietf_pot_profile.PotProfiles.PotProfileSet.PotProfileList>`
        
        

        """

        _prefix = 'ietf-pot-profile'
        _revision = '2016-06-15'

        def __init__(self):
            self.parent = None
            self.pot_profile_name = None
            self.active_profile_index = None
            self.pot_profile_list = YList()
            self.pot_profile_list.parent = self
            self.pot_profile_list.name = 'pot_profile_list'


        class PotProfileList(object):
            """
            A set of pot profiles.
            
            .. attribute:: pot_profile_index  <key>
            
            	Proof of transit profile index
            	**type**\:  int
            
            	**range:** 0..1
            
            	**mandatory**\: True
            
            .. attribute:: bitmask
            
            	Number of bits as mask used in controlling the size of the random value generation. 32\-bits of mask is default
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**default value**\: 4294967295
            
            .. attribute:: lpc
            
            	Lagrange Polynomial Coefficient
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            .. attribute:: prime_number
            
            	Prime number used for module math computation
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            .. attribute:: public_polynomial
            
            	Pre evaluated Public polynomial
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            .. attribute:: secret_share
            
            	Share of the secret of polynomial 1 used in computation
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**mandatory**\: True
            
            .. attribute:: validator
            
            	True if the node is a verifier node
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: validator_key
            
            	Secret key for validating the path, constant of poly 1
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'ietf-pot-profile'
            _revision = '2016-06-15'

            def __init__(self):
                self.parent = None
                self.pot_profile_index = None
                self.bitmask = None
                self.lpc = None
                self.prime_number = None
                self.public_polynomial = None
                self.secret_share = None
                self.validator = None
                self.validator_key = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.pot_profile_index is None:
                    raise YPYModelError('Key property pot_profile_index is None')

                return self.parent._common_path +'/ietf-pot-profile:pot-profile-list[ietf-pot-profile:pot-profile-index = ' + str(self.pot_profile_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.pot_profile_index is not None:
                    return True

                if self.bitmask is not None:
                    return True

                if self.lpc is not None:
                    return True

                if self.prime_number is not None:
                    return True

                if self.public_polynomial is not None:
                    return True

                if self.secret_share is not None:
                    return True

                if self.validator is not None:
                    return True

                if self.validator_key is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pot_profile as meta
                return meta._meta_table['PotProfiles.PotProfileSet.PotProfileList']['meta_info']

        @property
        def _common_path(self):
            if self.pot_profile_name is None:
                raise YPYModelError('Key property pot_profile_name is None')

            return '/ietf-pot-profile:pot-profiles/ietf-pot-profile:pot-profile-set[ietf-pot-profile:pot-profile-name = ' + str(self.pot_profile_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.pot_profile_name is not None:
                return True

            if self.active_profile_index is not None:
                return True

            if self.pot_profile_list is not None:
                for child_ref in self.pot_profile_list:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pot_profile as meta
            return meta._meta_table['PotProfiles.PotProfileSet']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pot-profile:pot-profiles'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.pot_profile_set is not None:
            for child_ref in self.pot_profile_set:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pot_profile as meta
        return meta._meta_table['PotProfiles']['meta_info']


