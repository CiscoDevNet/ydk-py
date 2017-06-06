""" Cisco_IOS_XR_crypto_sam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package operational data.

This module contains definitions
for the following management objects\:
  sam\: Software authentication manager certificate information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CertificateIssuerEnum(Enum):
    """
    CertificateIssuerEnum

    Certificate issuers

    .. data:: unknown = 0

    	Issuer is not known

    .. data:: code_signing_server_certificate_authority = 1

    	Issuer is code signing server certificate

    	authority

    """

    unknown = 0

    code_signing_server_certificate_authority = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['CertificateIssuerEnum']


class LogCodeEnum(Enum):
    """
    LogCodeEnum

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

    unknown = 0

    sam_server_restared_router_reboot = 1

    sam_server_restared = 2

    added_certificate_in_table = 3

    copied_certificate_in_table = 4

    certificate_flag_changed = 5

    validated_certificate = 6

    certificate_expired_detected = 7

    certificate_revoked_detected = 8

    ca_certificate_expired_detected = 9

    ca_certificate_revoked_detected = 10

    deleted_certificate_from_table = 11

    crl_added_updated_in_table = 12

    checked_memory_digest = 13

    nvram_digest_mismatch_detected = 14

    insecure_backup_file_detected = 15

    error_restore_operation = 16

    backup_file_on_nvram_deleted = 17

    sam_log_file_recovered_from_system_database = 18

    validated_elf = 19

    namespace_deleted_recovered_by_sam = 20


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogCodeEnum']


class LogErrorEnum(Enum):
    """
    LogErrorEnum

    Log errors

    .. data:: unknown = 0

    	Log error is not known

    .. data:: log_message_error = 1

    	Log error is message error

    .. data:: get_issuer_name_failed = 2

    	Log error is get issuer name failed

    """

    unknown = 0

    log_message_error = 1

    get_issuer_name_failed = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogErrorEnum']


class LogTablesEnum(Enum):
    """
    LogTablesEnum

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

    unkown = 0

    memory_digest_table = 1

    system_database_digest = 2

    sam_tables = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['LogTablesEnum']



class Sam(object):
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
        self.certificate_revocation_list_summary = Sam.CertificateRevocationListSummary()
        self.certificate_revocation_list_summary.parent = self
        self.certificate_revocations = Sam.CertificateRevocations()
        self.certificate_revocations.parent = self
        self.devices = Sam.Devices()
        self.devices.parent = self
        self.log_contents = Sam.LogContents()
        self.log_contents.parent = self
        self.packages = Sam.Packages()
        self.packages.parent = self
        self.system_information = Sam.SystemInformation()
        self.system_information.parent = self


    class SystemInformation(object):
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
            self.parent = None
            self.is_default_response = None
            self.is_running = None
            self.prompt_interval = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:system-information'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.is_default_response is not None:
                return True

            if self.is_running is not None:
                return True

            if self.prompt_interval is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.SystemInformation']['meta_info']


    class LogContents(object):
        """
        SAM log content table information
        
        .. attribute:: log_content
        
        	Number of lines for SAM log message
        	**type**\: list of    :py:class:`LogContent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.LogContents.LogContent>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.log_content = YList()
            self.log_content.parent = self
            self.log_content.name = 'log_content'


        class LogContent(object):
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
                self.parent = None
                self.number_of_lines = None
                self.entries_shown = None
                self.logs = YList()
                self.logs.parent = self
                self.logs.name = 'logs'
                self.total_entries = None


            class Logs(object):
                """
                SAM logs
                
                .. attribute:: code
                
                	Log code
                	**type**\:   :py:class:`LogCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogCodeEnum>`
                
                .. attribute:: error
                
                	Log error message
                	**type**\:   :py:class:`LogErrorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogErrorEnum>`
                
                .. attribute:: index
                
                	Device index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: issuer
                
                	Issuer of the certificate
                	**type**\:   :py:class:`CertificateIssuerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.CertificateIssuerEnum>`
                
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
                	**type**\:   :py:class:`LogTablesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.LogTablesEnum>`
                
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
                    self.parent = None
                    self.code = None
                    self.error = None
                    self.index = None
                    self.issuer = None
                    self.sam_table_index = None
                    self.serial_no = None
                    self.source_device = None
                    self.table = None
                    self.target_device = None
                    self.time = None
                    self.update_time = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:logs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.code is not None:
                        return True

                    if self.error is not None:
                        return True

                    if self.index is not None:
                        return True

                    if self.issuer is not None:
                        return True

                    if self.sam_table_index is not None:
                        return True

                    if self.serial_no is not None:
                        return True

                    if self.source_device is not None:
                        return True

                    if self.table is not None:
                        return True

                    if self.target_device is not None:
                        return True

                    if self.time is not None:
                        return True

                    if self.update_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.LogContents.LogContent.Logs']['meta_info']

            @property
            def _common_path(self):
                if self.number_of_lines is None:
                    raise YPYModelError('Key property number_of_lines is None')

                return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:log-contents/Cisco-IOS-XR-crypto-sam-oper:log-content[Cisco-IOS-XR-crypto-sam-oper:number-of-lines = ' + str(self.number_of_lines) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.number_of_lines is not None:
                    return True

                if self.entries_shown is not None:
                    return True

                if self.logs is not None:
                    for child_ref in self.logs:
                        if child_ref._has_data():
                            return True

                if self.total_entries is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.LogContents.LogContent']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:log-contents'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.log_content is not None:
                for child_ref in self.log_content:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.LogContents']['meta_info']


    class Devices(object):
        """
        Certificate device table information
        
        .. attribute:: device
        
        	Certificate table device information
        	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.device = YList()
            self.device.parent = self
            self.device.name = 'device'


        class Device(object):
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
                self.parent = None
                self.device_name = None
                self.certificate = Sam.Devices.Device.Certificate()
                self.certificate.parent = self


            class Certificate(object):
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
                    self.parent = None
                    self.brief = Sam.Devices.Device.Certificate.Brief()
                    self.brief.parent = self
                    self.certificate_indexes = Sam.Devices.Device.Certificate.CertificateIndexes()
                    self.certificate_indexes.parent = self


                class Brief(object):
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
                        self.parent = None
                        self.certificate_flags = Sam.Devices.Device.Certificate.Brief.CertificateFlags()
                        self.certificate_flags.parent = self
                        self.certificate_index = None
                        self.location = None


                    class CertificateFlags(object):
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
                            self.parent = None
                            self.is_expired = None
                            self.is_revoked = None
                            self.is_trusted = None
                            self.is_validated = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.is_expired is not None:
                                return True

                            if self.is_revoked is not None:
                                return True

                            if self.is_trusted is not None:
                                return True

                            if self.is_validated is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                            return meta._meta_table['Sam.Devices.Device.Certificate.Brief.CertificateFlags']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:brief'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.certificate_flags is not None and self.certificate_flags._has_data():
                            return True

                        if self.certificate_index is not None:
                            return True

                        if self.location is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.Devices.Device.Certificate.Brief']['meta_info']


                class CertificateIndexes(object):
                    """
                    Certificate detail index table information
                    
                    .. attribute:: certificate_index
                    
                    	Certificate detail index information
                    	**type**\: list of    :py:class:`CertificateIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex>`
                    
                    

                    """

                    _prefix = 'crypto-sam-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.certificate_index = YList()
                        self.certificate_index.parent = self
                        self.certificate_index.name = 'certificate_index'


                    class CertificateIndex(object):
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
                            self.parent = None
                            self.index = None
                            self.detail = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail()
                            self.detail.parent = self


                        class Detail(object):
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
                                self.parent = None
                                self.certificate_flags = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags()
                                self.certificate_flags.parent = self
                                self.certificate_index = None
                                self.location = None


                            class CertificateFlags(object):
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
                                    self.parent = None
                                    self.is_expired = None
                                    self.is_revoked = None
                                    self.is_trusted = None
                                    self.is_validated = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-flags'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_expired is not None:
                                        return True

                                    if self.is_revoked is not None:
                                        return True

                                    if self.is_trusted is not None:
                                        return True

                                    if self.is_validated is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                                    return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:detail'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.certificate_flags is not None and self.certificate_flags._has_data():
                                    return True

                                if self.certificate_index is not None:
                                    return True

                                if self.location is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                                return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index is None:
                                raise YPYModelError('Key property index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-index[Cisco-IOS-XR-crypto-sam-oper:index = ' + str(self.index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.detail is not None and self.detail._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                            return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-indexes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.certificate_index is not None:
                            for child_ref in self.certificate_index:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.Devices.Device.Certificate.CertificateIndexes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.brief is not None and self.brief._has_data():
                        return True

                    if self.certificate_indexes is not None and self.certificate_indexes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.Devices.Device.Certificate']['meta_info']

            @property
            def _common_path(self):
                if self.device_name is None:
                    raise YPYModelError('Key property device_name is None')

                return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:devices/Cisco-IOS-XR-crypto-sam-oper:device[Cisco-IOS-XR-crypto-sam-oper:device-name = ' + str(self.device_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.device_name is not None:
                    return True

                if self.certificate is not None and self.certificate._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.Devices.Device']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:devices'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.device is not None:
                for child_ref in self.device:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.Devices']['meta_info']


    class Packages(object):
        """
        SAM certificate information  package
        
        .. attribute:: package
        
        	SAM certificate information for a specific package
        	**type**\: list of    :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_oper.Sam.Packages.Package>`
        
        

        """

        _prefix = 'crypto-sam-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.package = YList()
            self.package.parent = self
            self.package.name = 'package'


        class Package(object):
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
                self.parent = None
                self.package_name = None
                self.certificate_flags = Sam.Packages.Package.CertificateFlags()
                self.certificate_flags.parent = self
                self.certificate_index = None
                self.location = None


            class CertificateFlags(object):
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
                    self.parent = None
                    self.is_expired = None
                    self.is_revoked = None
                    self.is_trusted = None
                    self.is_validated = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-flags'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.is_expired is not None:
                        return True

                    if self.is_revoked is not None:
                        return True

                    if self.is_trusted is not None:
                        return True

                    if self.is_validated is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.Packages.Package.CertificateFlags']['meta_info']

            @property
            def _common_path(self):
                if self.package_name is None:
                    raise YPYModelError('Key property package_name is None')

                return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:packages/Cisco-IOS-XR-crypto-sam-oper:package[Cisco-IOS-XR-crypto-sam-oper:package-name = ' + str(self.package_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.package_name is not None:
                    return True

                if self.certificate_flags is not None and self.certificate_flags._has_data():
                    return True

                if self.certificate_index is not None:
                    return True

                if self.location is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.Packages.Package']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:packages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.package is not None:
                for child_ref in self.package:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.Packages']['meta_info']


    class CertificateRevocations(object):
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
            self.parent = None
            self.certificate_revocation = YList()
            self.certificate_revocation.parent = self
            self.certificate_revocation.name = 'certificate_revocation'


        class CertificateRevocation(object):
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
                self.parent = None
                self.crl_index = None
                self.certificate_revocation_list_detail = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail()
                self.certificate_revocation_list_detail.parent = self


            class CertificateRevocationListDetail(object):
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
                    self.parent = None
                    self.crl_index = None
                    self.issuer = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer()
                    self.issuer.parent = self
                    self.updates = None


                class Issuer(object):
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
                        self.parent = None
                        self.common_name = None
                        self.country = None
                        self.organization = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:issuer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.common_name is not None:
                            return True

                        if self.country is not None:
                            return True

                        if self.organization is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                        return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-crypto-sam-oper:certificate-revocation-list-detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.crl_index is not None:
                        return True

                    if self.issuer is not None and self.issuer._has_data():
                        return True

                    if self.updates is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                    return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail']['meta_info']

            @property
            def _common_path(self):
                if self.crl_index is None:
                    raise YPYModelError('Key property crl_index is None')

                return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:certificate-revocations/Cisco-IOS-XR-crypto-sam-oper:certificate-revocation[Cisco-IOS-XR-crypto-sam-oper:crl-index = ' + str(self.crl_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.crl_index is not None:
                    return True

                if self.certificate_revocation_list_detail is not None and self.certificate_revocation_list_detail._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.CertificateRevocations.CertificateRevocation']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:certificate-revocations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.certificate_revocation is not None:
                for child_ref in self.certificate_revocation:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.CertificateRevocations']['meta_info']


    class CertificateRevocationListSummary(object):
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
            self.parent = None
            self.crl_index = None
            self.issuer = Sam.CertificateRevocationListSummary.Issuer()
            self.issuer.parent = self
            self.updates = None


        class Issuer(object):
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
                self.parent = None
                self.common_name = None
                self.country = None
                self.organization = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:certificate-revocation-list-summary/Cisco-IOS-XR-crypto-sam-oper:issuer'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.common_name is not None:
                    return True

                if self.country is not None:
                    return True

                if self.organization is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
                return meta._meta_table['Sam.CertificateRevocationListSummary.Issuer']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-sam-oper:sam/Cisco-IOS-XR-crypto-sam-oper:certificate-revocation-list-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.crl_index is not None:
                return True

            if self.issuer is not None and self.issuer._has_data():
                return True

            if self.updates is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
            return meta._meta_table['Sam.CertificateRevocationListSummary']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-sam-oper:sam'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.certificate_revocation_list_summary is not None and self.certificate_revocation_list_summary._has_data():
            return True

        if self.certificate_revocations is not None and self.certificate_revocations._has_data():
            return True

        if self.devices is not None and self.devices._has_data():
            return True

        if self.log_contents is not None and self.log_contents._has_data():
            return True

        if self.packages is not None and self.packages._has_data():
            return True

        if self.system_information is not None and self.system_information._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_crypto_sam_oper as meta
        return meta._meta_table['Sam']['meta_info']


