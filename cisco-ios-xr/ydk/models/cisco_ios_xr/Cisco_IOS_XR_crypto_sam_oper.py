""" Cisco_IOS_XR_crypto_sam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package operational data.

This module contains definitions
for the following management objects\:
  sam\: Software authentication manager certificate information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CertificateIssuer(Enum):
    """
    CertificateIssuer

    Certificate issuers

    .. data:: unknown = 0

    	Issuer is not known

    .. data:: code_signing_server_certificate_authority = 1

    	Issuer is code signing server certificate

    	authority

    """

    unknown = Enum.YLeaf(0, "unknown")

    code_signing_server_certificate_authority = Enum.YLeaf(1, "code-signing-server-certificate-authority")


class LogCode(Enum):
    """
    LogCode

    Log code types

    .. data:: unknown = 0

    	Log code is not known

    .. data:: sam_server_restared_router_reboot = 1

    	Log code is SAM server restarted through router

    	reboot

    .. data:: sam_server_restared = 2

    	Log code is SAM server restarted

    .. data:: added_certificate_in_table = 3

    	Log code is Added certificate in table

    .. data:: copied_certificate_in_table = 4

    	Log code is Copied certificate in table

    .. data:: certificate_flag_changed = 5

    	Log code is Certificate flag changed

    .. data:: validated_certificate = 6

    	Log code is validated ceritificate

    .. data:: certificate_expired_detected = 7

    	Log code is Ceritificate expired detected

    .. data:: certificate_revoked_detected = 8

    	Log code is Ceritificate revoked detected

    .. data:: ca_certificate_expired_detected = 9

    	Log code is CA Ceritificate expired detected

    .. data:: ca_certificate_revoked_detected = 10

    	Log code is CA Ceritificate revoked detected

    .. data:: deleted_certificate_from_table = 11

    	Log code is Deleted certificate from table

    .. data:: crl_added_updated_in_table = 12

    	Log code is CRL added/updated in table

    .. data:: checked_memory_digest = 13

    	Log code is Checked memory digest

    .. data:: nvram_digest_mismatch_detected = 14

    	Log code is NVRAM digest Mistmatch detected

    .. data:: insecure_backup_file_detected = 15

    	Log code is Insecure backup file detected

    .. data:: error_restore_operation = 16

    	Log code is Error during restore operation,

    	backup file might have not been intact

    .. data:: backup_file_on_nvram_deleted = 17

    	Log code is Found backup file on NVRAM for SAM

    	log had been deleted

    .. data:: sam_log_file_recovered_from_system_database = 18

    	Log code is SAM log backup file recovered from

    	system database

    .. data:: validated_elf = 19

    	Log code is validated ELF

    .. data:: namespace_deleted_recovered_by_sam = 20

    	Log code is SAM system database name space

    	deleted/recovered by SAM

    """

    unknown = Enum.YLeaf(0, "unknown")

    sam_server_restared_router_reboot = Enum.YLeaf(1, "sam-server-restared-router-reboot")

    sam_server_restared = Enum.YLeaf(2, "sam-server-restared")

    added_certificate_in_table = Enum.YLeaf(3, "added-certificate-in-table")

    copied_certificate_in_table = Enum.YLeaf(4, "copied-certificate-in-table")

    certificate_flag_changed = Enum.YLeaf(5, "certificate-flag-changed")

    validated_certificate = Enum.YLeaf(6, "validated-certificate")

    certificate_expired_detected = Enum.YLeaf(7, "certificate-expired-detected")

    certificate_revoked_detected = Enum.YLeaf(8, "certificate-revoked-detected")

    ca_certificate_expired_detected = Enum.YLeaf(9, "ca-certificate-expired-detected")

    ca_certificate_revoked_detected = Enum.YLeaf(10, "ca-certificate-revoked-detected")

    deleted_certificate_from_table = Enum.YLeaf(11, "deleted-certificate-from-table")

    crl_added_updated_in_table = Enum.YLeaf(12, "crl-added-updated-in-table")

    checked_memory_digest = Enum.YLeaf(13, "checked-memory-digest")

    nvram_digest_mismatch_detected = Enum.YLeaf(14, "nvram-digest-mismatch-detected")

    insecure_backup_file_detected = Enum.YLeaf(15, "insecure-backup-file-detected")

    error_restore_operation = Enum.YLeaf(16, "error-restore-operation")

    backup_file_on_nvram_deleted = Enum.YLeaf(17, "backup-file-on-nvram-deleted")

    sam_log_file_recovered_from_system_database = Enum.YLeaf(18, "sam-log-file-recovered-from-system-database")

    validated_elf = Enum.YLeaf(19, "validated-elf")

    namespace_deleted_recovered_by_sam = Enum.YLeaf(20, "namespace-deleted-recovered-by-sam")


class LogError(Enum):
    """
    LogError

    Log errors

    .. data:: unknown = 0

    	Log error is not known

    .. data:: log_message_error = 1

    	Log error is message error

    .. data:: get_issuer_name_failed = 2

    	Log error is get issuer name failed

    """

    unknown = Enum.YLeaf(0, "unknown")

    log_message_error = Enum.YLeaf(1, "log-message-error")

    get_issuer_name_failed = Enum.YLeaf(2, "get-issuer-name-failed")


class LogTables(Enum):
    """
    LogTables

    Log tables

    .. data:: unkown = 0

    	Table is not known

    .. data:: memory_digest_table = 1

    	Table is memory digest table

    .. data:: system_database_digest = 2

    	Table is system database digest table

    .. data:: sam_tables = 3

    	Table is SAM table

    """

    unkown = Enum.YLeaf(0, "unkown")

    memory_digest_table = Enum.YLeaf(1, "memory-digest-table")

    system_database_digest = Enum.YLeaf(2, "system-database-digest")

    sam_tables = Enum.YLeaf(3, "sam-tables")



class Sam(Entity):
    """
    Software authentication manager certificate
    information
    
    .. attribute:: certificate_revocation_list_summary
    
    	Certificate revocation list summary information 
    	**type**\:   :py:class:`CertificateRevocationListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary>`
    
    .. attribute:: certificate_revocations
    
    	Certificate revocation list index table information
    	**type**\:   :py:class:`CertificateRevocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations>`
    
    .. attribute:: devices
    
    	Certificate device table information
    	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices>`
    
    .. attribute:: log_contents
    
    	SAM log content table information
    	**type**\:   :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents>`
    
    .. attribute:: packages
    
    	SAM certificate information  package
    	**type**\:   :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages>`
    
    .. attribute:: system_information
    
    	SAM system information
    	**type**\:   :py:class:`SystemInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.SystemInformation>`
    
    

    """

    _prefix = 'crypto-sam-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Sam, self).__init__()
        self._top_entity = None

        self.yang_name = "sam"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-sam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"certificate-revocation-list-summary" : ("certificate_revocation_list_summary", Sam.CertificateRevocationListSummary), "certificate-revocations" : ("certificate_revocations", Sam.CertificateRevocations), "devices" : ("devices", Sam.Devices), "log-contents" : ("log_contents", Sam.LogContents), "packages" : ("packages", Sam.Packages), "system-information" : ("system_information", Sam.SystemInformation)}
        self._child_list_classes = {}

        self.certificate_revocation_list_summary = Sam.CertificateRevocationListSummary()
        self.certificate_revocation_list_summary.parent = self
        self._children_name_map["certificate_revocation_list_summary"] = "certificate-revocation-list-summary"
        self._children_yang_names.add("certificate-revocation-list-summary")

        self.certificate_revocations = Sam.CertificateRevocations()
        self.certificate_revocations.parent = self
        self._children_name_map["certificate_revocations"] = "certificate-revocations"
        self._children_yang_names.add("certificate-revocations")

        self.devices = Sam.Devices()
        self.devices.parent = self
        self._children_name_map["devices"] = "devices"
        self._children_yang_names.add("devices")

        self.log_contents = Sam.LogContents()
        self.log_contents.parent = self
        self._children_name_map["log_contents"] = "log-contents"
        self._children_yang_names.add("log-contents")

        self.packages = Sam.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"
        self._children_yang_names.add("packages")

        self.system_information = Sam.SystemInformation()
        self.system_information.parent = self
        self._children_name_map["system_information"] = "system-information"
        self._children_yang_names.add("system-information")
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam"


    class CertificateRevocationListSummary(Entity):
        """
        Certificate revocation list summary information 
        
        .. attribute:: crl_index
        
        	 CRL index
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: issuer
        
        	Issuer name
        	**type**\:   :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary.Issuer>`
        
        .. attribute:: updates
        
        	Updated time of CRL is displayed
        	**type**\:  str
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.CertificateRevocationListSummary, self).__init__()

            self.yang_name = "certificate-revocation-list-summary"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"issuer" : ("issuer", Sam.CertificateRevocationListSummary.Issuer)}
            self._child_list_classes = {}

            self.crl_index = YLeaf(YType.uint16, "crl-index")

            self.updates = YLeaf(YType.str, "updates")

            self.issuer = Sam.CertificateRevocationListSummary.Issuer()
            self.issuer.parent = self
            self._children_name_map["issuer"] = "issuer"
            self._children_yang_names.add("issuer")
            self._segment_path = lambda: "certificate-revocation-list-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.CertificateRevocationListSummary, ['crl_index', 'updates'], name, value)


        class Issuer(Entity):
            """
            Issuer name
            
            .. attribute:: common_name
            
            	Common name
            	**type**\:  str
            
            .. attribute:: country
            
            	Country
            	**type**\:  str
            
            .. attribute:: organization
            
            	Organization
            	**type**\:  str
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Sam.CertificateRevocationListSummary.Issuer, self).__init__()

                self.yang_name = "issuer"
                self.yang_parent_name = "certificate-revocation-list-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.common_name = YLeaf(YType.str, "common-name")

                self.country = YLeaf(YType.str, "country")

                self.organization = YLeaf(YType.str, "organization")
                self._segment_path = lambda: "issuer"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocation-list-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.CertificateRevocationListSummary.Issuer, ['common_name', 'country', 'organization'], name, value)


    class CertificateRevocations(Entity):
        """
        Certificate revocation list index table
        information
        
        .. attribute:: certificate_revocation
        
        	Certificate revocation list index information
        	**type**\: list of    :py:class:`CertificateRevocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.CertificateRevocations, self).__init__()

            self.yang_name = "certificate-revocations"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"certificate-revocation" : ("certificate_revocation", Sam.CertificateRevocations.CertificateRevocation)}

            self.certificate_revocation = YList(self)
            self._segment_path = lambda: "certificate-revocations"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.CertificateRevocations, [], name, value)


        class CertificateRevocation(Entity):
            """
            Certificate revocation list index information
            
            .. attribute:: crl_index  <key>
            
            	CRL index
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: certificate_revocation_list_detail
            
            	Certificate revocation list detail information
            	**type**\:   :py:class:`CertificateRevocationListDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail>`
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Sam.CertificateRevocations.CertificateRevocation, self).__init__()

                self.yang_name = "certificate-revocation"
                self.yang_parent_name = "certificate-revocations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"certificate-revocation-list-detail" : ("certificate_revocation_list_detail", Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail)}
                self._child_list_classes = {}

                self.crl_index = YLeaf(YType.int32, "crl-index")

                self.certificate_revocation_list_detail = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail()
                self.certificate_revocation_list_detail.parent = self
                self._children_name_map["certificate_revocation_list_detail"] = "certificate-revocation-list-detail"
                self._children_yang_names.add("certificate-revocation-list-detail")
                self._segment_path = lambda: "certificate-revocation" + "[crl-index='" + self.crl_index.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation, ['crl_index'], name, value)


            class CertificateRevocationListDetail(Entity):
                """
                Certificate revocation list detail information
                
                .. attribute:: crl_index
                
                	 CRL index
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: issuer
                
                	Issuer name
                	**type**\:   :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer>`
                
                .. attribute:: updates
                
                	Updated time of CRL is displayed
                	**type**\:  str
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, self).__init__()

                    self.yang_name = "certificate-revocation-list-detail"
                    self.yang_parent_name = "certificate-revocation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"issuer" : ("issuer", Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer)}
                    self._child_list_classes = {}

                    self.crl_index = YLeaf(YType.uint16, "crl-index")

                    self.updates = YLeaf(YType.str, "updates")

                    self.issuer = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer()
                    self.issuer.parent = self
                    self._children_name_map["issuer"] = "issuer"
                    self._children_yang_names.add("issuer")
                    self._segment_path = lambda: "certificate-revocation-list-detail"

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, ['crl_index', 'updates'], name, value)


                class Issuer(Entity):
                    """
                    Issuer name
                    
                    .. attribute:: common_name
                    
                    	Common name
                    	**type**\:  str
                    
                    .. attribute:: country
                    
                    	Country
                    	**type**\:  str
                    
                    .. attribute:: organization
                    
                    	Organization
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, self).__init__()

                        self.yang_name = "issuer"
                        self.yang_parent_name = "certificate-revocation-list-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.common_name = YLeaf(YType.str, "common-name")

                        self.country = YLeaf(YType.str, "country")

                        self.organization = YLeaf(YType.str, "organization")
                        self._segment_path = lambda: "issuer"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, ['common_name', 'country', 'organization'], name, value)


    class Devices(Entity):
        """
        Certificate device table information
        
        .. attribute:: device
        
        	Certificate table device information
        	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.Devices, self).__init__()

            self.yang_name = "devices"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"device" : ("device", Sam.Devices.Device)}

            self.device = YList(self)
            self._segment_path = lambda: "devices"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.Devices, [], name, value)


        class Device(Entity):
            """
            Certificate table device information
            
            .. attribute:: device_name  <key>
            
            	Specify device name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: certificate
            
            	Certificate table information
            	**type**\:   :py:class:`Certificate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate>`
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Sam.Devices.Device, self).__init__()

                self.yang_name = "device"
                self.yang_parent_name = "devices"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"certificate" : ("certificate", Sam.Devices.Device.Certificate)}
                self._child_list_classes = {}

                self.device_name = YLeaf(YType.str, "device-name")

                self.certificate = Sam.Devices.Device.Certificate()
                self.certificate.parent = self
                self._children_name_map["certificate"] = "certificate"
                self._children_yang_names.add("certificate")
                self._segment_path = lambda: "device" + "[device-name='" + self.device_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/devices/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.Devices.Device, ['device_name'], name, value)


            class Certificate(Entity):
                """
                Certificate table information
                
                .. attribute:: brief
                
                	Certificate table brief information
                	**type**\:   :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief>`
                
                .. attribute:: certificate_indexes
                
                	Certificate detail index table information
                	**type**\:   :py:class:`CertificateIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes>`
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Sam.Devices.Device.Certificate, self).__init__()

                    self.yang_name = "certificate"
                    self.yang_parent_name = "device"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"brief" : ("brief", Sam.Devices.Device.Certificate.Brief), "certificate-indexes" : ("certificate_indexes", Sam.Devices.Device.Certificate.CertificateIndexes)}
                    self._child_list_classes = {}

                    self.brief = Sam.Devices.Device.Certificate.Brief()
                    self.brief.parent = self
                    self._children_name_map["brief"] = "brief"
                    self._children_yang_names.add("brief")

                    self.certificate_indexes = Sam.Devices.Device.Certificate.CertificateIndexes()
                    self.certificate_indexes.parent = self
                    self._children_name_map["certificate_indexes"] = "certificate-indexes"
                    self._children_yang_names.add("certificate-indexes")
                    self._segment_path = lambda: "certificate"


                class Brief(Entity):
                    """
                    Certificate table brief information
                    
                    .. attribute:: certificate_flags
                    
                    	Certificate flags
                    	**type**\:   :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief.CertificateFlags>`
                    
                    .. attribute:: certificate_index
                    
                    	Certificate index
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: location
                    
                    	Certificate location
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Sam.Devices.Device.Certificate.Brief, self).__init__()

                        self.yang_name = "brief"
                        self.yang_parent_name = "certificate"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"certificate-flags" : ("certificate_flags", Sam.Devices.Device.Certificate.Brief.CertificateFlags)}
                        self._child_list_classes = {}

                        self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                        self.location = YLeaf(YType.str, "location")

                        self.certificate_flags = Sam.Devices.Device.Certificate.Brief.CertificateFlags()
                        self.certificate_flags.parent = self
                        self._children_name_map["certificate_flags"] = "certificate-flags"
                        self._children_yang_names.add("certificate-flags")
                        self._segment_path = lambda: "brief"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.Devices.Device.Certificate.Brief, ['certificate_index', 'location'], name, value)


                    class CertificateFlags(Entity):
                        """
                        Certificate flags
                        
                        .. attribute:: is_expired
                        
                        	Expired flag
                        	**type**\:  bool
                        
                        .. attribute:: is_revoked
                        
                        	Revoked flag
                        	**type**\:  bool
                        
                        .. attribute:: is_trusted
                        
                        	Trusted flag
                        	**type**\:  bool
                        
                        .. attribute:: is_validated
                        
                        	Validated flag
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Sam.Devices.Device.Certificate.Brief.CertificateFlags, self).__init__()

                            self.yang_name = "certificate-flags"
                            self.yang_parent_name = "brief"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.is_expired = YLeaf(YType.boolean, "is-expired")

                            self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                            self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                            self.is_validated = YLeaf(YType.boolean, "is-validated")
                            self._segment_path = lambda: "certificate-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sam.Devices.Device.Certificate.Brief.CertificateFlags, ['is_expired', 'is_revoked', 'is_trusted', 'is_validated'], name, value)


                class CertificateIndexes(Entity):
                    """
                    Certificate detail index table information
                    
                    .. attribute:: certificate_index
                    
                    	Certificate detail index information
                    	**type**\: list of    :py:class:`CertificateIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex>`
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(Sam.Devices.Device.Certificate.CertificateIndexes, self).__init__()

                        self.yang_name = "certificate-indexes"
                        self.yang_parent_name = "certificate"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"certificate-index" : ("certificate_index", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex)}

                        self.certificate_index = YList(self)
                        self._segment_path = lambda: "certificate-indexes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes, [], name, value)


                    class CertificateIndex(Entity):
                        """
                        Certificate detail index information
                        
                        .. attribute:: index  <key>
                        
                        	Specify certificate index
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: detail
                        
                        	Certificate table detail information
                        	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail>`
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, self).__init__()

                            self.yang_name = "certificate-index"
                            self.yang_parent_name = "certificate-indexes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"detail" : ("detail", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail)}
                            self._child_list_classes = {}

                            self.index = YLeaf(YType.int32, "index")

                            self.detail = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail()
                            self.detail.parent = self
                            self._children_name_map["detail"] = "detail"
                            self._children_yang_names.add("detail")
                            self._segment_path = lambda: "certificate-index" + "[index='" + self.index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, ['index'], name, value)


                        class Detail(Entity):
                            """
                            Certificate table detail information
                            
                            .. attribute:: certificate_flags
                            
                            	Certificate flags
                            	**type**\:   :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags>`
                            
                            .. attribute:: certificate_index
                            
                            	Certificate index
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: location
                            
                            	Certificate location
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'crypto-sam-oper'
                            _revision = '2015-01-07'

                            def __init__(self):
                                super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, self).__init__()

                                self.yang_name = "detail"
                                self.yang_parent_name = "certificate-index"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"certificate-flags" : ("certificate_flags", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags)}
                                self._child_list_classes = {}

                                self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                                self.location = YLeaf(YType.str, "location")

                                self.certificate_flags = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags()
                                self.certificate_flags.parent = self
                                self._children_name_map["certificate_flags"] = "certificate-flags"
                                self._children_yang_names.add("certificate-flags")
                                self._segment_path = lambda: "detail"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, ['certificate_index', 'location'], name, value)


                            class CertificateFlags(Entity):
                                """
                                Certificate flags
                                
                                .. attribute:: is_expired
                                
                                	Expired flag
                                	**type**\:  bool
                                
                                .. attribute:: is_revoked
                                
                                	Revoked flag
                                	**type**\:  bool
                                
                                .. attribute:: is_trusted
                                
                                	Trusted flag
                                	**type**\:  bool
                                
                                .. attribute:: is_validated
                                
                                	Validated flag
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'crypto-sam-oper'
                                _revision = '2015-01-07'

                                def __init__(self):
                                    super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, self).__init__()

                                    self.yang_name = "certificate-flags"
                                    self.yang_parent_name = "detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.is_expired = YLeaf(YType.boolean, "is-expired")

                                    self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                                    self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                                    self.is_validated = YLeaf(YType.boolean, "is-validated")
                                    self._segment_path = lambda: "certificate-flags"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, ['is_expired', 'is_revoked', 'is_trusted', 'is_validated'], name, value)


    class LogContents(Entity):
        """
        SAM log content table information
        
        .. attribute:: log_content
        
        	Number of lines for SAM log message
        	**type**\: list of    :py:class:`LogContent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.LogContents, self).__init__()

            self.yang_name = "log-contents"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"log-content" : ("log_content", Sam.LogContents.LogContent)}

            self.log_content = YList(self)
            self._segment_path = lambda: "log-contents"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.LogContents, [], name, value)


        class LogContent(Entity):
            """
            Number of lines for SAM log message
            
            .. attribute:: number_of_lines  <key>
            
            	Number of lines
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: entries_shown
            
            	Total entries shown
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: logs
            
            	SAM logs
            	**type**\: list of    :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent.Logs>`
            
            .. attribute:: total_entries
            
            	Total log entries available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Sam.LogContents.LogContent, self).__init__()

                self.yang_name = "log-content"
                self.yang_parent_name = "log-contents"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"logs" : ("logs", Sam.LogContents.LogContent.Logs)}

                self.number_of_lines = YLeaf(YType.int32, "number-of-lines")

                self.entries_shown = YLeaf(YType.uint32, "entries-shown")

                self.total_entries = YLeaf(YType.uint32, "total-entries")

                self.logs = YList(self)
                self._segment_path = lambda: "log-content" + "[number-of-lines='" + self.number_of_lines.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/log-contents/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.LogContents.LogContent, ['number_of_lines', 'entries_shown', 'total_entries'], name, value)


            class Logs(Entity):
                """
                SAM logs
                
                .. attribute:: code
                
                	Log code
                	**type**\:   :py:class:`LogCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogCode>`
                
                .. attribute:: error
                
                	Log error message
                	**type**\:   :py:class:`LogError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogError>`
                
                .. attribute:: index
                
                	Device index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: issuer
                
                	Issuer of the certificate
                	**type**\:   :py:class:`CertificateIssuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.CertificateIssuer>`
                
                .. attribute:: sam_table_index
                
                	SAM table index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: serial_no
                
                	Serial number
                	**type**\:  str
                
                .. attribute:: source_device
                
                	source device name
                	**type**\:  str
                
                .. attribute:: table
                
                	Log table information
                	**type**\:   :py:class:`LogTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogTables>`
                
                .. attribute:: target_device
                
                	Target device
                	**type**\:  str
                
                .. attribute:: time
                
                	Log time
                	**type**\:  str
                
                .. attribute:: update_time
                
                	Last update time of the certificate
                	**type**\:  str
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Sam.LogContents.LogContent.Logs, self).__init__()

                    self.yang_name = "logs"
                    self.yang_parent_name = "log-content"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.code = YLeaf(YType.enumeration, "code")

                    self.error = YLeaf(YType.enumeration, "error")

                    self.index = YLeaf(YType.uint32, "index")

                    self.issuer = YLeaf(YType.enumeration, "issuer")

                    self.sam_table_index = YLeaf(YType.uint32, "sam-table-index")

                    self.serial_no = YLeaf(YType.str, "serial-no")

                    self.source_device = YLeaf(YType.str, "source-device")

                    self.table = YLeaf(YType.enumeration, "table")

                    self.target_device = YLeaf(YType.str, "target-device")

                    self.time = YLeaf(YType.str, "time")

                    self.update_time = YLeaf(YType.str, "update-time")
                    self._segment_path = lambda: "logs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.LogContents.LogContent.Logs, ['code', 'error', 'index', 'issuer', 'sam_table_index', 'serial_no', 'source_device', 'table', 'target_device', 'time', 'update_time'], name, value)


    class Packages(Entity):
        """
        SAM certificate information  package
        
        .. attribute:: package
        
        	SAM certificate information for a specific package
        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"package" : ("package", Sam.Packages.Package)}

            self.package = YList(self)
            self._segment_path = lambda: "packages"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.Packages, [], name, value)


        class Package(Entity):
            """
            SAM certificate information for a specific
            package
            
            .. attribute:: package_name  <key>
            
            	Specify package name
            	**type**\:  str
            
            .. attribute:: certificate_flags
            
            	Certificate flags
            	**type**\:   :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package.CertificateFlags>`
            
            .. attribute:: certificate_index
            
            	Certificate index
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: location
            
            	Certificate location
            	**type**\:  str
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(Sam.Packages.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "packages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"certificate-flags" : ("certificate_flags", Sam.Packages.Package.CertificateFlags)}
                self._child_list_classes = {}

                self.package_name = YLeaf(YType.str, "package-name")

                self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                self.location = YLeaf(YType.str, "location")

                self.certificate_flags = Sam.Packages.Package.CertificateFlags()
                self.certificate_flags.parent = self
                self._children_name_map["certificate_flags"] = "certificate-flags"
                self._children_yang_names.add("certificate-flags")
                self._segment_path = lambda: "package" + "[package-name='" + self.package_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/packages/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.Packages.Package, ['package_name', 'certificate_index', 'location'], name, value)


            class CertificateFlags(Entity):
                """
                Certificate flags
                
                .. attribute:: is_expired
                
                	Expired flag
                	**type**\:  bool
                
                .. attribute:: is_revoked
                
                	Revoked flag
                	**type**\:  bool
                
                .. attribute:: is_trusted
                
                	Trusted flag
                	**type**\:  bool
                
                .. attribute:: is_validated
                
                	Validated flag
                	**type**\:  bool
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(Sam.Packages.Package.CertificateFlags, self).__init__()

                    self.yang_name = "certificate-flags"
                    self.yang_parent_name = "package"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.is_expired = YLeaf(YType.boolean, "is-expired")

                    self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                    self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                    self.is_validated = YLeaf(YType.boolean, "is-validated")
                    self._segment_path = lambda: "certificate-flags"

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.Packages.Package.CertificateFlags, ['is_expired', 'is_revoked', 'is_trusted', 'is_validated'], name, value)


    class SystemInformation(Entity):
        """
        SAM system information
        
        .. attribute:: is_default_response
        
        	True if promptdefault response is true
        	**type**\:  bool
        
        .. attribute:: is_running
        
        	True if SAM status information runs
        	**type**\:  bool
        
        .. attribute:: prompt_interval
        
        	Prompt interval atreboot time in seconds
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(Sam.SystemInformation, self).__init__()

            self.yang_name = "system-information"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.is_default_response = YLeaf(YType.boolean, "is-default-response")

            self.is_running = YLeaf(YType.boolean, "is-running")

            self.prompt_interval = YLeaf(YType.uint32, "prompt-interval")
            self._segment_path = lambda: "system-information"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.SystemInformation, ['is_default_response', 'is_running', 'prompt_interval'], name, value)

    def clone_ptr(self):
        self._top_entity = Sam()
        return self._top_entity

