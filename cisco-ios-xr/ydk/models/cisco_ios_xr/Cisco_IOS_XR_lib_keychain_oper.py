""" Cisco_IOS_XR_lib_keychain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package operational data.

This module contains definitions
for the following management objects\:
  keychain\: Keychain operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CrytoAlgoEnum(Enum):
    """
    CrytoAlgoEnum

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

    """

    not_configured = 0

    hmac_sha1_12 = 2

    md5 = 3

    sha1 = 4

    hmac_md5 = 5

    hmac_sha1_20 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
        return meta._meta_table['CrytoAlgoEnum']



class Keychain(object):
    """
    Keychain operational data
    
    .. attribute:: keies
    
    	List of configured key names
    	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies>`
    
    

    """

    _prefix = 'lib-keychain-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.keies = Keychain.Keies()
        self.keies.parent = self


    class Keies(object):
        """
        List of configured key names
        
        .. attribute:: key
        
        	Configured key name
        	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key>`
        
        

        """

        _prefix = 'lib-keychain-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.key = YList()
            self.key.parent = self
            self.key.name = 'key'


        class Key(object):
            """
            Configured key name
            
            .. attribute:: key_name  <key>
            
            	Key name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: accept_tolerance
            
            	Accept tolerance is infinite if value is 0xffffffff
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: key
            
            	Key properties
            	**type**\:   :py:class:`Key_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key_>`
            
            

            """

            _prefix = 'lib-keychain-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.key_name = None
                self.accept_tolerance = None
                self.key = Keychain.Keies.Key.Key_()
                self.key.parent = self


            class Key_(object):
                """
                Key properties
                
                .. attribute:: key_id
                
                	key id
                	**type**\: list of    :py:class:`KeyId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key_.KeyId>`
                
                

                """

                _prefix = 'lib-keychain-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.key_id = YList()
                    self.key_id.parent = self
                    self.key_id.name = 'key_id'


                class KeyId(object):
                    """
                    key id
                    
                    .. attribute:: accept_lifetime
                    
                    	Accept Lifetime of the key
                    	**type**\:   :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key_.KeyId.AcceptLifetime>`
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic algorithm
                    	**type**\:   :py:class:`CrytoAlgoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.CrytoAlgoEnum>`
                    
                    .. attribute:: key_id
                    
                    	Key ID
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: key_string
                    
                    	Key string
                    	**type**\:  str
                    
                    .. attribute:: send_lifetime
                    
                    	Lifetime of the key
                    	**type**\:   :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper.Keychain.Keies.Key.Key_.KeyId.SendLifetime>`
                    
                    

                    """

                    _prefix = 'lib-keychain-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.accept_lifetime = Keychain.Keies.Key.Key_.KeyId.AcceptLifetime()
                        self.accept_lifetime.parent = self
                        self.cryptographic_algorithm = None
                        self.key_id = None
                        self.key_string = None
                        self.send_lifetime = Keychain.Keies.Key.Key_.KeyId.SendLifetime()
                        self.send_lifetime.parent = self


                    class SendLifetime(object):
                        """
                        Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                            self.parent = None
                            self.duration = None
                            self.end = None
                            self.is_always_valid = None
                            self.is_valid_now = None
                            self.start = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-oper:send-lifetime'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.duration is not None:
                                return True

                            if self.end is not None:
                                return True

                            if self.is_always_valid is not None:
                                return True

                            if self.is_valid_now is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
                            return meta._meta_table['Keychain.Keies.Key.Key_.KeyId.SendLifetime']['meta_info']


                    class AcceptLifetime(object):
                        """
                        Accept Lifetime of the key
                        
                        .. attribute:: duration
                        
                        	Duration of the key in seconds. value 0xffffffff reflects infinite, never expires, is configured 
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                            self.parent = None
                            self.duration = None
                            self.end = None
                            self.is_always_valid = None
                            self.is_valid_now = None
                            self.start = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-oper:accept-lifetime'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.duration is not None:
                                return True

                            if self.end is not None:
                                return True

                            if self.is_always_valid is not None:
                                return True

                            if self.is_valid_now is not None:
                                return True

                            if self.start is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
                            return meta._meta_table['Keychain.Keies.Key.Key_.KeyId.AcceptLifetime']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-oper:key-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accept_lifetime is not None and self.accept_lifetime._has_data():
                            return True

                        if self.cryptographic_algorithm is not None:
                            return True

                        if self.key_id is not None:
                            return True

                        if self.key_string is not None:
                            return True

                        if self.send_lifetime is not None and self.send_lifetime._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
                        return meta._meta_table['Keychain.Keies.Key.Key_.KeyId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-oper:key'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.key_id is not None:
                        for child_ref in self.key_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
                    return meta._meta_table['Keychain.Keies.Key.Key_']['meta_info']

            @property
            def _common_path(self):
                if self.key_name is None:
                    raise YPYModelError('Key property key_name is None')

                return '/Cisco-IOS-XR-lib-keychain-oper:keychain/Cisco-IOS-XR-lib-keychain-oper:keies/Cisco-IOS-XR-lib-keychain-oper:key[Cisco-IOS-XR-lib-keychain-oper:key-name = ' + str(self.key_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.key_name is not None:
                    return True

                if self.accept_tolerance is not None:
                    return True

                if self.key is not None and self.key._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
                return meta._meta_table['Keychain.Keies.Key']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-lib-keychain-oper:keychain/Cisco-IOS-XR-lib-keychain-oper:keies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.key is not None:
                for child_ref in self.key:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
            return meta._meta_table['Keychain.Keies']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lib-keychain-oper:keychain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.keies is not None and self.keies._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_oper as meta
        return meta._meta_table['Keychain']['meta_info']


