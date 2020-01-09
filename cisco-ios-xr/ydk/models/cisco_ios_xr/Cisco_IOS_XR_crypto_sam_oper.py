""" Cisco_IOS_XR_crypto_sam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package operational data.

This module contains definitions
for the following management objects\:
  sam\: Software authentication manager certificate information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['CertificateIssuer']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogCode']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogError']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogTables']



class Sam(_Entity_):
    """
    Software authentication manager certificate
    information
    
    .. attribute:: system_information
    
    	SAM system information
    	**type**\:  :py:class:`SystemInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.SystemInformation>`
    
    	**config**\: False
    
    .. attribute:: log_contents
    
    	SAM log content table information
    	**type**\:  :py:class:`LogContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents>`
    
    	**config**\: False
    
    .. attribute:: devices
    
    	Certificate device table information
    	**type**\:  :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices>`
    
    	**config**\: False
    
    .. attribute:: packages
    
    	SAM certificate information  package
    	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages>`
    
    	**config**\: False
    
    .. attribute:: certificate_revocations
    
    	Certificate revocation list index table information
    	**type**\:  :py:class:`CertificateRevocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations>`
    
    	**config**\: False
    
    .. attribute:: certificate_revocation_list_summary
    
    	Certificate revocation list summary information 
    	**type**\:  :py:class:`CertificateRevocationListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary>`
    
    	**config**\: False
    
    

    """

    _prefix = 'crypto-sam-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class SystemInformation(_Entity_):
        """
        SAM system information
        
        .. attribute:: is_running
        
        	True if SAM status information runs
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: prompt_interval
        
        	Prompt interval atreboot time in seconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: second
        
        .. attribute:: is_default_response
        
        	True if promptdefault response is true
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._perform_setattr(Sam.SystemInformation, ['is_running', 'prompt_interval', 'is_default_response'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.SystemInformation']['meta_info']


    class LogContents(_Entity_):
        """
        SAM log content table information
        
        .. attribute:: log_content
        
        	Number of lines for SAM log message
        	**type**\: list of  		 :py:class:`LogContent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class LogContent(_Entity_):
            """
            Number of lines for SAM log message
            
            .. attribute:: number_of_lines  (key)
            
            	Number of lines
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: total_entries
            
            	Total log entries available
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: entries_shown
            
            	Total entries shown
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: logs
            
            	SAM logs
            	**type**\: list of  		 :py:class:`Logs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent.Logs>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(Sam.LogContents.LogContent, ['number_of_lines', 'total_entries', 'entries_shown'], name, value)


            class Logs(_Entity_):
                """
                SAM logs
                
                .. attribute:: time
                
                	Log time
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: code
                
                	Log code
                	**type**\:  :py:class:`LogCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogCode>`
                
                	**config**\: False
                
                .. attribute:: target_device
                
                	Target device
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: index
                
                	Device index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: error
                
                	Log error message
                	**type**\:  :py:class:`LogError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogError>`
                
                	**config**\: False
                
                .. attribute:: issuer
                
                	Issuer of the certificate
                	**type**\:  :py:class:`CertificateIssuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.CertificateIssuer>`
                
                	**config**\: False
                
                .. attribute:: serial_no
                
                	Serial number
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sam_table_index
                
                	SAM table index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: update_time
                
                	Last update time of the certificate
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: source_device
                
                	source device name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: table
                
                	Log table information
                	**type**\:  :py:class:`LogTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogTables>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Sam.LogContents.LogContent.Logs, ['time', 'code', 'target_device', 'index', 'error', 'issuer', 'serial_no', 'sam_table_index', 'update_time', 'source_device', 'table'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.LogContents.LogContent.Logs']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.LogContents.LogContent']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.LogContents']['meta_info']


    class Devices(_Entity_):
        """
        Certificate device table information
        
        .. attribute:: device
        
        	Certificate table device information
        	**type**\: list of  		 :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Device(_Entity_):
            """
            Certificate table device information
            
            .. attribute:: device_name  (key)
            
            	Specify device name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: certificate
            
            	Certificate table information
            	**type**\:  :py:class:`Certificate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Certificate(_Entity_):
                """
                Certificate table information
                
                .. attribute:: brief
                
                	Certificate table brief information
                	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief>`
                
                	**config**\: False
                
                .. attribute:: certificate_indexes
                
                	Certificate detail index table information
                	**type**\:  :py:class:`CertificateIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes>`
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Brief(_Entity_):
                    """
                    Certificate table brief information
                    
                    .. attribute:: certificate_flags
                    
                    	Certificate flags
                    	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.Brief.CertificateFlags>`
                    
                    	**config**\: False
                    
                    .. attribute:: location
                    
                    	Certificate location
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: certificate_index
                    
                    	Certificate index
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Sam.Devices.Device.Certificate.Brief, ['location', 'certificate_index'], name, value)


                    class CertificateFlags(_Entity_):
                        """
                        Certificate flags
                        
                        .. attribute:: is_trusted
                        
                        	Trusted flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_revoked
                        
                        	Revoked flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_expired
                        
                        	Expired flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_validated
                        
                        	Validated flag
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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
                            self._perform_setattr(Sam.Devices.Device.Certificate.Brief.CertificateFlags, ['is_trusted', 'is_revoked', 'is_expired', 'is_validated'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                            return meta._meta_table['Sam.Devices.Device.Certificate.Brief.CertificateFlags']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info']


                class CertificateIndexes(_Entity_):
                    """
                    Certificate detail index table information
                    
                    .. attribute:: certificate_index
                    
                    	Certificate detail index information
                    	**type**\: list of  		 :py:class:`CertificateIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class CertificateIndex(_Entity_):
                        """
                        Certificate detail index information
                        
                        .. attribute:: index  (key)
                        
                        	Specify certificate index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: detail
                        
                        	Certificate table detail information
                        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'crypto-sam-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Detail(_Entity_):
                            """
                            Certificate table detail information
                            
                            .. attribute:: certificate_flags
                            
                            	Certificate flags
                            	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags>`
                            
                            	**config**\: False
                            
                            .. attribute:: location
                            
                            	Certificate location
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: certificate_index
                            
                            	Certificate index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'crypto-sam-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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
                                self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, ['location', 'certificate_index'], name, value)


                            class CertificateFlags(_Entity_):
                                """
                                Certificate flags
                                
                                .. attribute:: is_trusted
                                
                                	Trusted flag
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_revoked
                                
                                	Revoked flag
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_expired
                                
                                	Expired flag
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: is_validated
                                
                                	Validated flag
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'crypto-sam-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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
                                    self._perform_setattr(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, ['is_trusted', 'is_revoked', 'is_expired', 'is_validated'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                                    return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                                return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                            return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.Devices.Device.Certificate']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.Devices.Device']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.Devices']['meta_info']


    class Packages(_Entity_):
        """
        SAM certificate information  package
        
        .. attribute:: package
        
        	SAM certificate information for a specific package
        	**type**\: list of  		 :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Package(_Entity_):
            """
            SAM certificate information for a specific
            package
            
            .. attribute:: package_name  (key)
            
            	Specify package name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: certificate_flags
            
            	Certificate flags
            	**type**\:  :py:class:`CertificateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package.CertificateFlags>`
            
            	**config**\: False
            
            .. attribute:: location
            
            	Certificate location
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: certificate_index
            
            	Certificate index
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(Sam.Packages.Package, ['package_name', 'location', 'certificate_index'], name, value)


            class CertificateFlags(_Entity_):
                """
                Certificate flags
                
                .. attribute:: is_trusted
                
                	Trusted flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_revoked
                
                	Revoked flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_expired
                
                	Expired flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_validated
                
                	Validated flag
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Sam.Packages.Package.CertificateFlags, ['is_trusted', 'is_revoked', 'is_expired', 'is_validated'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.Packages.Package.CertificateFlags']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.Packages.Package']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.Packages']['meta_info']


    class CertificateRevocations(_Entity_):
        """
        Certificate revocation list index table
        information
        
        .. attribute:: certificate_revocation
        
        	Certificate revocation list index information
        	**type**\: list of  		 :py:class:`CertificateRevocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation>`
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class CertificateRevocation(_Entity_):
            """
            Certificate revocation list index information
            
            .. attribute:: crl_index  (key)
            
            	CRL index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: certificate_revocation_list_detail
            
            	Certificate revocation list detail information
            	**type**\:  :py:class:`CertificateRevocationListDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class CertificateRevocationListDetail(_Entity_):
                """
                Certificate revocation list detail information
                
                .. attribute:: issuer
                
                	Issuer name
                	**type**\:  :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer>`
                
                	**config**\: False
                
                .. attribute:: crl_index
                
                	 CRL index
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: updates
                
                	Updated time of CRL is displayed
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'crypto-sam-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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
                    self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, ['crl_index', 'updates'], name, value)


                class Issuer(_Entity_):
                    """
                    Issuer name
                    
                    .. attribute:: common_name
                    
                    	Common name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: organization
                    
                    	Organization
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: country
                    
                    	Country
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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
                        self._perform_setattr(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, ['common_name', 'organization', 'country'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.CertificateRevocations']['meta_info']


    class CertificateRevocationListSummary(_Entity_):
        """
        Certificate revocation list summary information 
        
        .. attribute:: issuer
        
        	Issuer name
        	**type**\:  :py:class:`Issuer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.CertificateRevocationListSummary.Issuer>`
        
        	**config**\: False
        
        .. attribute:: crl_index
        
        	 CRL index
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: updates
        
        	Updated time of CRL is displayed
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._perform_setattr(Sam.CertificateRevocationListSummary, ['crl_index', 'updates'], name, value)


        class Issuer(_Entity_):
            """
            Issuer name
            
            .. attribute:: common_name
            
            	Common name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: organization
            
            	Organization
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: country
            
            	Country
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'crypto-sam-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                self._perform_setattr(Sam.CertificateRevocationListSummary.Issuer, ['common_name', 'organization', 'country'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.CertificateRevocationListSummary.Issuer']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.CertificateRevocationListSummary']['meta_info']

    def clone_ptr(self):
        self._top_entity = Sam()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['Sam']['meta_info']


