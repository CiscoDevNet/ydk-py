""" Cisco_IOS_XE_boot_integrity_oper 

This module contains a collection of YANG definitions
for Cisco IOS XE boot integrity visibility.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class BootIntegrityOperData(Entity):
    """
    Enclosing container for the boot integrity 
    measurements of the system
    
    .. attribute:: boot_integrity
    
    	List of system boot integrity measurements for Boot,  Boot Loader, and OS versions, hashes, and signatures as well as Platform Configuration Registers (PCR) content. These measurements are captured utilizing Trusted Anchor Module (TAM) services to communicate with system ACT2  (2nd Gen Anti\-Counterfeit Technology) hardware chip
    	**type**\:  :py:class:`BootIntegrity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_boot_integrity_oper.BootIntegrityOperData.BootIntegrity>`
    
    	**presence node**\: True
    
    .. attribute:: sudi_certificate
    
    	List of system  certificate measurements for Cisco Root CA (CRCA), Cisco Manufacturing CA (CMCA), and ACT2 RSA Secure Unique Device  Identity (SUDI) CA PEM certifcates and SUDI generated signatures. These measurements are captured utilizing Trusted Anchor Module (TAM) services to communicate with system ACT2  (2nd Gen Anti\-Counterfeit Technology) hardware chip
    	**type**\:  :py:class:`SudiCertificate <ydk.models.cisco_ios_xe.Cisco_IOS_XE_boot_integrity_oper.BootIntegrityOperData.SudiCertificate>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'boot-integrity-ios-xe-oper'
    _revision = '2018-01-31'

    def __init__(self):
        super(BootIntegrityOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "boot-integrity-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-boot-integrity-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("boot-integrity", ("boot_integrity", BootIntegrityOperData.BootIntegrity)), ("sudi-certificate", ("sudi_certificate", BootIntegrityOperData.SudiCertificate))])
        self._leafs = OrderedDict()

        self.boot_integrity = None
        self._children_name_map["boot_integrity"] = "boot-integrity"

        self.sudi_certificate = None
        self._children_name_map["sudi_certificate"] = "sudi-certificate"
        self._segment_path = lambda: "Cisco-IOS-XE-boot-integrity-oper:boot-integrity-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(BootIntegrityOperData, [], name, value)


    class BootIntegrity(Entity):
        """
        List of system boot integrity measurements for Boot, 
        Boot Loader, and OS versions, hashes, and signatures
        as well as Platform Configuration Registers (PCR) content.
        These measurements are captured utilizing Trusted Anchor Module (TAM)
        services to communicate with system ACT2 
        (2nd Gen Anti\-Counterfeit Technology) hardware chip.
        
        .. attribute:: platform
        
        	Product Identifier
        	**type**\: str
        
        .. attribute:: boot_ver
        
        	Boot 0 Version
        	**type**\: str
        
        .. attribute:: boot_loader_ver
        
        	Boot Loader Version
        	**type**\: str
        
        .. attribute:: os_version
        
        	Operating System Version
        	**type**\: str
        
        .. attribute:: boot_hash
        
        	Boot 0 Hash
        	**type**\: str
        
        .. attribute:: boot_loader_hash
        
        	Boot Loader Hash
        	**type**\: str
        
        .. attribute:: os_hash
        
        	Operating System Hash
        	**type**\: str
        
        .. attribute:: package_count
        
        	Number of Active Packages
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: pcr_register
        
        	System Platform Configuration Registers
        	**type**\: list of  		 :py:class:`PcrRegister <ydk.models.cisco_ios_xe.Cisco_IOS_XE_boot_integrity_oper.BootIntegrityOperData.BootIntegrity.PcrRegister>`
        
        .. attribute:: package_signature
        
        	System Package Signatures
        	**type**\: list of  		 :py:class:`PackageSignature <ydk.models.cisco_ios_xe.Cisco_IOS_XE_boot_integrity_oper.BootIntegrityOperData.BootIntegrity.PackageSignature>`
        
        .. attribute:: signature
        
        	System ACT2 PCR Quote Signed Signature
        	**type**\: str
        
        .. attribute:: sig_version
        
        	System ACT2 PCR Quote Signature Version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'boot-integrity-ios-xe-oper'
        _revision = '2018-01-31'

        def __init__(self):
            super(BootIntegrityOperData.BootIntegrity, self).__init__()

            self.yang_name = "boot-integrity"
            self.yang_parent_name = "boot-integrity-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pcr-register", ("pcr_register", BootIntegrityOperData.BootIntegrity.PcrRegister)), ("package-signature", ("package_signature", BootIntegrityOperData.BootIntegrity.PackageSignature))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('platform', (YLeaf(YType.str, 'platform'), ['str'])),
                ('boot_ver', (YLeaf(YType.str, 'boot-ver'), ['str'])),
                ('boot_loader_ver', (YLeaf(YType.str, 'boot-loader-ver'), ['str'])),
                ('os_version', (YLeaf(YType.str, 'os-version'), ['str'])),
                ('boot_hash', (YLeaf(YType.str, 'boot-hash'), ['str'])),
                ('boot_loader_hash', (YLeaf(YType.str, 'boot-loader-hash'), ['str'])),
                ('os_hash', (YLeaf(YType.str, 'os-hash'), ['str'])),
                ('package_count', (YLeaf(YType.uint8, 'package-count'), ['int'])),
                ('signature', (YLeaf(YType.str, 'signature'), ['str'])),
                ('sig_version', (YLeaf(YType.uint32, 'sig-version'), ['int'])),
            ])
            self.platform = None
            self.boot_ver = None
            self.boot_loader_ver = None
            self.os_version = None
            self.boot_hash = None
            self.boot_loader_hash = None
            self.os_hash = None
            self.package_count = None
            self.signature = None
            self.sig_version = None

            self.pcr_register = YList(self)
            self.package_signature = YList(self)
            self._segment_path = lambda: "boot-integrity"
            self._absolute_path = lambda: "Cisco-IOS-XE-boot-integrity-oper:boot-integrity-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(BootIntegrityOperData.BootIntegrity, ['platform', 'boot_ver', 'boot_loader_ver', 'os_version', 'boot_hash', 'boot_loader_hash', 'os_hash', 'package_count', 'signature', 'sig_version'], name, value)


        class PcrRegister(Entity):
            """
            System Platform Configuration Registers
            
            .. attribute:: index  (key)
            
            	References PCR Register Index
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: pcr_content
            
            	References PCR Register Content
            	**type**\: str
            
            

            """

            _prefix = 'boot-integrity-ios-xe-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(BootIntegrityOperData.BootIntegrity.PcrRegister, self).__init__()

                self.yang_name = "pcr-register"
                self.yang_parent_name = "boot-integrity"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['index']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                    ('pcr_content', (YLeaf(YType.str, 'pcr-content'), ['str'])),
                ])
                self.index = None
                self.pcr_content = None
                self._segment_path = lambda: "pcr-register" + "[index='" + str(self.index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-boot-integrity-oper:boot-integrity-oper-data/boot-integrity/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(BootIntegrityOperData.BootIntegrity.PcrRegister, ['index', 'pcr_content'], name, value)


        class PackageSignature(Entity):
            """
            System Package Signatures
            
            .. attribute:: name  (key)
            
            	Package Name
            	**type**\: str
            
            .. attribute:: hash
            
            	Package Hash
            	**type**\: str
            
            

            """

            _prefix = 'boot-integrity-ios-xe-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(BootIntegrityOperData.BootIntegrity.PackageSignature, self).__init__()

                self.yang_name = "package-signature"
                self.yang_parent_name = "boot-integrity"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('hash', (YLeaf(YType.str, 'hash'), ['str'])),
                ])
                self.name = None
                self.hash = None
                self._segment_path = lambda: "package-signature" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-boot-integrity-oper:boot-integrity-oper-data/boot-integrity/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(BootIntegrityOperData.BootIntegrity.PackageSignature, ['name', 'hash'], name, value)


    class SudiCertificate(Entity):
        """
        List of system  certificate measurements for Cisco Root CA (CRCA),
        Cisco Manufacturing CA (CMCA), and ACT2 RSA Secure Unique Device 
        Identity (SUDI) CA PEM certifcates and SUDI generated signatures.
        These measurements are captured utilizing Trusted Anchor Module (TAM)
        services to communicate with system ACT2 
        (2nd Gen Anti\-Counterfeit Technology) hardware chip.
        
        .. attribute:: crca_pem
        
        	Cisco Root CA PEM Certficate
        	**type**\: str
        
        .. attribute:: cmca_pem
        
        	Cisco Manufacturing CA PEM Certficate
        	**type**\: str
        
        .. attribute:: sudi_pem
        
        	ACT2 RSA SUDI CA PEM Certficate
        	**type**\: str
        
        .. attribute:: sudi_signature
        
        	ACT2 RSA SUDI Certificate Generated Signature
        	**type**\: str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'boot-integrity-ios-xe-oper'
        _revision = '2018-01-31'

        def __init__(self):
            super(BootIntegrityOperData.SudiCertificate, self).__init__()

            self.yang_name = "sudi-certificate"
            self.yang_parent_name = "boot-integrity-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('crca_pem', (YLeaf(YType.str, 'crca-pem'), ['str'])),
                ('cmca_pem', (YLeaf(YType.str, 'cmca-pem'), ['str'])),
                ('sudi_pem', (YLeaf(YType.str, 'sudi-pem'), ['str'])),
                ('sudi_signature', (YLeaf(YType.str, 'sudi-signature'), ['str'])),
            ])
            self.crca_pem = None
            self.cmca_pem = None
            self.sudi_pem = None
            self.sudi_signature = None
            self._segment_path = lambda: "sudi-certificate"
            self._absolute_path = lambda: "Cisco-IOS-XE-boot-integrity-oper:boot-integrity-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(BootIntegrityOperData.SudiCertificate, ['crca_pem', 'cmca_pem', 'sudi_pem', 'sudi_signature'], name, value)

    def clone_ptr(self):
        self._top_entity = BootIntegrityOperData()
        return self._top_entity

