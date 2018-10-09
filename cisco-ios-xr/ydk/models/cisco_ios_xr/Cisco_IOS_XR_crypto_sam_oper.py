""" Cisco_IOS_XR_crypto_sam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package operational data.

This module contains definitions
for the following management objects\:
  sam\: Software authentication manager certificate information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CertificateIssuer(Enum):
    """
    CertificateIssuer (Enum Class)

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
    LogCode (Enum Class)

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
    LogError (Enum Class)

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
    LogTables (Enum Class)

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
    
    .. attribute:: system_information
    
    	SAM system information
    	**type**\:  :py:class:`SystemInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.SystemInformation>`
    
    .. attribute:: log_contents
    
    	SAM log content table information
    	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents>`
    
    .. attribute:: devices
    
    	Certificate device table information
    	**type**\:  :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices>`
    
    .. attribute:: packages
    
    	SAM certificate information  package
    	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages>`
    
    .. attribute:: certificate_revocations
    
    	Certificate revocation list index table information
    	**type**\:  :py:class:`CertificateRevocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations>`
    
    .. attribute:: certificate_revocation_list_summary
    
    	Certificate revocation list summary information 
    	**type**\:  :py:class:`CertificateRevocationListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary>`
    
    

    """

    _prefix = 'crypto-sam-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(Sam, self).__init__()
        self._top_entity = None

        self.yang_name = "sam"
        self.yang_parent_name = "Cisco-IOS-XR-crypto-sam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("system-information", ("system_information", Sam.SystemInformation)), ("log-contents", ("log_contents", Sam.LogContents)), ("devices", ("devices", Sam.Devices)), ("packages", ("packages", Sam.Packages)), ("certificate-revocations", ("certificate_revocations", Sam.CertificateRevocations)), ("certificate-revocation-list-summary", ("certificate_revocation_list_summary", Sam.CertificateRevocationListSummary))])
        self._leafs = OrderedDict()

        self.system_information = Sam.SystemInformation()
        self.system_information.parent = self
        self._children_name_map["system_information"] = "system-information"

        self.log_contents = Sam.LogContents()
        self.log_contents.parent = self
        self._children_name_map["log_contents"] = "log-contents"

        self.devices = Sam.Devices()
        self.devices.parent = self
        self._children_name_map["devices"] = "devices"

        self.packages = Sam.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"

        self.certificate_revocations = Sam.CertificateRevocations()
        self.certificate_revocations.parent = self
        self._children_name_map["certificate_revocations"] = "certificate-revocations"

        self.certificate_revocation_list_summary = Sam.CertificateRevocationListSummary()
        self.certificate_revocation_list_summary.parent = self
        self._children_name_map["certificate_revocation_list_summary"] = "certificate-revocation-list-summary"
        self._segment_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sam, [], name, value)


    class SystemInformation(Entity):
        """
        SAM system information
        
        .. attribute:: is_running
        
        	True if SAM status information runs
        	**type**\: bool
        
        .. attribute:: prompt_interval
        
        	Prompt interval atreboot time in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: is_default_response
        
        	True if promptdefault response is true
        	**type**\: bool
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.SystemInformation, self).__init__()

            self.yang_name = "system-information"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('is_running', (YLeaf(YType.boolean, 'is-running'), ['bool'])),
                ('prompt_interval', (YLeaf(YType.uint32, 'prompt-interval'), ['int'])),
                ('is_default_response', (YLeaf(YType.boolean, 'is-default-response'), ['bool'])),
            ])
            self.is_running = None
            self.prompt_interval = None
            self.is_default_response = None
            self._segment_path = lambda: "system-information"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.SystemInformation, [u'is_running', u'prompt_interval', u'is_default_response'], name, value)


    class LogContents(Entity):
        """
        SAM log content table information
        
        .. attribute:: log_content
        
        	Number of lines for SAM log message
        	**type**\: list of  		 :py:class:`LogContent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.LogContents, self).__init__()

            self.yang_name = "log-contents"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("log-content", ("log_content", Sam.LogContents.LogContent))])
            self._leafs = OrderedDict()

            self.log_content = YList(self)
            self._segment_path = lambda: "log-contents"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.LogContents, [], name, value)


        class LogContent(Entity):
            """
            Number of lines for SAM log message
            
            .. attribute:: number_of_lines  (key)
            
            	Number of lines
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_entries
            
            	Total log entries available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entries_shown
            
            	Total entries shown
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: logs
            
            	SAM logs
            	**type**\: list of  		 :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent.Logs>`
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sam.LogContents.LogContent, self).__init__()

                self.yang_name = "log-content"
                self.yang_parent_name = "log-contents"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['number_of_lines']
                self._child_classes = OrderedDict([("logs", ("logs", Sam.LogContents.LogContent.Logs))])
                self._leafs = OrderedDict([
                    ('number_of_lines', (YLeaf(YType.uint32, 'number-of-lines'), ['int'])),
                    ('total_entries', (YLeaf(YType.uint32, 'total-entries'), ['int'])),
                    ('entries_shown', (YLeaf(YType.uint32, 'entries-shown'), ['int'])),
                ])
                self.number_of_lines = None
                self.total_entries = None
                self.entries_shown = None

                self.logs = YList(self)
                self._segment_path = lambda: "log-content" + "[number-of-lines='" + str(self.number_of_lines) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/log-contents/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.LogContents.LogContent, ['number_of_lines', u'total_entries', u'entries_shown'], name, value)


            class Logs(Entity):
                """
                SAM logs
                
                .. attribute:: time
                
                	Log time
                	**type**\: str
                
                .. attribute:: code
                
                	Log code
                	**type**\:  :py:class:`LogCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogCode>`
                
                .. attribute:: target_device
                
                	Target device
                	**type**\: str
                
                .. attribute:: index
                
                	Device index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: error
                
                	Log error message
                	**type**\:  :py:class:`LogError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogError>`
                
                .. attribute:: issuer
                
                	Issuer of the certificate
                	**type**\:  :py:class:`CertificateIssuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.CertificateIssuer>`
                
                .. attribute:: serial_no
                
                	Serial number
                	**type**\: str
                
                .. attribute:: sam_table_index
                
                	SAM table index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_time
                
                	Last update time of the certificate
                	**type**\: str
                
                .. attribute:: source_device
                
                	source device name
                	**type**\: str
                
                .. attribute:: table
                
                	Log table information
                	**type**\:  :py:class:`LogTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogTables>`
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sam.LogContents.LogContent.Logs, self).__init__()

                    self.yang_name = "logs"
                    self.yang_parent_name = "log-content"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time', (YLeaf(YType.str, 'time'), ['str'])),
                        ('code', (YLeaf(YType.enumeration, 'code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogCode', '')])),
                        ('target_device', (YLeaf(YType.str, 'target-device'), ['str'])),
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('error', (YLeaf(YType.enumeration, 'error'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogError', '')])),
                        ('issuer', (YLeaf(YType.enumeration, 'issuer'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'CertificateIssuer', '')])),
                        ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                        ('sam_table_index', (YLeaf(YType.uint32, 'sam-table-index'), ['int'])),
                        ('update_time', (YLeaf(YType.str, 'update-time'), ['str'])),
                        ('source_device', (YLeaf(YType.str, 'source-device'), ['str'])),
                        ('table', (YLeaf(YType.enumeration, 'table'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper', 'LogTables', '')])),
                    ])
                    self.time = None
                    self.code = None
                    self.target_device = None
                    self.index = None
                    self.error = None
                    self.issuer = None
                    self.serial_no = None
                    self.sam_table_index = None
                    self.update_time = None
                    self.source_device = None
                    self.table = None
                    self._segment_path = lambda: "logs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.LogContents.LogContent.Logs, [u'time', u'code', u'target_device', u'index', u'error', u'issuer', u'serial_no', u'sam_table_index', u'update_time', u'source_device', u'table'], name, value)


    class Devices(Entity):
        """
        Certificate device table information
        
        .. attribute:: device
        
        	Certificate table device information
        	**type**\: list of  		 :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.Devices, self).__init__()

            self.yang_name = "devices"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("device", ("device", Sam.Devices.Device))])
            self._leafs = OrderedDict()

            self.device = YList(self)
            self._segment_path = lambda: "devices"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.Devices, [], name, value)


        class Device(Entity):
            """
            Certificate table device information
            
            .. attribute:: device_name  (key)
            
            	Specify device name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: certificate
            
            	Certificate table information
            	**type**\:  :py:class:`Certificate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate>`
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sam.Devices.Device, self).__init__()

                self.yang_name = "device"
                self.yang_parent_name = "devices"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['device_name']
                self._child_classes = OrderedDict([("certificate", ("certificate", Sam.Devices.Device.Certificate))])
                self._leafs = OrderedDict([
                    ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                ])
                self.device_name = None

                self.certificate = Sam.Devices.Device.Certificate()
                self.certificate.parent = self
                self._children_name_map["certificate"] = "certificate"
                self._segment_path = lambda: "device" + "[device-name='" + str(self.device_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/devices/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.Devices.Device, ['device_name'], name, value)


            class Certificate(Entity):
                """
                Certificate table information
                
                .. attribute:: brief
                
                	Certificate table brief information
                	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief>`
                
                .. attribute:: certificate_indexes
                
                	Certificate detail index table information
                	**type**\:  :py:class:`CertificateIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes>`
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sam.Devices.Device.Certificate, self).__init__()

                    self.yang_name = "certificate"
                    self.yang_parent_name = "device"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief", ("brief", Sam.Devices.Device.Certificate.Brief)), ("certificate-indexes", ("certificate_indexes", Sam.Devices.Device.Certificate.CertificateIndexes))])
                    self._leafs = OrderedDict()

                    self.brief = Sam.Devices.Device.Certificate.Brief()
                    self.brief.parent = self
                    self._children_name_map["brief"] = "brief"

                    self.certificate_indexes = Sam.Devices.Device.Certificate.CertificateIndexes()
                    self.certificate_indexes.parent = self
                    self._children_name_map["certificate_indexes"] = "certificate-indexes"
                    self._segment_path = lambda: "certificate"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.Devices.Device.Certificate, [], name, value)


                class Brief(Entity):
                    """
                    Certificate table brief information
                    
                    .. attribute:: certificate_flags
                    
                    	Certificate flags
                    	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief.CertificateFlags>`
                    
                    .. attribute:: location
                    
                    	Certificate location
                    	**type**\: str
                    
                    .. attribute:: certificate_index
                    
                    	Certificate index
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sam.Devices.Device.Certificate.Brief, self).__init__()

                        self.yang_name = "brief"
                        self.yang_parent_name = "certificate"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("certificate-flags", ("certificate_flags", Sam.Devices.Device.Certificate.Brief.CertificateFlags))])
                        self._leafs = OrderedDict([
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('certificate_index', (YLeaf(YType.uint16, 'certificate-index'), ['int'])),
                        ])
                        self.location = None
                        self.certificate_index = None

                        self.certificate_flags = Sam.Devices.Device.Certificate.Brief.CertificateFlags()
                        self.certificate_flags.parent = self
                        self._children_name_map["certificate_flags"] = "certificate-flags"
                        self._segment_path = lambda: "brief"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.Devices.Device.Certificate.Brief, [u'location', u'certificate_index'], name, value)


                    class CertificateFlags(Entity):
                        """
                        Certificate flags
                        
                        .. attribute:: is_trusted
                        
                        	Trusted flag
                        	**type**\: bool
                        
                        .. attribute:: is_revoked
                        
                        	Revoked flag
                        	**type**\: bool
                        
                        .. attribute:: is_expired
                        
                        	Expired flag
                        	**type**\: bool
                        
                        .. attribute:: is_validated
                        
                        	Validated flag
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Sam.Devices.Device.Certificate.Brief.CertificateFlags, self).__init__()

                            self.yang_name = "certificate-flags"
                            self.yang_parent_name = "brief"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('is_trusted', (YLeaf(YType.boolean, 'is-trusted'), ['bool'])),
                                ('is_revoked', (YLeaf(YType.boolean, 'is-revoked'), ['bool'])),
                                ('is_expired', (YLeaf(YType.boolean, 'is-expired'), ['bool'])),
                                ('is_validated', (YLeaf(YType.boolean, 'is-validated'), ['bool'])),
                            ])
                            self.is_trusted = None
                            self.is_revoked = None
                            self.is_expired = None
                            self.is_validated = None
                            self._segment_path = lambda: "certificate-flags"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sam.Devices.Device.Certificate.Brief.CertificateFlags, [u'is_trusted', u'is_revoked', u'is_expired', u'is_validated'], name, value)


                class CertificateIndexes(Entity):
                    """
                    Certificate detail index table information
                    
                    .. attribute:: certificate_index
                    
                    	Certificate detail index information
                    	**type**\: list of  		 :py:class:`CertificateIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex>`
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sam.Devices.Device.Certificate.CertificateIndexes, self).__init__()

                        self.yang_name = "certificate-indexes"
                        self.yang_parent_name = "certificate"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("certificate-index", ("certificate_index", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex))])
                        self._leafs = OrderedDict()

                        self.certificate_index = YList(self)
                        self._segment_path = lambda: "certificate-indexes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes, [], name, value)


                    class CertificateIndex(Entity):
                        """
                        Certificate detail index information
                        
                        .. attribute:: index  (key)
                        
                        	Specify certificate index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: detail
                        
                        	Certificate table detail information
                        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail>`
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, self).__init__()

                            self.yang_name = "certificate-index"
                            self.yang_parent_name = "certificate-indexes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index']
                            self._child_classes = OrderedDict([("detail", ("detail", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                            ])
                            self.index = None

                            self.detail = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail()
                            self.detail.parent = self
                            self._children_name_map["detail"] = "detail"
                            self._segment_path = lambda: "certificate-index" + "[index='" + str(self.index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, ['index'], name, value)


                        class Detail(Entity):
                            """
                            Certificate table detail information
                            
                            .. attribute:: certificate_flags
                            
                            	Certificate flags
                            	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags>`
                            
                            .. attribute:: location
                            
                            	Certificate location
                            	**type**\: str
                            
                            .. attribute:: certificate_index
                            
                            	Certificate index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'crypto-sam-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, self).__init__()

                                self.yang_name = "detail"
                                self.yang_parent_name = "certificate-index"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("certificate-flags", ("certificate_flags", Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags))])
                                self._leafs = OrderedDict([
                                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                                    ('certificate_index', (YLeaf(YType.uint16, 'certificate-index'), ['int'])),
                                ])
                                self.location = None
                                self.certificate_index = None

                                self.certificate_flags = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags()
                                self.certificate_flags.parent = self
                                self._children_name_map["certificate_flags"] = "certificate-flags"
                                self._segment_path = lambda: "detail"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, [u'location', u'certificate_index'], name, value)


                            class CertificateFlags(Entity):
                                """
                                Certificate flags
                                
                                .. attribute:: is_trusted
                                
                                	Trusted flag
                                	**type**\: bool
                                
                                .. attribute:: is_revoked
                                
                                	Revoked flag
                                	**type**\: bool
                                
                                .. attribute:: is_expired
                                
                                	Expired flag
                                	**type**\: bool
                                
                                .. attribute:: is_validated
                                
                                	Validated flag
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'crypto-sam-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, self).__init__()

                                    self.yang_name = "certificate-flags"
                                    self.yang_parent_name = "detail"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('is_trusted', (YLeaf(YType.boolean, 'is-trusted'), ['bool'])),
                                        ('is_revoked', (YLeaf(YType.boolean, 'is-revoked'), ['bool'])),
                                        ('is_expired', (YLeaf(YType.boolean, 'is-expired'), ['bool'])),
                                        ('is_validated', (YLeaf(YType.boolean, 'is-validated'), ['bool'])),
                                    ])
                                    self.is_trusted = None
                                    self.is_revoked = None
                                    self.is_expired = None
                                    self.is_validated = None
                                    self._segment_path = lambda: "certificate-flags"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, [u'is_trusted', u'is_revoked', u'is_expired', u'is_validated'], name, value)


    class Packages(Entity):
        """
        SAM certificate information  package
        
        .. attribute:: package
        
        	SAM certificate information for a specific package
        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("package", ("package", Sam.Packages.Package))])
            self._leafs = OrderedDict()

            self.package = YList(self)
            self._segment_path = lambda: "packages"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.Packages, [], name, value)


        class Package(Entity):
            """
            SAM certificate information for a specific
            package
            
            .. attribute:: package_name  (key)
            
            	Specify package name
            	**type**\: str
            
            .. attribute:: certificate_flags
            
            	Certificate flags
            	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package.CertificateFlags>`
            
            .. attribute:: location
            
            	Certificate location
            	**type**\: str
            
            .. attribute:: certificate_index
            
            	Certificate index
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sam.Packages.Package, self).__init__()

                self.yang_name = "package"
                self.yang_parent_name = "packages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['package_name']
                self._child_classes = OrderedDict([("certificate-flags", ("certificate_flags", Sam.Packages.Package.CertificateFlags))])
                self._leafs = OrderedDict([
                    ('package_name', (YLeaf(YType.str, 'package-name'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('certificate_index', (YLeaf(YType.uint16, 'certificate-index'), ['int'])),
                ])
                self.package_name = None
                self.location = None
                self.certificate_index = None

                self.certificate_flags = Sam.Packages.Package.CertificateFlags()
                self.certificate_flags.parent = self
                self._children_name_map["certificate_flags"] = "certificate-flags"
                self._segment_path = lambda: "package" + "[package-name='" + str(self.package_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/packages/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.Packages.Package, ['package_name', u'location', u'certificate_index'], name, value)


            class CertificateFlags(Entity):
                """
                Certificate flags
                
                .. attribute:: is_trusted
                
                	Trusted flag
                	**type**\: bool
                
                .. attribute:: is_revoked
                
                	Revoked flag
                	**type**\: bool
                
                .. attribute:: is_expired
                
                	Expired flag
                	**type**\: bool
                
                .. attribute:: is_validated
                
                	Validated flag
                	**type**\: bool
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sam.Packages.Package.CertificateFlags, self).__init__()

                    self.yang_name = "certificate-flags"
                    self.yang_parent_name = "package"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_trusted', (YLeaf(YType.boolean, 'is-trusted'), ['bool'])),
                        ('is_revoked', (YLeaf(YType.boolean, 'is-revoked'), ['bool'])),
                        ('is_expired', (YLeaf(YType.boolean, 'is-expired'), ['bool'])),
                        ('is_validated', (YLeaf(YType.boolean, 'is-validated'), ['bool'])),
                    ])
                    self.is_trusted = None
                    self.is_revoked = None
                    self.is_expired = None
                    self.is_validated = None
                    self._segment_path = lambda: "certificate-flags"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.Packages.Package.CertificateFlags, [u'is_trusted', u'is_revoked', u'is_expired', u'is_validated'], name, value)


    class CertificateRevocations(Entity):
        """
        Certificate revocation list index table
        information
        
        .. attribute:: certificate_revocation
        
        	Certificate revocation list index information
        	**type**\: list of  		 :py:class:`CertificateRevocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.CertificateRevocations, self).__init__()

            self.yang_name = "certificate-revocations"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("certificate-revocation", ("certificate_revocation", Sam.CertificateRevocations.CertificateRevocation))])
            self._leafs = OrderedDict()

            self.certificate_revocation = YList(self)
            self._segment_path = lambda: "certificate-revocations"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.CertificateRevocations, [], name, value)


        class CertificateRevocation(Entity):
            """
            Certificate revocation list index information
            
            .. attribute:: crl_index  (key)
            
            	CRL index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: certificate_revocation_list_detail
            
            	Certificate revocation list detail information
            	**type**\:  :py:class:`CertificateRevocationListDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail>`
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sam.CertificateRevocations.CertificateRevocation, self).__init__()

                self.yang_name = "certificate-revocation"
                self.yang_parent_name = "certificate-revocations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['crl_index']
                self._child_classes = OrderedDict([("certificate-revocation-list-detail", ("certificate_revocation_list_detail", Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail))])
                self._leafs = OrderedDict([
                    ('crl_index', (YLeaf(YType.uint32, 'crl-index'), ['int'])),
                ])
                self.crl_index = None

                self.certificate_revocation_list_detail = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail()
                self.certificate_revocation_list_detail.parent = self
                self._children_name_map["certificate_revocation_list_detail"] = "certificate-revocation-list-detail"
                self._segment_path = lambda: "certificate-revocation" + "[crl-index='" + str(self.crl_index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation, ['crl_index'], name, value)


            class CertificateRevocationListDetail(Entity):
                """
                Certificate revocation list detail information
                
                .. attribute:: issuer
                
                	Issuer name
                	**type**\:  :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer>`
                
                .. attribute:: crl_index
                
                	 CRL index
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: updates
                
                	Updated time of CRL is displayed
                	**type**\: str
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, self).__init__()

                    self.yang_name = "certificate-revocation-list-detail"
                    self.yang_parent_name = "certificate-revocation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("issuer", ("issuer", Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer))])
                    self._leafs = OrderedDict([
                        ('crl_index', (YLeaf(YType.uint16, 'crl-index'), ['int'])),
                        ('updates', (YLeaf(YType.str, 'updates'), ['str'])),
                    ])
                    self.crl_index = None
                    self.updates = None

                    self.issuer = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer()
                    self.issuer.parent = self
                    self._children_name_map["issuer"] = "issuer"
                    self._segment_path = lambda: "certificate-revocation-list-detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, [u'crl_index', u'updates'], name, value)


                class Issuer(Entity):
                    """
                    Issuer name
                    
                    .. attribute:: common_name
                    
                    	Common name
                    	**type**\: str
                    
                    .. attribute:: organization
                    
                    	Organization
                    	**type**\: str
                    
                    .. attribute:: country
                    
                    	Country
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, self).__init__()

                        self.yang_name = "issuer"
                        self.yang_parent_name = "certificate-revocation-list-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('common_name', (YLeaf(YType.str, 'common-name'), ['str'])),
                            ('organization', (YLeaf(YType.str, 'organization'), ['str'])),
                            ('country', (YLeaf(YType.str, 'country'), ['str'])),
                        ])
                        self.common_name = None
                        self.organization = None
                        self.country = None
                        self._segment_path = lambda: "issuer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, [u'common_name', u'organization', u'country'], name, value)


    class CertificateRevocationListSummary(Entity):
        """
        Certificate revocation list summary information 
        
        .. attribute:: issuer
        
        	Issuer name
        	**type**\:  :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary.Issuer>`
        
        .. attribute:: crl_index
        
        	 CRL index
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: updates
        
        	Updated time of CRL is displayed
        	**type**\: str
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Sam.CertificateRevocationListSummary, self).__init__()

            self.yang_name = "certificate-revocation-list-summary"
            self.yang_parent_name = "sam"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("issuer", ("issuer", Sam.CertificateRevocationListSummary.Issuer))])
            self._leafs = OrderedDict([
                ('crl_index', (YLeaf(YType.uint16, 'crl-index'), ['int'])),
                ('updates', (YLeaf(YType.str, 'updates'), ['str'])),
            ])
            self.crl_index = None
            self.updates = None

            self.issuer = Sam.CertificateRevocationListSummary.Issuer()
            self.issuer.parent = self
            self._children_name_map["issuer"] = "issuer"
            self._segment_path = lambda: "certificate-revocation-list-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sam.CertificateRevocationListSummary, [u'crl_index', u'updates'], name, value)


        class Issuer(Entity):
            """
            Issuer name
            
            .. attribute:: common_name
            
            	Common name
            	**type**\: str
            
            .. attribute:: organization
            
            	Organization
            	**type**\: str
            
            .. attribute:: country
            
            	Country
            	**type**\: str
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Sam.CertificateRevocationListSummary.Issuer, self).__init__()

                self.yang_name = "issuer"
                self.yang_parent_name = "certificate-revocation-list-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('common_name', (YLeaf(YType.str, 'common-name'), ['str'])),
                    ('organization', (YLeaf(YType.str, 'organization'), ['str'])),
                    ('country', (YLeaf(YType.str, 'country'), ['str'])),
                ])
                self.common_name = None
                self.organization = None
                self.country = None
                self._segment_path = lambda: "issuer"
                self._absolute_path = lambda: "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocation-list-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sam.CertificateRevocationListSummary.Issuer, [u'common_name', u'organization', u'country'], name, value)

    def clone_ptr(self):
        self._top_entity = Sam()
        return self._top_entity

