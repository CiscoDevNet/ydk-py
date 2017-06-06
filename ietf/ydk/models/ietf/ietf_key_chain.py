""" ietf_key_chain 

This YANG module defines the generic configuration
data for key\-chain. It is intended that the module
will be extended by vendors to define vendor\-specific
key\-chain configuration parameters.


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class KeyChains(object):
    """
    A key\-chain is a sequence of keys that are collectively
    managed for authentication.
    
    .. attribute:: name  <key>
    
    	Name of the key\-chain
    	**type**\:  str
    
    .. attribute:: accept_tolerance
    
    	Tolerance for key lifetime acceptance (seconds)
    	**type**\:   :py:class:`AcceptTolerance <ydk.models.ietf.ietf_key_chain.KeyChains.AcceptTolerance>`
    
    .. attribute:: key
    
    	One key
    	**type**\: list of    :py:class:`Key <ydk.models.ietf.ietf_key_chain.KeyChains.Key>`
    
    

    """

    _prefix = 'key-chain'
    _revision = '2015-02-24'

    def __init__(self):
        self.name = None
        self.accept_tolerance = KeyChains.AcceptTolerance()
        self.accept_tolerance.parent = self
        self.key = YList()
        self.key.parent = self
        self.key.name = 'key'


    class AcceptTolerance(object):
        """
        Tolerance for key lifetime acceptance (seconds).
        
        .. attribute:: duration
        
        	Tolerance range, in seconds
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        	**default value**\: 0
        
        

        """

        _prefix = 'key-chain'
        _revision = '2015-02-24'

        def __init__(self):
            self.parent = None
            self.duration = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/ietf-key-chain:accept-tolerance'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.duration is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_key_chain as meta
            return meta._meta_table['KeyChains.AcceptTolerance']['meta_info']


    class Key(object):
        """
        One key.
        
        .. attribute:: key_id  <key>
        
        	Key id
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: crypto_algorithm
        
        	Cryptographic algorithm associated with key
        	**type**\:   :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_key_chain.KeyChains.Key.CryptoAlgorithm>`
        
        .. attribute:: key_string
        
        	The key string
        	**type**\:   :py:class:`KeyString <ydk.models.ietf.ietf_key_chain.KeyChains.Key.KeyString>`
        
        .. attribute:: lifetime
        
        	Specify a key's lifetime
        	**type**\:   :py:class:`Lifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime>`
        
        

        """

        _prefix = 'key-chain'
        _revision = '2015-02-24'

        def __init__(self):
            self.parent = None
            self.key_id = None
            self.crypto_algorithm = KeyChains.Key.CryptoAlgorithm()
            self.crypto_algorithm.parent = self
            self.key_string = KeyChains.Key.KeyString()
            self.key_string.parent = self
            self.lifetime = KeyChains.Key.Lifetime()
            self.lifetime.parent = self


        class KeyString(object):
            """
            The key string.
            
            .. attribute:: hexadecimal_string
            
            	Key in hexadecimal string format
            	**type**\:  str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: keystring
            
            	Key string in ASCII format
            	**type**\:  str
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                self.parent = None
                self.hexadecimal_string = None
                self.keystring = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-key-chain:key-string'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.hexadecimal_string is not None:
                    return True

                if self.keystring is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_key_chain as meta
                return meta._meta_table['KeyChains.Key.KeyString']['meta_info']


        class Lifetime(object):
            """
            Specify a key's lifetime.
            
            .. attribute:: accept_lifetime
            
            	Separate lifetime specification for accept lifetime
            	**type**\:   :py:class:`AcceptLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.AcceptLifetime>`
            
            .. attribute:: send_accept_lifetime
            
            	Single lifetime specification for both send and accept lifetimes
            	**type**\:   :py:class:`SendAcceptLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.SendAcceptLifetime>`
            
            .. attribute:: send_lifetime
            
            	Separate lifetime specification for send lifetime
            	**type**\:   :py:class:`SendLifetime <ydk.models.ietf.ietf_key_chain.KeyChains.Key.Lifetime.SendLifetime>`
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                self.parent = None
                self.accept_lifetime = KeyChains.Key.Lifetime.AcceptLifetime()
                self.accept_lifetime.parent = self
                self.send_accept_lifetime = KeyChains.Key.Lifetime.SendAcceptLifetime()
                self.send_accept_lifetime.parent = self
                self.send_lifetime = KeyChains.Key.Lifetime.SendLifetime()
                self.send_lifetime.parent = self


            class SendAcceptLifetime(object):
                """
                Single lifetime specification for both send and
                accept lifetimes.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    self.parent = None
                    self.always = None
                    self.duration = None
                    self.end_date_time = None
                    self.no_end_time = None
                    self.start_date_time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-key-chain:send-accept-lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.always is not None:
                        return True

                    if self.duration is not None:
                        return True

                    if self.end_date_time is not None:
                        return True

                    if self.no_end_time is not None:
                        return True

                    if self.start_date_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_key_chain as meta
                    return meta._meta_table['KeyChains.Key.Lifetime.SendAcceptLifetime']['meta_info']


            class SendLifetime(object):
                """
                Separate lifetime specification for send
                lifetime.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    self.parent = None
                    self.always = None
                    self.duration = None
                    self.end_date_time = None
                    self.no_end_time = None
                    self.start_date_time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-key-chain:send-lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.always is not None:
                        return True

                    if self.duration is not None:
                        return True

                    if self.end_date_time is not None:
                        return True

                    if self.no_end_time is not None:
                        return True

                    if self.start_date_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_key_chain as meta
                    return meta._meta_table['KeyChains.Key.Lifetime.SendLifetime']['meta_info']


            class AcceptLifetime(object):
                """
                Separate lifetime specification for accept
                lifetime.
                
                .. attribute:: always
                
                	Indicates key lifetime is always valid
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: duration
                
                	Key lifetime duration, in seconds
                	**type**\:  int
                
                	**range:** 1..2147483646
                
                	**units**\: seconds
                
                .. attribute:: end_date_time
                
                	End time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: no_end_time
                
                	Indicates key lifetime end\-time in infinite
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: start_date_time
                
                	Start time
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'key-chain'
                _revision = '2015-02-24'

                def __init__(self):
                    self.parent = None
                    self.always = None
                    self.duration = None
                    self.end_date_time = None
                    self.no_end_time = None
                    self.start_date_time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-key-chain:accept-lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.always is not None:
                        return True

                    if self.duration is not None:
                        return True

                    if self.end_date_time is not None:
                        return True

                    if self.no_end_time is not None:
                        return True

                    if self.start_date_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_key_chain as meta
                    return meta._meta_table['KeyChains.Key.Lifetime.AcceptLifetime']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-key-chain:lifetime'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accept_lifetime is not None and self.accept_lifetime._has_data():
                    return True

                if self.send_accept_lifetime is not None and self.send_accept_lifetime._has_data():
                    return True

                if self.send_lifetime is not None and self.send_lifetime._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_key_chain as meta
                return meta._meta_table['KeyChains.Key.Lifetime']['meta_info']


        class CryptoAlgorithm(object):
            """
            Cryptographic algorithm associated with key.
            
            .. attribute:: hmac_sha1_12
            
            	The HMAC\-SHA1\-12 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha1_20
            
            	The HMAC\-SHA1\-20 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_1
            
            	HMAC\-SHA\-1 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_256
            
            	HMAC\-SHA\-256 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_384
            
            	HMAC\-SHA\-384 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hmac_sha_512
            
            	HMAC\-SHA\-512 authentication algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: md5
            
            	The MD5 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: sha_1
            
            	The SHA\-1 algorithm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'key-chain'
            _revision = '2015-02-24'

            def __init__(self):
                self.parent = None
                self.hmac_sha1_12 = None
                self.hmac_sha1_20 = None
                self.hmac_sha_1 = None
                self.hmac_sha_256 = None
                self.hmac_sha_384 = None
                self.hmac_sha_512 = None
                self.md5 = None
                self.sha_1 = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-key-chain:crypto-algorithm'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.hmac_sha1_12 is not None:
                    return True

                if self.hmac_sha1_20 is not None:
                    return True

                if self.hmac_sha_1 is not None:
                    return True

                if self.hmac_sha_256 is not None:
                    return True

                if self.hmac_sha_384 is not None:
                    return True

                if self.hmac_sha_512 is not None:
                    return True

                if self.md5 is not None:
                    return True

                if self.sha_1 is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_key_chain as meta
                return meta._meta_table['KeyChains.Key.CryptoAlgorithm']['meta_info']

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')
            if self.key_id is None:
                raise YPYModelError('Key property key_id is None')

            return self.parent._common_path +'/ietf-key-chain:key[ietf-key-chain:key-id = ' + str(self.key_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.key_id is not None:
                return True

            if self.crypto_algorithm is not None and self.crypto_algorithm._has_data():
                return True

            if self.key_string is not None and self.key_string._has_data():
                return True

            if self.lifetime is not None and self.lifetime._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_key_chain as meta
            return meta._meta_table['KeyChains.Key']['meta_info']

    @property
    def _common_path(self):
        if self.name is None:
            raise YPYModelError('Key property name is None')

        return '/ietf-key-chain:key-chains[ietf-key-chain:name = ' + str(self.name) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.name is not None:
            return True

        if self.accept_tolerance is not None and self.accept_tolerance._has_data():
            return True

        if self.key is not None:
            for child_ref in self.key:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_key_chain as meta
        return meta._meta_table['KeyChains']['meta_info']


