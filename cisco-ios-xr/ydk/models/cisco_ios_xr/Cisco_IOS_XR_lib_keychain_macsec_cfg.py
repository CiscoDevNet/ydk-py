""" Cisco_IOS_XR_lib_keychain_macsec_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-keychain\-macsec package configuration.

This module contains definitions
for the following management objects\:
  mac\-sec\-keychains\: Configure a Key Chain

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MacSecCryptoAlgEnum(Enum):
    """
    MacSecCryptoAlgEnum

    Mac sec crypto alg

    .. data:: aes_128_cmac = 7

    	aes 128 cmac

    .. data:: aes_256_cmac = 8

    	aes 256 cmac

    """

    aes_128_cmac = 7

    aes_256_cmac = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
        return meta._meta_table['MacSecCryptoAlgEnum']


class MacSecKeyChainMonthEnum(Enum):
    """
    MacSecKeyChainMonthEnum

    Mac sec key chain month

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
        return meta._meta_table['MacSecKeyChainMonthEnum']



class MacSecKeychains(object):
    """
    Configure a Key Chain
    
    .. attribute:: mac_sec_keychain
    
    	Name of the key chain for MACSec
    	**type**\: list of    :py:class:`MacSecKeychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain>`
    
    

    """

    _prefix = 'lib-keychain-macsec-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.mac_sec_keychain = YList()
        self.mac_sec_keychain.parent = self
        self.mac_sec_keychain.name = 'mac_sec_keychain'


    class MacSecKeychain(object):
        """
        Name of the key chain for MACSec
        
        .. attribute:: chain_name  <key>
        
        	Name of the key chain
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: keies
        
        	Configure a Key
        	**type**\:   :py:class:`Keies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies>`
        
        

        """

        _prefix = 'lib-keychain-macsec-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.chain_name = None
            self.keies = MacSecKeychains.MacSecKeychain.Keies()
            self.keies.parent = self


        class Keies(object):
            """
            Configure a Key
            
            .. attribute:: key
            
            	Key Identifier
            	**type**\: list of    :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key>`
            
            

            """

            _prefix = 'lib-keychain-macsec-cfg'
            _revision = '2015-11-09'

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
                
                .. attribute:: key_string
                
                	Configure a clear text/encrypted Key string along with cryptographic algorithm
                	**type**\:   :py:class:`KeyString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key.KeyString>`
                
                	**presence node**\: True
                
                .. attribute:: lifetime
                
                	Configure a key Lifetime
                	**type**\:   :py:class:`Lifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime>`
                
                

                """

                _prefix = 'lib-keychain-macsec-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.key_id = None
                    self.key_string = None
                    self.lifetime = MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime()
                    self.lifetime.parent = self


                class Lifetime(object):
                    """
                    Configure a key Lifetime
                    
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
                    	**type**\:   :py:class:`MacSecKeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeyChainMonthEnum>`
                    
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
                    	**type**\:   :py:class:`MacSecKeyChainMonthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecKeyChainMonthEnum>`
                    
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

                    _prefix = 'lib-keychain-macsec-cfg'
                    _revision = '2015-11-09'

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

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-macsec-cfg:lifetime'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
                        return meta._meta_table['MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime']['meta_info']


                class KeyString(object):
                    """
                    Configure a clear text/encrypted Key string
                    along with cryptographic algorithm
                    
                    .. attribute:: cryptographic_algorithm
                    
                    	Cryptographic Algorithm
                    	**type**\:   :py:class:`MacSecCryptoAlgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg.MacSecCryptoAlgEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: string
                    
                    	Key String
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'lib-keychain-macsec-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.cryptographic_algorithm = None
                        self.string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-macsec-cfg:key-string'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.cryptographic_algorithm is not None:
                            return True

                        if self.string is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
                        return meta._meta_table['MacSecKeychains.MacSecKeychain.Keies.Key.KeyString']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.key_id is None:
                        raise YPYModelError('Key property key_id is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-macsec-cfg:key[Cisco-IOS-XR-lib-keychain-macsec-cfg:key-id = ' + str(self.key_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.key_id is not None:
                        return True

                    if self.key_string is not None and self.key_string._has_data():
                        return True

                    if self.lifetime is not None and self.lifetime._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
                    return meta._meta_table['MacSecKeychains.MacSecKeychain.Keies.Key']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lib-keychain-macsec-cfg:keies'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
                return meta._meta_table['MacSecKeychains.MacSecKeychain.Keies']['meta_info']

        @property
        def _common_path(self):
            if self.chain_name is None:
                raise YPYModelError('Key property chain_name is None')

            return '/Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains/Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychain[Cisco-IOS-XR-lib-keychain-macsec-cfg:chain-name = ' + str(self.chain_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.chain_name is not None:
                return True

            if self.keies is not None and self.keies._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
            return meta._meta_table['MacSecKeychains.MacSecKeychain']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-lib-keychain-macsec-cfg:mac-sec-keychains'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.mac_sec_keychain is not None:
            for child_ref in self.mac_sec_keychain:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lib_keychain_macsec_cfg as meta
        return meta._meta_table['MacSecKeychains']['meta_info']


