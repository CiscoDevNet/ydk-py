""" Cisco_IOS_XR_lib_keychain_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain package configuration.

This module contains definitions
for the following management objects\:
  keychains\: Configure a Key Chain

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CryptoAlgEnum(Enum):
    """
    CryptoAlgEnum

    Crypto alg

    .. data:: alg_hmac_sha1_12 = 2

    	HMAC SHA 1 12

    .. data:: alg_md5_16 = 3

    	MD5 16

    .. data:: alg_sha1_20 = 4

    	SHA 1 20

    .. data:: alg_hmac_md5_16 = 5

    	HMAC MD5 16

    .. data:: alg_hmac_sha1_20 = 6

    	HMAC SHA 1 20

    """

    alg_hmac_sha1_12 = 2

    alg_md5_16 = 3

    alg_sha1_20 = 4

    alg_hmac_md5_16 = 5

    alg_hmac_sha1_20 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
        return meta._meta_table['CryptoAlgEnum']


class KeyChainMonthEnum(Enum):
    """
    KeyChainMonthEnum

    Key chain month

    .. data:: jan = 0

    	January

    .. data:: feb = 1

    	February

    .. data:: mar = 2

    	March

    .. data:: apr = 3

    	April

    .. data:: may = 4

    	May

    .. data:: jun = 5

    	June

    .. data:: jul = 6

    	July

    .. data:: aug = 7

    	August

    .. data:: sep = 8

    	September

    .. data:: oct = 9

    	October

    .. data:: nov = 10

    	November

    .. data:: dec = 11

    	December

    """

    jan = 0

    feb = 1

    mar = 2

    apr = 3

    may = 4

    jun = 5

    jul = 6

    aug = 7

    sep = 8

    oct = 9

    nov = 10

    dec = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
        return meta._meta_table['KeyChainMonthEnum']



class Keychains(object):
    """
    Configure a Key Chain
    
    .. attribute:: keychain
    
    	Name of the key chain
    	**type**\: list of    :py:class:`Keychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain>`
    
    

    """

    _prefix = 'lib-keychain-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.keychain = YList()
        self.keychain.parent = self
        self.keychain.name = 'keychain'


    class Keychain(object):
        """
        Name of the key chain
        
        .. attribute:: chain_name  <key>
        
        	Name of the key chain
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: accept_tolerance
        
        	Accept Tolerance in seconds or infinite
        	**type**\:   :py:class:`AcceptTolerance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.AcceptTolerance>`
        
        .. attribute:: keies
        
        	Configure a Key
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies>`
        
        

        """

        _prefix = 'lib-keychain-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.chain_name = None
            self.accept_tolerance = Keychains.Keychain.AcceptTolerance()
            self.accept_tolerance.parent = self
            self.keies = Keychains.Keychain.Keies()
            self.keies.parent = self


        class AcceptTolerance(object):
            """
            Accept Tolerance in seconds or infinite
            
            .. attribute:: infinite
            
            	Infinite tolerance
            	**type**\:  bool
            
            .. attribute:: value
            
            	Value in seconds
            	**type**\:  int
            
            	**range:** 1..8640000
            
            	**units**\: second
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.infinite = None
                self.value = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-cfg:accept-tolerance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.infinite is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
                return meta._meta_table['Keychains.Keychain.AcceptTolerance']['meta_info']


        class Keies(object):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key>`
            
            

            """

            _prefix = 'lib-keychain-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.key = YList()
                self.key.parent = self
                self.key.name = 'key'


            class Key(object):
                """
                Key Identifier
                
                .. attribute:: key_id  <key>
                
                	48\-bit Key identifier
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accept_lifetime
                
                	Configure a key Acceptance Lifetime
                	**type**\:   :py:class:`AcceptLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key.AcceptLifetime>`
                
                .. attribute:: cryptographic_algorithm
                
                	Configure the cryptographic algorithm
                	**type**\:   :py:class:`CryptoAlgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.CryptoAlgEnum>`
                
                .. attribute:: key_string
                
                	Configure a clear text/encrypted Key string 
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: send_lifetime
                
                	Configure a Send Lifetime
                	**type**\:   :py:class:`SendLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.Keychains.Keychain.Keies.Key.SendLifetime>`
                
                

                """

                _prefix = 'lib-keychain-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.key_id = None
                    self.accept_lifetime = Keychains.Keychain.Keies.Key.AcceptLifetime()
                    self.accept_lifetime.parent = self
                    self.cryptographic_algorithm = None
                    self.key_string = None
                    self.send_lifetime = Keychains.Keychain.Keies.Key.SendLifetime()
                    self.send_lifetime.parent = self


                class AcceptLifetime(object):
                    """
                    Configure a key Acceptance Lifetime
                    
                    .. attribute:: end_date
                    
                    	End Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: end_hour
                    
                    	End Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: end_minutes
                    
                    	End Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: end_month
                    
                    	End Month
                    	**type**\:   :py:class:`KeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonthEnum>`
                    
                    .. attribute:: end_seconds
                    
                    	End Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: end_year
                    
                    	End Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    .. attribute:: infinite_flag
                    
                    	Infinite Lifetime flag
                    	**type**\:  bool
                    
                    .. attribute:: life_time
                    
                    	Lifetime duration in seconds
                    	**type**\:  int
                    
                    	**range:** 1..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: start_date
                    
                    	Start Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: start_hour
                    
                    	Start Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: start_minutes
                    
                    	Start Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: start_month
                    
                    	Start Month
                    	**type**\:   :py:class:`KeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonthEnum>`
                    
                    .. attribute:: start_seconds
                    
                    	Start Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: start_year
                    
                    	Start Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    

                    """

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.end_date = None
                        self.end_hour = None
                        self.end_minutes = None
                        self.end_month = None
                        self.end_seconds = None
                        self.end_year = None
                        self.infinite_flag = None
                        self.life_time = None
                        self.start_date = None
                        self.start_hour = None
                        self.start_minutes = None
                        self.start_month = None
                        self.start_seconds = None
                        self.start_year = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-cfg:accept-lifetime'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.end_date is not None:
                            return True

                        if self.end_hour is not None:
                            return True

                        if self.end_minutes is not None:
                            return True

                        if self.end_month is not None:
                            return True

                        if self.end_seconds is not None:
                            return True

                        if self.end_year is not None:
                            return True

                        if self.infinite_flag is not None:
                            return True

                        if self.life_time is not None:
                            return True

                        if self.start_date is not None:
                            return True

                        if self.start_hour is not None:
                            return True

                        if self.start_minutes is not None:
                            return True

                        if self.start_month is not None:
                            return True

                        if self.start_seconds is not None:
                            return True

                        if self.start_year is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
                        return meta._meta_table['Keychains.Keychain.Keies.Key.AcceptLifetime']['meta_info']


                class SendLifetime(object):
                    """
                    Configure a Send Lifetime
                    
                    .. attribute:: end_date
                    
                    	End Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: end_hour
                    
                    	End Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: end_minutes
                    
                    	End Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: end_month
                    
                    	End Month
                    	**type**\:   :py:class:`KeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonthEnum>`
                    
                    .. attribute:: end_seconds
                    
                    	End Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: end_year
                    
                    	End Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    .. attribute:: infinite_flag
                    
                    	Infinite Lifetime flag
                    	**type**\:  bool
                    
                    .. attribute:: life_time
                    
                    	Lifetime duration in seconds
                    	**type**\:  int
                    
                    	**range:** 1..2147483647
                    
                    	**units**\: second
                    
                    .. attribute:: start_date
                    
                    	Start Date
                    	**type**\:  int
                    
                    	**range:** 1..31
                    
                    .. attribute:: start_hour
                    
                    	Start Hour
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    .. attribute:: start_minutes
                    
                    	Start Minutes
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: start_month
                    
                    	Start Month
                    	**type**\:   :py:class:`KeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg.KeyChainMonthEnum>`
                    
                    .. attribute:: start_seconds
                    
                    	Start Seconds
                    	**type**\:  int
                    
                    	**range:** 0..59
                    
                    	**units**\: second
                    
                    .. attribute:: start_year
                    
                    	Start Year
                    	**type**\:  int
                    
                    	**range:** 1993..2035
                    
                    

                    """

                    _prefix = 'lib-keychain-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.end_date = None
                        self.end_hour = None
                        self.end_minutes = None
                        self.end_month = None
                        self.end_seconds = None
                        self.end_year = None
                        self.infinite_flag = None
                        self.life_time = None
                        self.start_date = None
                        self.start_hour = None
                        self.start_minutes = None
                        self.start_month = None
                        self.start_seconds = None
                        self.start_year = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-cfg:send-lifetime'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.end_date is not None:
                            return True

                        if self.end_hour is not None:
                            return True

                        if self.end_minutes is not None:
                            return True

                        if self.end_month is not None:
                            return True

                        if self.end_seconds is not None:
                            return True

                        if self.end_year is not None:
                            return True

                        if self.infinite_flag is not None:
                            return True

                        if self.life_time is not None:
                            return True

                        if self.start_date is not None:
                            return True

                        if self.start_hour is not None:
                            return True

                        if self.start_minutes is not None:
                            return True

                        if self.start_month is not None:
                            return True

                        if self.start_seconds is not None:
                            return True

                        if self.start_year is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
                        return meta._meta_table['Keychains.Keychain.Keies.Key.SendLifetime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.key_id is None:
                        raise YPYModelError('Key property key_id is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-cfg:key[Cisco-IOS-XR-lib-keychain-cfg:key-id = ' + str(self.key_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key_id is not None:
                        return True

                    if self.accept_lifetime is not None and self.accept_lifetime._has_data():
                        return True

                    if self.cryptographic_algorithm is not None:
                        return True

                    if self.key_string is not None:
                        return True

                    if self.send_lifetime is not None and self.send_lifetime._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
                    return meta._meta_table['Keychains.Keychain.Keies.Key']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-cfg:keies'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.key is not None:
                    for child_ref in self.key:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
                return meta._meta_table['Keychains.Keychain.Keies']['meta_info']

        @property
        def _common_path(self):
            if self.chain_name is None:
                raise YPYModelError('Key property chain_name is None')

            return '/Cisco-IOS-XR-lib-keychain-cfg:keychains/Cisco-IOS-XR-lib-keychain-cfg:keychain[Cisco-IOS-XR-lib-keychain-cfg:chain-name = ' + str(self.chain_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.chain_name is not None:
                return True

            if self.accept_tolerance is not None and self.accept_tolerance._has_data():
                return True

            if self.keies is not None and self.keies._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
            return meta._meta_table['Keychains.Keychain']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lib-keychain-cfg:keychains'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.keychain is not None:
            for child_ref in self.keychain:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_cfg as meta
        return meta._meta_table['Keychains']['meta_info']


