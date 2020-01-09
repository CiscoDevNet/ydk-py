""" Cisco_IOS_XR_remote_attestation_act 

This module defines procedure for remote attestation
 of a network platform''s security posture.
 This is useful to assess trustworthiness of
 hardware and software of a network device.

Copyright (c) 2017 IETF Trust and the persons identified
as authors of the code. All rights reserved.

Redistribution and use in source and binary forms, with
or without modification, is permitted pursuant to, and
subject to the license terms contained in, the Simplified
BSD License set forth in Section 4.c of the IETF Trust''s
Legal Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC VVVV; see
the RFC itself for full legal notices.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class GetCertificate(_Entity_):
    """
    Query certificate.
    Returns certificate chain
    associated with the queried certificate.
    An optional nonce can be provided, that is then used to
    return a signature over the certificate contents returned.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Output>`
    
    

    """

    _prefix = 'sb-attest'
    _revision = '2017-06-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(GetCertificate, self).__init__()
        self._top_entity = None

        self.yang_name = "get-certificate"
        self.yang_parent_name = "Cisco-IOS-XR-remote-attestation-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = GetCertificate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = GetCertificate.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-certificate"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: nonce
        
        	Nonce to be included in the attested output to prevent replay attacks
        	**type**\: str
        
        	**length:** 0..64
        
        .. attribute:: certificate_identifier
        
        	Certificate identifier
        	**type**\: str
        
        .. attribute:: location
        
        	In a distributed system get the data from a specific node identified by the location. If this field is not specified data associated with each node forming the system will be returned
        	**type**\: str
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetCertificate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-certificate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('nonce', (YLeaf(YType.str, 'nonce'), ['str'])),
                ('certificate_identifier', (YLeaf(YType.str, 'certificate-identifier'), ['str'])),
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.nonce = None
            self.certificate_identifier = None
            self.location = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-certificate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetCertificate.Input, ['nonce', 'certificate_identifier', 'location'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetCertificate.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: get_certificate_response
        
        	
        	**type**\:  :py:class:`GetCertificateResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Output.GetCertificateResponse>`
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetCertificate.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-certificate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("get-certificate-response", ("get_certificate_response", GetCertificate.Output.GetCertificateResponse))])
            self._leafs = OrderedDict()

            self.get_certificate_response = GetCertificate.Output.GetCertificateResponse()
            self.get_certificate_response.parent = self
            self._children_name_map["get_certificate_response"] = "get-certificate-response"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-certificate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetCertificate.Output, [], name, value)


        class GetCertificateResponse(_Entity_):
            """
            
            
            .. attribute:: system_certificates
            
            	Certificate data of a node in a distributed system identified by the location
            	**type**\: list of  		 :py:class:`SystemCertificates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Output.GetCertificateResponse.SystemCertificates>`
            
            

            """

            _prefix = 'sb-attest'
            _revision = '2017-06-08'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GetCertificate.Output.GetCertificateResponse, self).__init__()

                self.yang_name = "get-certificate-response"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("system-certificates", ("system_certificates", GetCertificate.Output.GetCertificateResponse.SystemCertificates))])
                self._leafs = OrderedDict()

                self.system_certificates = YList(self)
                self._segment_path = lambda: "get-certificate-response"
                self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-certificate/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GetCertificate.Output.GetCertificateResponse, [], name, value)


            class SystemCertificates(_Entity_):
                """
                Certificate data of a node in a distributed system
                identified by the location
                
                .. attribute:: node_location  (key)
                
                	Location of the node in the distributed system
                	**type**\: str
                
                .. attribute:: nonce
                
                	Nonce used for this output
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: certificates
                
                	Certificates chain associated with the certificate being queried
                	**type**\:  :py:class:`Certificates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates>`
                
                .. attribute:: signature_version
                
                	Signature version designates the format of the signed data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: signature
                
                	The optional RSA or ECDSA signature across the certificates,the signature version and the input nonce.Signed data format is\: Nonce \|\| UINT32 signature version \|\| [Certificate included in the response in DER format]
                	**type**\: str
                
                

                """

                _prefix = 'sb-attest'
                _revision = '2017-06-08'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GetCertificate.Output.GetCertificateResponse.SystemCertificates, self).__init__()

                    self.yang_name = "system-certificates"
                    self.yang_parent_name = "get-certificate-response"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([("certificates", ("certificates", GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates))])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('nonce', (YLeaf(YType.str, 'nonce'), ['str'])),
                        ('signature_version', (YLeaf(YType.uint32, 'signature_version'), ['int'])),
                        ('signature', (YLeaf(YType.str, 'signature'), ['str'])),
                    ])
                    self.node_location = None
                    self.nonce = None
                    self.signature_version = None
                    self.signature = None

                    self.certificates = GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates()
                    self.certificates.parent = self
                    self._children_name_map["certificates"] = "certificates"
                    self._segment_path = lambda: "system-certificates" + "[node-location='" + str(self.node_location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-certificate/output/get-certificate-response/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GetCertificate.Output.GetCertificateResponse.SystemCertificates, ['node_location', 'nonce', 'signature_version', 'signature'], name, value)


                class Certificates(_Entity_):
                    """
                    Certificates chain associated with the certificate
                    being queried
                    
                    .. attribute:: certificate
                    
                    	A X.509 certificate
                    	**type**\: list of  		 :py:class:`Certificate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate>`
                    
                    

                    """

                    _prefix = 'sb-attest'
                    _revision = '2017-06-08'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates, self).__init__()

                        self.yang_name = "certificates"
                        self.yang_parent_name = "system-certificates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("certificate", ("certificate", GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate))])
                        self._leafs = OrderedDict()

                        self.certificate = YList(self)
                        self._segment_path = lambda: "certificates"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates, [], name, value)


                    class Certificate(_Entity_):
                        """
                        A X.509 certificate
                        
                        .. attribute:: name  (key)
                        
                        	A node\-unique certificate identifier
                        	**type**\: str
                        
                        .. attribute:: value
                        
                        	Certificate content in DER format
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'sb-attest'
                        _revision = '2017-06-08'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate, self).__init__()

                            self.yang_name = "certificate"
                            self.yang_parent_name = "certificates"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.name = None
                            self.value = None
                            self._segment_path = lambda: "certificate" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate, ['name', 'value'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                            return meta._meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates.Certificate']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                        return meta._meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates.Certificates']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                    return meta._meta_table['GetCertificate.Output.GetCertificateResponse.SystemCertificates']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                return meta._meta_table['GetCertificate.Output.GetCertificateResponse']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetCertificate.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = GetCertificate()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
        return meta._meta_table['GetCertificate']['meta_info']


class AttestPlatformConfigRegisters(_Entity_):
    """
    Attest Platform Configuration Register(PCRs)
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.AttestPlatformConfigRegisters.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.AttestPlatformConfigRegisters.Output>`
    
    

    """

    _prefix = 'sb-attest'
    _revision = '2017-06-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(AttestPlatformConfigRegisters, self).__init__()
        self._top_entity = None

        self.yang_name = "attest-platform-config-registers"
        self.yang_parent_name = "Cisco-IOS-XR-remote-attestation-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = AttestPlatformConfigRegisters.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = AttestPlatformConfigRegisters.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-remote-attestation-act:attest-platform-config-registers"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: pcr_index
        
        	PCR register indices to be included in the attested output
        	**type**\: list of int
        
        	**range:** 0..65535
        
        .. attribute:: nonce
        
        	Nonce to be included in the attested output to prevent replay attacks
        	**type**\: str
        
        	**length:** 0..64
        
        .. attribute:: attestation_certificate_identifier
        
        	Identifier of the certificate to be used for attestation
        	**type**\: str
        
        .. attribute:: location
        
        	In a distributed system get the data from a specific node identified by the location. If this field is not specified data associated with each node forming the system will be returned
        	**type**\: str
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AttestPlatformConfigRegisters.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "attest-platform-config-registers"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('pcr_index', (YLeafList(YType.uint16, 'pcr-index'), ['int'])),
                ('nonce', (YLeaf(YType.str, 'nonce'), ['str'])),
                ('attestation_certificate_identifier', (YLeaf(YType.str, 'attestation-certificate-identifier'), ['str'])),
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.pcr_index = []
            self.nonce = None
            self.attestation_certificate_identifier = None
            self.location = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:attest-platform-config-registers/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AttestPlatformConfigRegisters.Input, ['pcr_index', 'nonce', 'attestation_certificate_identifier', 'location'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['AttestPlatformConfigRegisters.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: platform_config_registers
        
        	Attested Platform Config Register values
        	**type**\:  :py:class:`PlatformConfigRegisters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.AttestPlatformConfigRegisters.Output.PlatformConfigRegisters>`
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AttestPlatformConfigRegisters.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "attest-platform-config-registers"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("platform-config-registers", ("platform_config_registers", AttestPlatformConfigRegisters.Output.PlatformConfigRegisters))])
            self._leafs = OrderedDict()

            self.platform_config_registers = AttestPlatformConfigRegisters.Output.PlatformConfigRegisters()
            self.platform_config_registers.parent = self
            self._children_name_map["platform_config_registers"] = "platform-config-registers"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:attest-platform-config-registers/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AttestPlatformConfigRegisters.Output, [], name, value)


        class PlatformConfigRegisters(_Entity_):
            """
            Attested Platform Config Register values
            
            .. attribute:: nonce
            
            	Nonce used for this output
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: node_data
            
            	Certificate data of a node in a distributed system identified by the location
            	**type**\: list of  		 :py:class:`NodeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData>`
            
            

            """

            _prefix = 'sb-attest'
            _revision = '2017-06-08'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters, self).__init__()

                self.yang_name = "platform-config-registers"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node-data", ("node_data", AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData))])
                self._leafs = OrderedDict([
                    ('nonce', (YLeaf(YType.str, 'nonce'), ['str'])),
                ])
                self.nonce = None

                self.node_data = YList(self)
                self._segment_path = lambda: "platform-config-registers"
                self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:attest-platform-config-registers/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters, ['nonce'], name, value)


            class NodeData(_Entity_):
                """
                Certificate data of a node in a distributed system
                identified by the location
                
                .. attribute:: node_location  (key)
                
                	Location of the node in the distributed system
                	**type**\: str
                
                .. attribute:: up_time
                
                	Uptime in seconds of this node reporting its data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcr
                
                	List of requested PCR contents
                	**type**\: list of  		 :py:class:`PCR <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR>`
                
                .. attribute:: pcr_quote
                
                	TPM PCR Quote
                	**type**\: str
                
                .. attribute:: pcr_quote_signature
                
                	PCR Quote signature using TPM\-held ECC or RSA restricted key
                	**type**\: str
                
                

                """

                _prefix = 'sb-attest'
                _revision = '2017-06-08'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData, self).__init__()

                    self.yang_name = "node-data"
                    self.yang_parent_name = "platform-config-registers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([("PCR", ("pcr", AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR))])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('up_time', (YLeaf(YType.uint32, 'up-time'), ['int'])),
                        ('pcr_quote', (YLeaf(YType.str, 'pcr-quote'), ['str'])),
                        ('pcr_quote_signature', (YLeaf(YType.str, 'pcr-quote-signature'), ['str'])),
                    ])
                    self.node_location = None
                    self.up_time = None
                    self.pcr_quote = None
                    self.pcr_quote_signature = None

                    self.pcr = YList(self)
                    self._segment_path = lambda: "node-data" + "[node-location='" + str(self.node_location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:attest-platform-config-registers/output/platform-config-registers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData, ['node_location', 'up_time', 'pcr_quote', 'pcr_quote_signature'], name, value)


                class PCR(_Entity_):
                    """
                    List of requested PCR contents
                    
                    .. attribute:: index  (key)
                    
                    	PCR index
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: value
                    
                    	PCR register content
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'sb-attest'
                    _revision = '2017-06-08'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR, self).__init__()

                        self.yang_name = "PCR"
                        self.yang_parent_name = "node-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                            ('value', (YLeafList(YType.uint8, 'value'), ['int'])),
                        ])
                        self.index = None
                        self.value = []
                        self._segment_path = lambda: "PCR" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR, ['index', 'value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                        return meta._meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData.PCR']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                    return meta._meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters.NodeData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                return meta._meta_table['AttestPlatformConfigRegisters.Output.PlatformConfigRegisters']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['AttestPlatformConfigRegisters.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = AttestPlatformConfigRegisters()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
        return meta._meta_table['AttestPlatformConfigRegisters']['meta_info']


class GetPlatformBootIntegrityEventLogs(_Entity_):
    """
    Get platform's boot integrity
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output>`
    
    

    """

    _prefix = 'sb-attest'
    _revision = '2017-06-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(GetPlatformBootIntegrityEventLogs, self).__init__()
        self._top_entity = None

        self.yang_name = "get-platform-boot-integrity-event-logs"
        self.yang_parent_name = "Cisco-IOS-XR-remote-attestation-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = GetPlatformBootIntegrityEventLogs.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = GetPlatformBootIntegrityEventLogs.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-boot-integrity-event-logs"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: location
        
        	In a distributed system get the data from a specific node identified by the location. If this field is not specified data associated with each node forming the system will be returned
        	**type**\: str
        
        .. attribute:: start_event_number
        
        	To filter event logs to be retrieved. \- If set only events with sequence number greater than that specified in this argument will be returned
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: end_event_number
        
        	To control event logs to be retrieved. \- If set only events with sequence number in the range of start\-event\-number to end\-event\-number will be returned
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetPlatformBootIntegrityEventLogs.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-platform-boot-integrity-event-logs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('start_event_number', (YLeaf(YType.uint64, 'start-event-number'), ['int'])),
                ('end_event_number', (YLeaf(YType.uint64, 'end-event-number'), ['int'])),
            ])
            self.location = None
            self.start_event_number = None
            self.end_event_number = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-boot-integrity-event-logs/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetPlatformBootIntegrityEventLogs.Input, ['location', 'start_event_number', 'end_event_number'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetPlatformBootIntegrityEventLogs.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: system_boot_integrity
        
        	Boot integrity event logs
        	**type**\:  :py:class:`SystemBootIntegrity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity>`
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetPlatformBootIntegrityEventLogs.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-platform-boot-integrity-event-logs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("system-boot-integrity", ("system_boot_integrity", GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity))])
            self._leafs = OrderedDict()

            self.system_boot_integrity = GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity()
            self.system_boot_integrity.parent = self
            self._children_name_map["system_boot_integrity"] = "system-boot-integrity"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-boot-integrity-event-logs/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetPlatformBootIntegrityEventLogs.Output, [], name, value)


        class SystemBootIntegrity(_Entity_):
            """
            Boot integrity event logs
            
            .. attribute:: node_data
            
            	Boot integrity event logs of a node in a distributed system identified by the location
            	**type**\: list of  		 :py:class:`NodeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData>`
            
            

            """

            _prefix = 'sb-attest'
            _revision = '2017-06-08'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity, self).__init__()

                self.yang_name = "system-boot-integrity"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node-data", ("node_data", GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData))])
                self._leafs = OrderedDict()

                self.node_data = YList(self)
                self._segment_path = lambda: "system-boot-integrity"
                self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-boot-integrity-event-logs/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity, [], name, value)


            class NodeData(_Entity_):
                """
                Boot integrity event logs of a node in a distributed system
                identified by the location
                
                .. attribute:: node_location  (key)
                
                	Location of the node in the distributed system
                	**type**\: str
                
                .. attribute:: up_time
                
                	Uptime in seconds of this node reporting its data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: event_log
                
                	Ordered list of TCG described event log that extended the PCRs in the order they were logged
                	**type**\: list of  		 :py:class:`EventLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog>`
                
                

                """

                _prefix = 'sb-attest'
                _revision = '2017-06-08'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData, self).__init__()

                    self.yang_name = "node-data"
                    self.yang_parent_name = "system-boot-integrity"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([("event_log", ("event_log", GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog))])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('up_time', (YLeaf(YType.uint32, 'up-time'), ['int'])),
                    ])
                    self.node_location = None
                    self.up_time = None

                    self.event_log = YList(self)
                    self._segment_path = lambda: "node-data" + "[node-location='" + str(self.node_location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-boot-integrity-event-logs/output/system-boot-integrity/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData, ['node_location', 'up_time'], name, value)


                class EventLog(_Entity_):
                    """
                    Ordered list of TCG described event log
                    that extended the PCRs in the order they
                    were logged
                    
                    .. attribute:: event_number  (key)
                    
                    	Unique event number of this event
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_type
                    
                    	log event type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pcr_index
                    
                    	Defines the PCR index that this event extended
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: digest_list
                    
                    	Hash of event data
                    	**type**\: list of  		 :py:class:`DigestList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList>`
                    
                    .. attribute:: event_size
                    
                    	Size of the event data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_data
                    
                    	the event data size determined by event\-size
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'sb-attest'
                    _revision = '2017-06-08'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog, self).__init__()

                        self.yang_name = "event_log"
                        self.yang_parent_name = "node-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['event_number']
                        self._child_classes = OrderedDict([("digest-list", ("digest_list", GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList))])
                        self._leafs = OrderedDict([
                            ('event_number', (YLeaf(YType.uint32, 'event-number'), ['int'])),
                            ('event_type', (YLeaf(YType.uint32, 'event-type'), ['int'])),
                            ('pcr_index', (YLeaf(YType.uint16, 'pcr-index'), ['int'])),
                            ('event_size', (YLeaf(YType.uint32, 'event-size'), ['int'])),
                            ('event_data', (YLeaf(YType.str, 'event-data'), ['str'])),
                        ])
                        self.event_number = None
                        self.event_type = None
                        self.pcr_index = None
                        self.event_size = None
                        self.event_data = None

                        self.digest_list = YList(self)
                        self._segment_path = lambda: "event_log" + "[event-number='" + str(self.event_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog, ['event_number', 'event_type', 'pcr_index', 'event_size', 'event_data'], name, value)


                    class DigestList(_Entity_):
                        """
                        Hash of event data
                        
                        .. attribute:: digest_hash_algorithm  (key)
                        
                        	Algorithm for this digest
                        	**type**\:  :py:class:`DigestHashAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm>`
                        
                        .. attribute:: digest
                        
                        	The hash of the event data
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'sb-attest'
                        _revision = '2017-06-08'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList, self).__init__()

                            self.yang_name = "digest-list"
                            self.yang_parent_name = "event_log"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['digest_hash_algorithm']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('digest_hash_algorithm', (YLeaf(YType.enumeration, 'digest-hash-algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act', 'GetPlatformBootIntegrityEventLogs', 'Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm')])),
                                ('digest', (YLeaf(YType.str, 'digest'), ['str'])),
                            ])
                            self.digest_hash_algorithm = None
                            self.digest = None
                            self._segment_path = lambda: "digest-list" + "[digest-hash-algorithm='" + str(self.digest_hash_algorithm) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList, ['digest_hash_algorithm', 'digest'], name, value)

                        class DigestHashAlgorithm(Enum):
                            """
                            DigestHashAlgorithm (Enum Class)

                            Algorithm for this digest

                            .. data:: SHA1 = 0

                            .. data:: SHA256 = 1

                            .. data:: SHA384 = 2

                            .. data:: SHA512 = 3

                            """

                            SHA1 = Enum.YLeaf(0, "SHA1")

                            SHA256 = Enum.YLeaf(1, "SHA256")

                            SHA384 = Enum.YLeaf(2, "SHA384")

                            SHA512 = Enum.YLeaf(3, "SHA512")


                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                                return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList.DigestHashAlgorithm']


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                            return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog.DigestList']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                        return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData.EventLog']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                    return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity.NodeData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output.SystemBootIntegrity']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetPlatformBootIntegrityEventLogs.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = GetPlatformBootIntegrityEventLogs()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
        return meta._meta_table['GetPlatformBootIntegrityEventLogs']['meta_info']


class GetPlatformImaEventLogs(_Entity_):
    """
    Get platform IMA event logs
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformImaEventLogs.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformImaEventLogs.Output>`
    
    

    """

    _prefix = 'sb-attest'
    _revision = '2017-06-08'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(GetPlatformImaEventLogs, self).__init__()
        self._top_entity = None

        self.yang_name = "get-platform-ima-event-logs"
        self.yang_parent_name = "Cisco-IOS-XR-remote-attestation-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = GetPlatformImaEventLogs.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = GetPlatformImaEventLogs.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-ima-event-logs"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: location
        
        	In a distributed system get the data from a specific node identified by the location. If this field is not specified data associated with each node forming the system will be returned
        	**type**\: str
        
        .. attribute:: start_event_number
        
        	To filter event logs to be retrieved. \- If set only events with sequence number greater than that specified in this argument will be returned
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: end_event_number
        
        	To control event logs to be retrieved. \- If set only events with sequence number in the range of start\-event\-number to end\-event\-number will be returned
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetPlatformImaEventLogs.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-platform-ima-event-logs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('start_event_number', (YLeaf(YType.uint64, 'start-event-number'), ['int'])),
                ('end_event_number', (YLeaf(YType.uint64, 'end-event-number'), ['int'])),
            ])
            self.location = None
            self.start_event_number = None
            self.end_event_number = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-ima-event-logs/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetPlatformImaEventLogs.Input, ['location', 'start_event_number', 'end_event_number'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetPlatformImaEventLogs.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: system_ima
        
        	Runtime integrity measurement event logs
        	**type**\:  :py:class:`SystemIma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformImaEventLogs.Output.SystemIma>`
        
        

        """

        _prefix = 'sb-attest'
        _revision = '2017-06-08'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(GetPlatformImaEventLogs.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-platform-ima-event-logs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("system-ima", ("system_ima", GetPlatformImaEventLogs.Output.SystemIma))])
            self._leafs = OrderedDict()

            self.system_ima = GetPlatformImaEventLogs.Output.SystemIma()
            self.system_ima.parent = self
            self._children_name_map["system_ima"] = "system-ima"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-ima-event-logs/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GetPlatformImaEventLogs.Output, [], name, value)


        class SystemIma(_Entity_):
            """
            Runtime integrity measurement event logs
            
            .. attribute:: node_data
            
            	IMA event logs of a node in a distributed system identified by the location
            	**type**\: list of  		 :py:class:`NodeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformImaEventLogs.Output.SystemIma.NodeData>`
            
            

            """

            _prefix = 'sb-attest'
            _revision = '2017-06-08'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(GetPlatformImaEventLogs.Output.SystemIma, self).__init__()

                self.yang_name = "system-ima"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node-data", ("node_data", GetPlatformImaEventLogs.Output.SystemIma.NodeData))])
                self._leafs = OrderedDict()

                self.node_data = YList(self)
                self._segment_path = lambda: "system-ima"
                self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-ima-event-logs/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GetPlatformImaEventLogs.Output.SystemIma, [], name, value)


            class NodeData(_Entity_):
                """
                IMA event logs of a node in a distributed system
                identified by the location
                
                .. attribute:: node_location  (key)
                
                	Location of the node in the distributed system
                	**type**\: str
                
                .. attribute:: up_time
                
                	Uptime in seconds of this node reporting its data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ima_event_log
                
                	Ordered list of ima event logs by event\-number
                	**type**\: list of  		 :py:class:`ImaEventLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_remote_attestation_act.GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog>`
                
                

                """

                _prefix = 'sb-attest'
                _revision = '2017-06-08'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(GetPlatformImaEventLogs.Output.SystemIma.NodeData, self).__init__()

                    self.yang_name = "node-data"
                    self.yang_parent_name = "system-ima"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_location']
                    self._child_classes = OrderedDict([("ima-event-log", ("ima_event_log", GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog))])
                    self._leafs = OrderedDict([
                        ('node_location', (YLeaf(YType.str, 'node-location'), ['str'])),
                        ('up_time', (YLeaf(YType.uint32, 'up-time'), ['int'])),
                    ])
                    self.node_location = None
                    self.up_time = None

                    self.ima_event_log = YList(self)
                    self._segment_path = lambda: "node-data" + "[node-location='" + str(self.node_location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-remote-attestation-act:get-platform-ima-event-logs/output/system-ima/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GetPlatformImaEventLogs.Output.SystemIma.NodeData, ['node_location', 'up_time'], name, value)


                class ImaEventLog(_Entity_):
                    """
                    Ordered list of ima event logs by event\-number
                    
                    .. attribute:: event_number  (key)
                    
                    	Unique number for this event for sequencing
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ima_template
                    
                    	Name of the template used for event for e.g. ima, ima\-ng
                    	**type**\: str
                    
                    .. attribute:: filename_hint
                    
                    	File that was measured
                    	**type**\: str
                    
                    .. attribute:: filedata_hash
                    
                    	Hash of filedata
                    	**type**\: str
                    
                    .. attribute:: template_hash_algorithm
                    
                    	Algorithm used for template\-hash
                    	**type**\: str
                    
                    .. attribute:: template_hash
                    
                    	 hash(filedata\-hash, filename\-hint)
                    	**type**\: str
                    
                    .. attribute:: pcr_index
                    
                    	Defines the PCR index that this event extended
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: signature
                    
                    	The file signature
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'sb-attest'
                    _revision = '2017-06-08'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog, self).__init__()

                        self.yang_name = "ima-event-log"
                        self.yang_parent_name = "node-data"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['event_number']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('event_number', (YLeaf(YType.uint64, 'event-number'), ['int'])),
                            ('ima_template', (YLeaf(YType.str, 'ima-template'), ['str'])),
                            ('filename_hint', (YLeaf(YType.str, 'filename-hint'), ['str'])),
                            ('filedata_hash', (YLeaf(YType.str, 'filedata-hash'), ['str'])),
                            ('template_hash_algorithm', (YLeaf(YType.str, 'template-hash-algorithm'), ['str'])),
                            ('template_hash', (YLeaf(YType.str, 'template-hash'), ['str'])),
                            ('pcr_index', (YLeaf(YType.uint16, 'pcr-index'), ['int'])),
                            ('signature', (YLeaf(YType.str, 'signature'), ['str'])),
                        ])
                        self.event_number = None
                        self.ima_template = None
                        self.filename_hint = None
                        self.filedata_hash = None
                        self.template_hash_algorithm = None
                        self.template_hash = None
                        self.pcr_index = None
                        self.signature = None
                        self._segment_path = lambda: "ima-event-log" + "[event-number='" + str(self.event_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog, ['event_number', 'ima_template', 'filename_hint', 'filedata_hash', 'template_hash_algorithm', 'template_hash', 'pcr_index', 'signature'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                        return meta._meta_table['GetPlatformImaEventLogs.Output.SystemIma.NodeData.ImaEventLog']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                    return meta._meta_table['GetPlatformImaEventLogs.Output.SystemIma.NodeData']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
                return meta._meta_table['GetPlatformImaEventLogs.Output.SystemIma']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
            return meta._meta_table['GetPlatformImaEventLogs.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = GetPlatformImaEventLogs()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_remote_attestation_act as meta
        return meta._meta_table['GetPlatformImaEventLogs']['meta_info']


