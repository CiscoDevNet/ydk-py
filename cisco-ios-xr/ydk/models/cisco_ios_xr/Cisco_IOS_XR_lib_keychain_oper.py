""" Cisco_IOS_XR_lib_keychain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package operational data.

This module contains definitions
for the following management objects\:
  keychain\: Keychain operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CrytoAlgo(Enum):
    """
    CrytoAlgo

    Cryptographic algorithm type

    .. data:: not_configured = 0

    	Not configured

    .. data:: hmac_sha1_12 = 2

    	HMAC SHA1 12 bytes

    .. data:: md5 = 3

    	MD5 16 bytes

    .. data:: sha1 = 4

    	SHA1 20 bytes

    .. data:: hmac_md5 = 5

    	HMAC MD5 16 bytes

    .. data:: hmac_sha1_20 = 6

    	HMAC SHA1 20 bytes

    .. data:: aes_128_cmac = 7

    	CMAC AES 32 bytes

    .. data:: aes_256_cmac = 8

    	CMAC AES 64 bytes

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    hmac_sha1_12 = Enum.YLeaf(2, "hmac-sha1-12")

    md5 = Enum.YLeaf(3, "md5")

    sha1 = Enum.YLeaf(4, "sha1")

    hmac_md5 = Enum.YLeaf(5, "hmac-md5")

    hmac_sha1_20 = Enum.YLeaf(6, "hmac-sha1-20")

    aes_128_cmac = Enum.YLeaf(7, "aes-128-cmac")

    aes_256_cmac = Enum.YLeaf(8, "aes-256-cmac")


class Enc(Enum):
    """
    Enc

    Type of password encryption

    .. data:: password_type7 = 0

    	Type 7 password type

    .. data:: password_type6 = 2

    	Type 6 Encryption

    """

    password_type7 = Enum.YLeaf(0, "password-type7")

    password_type6 = Enum.YLeaf(2, "password-type6")



class Keychain(Entity):
    """
    Keychain operational data
    
    .. attribute:: keies
    
    	List of configured key names
    	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies>`
    
    

    """

    _prefix = 'lib-keychain-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Keychain, self).__init__()
        self._top_entity = None

        self.yang_name = "keychain"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"keies" : ("keies", Keychain.Keies)}
        self._child_list_classes = {}

        self.keies = Keychain.Keies()
        self.keies.parent = self
        self._children_name_map["keies"] = "keies"
        self._children_yang_names.add("keies")
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain"


    class Keies(Entity):
        """
        List of configured key names
        
        .. attribute:: key
        
        	Configured key name
        	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key>`
        
        

        """

        _prefix = 'lib-keychain-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Keychain.Keies, self).__init__()

            self.yang_name = "keies"
            self.yang_parent_name = "keychain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"key" : ("key", Keychain.Keies.Key)}

            self.key = YList(self)
            self._segment_path = lambda: "keies"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Keychain.Keies, [], name, value)


        class Key(Entity):
            """
            Configured key name
            
            .. attribute:: key_name  <key>
            
            	Key name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accept_tolerance
            
            	Accept tolerance is infinite if value is 0xffffffff
            	**type**\:  str
            
            .. attribute:: key
            
            	Key properties
            	**type**\:   :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key>`
            
            

            """

            _prefix = 'lib-keychain-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Keychain.Keies.Key, self).__init__()

                self.yang_name = "key"
                self.yang_parent_name = "keies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"key" : ("key", Keychain.Keies.Key.Key)}
                self._child_list_classes = {}

                self.key_name = YLeaf(YType.str, "key-name")

                self.accept_tolerance = YLeaf(YType.str, "accept-tolerance")

                self.key = Keychain.Keies.Key.Key()
                self.key.parent = self
                self._children_name_map["key"] = "key"
                self._children_yang_names.add("key")
                self._segment_path = lambda: "key" + "[key-name='" + self.key_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-oper:keychain/keies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Keychain.Keies.Key, ['key_name', 'accept_tolerance'], name, value)


            class Key(Entity):
                """
                Key properties
                
                .. attribute:: key_id
                
                	key id
                	**type**\: list of    :py:class:`KeyId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId>`
                
                

                """

                _prefix = 'lib-keychain-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Keychain.Keies.Key.Key, self).__init__()

                    self.yang_name = "key"
                    self.yang_parent_name = "key"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"key-id" : ("key_id", Keychain.Keies.Key.Key.KeyId)}

                    self.key_id = YList(self)
                    self._segment_path = lambda: "key"

                def __setattr__(self, name, value):
                    self._perform_setattr(Keychain.Keies.Key.Key, [], name, value)


                class KeyId(Entity):
                    """
                    key id
                    
                    .. attribute:: accept_lifetime
                    
                    	Accept Lifetime of the key
                    	**type**\:   :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.AcceptLifetime>`
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic algorithm
                    	**type**\:   :py:class:`CrytoAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.CrytoAlgo>`
                    
                    .. attribute:: key_id
                    
                    	Key ID
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: key_string
                    
                    	Key string
                    	**type**\:  str
                    
                    .. attribute:: macsec
                    
                    	To check if it's a macsec key
                    	**type**\:   :py:class:`Macsec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.Macsec>`
                    
                    .. attribute:: send_lifetime
                    
                    	Lifetime of the key
                    	**type**\:   :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key.KeyId.SendLifetime>`
                    
                    .. attribute:: type
                    
                    	Type of key encryption
                    	**type**\:   :py:class:`Enc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Enc>`
                    
                    

                    """

                    _prefix = 'lib-keychain-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Keychain.Keies.Key.Key.KeyId, self).__init__()

                        self.yang_name = "key-id"
                        self.yang_parent_name = "key"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"accept-lifetime" : ("accept_lifetime", Keychain.Keies.Key.Key.KeyId.AcceptLifetime), "macsec" : ("macsec", Keychain.Keies.Key.Key.KeyId.Macsec), "send-lifetime" : ("send_lifetime", Keychain.Keies.Key.Key.KeyId.SendLifetime)}
                        self._child_list_classes = {}

                        self.cryptographic_algorithm = YLeaf(YType.enumeration, "cryptographic-algorithm")

                        self.key_id = YLeaf(YType.uint64, "key-id")

                        self.key_string = YLeaf(YType.str, "key-string")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.accept_lifetime = Keychain.Keies.Key.Key.KeyId.AcceptLifetime()
                        self.accept_lifetime.parent = self
                        self._children_name_map["accept_lifetime"] = "accept-lifetime"
                        self._children_yang_names.add("accept-lifetime")

                        self.macsec = Keychain.Keies.Key.Key.KeyId.Macsec()
                        self.macsec.parent = self
                        self._children_name_map["macsec"] = "macsec"
                        self._children_yang_names.add("macsec")

                        self.send_lifetime = Keychain.Keies.Key.Key.KeyId.SendLifetime()
                        self.send_lifetime.parent = self
                        self._children_name_map["send_lifetime"] = "send-lifetime"
                        self._children_yang_names.add("send-lifetime")
                        self._segment_path = lambda: "key-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Keychain.Keies.Key.Key.KeyId, ['cryptographic_algorithm', 'key_id', 'key_string', 'type'], name, value)


                    class AcceptLifetime(Entity):
                        """
                        Accept Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  str
                        
                        	**units**\: second
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\:  str
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\:  bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\:  bool
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.AcceptLifetime, self).__init__()

                            self.yang_name = "accept-lifetime"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.duration = YLeaf(YType.str, "duration")

                            self.end = YLeaf(YType.str, "end")

                            self.is_always_valid = YLeaf(YType.boolean, "is-always-valid")

                            self.is_valid_now = YLeaf(YType.boolean, "is-valid-now")

                            self.start = YLeaf(YType.str, "start")
                            self._segment_path = lambda: "accept-lifetime"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keies.Key.Key.KeyId.AcceptLifetime, ['duration', 'end', 'is_always_valid', 'is_valid_now', 'start'], name, value)


                    class Macsec(Entity):
                        """
                        To check if it's a macsec key
                        
                        .. attribute:: is_macsec_key
                        
                        	To check if it's a macsec key
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.Macsec, self).__init__()

                            self.yang_name = "macsec"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.is_macsec_key = YLeaf(YType.boolean, "is-macsec-key")
                            self._segment_path = lambda: "macsec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keies.Key.Key.KeyId.Macsec, ['is_macsec_key'], name, value)


                    class SendLifetime(Entity):
                        """
                        Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  str
                        
                        	**units**\: second
                        
                        .. attribute:: end
                        
                        	Key life end time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32 \:14 2011
                        	**type**\:  str
                        
                        .. attribute:: is_always_valid
                        
                        	Is TRUE if duration is 0xffffffff 
                        	**type**\:  bool
                        
                        .. attribute:: is_valid_now
                        
                        	Is TRUE if current time is betweenstart and end lifetime , else FALSE
                        	**type**\:  bool
                        
                        .. attribute:: start
                        
                        	Key life start time in format \: day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'lib-keychain-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Keychain.Keies.Key.Key.KeyId.SendLifetime, self).__init__()

                            self.yang_name = "send-lifetime"
                            self.yang_parent_name = "key-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.duration = YLeaf(YType.str, "duration")

                            self.end = YLeaf(YType.str, "end")

                            self.is_always_valid = YLeaf(YType.boolean, "is-always-valid")

                            self.is_valid_now = YLeaf(YType.boolean, "is-valid-now")

                            self.start = YLeaf(YType.str, "start")
                            self._segment_path = lambda: "send-lifetime"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Keychain.Keies.Key.Key.KeyId.SendLifetime, ['duration', 'end', 'is_always_valid', 'is_valid_now', 'start'], name, value)

    def clone_ptr(self):
        self._top_entity = Keychain()
        return self._top_entity

