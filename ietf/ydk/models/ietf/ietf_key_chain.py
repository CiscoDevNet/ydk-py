""" ietf_key_chain 

This YANG module defines the generic configuration
data for key\-chain. It is intended that the module
will be extended by vendors to define vendor\-specific
key\-chain configuration parameters.


"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class KeyChains(Entity):
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
        super(KeyChains, self).__init__()
        self._top_entity = None

        self.yang_name = "key-chains"
        self.yang_parent_name = "ietf-key-chain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"accept-tolerance" : ("accept_tolerance", KeyChains.AcceptTolerance)}
        self._child_list_classes = {"key" : ("key", KeyChains.Key)}

        self.name = YLeaf(YType.str, "name")

        self.accept_tolerance = KeyChains.AcceptTolerance()
        self.accept_tolerance.parent = self
        self._children_name_map["accept_tolerance"] = "accept-tolerance"
        self._children_yang_names.add("accept-tolerance")

        self.key = YList(self)
        self._segment_path = lambda: "ietf-key-chain:key-chains" + "[name='" + self.name.get() + "']"

    def __setattr__(self, name, value):
        self._perform_setattr(KeyChains, ['name'], name, value)


    class AcceptTolerance(Entity):
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
            super(KeyChains.AcceptTolerance, self).__init__()

            self.yang_name = "accept-tolerance"
            self.yang_parent_name = "key-chains"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.duration = YLeaf(YType.uint32, "duration")
            self._segment_path = lambda: "accept-tolerance"

        def __setattr__(self, name, value):
            self._perform_setattr(KeyChains.AcceptTolerance, ['duration'], name, value)


    class Key(Entity):
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
            super(KeyChains.Key, self).__init__()

            self.yang_name = "key"
            self.yang_parent_name = "key-chains"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self._child_container_classes = {"crypto-algorithm" : ("crypto_algorithm", KeyChains.Key.CryptoAlgorithm), "key-string" : ("key_string", KeyChains.Key.KeyString), "lifetime" : ("lifetime", KeyChains.Key.Lifetime)}
            self._child_list_classes = {}

            self.key_id = YLeaf(YType.uint64, "key-id")

            self.crypto_algorithm = KeyChains.Key.CryptoAlgorithm()
            self.crypto_algorithm.parent = self
            self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
            self._children_yang_names.add("crypto-algorithm")

            self.key_string = KeyChains.Key.KeyString()
            self.key_string.parent = self
            self._children_name_map["key_string"] = "key-string"
            self._children_yang_names.add("key-string")

            self.lifetime = KeyChains.Key.Lifetime()
            self.lifetime.parent = self
            self._children_name_map["lifetime"] = "lifetime"
            self._children_yang_names.add("lifetime")
            self._segment_path = lambda: "key" + "[key-id='" + self.key_id.get() + "']"

        def __setattr__(self, name, value):
            self._perform_setattr(KeyChains.Key, ['key_id'], name, value)


        class CryptoAlgorithm(Entity):
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
                super(KeyChains.Key.CryptoAlgorithm, self).__init__()

                self.yang_name = "crypto-algorithm"
                self.yang_parent_name = "key"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hmac_sha1_12 = YLeaf(YType.empty, "hmac-sha1-12")

                self.hmac_sha1_20 = YLeaf(YType.empty, "hmac-sha1-20")

                self.hmac_sha_1 = YLeaf(YType.empty, "hmac-sha-1")

                self.hmac_sha_256 = YLeaf(YType.empty, "hmac-sha-256")

                self.hmac_sha_384 = YLeaf(YType.empty, "hmac-sha-384")

                self.hmac_sha_512 = YLeaf(YType.empty, "hmac-sha-512")

                self.md5 = YLeaf(YType.empty, "md5")

                self.sha_1 = YLeaf(YType.empty, "sha-1")
                self._segment_path = lambda: "crypto-algorithm"

            def __setattr__(self, name, value):
                self._perform_setattr(KeyChains.Key.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512', 'md5', 'sha_1'], name, value)


        class KeyString(Entity):
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
                super(KeyChains.Key.KeyString, self).__init__()

                self.yang_name = "key-string"
                self.yang_parent_name = "key"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.hexadecimal_string = YLeaf(YType.str, "hexadecimal-string")

                self.keystring = YLeaf(YType.str, "keystring")
                self._segment_path = lambda: "key-string"

            def __setattr__(self, name, value):
                self._perform_setattr(KeyChains.Key.KeyString, ['hexadecimal_string', 'keystring'], name, value)


        class Lifetime(Entity):
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
                super(KeyChains.Key.Lifetime, self).__init__()

                self.yang_name = "lifetime"
                self.yang_parent_name = "key"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"accept-lifetime" : ("accept_lifetime", KeyChains.Key.Lifetime.AcceptLifetime), "send-accept-lifetime" : ("send_accept_lifetime", KeyChains.Key.Lifetime.SendAcceptLifetime), "send-lifetime" : ("send_lifetime", KeyChains.Key.Lifetime.SendLifetime)}
                self._child_list_classes = {}

                self.accept_lifetime = KeyChains.Key.Lifetime.AcceptLifetime()
                self.accept_lifetime.parent = self
                self._children_name_map["accept_lifetime"] = "accept-lifetime"
                self._children_yang_names.add("accept-lifetime")

                self.send_accept_lifetime = KeyChains.Key.Lifetime.SendAcceptLifetime()
                self.send_accept_lifetime.parent = self
                self._children_name_map["send_accept_lifetime"] = "send-accept-lifetime"
                self._children_yang_names.add("send-accept-lifetime")

                self.send_lifetime = KeyChains.Key.Lifetime.SendLifetime()
                self.send_lifetime.parent = self
                self._children_name_map["send_lifetime"] = "send-lifetime"
                self._children_yang_names.add("send-lifetime")
                self._segment_path = lambda: "lifetime"


            class AcceptLifetime(Entity):
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
                    super(KeyChains.Key.Lifetime.AcceptLifetime, self).__init__()

                    self.yang_name = "accept-lifetime"
                    self.yang_parent_name = "lifetime"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")
                    self._segment_path = lambda: "accept-lifetime"

                def __setattr__(self, name, value):
                    self._perform_setattr(KeyChains.Key.Lifetime.AcceptLifetime, ['always', 'duration', 'end_date_time', 'no_end_time', 'start_date_time'], name, value)


            class SendAcceptLifetime(Entity):
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
                    super(KeyChains.Key.Lifetime.SendAcceptLifetime, self).__init__()

                    self.yang_name = "send-accept-lifetime"
                    self.yang_parent_name = "lifetime"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")
                    self._segment_path = lambda: "send-accept-lifetime"

                def __setattr__(self, name, value):
                    self._perform_setattr(KeyChains.Key.Lifetime.SendAcceptLifetime, ['always', 'duration', 'end_date_time', 'no_end_time', 'start_date_time'], name, value)


            class SendLifetime(Entity):
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
                    super(KeyChains.Key.Lifetime.SendLifetime, self).__init__()

                    self.yang_name = "send-lifetime"
                    self.yang_parent_name = "lifetime"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.always = YLeaf(YType.empty, "always")

                    self.duration = YLeaf(YType.uint32, "duration")

                    self.end_date_time = YLeaf(YType.str, "end-date-time")

                    self.no_end_time = YLeaf(YType.empty, "no-end-time")

                    self.start_date_time = YLeaf(YType.str, "start-date-time")
                    self._segment_path = lambda: "send-lifetime"

                def __setattr__(self, name, value):
                    self._perform_setattr(KeyChains.Key.Lifetime.SendLifetime, ['always', 'duration', 'end_date_time', 'no_end_time', 'start_date_time'], name, value)

    def clone_ptr(self):
        self._top_entity = KeyChains()
        return self._top_entity

