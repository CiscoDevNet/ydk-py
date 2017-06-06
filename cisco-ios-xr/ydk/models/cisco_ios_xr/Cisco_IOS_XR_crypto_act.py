""" Cisco_IOS_XR_crypto_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class KeyGenerateRsaGeneralKeysRpc(object):
    """
    Generate a general purpose RSA key pair for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaGeneralKeysRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyGenerateRsaGeneralKeysRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.key_label = None
            self.key_modulus = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.key_label is not None:
                return True

            if self.key_modulus is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyGenerateRsaGeneralKeysRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-generate-rsa-general-keys'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyGenerateRsaGeneralKeysRpc']['meta_info']


class KeyGenerateRsaUsageKeysRpc(object):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaUsageKeysRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyGenerateRsaUsageKeysRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.key_label = None
            self.key_modulus = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.key_label is not None:
                return True

            if self.key_modulus is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyGenerateRsaUsageKeysRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-generate-rsa-usage-keys'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyGenerateRsaUsageKeysRpc']['meta_info']


class KeyGenerateRsaRpc(object):
    """
    Generate seperate RSA key pairs for signing and encryption
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateRsaRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyGenerateRsaRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: key_label
        
        	RSA keypair label
        	**type**\:  str
        
        .. attribute:: key_modulus
        
        	Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
        	**type**\:  int
        
        	**range:** 512..4096
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.key_label = None
            self.key_modulus = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-generate-rsa/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.key_label is not None:
                return True

            if self.key_modulus is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyGenerateRsaRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-generate-rsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyGenerateRsaRpc']['meta_info']


class KeyGenerateDsaRpc(object):
    """
    Generate DSA keys
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyGenerateDsaRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyGenerateDsaRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: key_modulus
        
        	Key modulus size can be 512, 768, or 1024 bits
        	**type**\:  int
        
        	**range:** 512..None \| 768..None \| 1024..None
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.key_modulus = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-generate-dsa/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.key_modulus is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyGenerateDsaRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-generate-dsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyGenerateDsaRpc']['meta_info']


class KeyZeroizeRsaRpc(object):
    """
    Remove RSA keys
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyZeroizeRsaRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyZeroizeRsaRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: key_label
        
        	RSA key label
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.key_label = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-zeroize-rsa/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.key_label is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyZeroizeRsaRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-zeroize-rsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyZeroizeRsaRpc']['meta_info']


class KeyZeroizeDsaRpc(object):
    """
    Remove DSA keys
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-zeroize-dsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyZeroizeDsaRpc']['meta_info']


class KeyZeroizeAuthenticationRsaRpc(object):
    """
    Remove RSA authentication key
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-zeroize-authentication-rsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyZeroizeAuthenticationRsaRpc']['meta_info']


class KeyImportAuthenticationRsaRpc(object):
    """
    Remove RSA authentication key
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.KeyImportAuthenticationRsaRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = KeyImportAuthenticationRsaRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: path
        
        	Path to RSA pubkey file
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.path = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:key-import-authentication-rsa/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.path is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['KeyImportAuthenticationRsaRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:key-import-authentication-rsa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['KeyImportAuthenticationRsaRpc']['meta_info']


class CaAuthenticateRpc(object):
    """
    Get the certification authority certificate
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaAuthenticateRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaAuthenticateRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.server_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-authenticate/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.server_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaAuthenticateRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-authenticate'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaAuthenticateRpc']['meta_info']


class CaEnrollRpc(object):
    """
    Request a certificate from a CA
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaEnrollRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaEnrollRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.server_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-enroll/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.server_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaEnrollRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-enroll'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaEnrollRpc']['meta_info']


class CaImportCertificateRpc(object):
    """
    Import a certificate from a s/tftp server or the terminal
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaImportCertificateRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaImportCertificateRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.server_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-import-certificate/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.server_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaImportCertificateRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-import-certificate'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaImportCertificateRpc']['meta_info']


class CaCancelEnrollRpc(object):
    """
    Cancel enrollment from a CA
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCancelEnrollRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaCancelEnrollRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: server_name
        
        	CA Server Name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.server_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-cancel-enroll/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.server_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaCancelEnrollRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-cancel-enroll'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaCancelEnrollRpc']['meta_info']


class CaCrlRequestRpc(object):
    """
    Actions on certificate revocation lists
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequestRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaCrlRequestRpc.Output>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaCrlRequestRpc.Input()
        self.input.parent = self
        self.output = CaCrlRequestRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: uri
        
        	CRL Distribution Point in URI format
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.uri = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-crl-request/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.uri is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaCrlRequestRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: certificate
        
        	Certificate returned
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.certificate = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-crl-request/Cisco-IOS-XR-crypto-act:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.certificate is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaCrlRequestRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-crl-request'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaCrlRequestRpc']['meta_info']


class CaTrustpoolImportUrlRpc(object):
    """
    Manual import trustpool certificates from URL
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrlRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaTrustpoolImportUrlRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.url = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-trustpool-import-url/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.url is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaTrustpoolImportUrlRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-trustpool-import-url'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaTrustpoolImportUrlRpc']['meta_info']


class CaTrustpoolImportUrlCleanRpc(object):
    """
    Remove downloaded certificates in trustpool
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act.CaTrustpoolImportUrlCleanRpc.Input>`
    
    

    """

    _prefix = 'crypto-act'
    _revision = '2016-04-17'

    def __init__(self):
        self.input = CaTrustpoolImportUrlCleanRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: url
        
        	in URL format
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-act'
        _revision = '2016-04-17'

        def __init__(self):
            self.parent = None
            self.url = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean/Cisco-IOS-XR-crypto-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.url is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
            return meta._meta_table['CaTrustpoolImportUrlCleanRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-act:ca-trustpool-import-url-clean'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_act as meta
        return meta._meta_table['CaTrustpoolImportUrlCleanRpc']['meta_info']


