""" Cisco_IOS_XR_crypto_sam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-sam package operational data.

This module contains definitions
for the following management objects\:
  sam\: Software authentication manager certificate information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.is_default_response = YLeaf(YType.boolean, "is-default-response")

            self.is_running = YLeaf(YType.boolean, "is-running")

            self.prompt_interval = YLeaf(YType.uint32, "prompt-interval")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("is_default_response",
                            "is_running",
                            "prompt_interval") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.SystemInformation, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.SystemInformation, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.is_default_response.is_set or
                self.is_running.is_set or
                self.prompt_interval.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.is_default_response.yfilter != YFilter.not_set or
                self.is_running.yfilter != YFilter.not_set or
                self.prompt_interval.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "system-information" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.is_default_response.is_set or self.is_default_response.yfilter != YFilter.not_set):
                leaf_name_data.append(self.is_default_response.get_name_leafdata())
            if (self.is_running.is_set or self.is_running.yfilter != YFilter.not_set):
                leaf_name_data.append(self.is_running.get_name_leafdata())
            if (self.prompt_interval.is_set or self.prompt_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prompt_interval.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "is-default-response" or name == "is-running" or name == "prompt-interval"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "is-default-response"):
                self.is_default_response = value
                self.is_default_response.value_namespace = name_space
                self.is_default_response.value_namespace_prefix = name_space_prefix
            if(value_path == "is-running"):
                self.is_running = value
                self.is_running.value_namespace = name_space
                self.is_running.value_namespace_prefix = name_space_prefix
            if(value_path == "prompt-interval"):
                self.prompt_interval = value
                self.prompt_interval.value_namespace = name_space
                self.prompt_interval.value_namespace_prefix = name_space_prefix


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

            self.log_content = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.LogContents, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.LogContents, self).__setattr__(name, value)


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

                self.number_of_lines = YLeaf(YType.int32, "number-of-lines")

                self.entries_shown = YLeaf(YType.uint32, "entries-shown")

                self.total_entries = YLeaf(YType.uint32, "total-entries")

                self.logs = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("number_of_lines",
                                "entries_shown",
                                "total_entries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sam.LogContents.LogContent, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sam.LogContents.LogContent, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("code",
                                    "error",
                                    "index",
                                    "issuer",
                                    "sam_table_index",
                                    "serial_no",
                                    "source_device",
                                    "table",
                                    "target_device",
                                    "time",
                                    "update_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sam.LogContents.LogContent.Logs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sam.LogContents.LogContent.Logs, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.code.is_set or
                        self.error.is_set or
                        self.index.is_set or
                        self.issuer.is_set or
                        self.sam_table_index.is_set or
                        self.serial_no.is_set or
                        self.source_device.is_set or
                        self.table.is_set or
                        self.target_device.is_set or
                        self.time.is_set or
                        self.update_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.code.yfilter != YFilter.not_set or
                        self.error.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.issuer.yfilter != YFilter.not_set or
                        self.sam_table_index.yfilter != YFilter.not_set or
                        self.serial_no.yfilter != YFilter.not_set or
                        self.source_device.yfilter != YFilter.not_set or
                        self.table.yfilter != YFilter.not_set or
                        self.target_device.yfilter != YFilter.not_set or
                        self.time.yfilter != YFilter.not_set or
                        self.update_time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "logs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.code.get_name_leafdata())
                    if (self.error.is_set or self.error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.error.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.issuer.is_set or self.issuer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.issuer.get_name_leafdata())
                    if (self.sam_table_index.is_set or self.sam_table_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sam_table_index.get_name_leafdata())
                    if (self.serial_no.is_set or self.serial_no.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.serial_no.get_name_leafdata())
                    if (self.source_device.is_set or self.source_device.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_device.get_name_leafdata())
                    if (self.table.is_set or self.table.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.table.get_name_leafdata())
                    if (self.target_device.is_set or self.target_device.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.target_device.get_name_leafdata())
                    if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time.get_name_leafdata())
                    if (self.update_time.is_set or self.update_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.update_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "code" or name == "error" or name == "index" or name == "issuer" or name == "sam-table-index" or name == "serial-no" or name == "source-device" or name == "table" or name == "target-device" or name == "time" or name == "update-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "code"):
                        self.code = value
                        self.code.value_namespace = name_space
                        self.code.value_namespace_prefix = name_space_prefix
                    if(value_path == "error"):
                        self.error = value
                        self.error.value_namespace = name_space
                        self.error.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "issuer"):
                        self.issuer = value
                        self.issuer.value_namespace = name_space
                        self.issuer.value_namespace_prefix = name_space_prefix
                    if(value_path == "sam-table-index"):
                        self.sam_table_index = value
                        self.sam_table_index.value_namespace = name_space
                        self.sam_table_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "serial-no"):
                        self.serial_no = value
                        self.serial_no.value_namespace = name_space
                        self.serial_no.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-device"):
                        self.source_device = value
                        self.source_device.value_namespace = name_space
                        self.source_device.value_namespace_prefix = name_space_prefix
                    if(value_path == "table"):
                        self.table = value
                        self.table.value_namespace = name_space
                        self.table.value_namespace_prefix = name_space_prefix
                    if(value_path == "target-device"):
                        self.target_device = value
                        self.target_device.value_namespace = name_space
                        self.target_device.value_namespace_prefix = name_space_prefix
                    if(value_path == "time"):
                        self.time = value
                        self.time.value_namespace = name_space
                        self.time.value_namespace_prefix = name_space_prefix
                    if(value_path == "update-time"):
                        self.update_time = value
                        self.update_time.value_namespace = name_space
                        self.update_time.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.logs:
                    if (c.has_data()):
                        return True
                return (
                    self.number_of_lines.is_set or
                    self.entries_shown.is_set or
                    self.total_entries.is_set)

            def has_operation(self):
                for c in self.logs:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.number_of_lines.yfilter != YFilter.not_set or
                    self.entries_shown.yfilter != YFilter.not_set or
                    self.total_entries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "log-content" + "[number-of-lines='" + self.number_of_lines.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/log-contents/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.number_of_lines.is_set or self.number_of_lines.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_lines.get_name_leafdata())
                if (self.entries_shown.is_set or self.entries_shown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entries_shown.get_name_leafdata())
                if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_entries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "logs"):
                    for c in self.logs:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sam.LogContents.LogContent.Logs()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.logs.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "logs" or name == "number-of-lines" or name == "entries-shown" or name == "total-entries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "number-of-lines"):
                    self.number_of_lines = value
                    self.number_of_lines.value_namespace = name_space
                    self.number_of_lines.value_namespace_prefix = name_space_prefix
                if(value_path == "entries-shown"):
                    self.entries_shown = value
                    self.entries_shown.value_namespace = name_space
                    self.entries_shown.value_namespace_prefix = name_space_prefix
                if(value_path == "total-entries"):
                    self.total_entries = value
                    self.total_entries.value_namespace = name_space
                    self.total_entries.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.log_content:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.log_content:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "log-contents" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "log-content"):
                for c in self.log_content:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Sam.LogContents.LogContent()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.log_content.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "log-content"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.device = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.Devices, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.Devices, self).__setattr__(name, value)


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

                self.device_name = YLeaf(YType.str, "device-name")

                self.certificate = Sam.Devices.Device.Certificate()
                self.certificate.parent = self
                self._children_name_map["certificate"] = "certificate"
                self._children_yang_names.add("certificate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("device_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sam.Devices.Device, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sam.Devices.Device, self).__setattr__(name, value)


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

                    self.brief = Sam.Devices.Device.Certificate.Brief()
                    self.brief.parent = self
                    self._children_name_map["brief"] = "brief"
                    self._children_yang_names.add("brief")

                    self.certificate_indexes = Sam.Devices.Device.Certificate.CertificateIndexes()
                    self.certificate_indexes.parent = self
                    self._children_name_map["certificate_indexes"] = "certificate-indexes"
                    self._children_yang_names.add("certificate-indexes")


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

                        self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                        self.location = YLeaf(YType.str, "location")

                        self.certificate_flags = Sam.Devices.Device.Certificate.Brief.CertificateFlags()
                        self.certificate_flags.parent = self
                        self._children_name_map["certificate_flags"] = "certificate-flags"
                        self._children_yang_names.add("certificate-flags")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("certificate_index",
                                        "location") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sam.Devices.Device.Certificate.Brief, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sam.Devices.Device.Certificate.Brief, self).__setattr__(name, value)


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

                            self.is_expired = YLeaf(YType.boolean, "is-expired")

                            self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                            self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                            self.is_validated = YLeaf(YType.boolean, "is-validated")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_expired",
                                            "is_revoked",
                                            "is_trusted",
                                            "is_validated") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sam.Devices.Device.Certificate.Brief.CertificateFlags, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sam.Devices.Device.Certificate.Brief.CertificateFlags, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.is_expired.is_set or
                                self.is_revoked.is_set or
                                self.is_trusted.is_set or
                                self.is_validated.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_expired.yfilter != YFilter.not_set or
                                self.is_revoked.yfilter != YFilter.not_set or
                                self.is_trusted.yfilter != YFilter.not_set or
                                self.is_validated.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "certificate-flags" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_expired.is_set or self.is_expired.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_expired.get_name_leafdata())
                            if (self.is_revoked.is_set or self.is_revoked.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_revoked.get_name_leafdata())
                            if (self.is_trusted.is_set or self.is_trusted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_trusted.get_name_leafdata())
                            if (self.is_validated.is_set or self.is_validated.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_validated.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "is-expired" or name == "is-revoked" or name == "is-trusted" or name == "is-validated"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-expired"):
                                self.is_expired = value
                                self.is_expired.value_namespace = name_space
                                self.is_expired.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-revoked"):
                                self.is_revoked = value
                                self.is_revoked.value_namespace = name_space
                                self.is_revoked.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-trusted"):
                                self.is_trusted = value
                                self.is_trusted.value_namespace = name_space
                                self.is_trusted.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-validated"):
                                self.is_validated = value
                                self.is_validated.value_namespace = name_space
                                self.is_validated.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.certificate_index.is_set or
                            self.location.is_set or
                            (self.certificate_flags is not None and self.certificate_flags.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.certificate_index.yfilter != YFilter.not_set or
                            self.location.yfilter != YFilter.not_set or
                            (self.certificate_flags is not None and self.certificate_flags.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "brief" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.certificate_index.is_set or self.certificate_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.certificate_index.get_name_leafdata())
                        if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.location.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "certificate-flags"):
                            if (self.certificate_flags is None):
                                self.certificate_flags = Sam.Devices.Device.Certificate.Brief.CertificateFlags()
                                self.certificate_flags.parent = self
                                self._children_name_map["certificate_flags"] = "certificate-flags"
                            return self.certificate_flags

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "certificate-flags" or name == "certificate-index" or name == "location"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "certificate-index"):
                            self.certificate_index = value
                            self.certificate_index.value_namespace = name_space
                            self.certificate_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "location"):
                            self.location = value
                            self.location.value_namespace = name_space
                            self.location.value_namespace_prefix = name_space_prefix


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

                        self.certificate_index = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sam.Devices.Device.Certificate.CertificateIndexes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sam.Devices.Device.Certificate.CertificateIndexes, self).__setattr__(name, value)


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

                            self.index = YLeaf(YType.int32, "index")

                            self.detail = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail()
                            self.detail.parent = self
                            self._children_name_map["detail"] = "detail"
                            self._children_yang_names.add("detail")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex, self).__setattr__(name, value)


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

                                self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                                self.location = YLeaf(YType.str, "location")

                                self.certificate_flags = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags()
                                self.certificate_flags.parent = self
                                self._children_name_map["certificate_flags"] = "certificate-flags"
                                self._children_yang_names.add("certificate-flags")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("certificate_index",
                                                "location") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail, self).__setattr__(name, value)


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

                                    self.is_expired = YLeaf(YType.boolean, "is-expired")

                                    self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                                    self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                                    self.is_validated = YLeaf(YType.boolean, "is-validated")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("is_expired",
                                                    "is_revoked",
                                                    "is_trusted",
                                                    "is_validated") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.is_expired.is_set or
                                        self.is_revoked.is_set or
                                        self.is_trusted.is_set or
                                        self.is_validated.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.is_expired.yfilter != YFilter.not_set or
                                        self.is_revoked.yfilter != YFilter.not_set or
                                        self.is_trusted.yfilter != YFilter.not_set or
                                        self.is_validated.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "certificate-flags" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.is_expired.is_set or self.is_expired.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_expired.get_name_leafdata())
                                    if (self.is_revoked.is_set or self.is_revoked.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_revoked.get_name_leafdata())
                                    if (self.is_trusted.is_set or self.is_trusted.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_trusted.get_name_leafdata())
                                    if (self.is_validated.is_set or self.is_validated.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_validated.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "is-expired" or name == "is-revoked" or name == "is-trusted" or name == "is-validated"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "is-expired"):
                                        self.is_expired = value
                                        self.is_expired.value_namespace = name_space
                                        self.is_expired.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-revoked"):
                                        self.is_revoked = value
                                        self.is_revoked.value_namespace = name_space
                                        self.is_revoked.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-trusted"):
                                        self.is_trusted = value
                                        self.is_trusted.value_namespace = name_space
                                        self.is_trusted.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-validated"):
                                        self.is_validated = value
                                        self.is_validated.value_namespace = name_space
                                        self.is_validated.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.certificate_index.is_set or
                                    self.location.is_set or
                                    (self.certificate_flags is not None and self.certificate_flags.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.certificate_index.yfilter != YFilter.not_set or
                                    self.location.yfilter != YFilter.not_set or
                                    (self.certificate_flags is not None and self.certificate_flags.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "detail" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.certificate_index.is_set or self.certificate_index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.certificate_index.get_name_leafdata())
                                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.location.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "certificate-flags"):
                                    if (self.certificate_flags is None):
                                        self.certificate_flags = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail.CertificateFlags()
                                        self.certificate_flags.parent = self
                                        self._children_name_map["certificate_flags"] = "certificate-flags"
                                    return self.certificate_flags

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "certificate-flags" or name == "certificate-index" or name == "location"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "certificate-index"):
                                    self.certificate_index = value
                                    self.certificate_index.value_namespace = name_space
                                    self.certificate_index.value_namespace_prefix = name_space_prefix
                                if(value_path == "location"):
                                    self.location = value
                                    self.location.value_namespace = name_space
                                    self.location.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.index.is_set or
                                (self.detail is not None and self.detail.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                (self.detail is not None and self.detail.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "certificate-index" + "[index='" + self.index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "detail"):
                                if (self.detail is None):
                                    self.detail = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex.Detail()
                                    self.detail.parent = self
                                    self._children_name_map["detail"] = "detail"
                                return self.detail

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "detail" or name == "index"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.certificate_index:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.certificate_index:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "certificate-indexes" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "certificate-index"):
                            for c in self.certificate_index:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Sam.Devices.Device.Certificate.CertificateIndexes.CertificateIndex()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.certificate_index.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "certificate-index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.brief is not None and self.brief.has_data()) or
                        (self.certificate_indexes is not None and self.certificate_indexes.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.brief is not None and self.brief.has_operation()) or
                        (self.certificate_indexes is not None and self.certificate_indexes.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "certificate" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "brief"):
                        if (self.brief is None):
                            self.brief = Sam.Devices.Device.Certificate.Brief()
                            self.brief.parent = self
                            self._children_name_map["brief"] = "brief"
                        return self.brief

                    if (child_yang_name == "certificate-indexes"):
                        if (self.certificate_indexes is None):
                            self.certificate_indexes = Sam.Devices.Device.Certificate.CertificateIndexes()
                            self.certificate_indexes.parent = self
                            self._children_name_map["certificate_indexes"] = "certificate-indexes"
                        return self.certificate_indexes

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "brief" or name == "certificate-indexes"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.device_name.is_set or
                    (self.certificate is not None and self.certificate.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.device_name.yfilter != YFilter.not_set or
                    (self.certificate is not None and self.certificate.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "device" + "[device-name='" + self.device_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/devices/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.device_name.is_set or self.device_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.device_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "certificate"):
                    if (self.certificate is None):
                        self.certificate = Sam.Devices.Device.Certificate()
                        self.certificate.parent = self
                        self._children_name_map["certificate"] = "certificate"
                    return self.certificate

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "certificate" or name == "device-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "device-name"):
                    self.device_name = value
                    self.device_name.value_namespace = name_space
                    self.device_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.device:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.device:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "devices" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "device"):
                for c in self.device:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Sam.Devices.Device()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.device.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "device"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.package = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.Packages, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.Packages, self).__setattr__(name, value)


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

                self.package_name = YLeaf(YType.str, "package-name")

                self.certificate_index = YLeaf(YType.uint16, "certificate-index")

                self.location = YLeaf(YType.str, "location")

                self.certificate_flags = Sam.Packages.Package.CertificateFlags()
                self.certificate_flags.parent = self
                self._children_name_map["certificate_flags"] = "certificate-flags"
                self._children_yang_names.add("certificate-flags")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("package_name",
                                "certificate_index",
                                "location") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sam.Packages.Package, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sam.Packages.Package, self).__setattr__(name, value)


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

                    self.is_expired = YLeaf(YType.boolean, "is-expired")

                    self.is_revoked = YLeaf(YType.boolean, "is-revoked")

                    self.is_trusted = YLeaf(YType.boolean, "is-trusted")

                    self.is_validated = YLeaf(YType.boolean, "is-validated")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_expired",
                                    "is_revoked",
                                    "is_trusted",
                                    "is_validated") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sam.Packages.Package.CertificateFlags, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sam.Packages.Package.CertificateFlags, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.is_expired.is_set or
                        self.is_revoked.is_set or
                        self.is_trusted.is_set or
                        self.is_validated.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_expired.yfilter != YFilter.not_set or
                        self.is_revoked.yfilter != YFilter.not_set or
                        self.is_trusted.yfilter != YFilter.not_set or
                        self.is_validated.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "certificate-flags" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_expired.is_set or self.is_expired.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_expired.get_name_leafdata())
                    if (self.is_revoked.is_set or self.is_revoked.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_revoked.get_name_leafdata())
                    if (self.is_trusted.is_set or self.is_trusted.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_trusted.get_name_leafdata())
                    if (self.is_validated.is_set or self.is_validated.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_validated.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "is-expired" or name == "is-revoked" or name == "is-trusted" or name == "is-validated"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-expired"):
                        self.is_expired = value
                        self.is_expired.value_namespace = name_space
                        self.is_expired.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-revoked"):
                        self.is_revoked = value
                        self.is_revoked.value_namespace = name_space
                        self.is_revoked.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-trusted"):
                        self.is_trusted = value
                        self.is_trusted.value_namespace = name_space
                        self.is_trusted.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-validated"):
                        self.is_validated = value
                        self.is_validated.value_namespace = name_space
                        self.is_validated.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.package_name.is_set or
                    self.certificate_index.is_set or
                    self.location.is_set or
                    (self.certificate_flags is not None and self.certificate_flags.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.package_name.yfilter != YFilter.not_set or
                    self.certificate_index.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    (self.certificate_flags is not None and self.certificate_flags.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "package" + "[package-name='" + self.package_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/packages/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.package_name.is_set or self.package_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.package_name.get_name_leafdata())
                if (self.certificate_index.is_set or self.certificate_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.certificate_index.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "certificate-flags"):
                    if (self.certificate_flags is None):
                        self.certificate_flags = Sam.Packages.Package.CertificateFlags()
                        self.certificate_flags.parent = self
                        self._children_name_map["certificate_flags"] = "certificate-flags"
                    return self.certificate_flags

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "certificate-flags" or name == "package-name" or name == "certificate-index" or name == "location"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "package-name"):
                    self.package_name = value
                    self.package_name.value_namespace = name_space
                    self.package_name.value_namespace_prefix = name_space_prefix
                if(value_path == "certificate-index"):
                    self.certificate_index = value
                    self.certificate_index.value_namespace = name_space
                    self.certificate_index.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.package:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.package:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "packages" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "package"):
                for c in self.package:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Sam.Packages.Package()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.package.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "package"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.certificate_revocation = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.CertificateRevocations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.CertificateRevocations, self).__setattr__(name, value)


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

                self.crl_index = YLeaf(YType.int32, "crl-index")

                self.certificate_revocation_list_detail = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail()
                self.certificate_revocation_list_detail.parent = self
                self._children_name_map["certificate_revocation_list_detail"] = "certificate-revocation-list-detail"
                self._children_yang_names.add("certificate-revocation-list-detail")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("crl_index") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sam.CertificateRevocations.CertificateRevocation, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sam.CertificateRevocations.CertificateRevocation, self).__setattr__(name, value)


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

                    self.crl_index = YLeaf(YType.uint16, "crl-index")

                    self.updates = YLeaf(YType.str, "updates")

                    self.issuer = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer()
                    self.issuer.parent = self
                    self._children_name_map["issuer"] = "issuer"
                    self._children_yang_names.add("issuer")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("crl_index",
                                    "updates") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail, self).__setattr__(name, value)


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

                        self.common_name = YLeaf(YType.str, "common-name")

                        self.country = YLeaf(YType.str, "country")

                        self.organization = YLeaf(YType.str, "organization")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("common_name",
                                        "country",
                                        "organization") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.common_name.is_set or
                            self.country.is_set or
                            self.organization.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.common_name.yfilter != YFilter.not_set or
                            self.country.yfilter != YFilter.not_set or
                            self.organization.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "issuer" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.common_name.is_set or self.common_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.common_name.get_name_leafdata())
                        if (self.country.is_set or self.country.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.country.get_name_leafdata())
                        if (self.organization.is_set or self.organization.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.organization.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "common-name" or name == "country" or name == "organization"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "common-name"):
                            self.common_name = value
                            self.common_name.value_namespace = name_space
                            self.common_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "country"):
                            self.country = value
                            self.country.value_namespace = name_space
                            self.country.value_namespace_prefix = name_space_prefix
                        if(value_path == "organization"):
                            self.organization = value
                            self.organization.value_namespace = name_space
                            self.organization.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.crl_index.is_set or
                        self.updates.is_set or
                        (self.issuer is not None and self.issuer.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.crl_index.yfilter != YFilter.not_set or
                        self.updates.yfilter != YFilter.not_set or
                        (self.issuer is not None and self.issuer.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "certificate-revocation-list-detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.crl_index.is_set or self.crl_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.crl_index.get_name_leafdata())
                    if (self.updates.is_set or self.updates.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.updates.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "issuer"):
                        if (self.issuer is None):
                            self.issuer = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail.Issuer()
                            self.issuer.parent = self
                            self._children_name_map["issuer"] = "issuer"
                        return self.issuer

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "issuer" or name == "crl-index" or name == "updates"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "crl-index"):
                        self.crl_index = value
                        self.crl_index.value_namespace = name_space
                        self.crl_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "updates"):
                        self.updates = value
                        self.updates.value_namespace = name_space
                        self.updates.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.crl_index.is_set or
                    (self.certificate_revocation_list_detail is not None and self.certificate_revocation_list_detail.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.crl_index.yfilter != YFilter.not_set or
                    (self.certificate_revocation_list_detail is not None and self.certificate_revocation_list_detail.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "certificate-revocation" + "[crl-index='" + self.crl_index.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.crl_index.is_set or self.crl_index.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.crl_index.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "certificate-revocation-list-detail"):
                    if (self.certificate_revocation_list_detail is None):
                        self.certificate_revocation_list_detail = Sam.CertificateRevocations.CertificateRevocation.CertificateRevocationListDetail()
                        self.certificate_revocation_list_detail.parent = self
                        self._children_name_map["certificate_revocation_list_detail"] = "certificate-revocation-list-detail"
                    return self.certificate_revocation_list_detail

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "certificate-revocation-list-detail" or name == "crl-index"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "crl-index"):
                    self.crl_index = value
                    self.crl_index.value_namespace = name_space
                    self.crl_index.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.certificate_revocation:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.certificate_revocation:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "certificate-revocations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "certificate-revocation"):
                for c in self.certificate_revocation:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Sam.CertificateRevocations.CertificateRevocation()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.certificate_revocation.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "certificate-revocation"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.crl_index = YLeaf(YType.uint16, "crl-index")

            self.updates = YLeaf(YType.str, "updates")

            self.issuer = Sam.CertificateRevocationListSummary.Issuer()
            self.issuer.parent = self
            self._children_name_map["issuer"] = "issuer"
            self._children_yang_names.add("issuer")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("crl_index",
                            "updates") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Sam.CertificateRevocationListSummary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Sam.CertificateRevocationListSummary, self).__setattr__(name, value)


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

                self.common_name = YLeaf(YType.str, "common-name")

                self.country = YLeaf(YType.str, "country")

                self.organization = YLeaf(YType.str, "organization")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("common_name",
                                "country",
                                "organization") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Sam.CertificateRevocationListSummary.Issuer, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sam.CertificateRevocationListSummary.Issuer, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.common_name.is_set or
                    self.country.is_set or
                    self.organization.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.common_name.yfilter != YFilter.not_set or
                    self.country.yfilter != YFilter.not_set or
                    self.organization.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "issuer" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/certificate-revocation-list-summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.common_name.is_set or self.common_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.common_name.get_name_leafdata())
                if (self.country.is_set or self.country.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.country.get_name_leafdata())
                if (self.organization.is_set or self.organization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.organization.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "common-name" or name == "country" or name == "organization"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "common-name"):
                    self.common_name = value
                    self.common_name.value_namespace = name_space
                    self.common_name.value_namespace_prefix = name_space_prefix
                if(value_path == "country"):
                    self.country = value
                    self.country.value_namespace = name_space
                    self.country.value_namespace_prefix = name_space_prefix
                if(value_path == "organization"):
                    self.organization = value
                    self.organization.value_namespace = name_space
                    self.organization.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.crl_index.is_set or
                self.updates.is_set or
                (self.issuer is not None and self.issuer.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.crl_index.yfilter != YFilter.not_set or
                self.updates.yfilter != YFilter.not_set or
                (self.issuer is not None and self.issuer.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "certificate-revocation-list-summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.crl_index.is_set or self.crl_index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.crl_index.get_name_leafdata())
            if (self.updates.is_set or self.updates.yfilter != YFilter.not_set):
                leaf_name_data.append(self.updates.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "issuer"):
                if (self.issuer is None):
                    self.issuer = Sam.CertificateRevocationListSummary.Issuer()
                    self.issuer.parent = self
                    self._children_name_map["issuer"] = "issuer"
                return self.issuer

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "issuer" or name == "crl-index" or name == "updates"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "crl-index"):
                self.crl_index = value
                self.crl_index.value_namespace = name_space
                self.crl_index.value_namespace_prefix = name_space_prefix
            if(value_path == "updates"):
                self.updates = value
                self.updates.value_namespace = name_space
                self.updates.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.certificate_revocation_list_summary is not None and self.certificate_revocation_list_summary.has_data()) or
            (self.certificate_revocations is not None and self.certificate_revocations.has_data()) or
            (self.devices is not None and self.devices.has_data()) or
            (self.log_contents is not None and self.log_contents.has_data()) or
            (self.packages is not None and self.packages.has_data()) or
            (self.system_information is not None and self.system_information.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.certificate_revocation_list_summary is not None and self.certificate_revocation_list_summary.has_operation()) or
            (self.certificate_revocations is not None and self.certificate_revocations.has_operation()) or
            (self.devices is not None and self.devices.has_operation()) or
            (self.log_contents is not None and self.log_contents.has_operation()) or
            (self.packages is not None and self.packages.has_operation()) or
            (self.system_information is not None and self.system_information.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-crypto-sam-oper:sam" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "certificate-revocation-list-summary"):
            if (self.certificate_revocation_list_summary is None):
                self.certificate_revocation_list_summary = Sam.CertificateRevocationListSummary()
                self.certificate_revocation_list_summary.parent = self
                self._children_name_map["certificate_revocation_list_summary"] = "certificate-revocation-list-summary"
            return self.certificate_revocation_list_summary

        if (child_yang_name == "certificate-revocations"):
            if (self.certificate_revocations is None):
                self.certificate_revocations = Sam.CertificateRevocations()
                self.certificate_revocations.parent = self
                self._children_name_map["certificate_revocations"] = "certificate-revocations"
            return self.certificate_revocations

        if (child_yang_name == "devices"):
            if (self.devices is None):
                self.devices = Sam.Devices()
                self.devices.parent = self
                self._children_name_map["devices"] = "devices"
            return self.devices

        if (child_yang_name == "log-contents"):
            if (self.log_contents is None):
                self.log_contents = Sam.LogContents()
                self.log_contents.parent = self
                self._children_name_map["log_contents"] = "log-contents"
            return self.log_contents

        if (child_yang_name == "packages"):
            if (self.packages is None):
                self.packages = Sam.Packages()
                self.packages.parent = self
                self._children_name_map["packages"] = "packages"
            return self.packages

        if (child_yang_name == "system-information"):
            if (self.system_information is None):
                self.system_information = Sam.SystemInformation()
                self.system_information.parent = self
                self._children_name_map["system_information"] = "system-information"
            return self.system_information

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "certificate-revocation-list-summary" or name == "certificate-revocations" or name == "devices" or name == "log-contents" or name == "packages" or name == "system-information"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Sam()
        return self._top_entity

