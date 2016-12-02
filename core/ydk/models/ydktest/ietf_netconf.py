""" ietf_netconf 

NETCONF Protocol Data Types and Protocol Operations.

Copyright (c) 2011 IETF Trust and the persons identified as
the document authors.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6241; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EditOperationTypeEnum(Enum):
    """
    EditOperationTypeEnum

    NETCONF 'operation' attribute values

    .. data:: merge = 0

    	The configuration data identified by the

    	element containing this attribute is merged

    	with the configuration at the corresponding

    	level in the configuration datastore identified

    	by the target parameter.

    .. data:: replace = 1

    	The configuration data identified by the element

    	containing this attribute replaces any related

    	configuration in the configuration datastore

    	identified by the target parameter.  If no such

    	configuration data exists in the configuration

    	datastore, it is created.  Unlike a

    	<copy-config> operation, which replaces the

    	entire target configuration, only the configuration

    	actually present in the config parameter is affected.

    .. data:: create = 2

    	The configuration data identified by the element

    	containing this attribute is added to the

    	configuration if and only if the configuration

    	data does not already exist in the configuration

    	datastore.  If the configuration data exists, an

    	<rpc-error> element is returned with an

    	<error-tag> value of 'data-exists'.

    .. data:: delete = 3

    	The configuration data identified by the element

    	containing this attribute is deleted from the

    	configuration if and only if the configuration

    	data currently exists in the configuration

    	datastore.  If the configuration data does not

    	exist, an <rpc-error> element is returned with

    	an <error-tag> value of 'data-missing'.

    .. data:: remove = 4

    	The configuration data identified by the element

    	containing this attribute is deleted from the

    	configuration if the configuration

    	data currently exists in the configuration

    	datastore.  If the configuration data does not

    	exist, the 'remove' operation is silently ignored

    	by the server.

    """

    merge = 0

    replace = 1

    create = 2

    delete = 3

    remove = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['EditOperationTypeEnum']


class ErrorSeverityTypeEnum(Enum):
    """
    ErrorSeverityTypeEnum

    NETCONF Error Severity

    .. data:: error = 0

    	Error severity

    .. data:: warning = 1

    	Warning severity

    """

    error = 0

    warning = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['ErrorSeverityTypeEnum']


class ErrorTagTypeEnum(Enum):
    """
    ErrorTagTypeEnum

    NETCONF Error Tag

    .. data:: in_use = 0

    	The request requires a resource that

    	already is in use.

    .. data:: invalid_value = 1

    	The request specifies an unacceptable value for one

    	or more parameters.

    .. data:: too_big = 2

    	The request or response (that would be generated) is

    	too large for the implementation to handle.

    .. data:: missing_attribute = 3

    	An expected attribute is missing.

    .. data:: bad_attribute = 4

    	An attribute value is not correct; e.g., wrong type,

    	out of range, pattern mismatch.

    .. data:: unknown_attribute = 5

    	An unexpected attribute is present.

    .. data:: missing_element = 6

    	An expected element is missing.

    .. data:: bad_element = 7

    	An element value is not correct; e.g., wrong type,

    	out of range, pattern mismatch.

    .. data:: unknown_element = 8

    	An unexpected element is present.

    .. data:: unknown_namespace = 9

    	An unexpected namespace is present.

    .. data:: access_denied = 10

    	Access to the requested protocol operation or

    	data model is denied because authorization failed.

    .. data:: lock_denied = 11

    	Access to the requested lock is denied because the

    	lock is currently held by another entity.

    .. data:: resource_denied = 12

    	Request could not be completed because of

    	insufficient resources.

    .. data:: rollback_failed = 13

    	Request to roll back some configuration change (via

    	rollback-on-error or <discard-changes> operations)

    	was not completed for some reason.

    .. data:: data_exists = 14

    	Request could not be completed because the relevant

    	data model content already exists.  For example,

    	a 'create' operation was attempted on data that

    	already exists.

    .. data:: data_missing = 15

    	Request could not be completed because the relevant

    	data model content does not exist.  For example,

    	a 'delete' operation was attempted on

    	data that does not exist.

    .. data:: operation_not_supported = 16

    	Request could not be completed because the requested

    	operation is not supported by this implementation.

    .. data:: operation_failed = 17

    	Request could not be completed because the requested

    	operation failed for some reason not covered by

    	any other error condition.

    .. data:: partial_operation = 18

    	This error-tag is obsolete, and SHOULD NOT be sent

    	by servers conforming to this document.

    .. data:: malformed_message = 19

    	A message could not be handled because it failed to

    	be parsed correctly.  For example, the message is not

    	well-formed XML or it uses an invalid character set.

    """

    in_use = 0

    invalid_value = 1

    too_big = 2

    missing_attribute = 3

    bad_attribute = 4

    unknown_attribute = 5

    missing_element = 6

    bad_element = 7

    unknown_element = 8

    unknown_namespace = 9

    access_denied = 10

    lock_denied = 11

    resource_denied = 12

    rollback_failed = 13

    data_exists = 14

    data_missing = 15

    operation_not_supported = 16

    operation_failed = 17

    partial_operation = 18

    malformed_message = 19


    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['ErrorTagTypeEnum']



class GetConfigRpc(object):
    """
    Retrieve all or part of a specified configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.GetConfigRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ydktest.ietf_netconf.GetConfigRpc.Output>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = GetConfigRpc.Input()
        self.input.parent = self
        self.output = GetConfigRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: filter
        
        	Subtree or XPath filter to use
        	**type**\:  anyxml
        
        .. attribute:: source
        
        	Particular configuration to retrieve
        	**type**\:   :py:class:`Source <ydk.models.ydktest.ietf_netconf.GetConfigRpc.Input.Source>`
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsModeEnum <ydk.models.ydktest.ietf_netconf_with_defaults.WithDefaultsModeEnum>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.filter = None
            self.source = GetConfigRpc.Input.Source()
            self.source.parent = self
            self.with_defaults = None


        class Source(object):
            """
            Particular configuration to retrieve.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source. This is optional\-to\-implement on the server because not all servers will support filtering for this datastore
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.running = None
                self.startup = None

            @property
            def _common_path(self):

                return '/ietf-netconf:get-config/ietf-netconf:input/ietf-netconf:source'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['GetConfigRpc.Input.Source']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:get-config/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.filter is not None:
                return True

            if self.source is not None and self.source._has_data():
                return True

            if self.with_defaults is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['GetConfigRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: data
        
        	Copy of the source datastore subset that matched the filter criteria (if any).  An empty data container indicates that the request did not produce any results
        	**type**\:  anyxml
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.data = None

        @property
        def _common_path(self):

            return '/ietf-netconf:get-config/ietf-netconf:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.data is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['GetConfigRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:get-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['GetConfigRpc']['meta_info']


class EditConfigRpc(object):
    """
    The <edit\-config> operation loads all or part of a specified
    configuration to the specified target configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.EditConfigRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = EditConfigRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: config
        
        	Inline Config content
        	**type**\:  anyxml
        
        .. attribute:: default_operation
        
        	The default operation to use
        	**type**\:   :py:class:`DefaultOperationEnum <ydk.models.ydktest.ietf_netconf.EditConfigRpc.Input.DefaultOperationEnum>`
        
        .. attribute:: error_option
        
        	The error option to use
        	**type**\:   :py:class:`ErrorOptionEnum <ydk.models.ydktest.ietf_netconf.EditConfigRpc.Input.ErrorOptionEnum>`
        
        .. attribute:: target
        
        	Particular configuration to edit
        	**type**\:   :py:class:`Target <ydk.models.ydktest.ietf_netconf.EditConfigRpc.Input.Target>`
        
        .. attribute:: test_option
        
        	The test option to use
        	**type**\:   :py:class:`TestOptionEnum <ydk.models.ydktest.ietf_netconf.EditConfigRpc.Input.TestOptionEnum>`
        
        .. attribute:: url
        
        	URL\-based config content
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.config = None
            self.default_operation = None
            self.error_option = None
            self.target = EditConfigRpc.Input.Target()
            self.target.parent = self
            self.test_option = None
            self.url = None

        class DefaultOperationEnum(Enum):
            """
            DefaultOperationEnum

            The default operation to use.

            .. data:: merge = 0

            	The default operation is merge.

            .. data:: replace = 1

            	The default operation is replace.

            .. data:: none = 2

            	There is no default operation.

            """

            merge = 0

            replace = 1

            none = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['EditConfigRpc.Input.DefaultOperationEnum']


        class ErrorOptionEnum(Enum):
            """
            ErrorOptionEnum

            The error option to use.

            .. data:: stop_on_error = 0

            	The server will stop on errors.

            .. data:: continue_on_error = 1

            	The server may continue on errors.

            .. data:: rollback_on_error = 2

            	The server will roll back on errors.

            	This value can only be used if the 'rollback-on-error'

            	feature is supported.

            """

            stop_on_error = 0

            continue_on_error = 1

            rollback_on_error = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['EditConfigRpc.Input.ErrorOptionEnum']


        class TestOptionEnum(Enum):
            """
            TestOptionEnum

            The test option to use.

            .. data:: test_then_set = 0

            	The server will test and then set if no errors.

            .. data:: set = 1

            	The server will set without a test first.

            .. data:: test_only = 2

            	The server will only test and not set, even

            	if there are no errors.

            """

            test_then_set = 0

            set = 1

            test_only = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['EditConfigRpc.Input.TestOptionEnum']



        class Target(object):
            """
            Particular configuration to edit.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.running = None

            @property
            def _common_path(self):

                return '/ietf-netconf:edit-config/ietf-netconf:input/ietf-netconf:target'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.running is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['EditConfigRpc.Input.Target']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:edit-config/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.config is not None:
                return True

            if self.default_operation is not None:
                return True

            if self.error_option is not None:
                return True

            if self.target is not None and self.target._has_data():
                return True

            if self.test_option is not None:
                return True

            if self.url is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['EditConfigRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:edit-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['EditConfigRpc']['meta_info']


class CopyConfigRpc(object):
    """
    Create or replace an entire configuration datastore with the
    contents of another complete configuration datastore.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.CopyConfigRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = CopyConfigRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: source
        
        	Particular configuration to copy from
        	**type**\:   :py:class:`Source <ydk.models.ydktest.ietf_netconf.CopyConfigRpc.Input.Source>`
        
        .. attribute:: target
        
        	Particular configuration to copy to
        	**type**\:   :py:class:`Target <ydk.models.ydktest.ietf_netconf.CopyConfigRpc.Input.Target>`
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsModeEnum <ydk.models.ydktest.ietf_netconf_with_defaults.WithDefaultsModeEnum>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.source = CopyConfigRpc.Input.Source()
            self.source.parent = self
            self.target = CopyConfigRpc.Input.Target()
            self.target.parent = self
            self.with_defaults = None


        class Target(object):
            """
            Particular configuration to copy to.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target. This is optional\-to\-implement on the server
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config target
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.running = None
                self.startup = None
                self.url = None

            @property
            def _common_path(self):

                return '/ietf-netconf:copy-config/ietf-netconf:input/ietf-netconf:target'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                if self.url is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['CopyConfigRpc.Input.Target']['meta_info']


        class Source(object):
            """
            Particular configuration to copy from.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: config
            
            	Inline Config content\: <config> element.  Represents an entire configuration datastore, not a subset of the running datastore
            	**type**\:  anyxml
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config source
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.config = None
                self.running = None
                self.startup = None
                self.url = None

            @property
            def _common_path(self):

                return '/ietf-netconf:copy-config/ietf-netconf:input/ietf-netconf:source'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.config is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                if self.url is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['CopyConfigRpc.Input.Source']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:copy-config/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.source is not None and self.source._has_data():
                return True

            if self.target is not None and self.target._has_data():
                return True

            if self.with_defaults is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['CopyConfigRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:copy-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['CopyConfigRpc']['meta_info']


class DeleteConfigRpc(object):
    """
    Delete a configuration datastore.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.DeleteConfigRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = DeleteConfigRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to delete
        	**type**\:   :py:class:`Target <ydk.models.ydktest.ietf_netconf.DeleteConfigRpc.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.target = DeleteConfigRpc.Input.Target()
            self.target.parent = self


        class Target(object):
            """
            Particular configuration to delete.
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config target
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.startup = None
                self.url = None

            @property
            def _common_path(self):

                return '/ietf-netconf:delete-config/ietf-netconf:input/ietf-netconf:target'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.startup is not None:
                    return True

                if self.url is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['DeleteConfigRpc.Input.Target']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:delete-config/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.target is not None and self.target._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['DeleteConfigRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:delete-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['DeleteConfigRpc']['meta_info']


class LockRpc(object):
    """
    The lock operation allows the client to lock the configuration
    system of a device.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.LockRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = LockRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to lock
        	**type**\:   :py:class:`Target <ydk.models.ydktest.ietf_netconf.LockRpc.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.target = LockRpc.Input.Target()
            self.target.parent = self


        class Target(object):
            """
            Particular configuration to lock.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.running = None
                self.startup = None

            @property
            def _common_path(self):

                return '/ietf-netconf:lock/ietf-netconf:input/ietf-netconf:target'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['LockRpc.Input.Target']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:lock/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.target is not None and self.target._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['LockRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:lock'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['LockRpc']['meta_info']


class UnlockRpc(object):
    """
    The unlock operation is used to release a configuration lock,
    previously obtained with the 'lock' operation.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.UnlockRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = UnlockRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: target
        
        	Particular configuration to unlock
        	**type**\:   :py:class:`Target <ydk.models.ydktest.ietf_netconf.UnlockRpc.Input.Target>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.target = UnlockRpc.Input.Target()
            self.target.parent = self


        class Target(object):
            """
            Particular configuration to unlock.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	The running configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config target
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.running = None
                self.startup = None

            @property
            def _common_path(self):

                return '/ietf-netconf:unlock/ietf-netconf:input/ietf-netconf:target'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['UnlockRpc.Input.Target']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:unlock/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.target is not None and self.target._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['UnlockRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:unlock'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['UnlockRpc']['meta_info']


class GetRpc(object):
    """
    Retrieve running configuration and device state information.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.GetRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ydktest.ietf_netconf.GetRpc.Output>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = GetRpc.Input()
        self.input.parent = self
        self.output = GetRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: filter
        
        	This parameter specifies the portion of the system configuration and state data to retrieve
        	**type**\:  anyxml
        
        .. attribute:: with_defaults
        
        	The explicit defaults processing mode requested
        	**type**\:   :py:class:`WithDefaultsModeEnum <ydk.models.ydktest.ietf_netconf_with_defaults.WithDefaultsModeEnum>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.filter = None
            self.with_defaults = None

        @property
        def _common_path(self):

            return '/ietf-netconf:get/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.filter is not None:
                return True

            if self.with_defaults is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['GetRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: data
        
        	Copy of the running datastore subset and/or state data that matched the filter criteria (if any). An empty data container indicates that the request did not produce any results
        	**type**\:  anyxml
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.data = None

        @property
        def _common_path(self):

            return '/ietf-netconf:get/ietf-netconf:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.data is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['GetRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:get'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['GetRpc']['meta_info']


class CloseSessionRpc(object):
    """
    Request graceful termination of a NETCONF session.
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/ietf-netconf:close-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['CloseSessionRpc']['meta_info']


class KillSessionRpc(object):
    """
    Force the termination of a NETCONF session.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.KillSessionRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = KillSessionRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: session_id
        
        	Particular session to kill
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.session_id = None

        @property
        def _common_path(self):

            return '/ietf-netconf:kill-session/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.session_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['KillSessionRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:kill-session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['KillSessionRpc']['meta_info']


class CommitRpc(object):
    """
    Commit the candidate configuration as the device's new
    current configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.CommitRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = CommitRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: confirm_timeout
        
        	The timeout interval for a confirmed commit
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        .. attribute:: confirmed
        
        	Requests a confirmed commit
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: persist
        
        	This parameter is used to make a confirmed commit persistent.  A persistent confirmed commit is not aborted if the NETCONF session terminates.  The only way to abort a persistent confirmed commit is to let the timer expire, or to use the <cancel\-commit> operation.  The value of this parameter is a token that must be given in the 'persist\-id' parameter of <commit> or <cancel\-commit> operations in order to confirm or cancel the persistent confirmed commit.  The token should be a random string
        	**type**\:  str
        
        .. attribute:: persist_id
        
        	This parameter is given in order to commit a persistent confirmed commit.  The value must be equal to the value given in the 'persist' parameter to the <commit> operation. If it does not match, the operation fails with an 'invalid\-value' error
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.confirm_timeout = None
            self.confirmed = None
            self.persist = None
            self.persist_id = None

        @property
        def _common_path(self):

            return '/ietf-netconf:commit/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.confirm_timeout is not None:
                return True

            if self.confirmed is not None:
                return True

            if self.persist is not None:
                return True

            if self.persist_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['CommitRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:commit'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['CommitRpc']['meta_info']


class DiscardChangesRpc(object):
    """
    Revert the candidate configuration to the current
    running configuration.
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):

        self.is_rpc = True

    @property
    def _common_path(self):

        return '/ietf-netconf:discard-changes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['DiscardChangesRpc']['meta_info']


class CancelCommitRpc(object):
    """
    This operation is used to cancel an ongoing confirmed commit.
    If the confirmed commit is persistent, the parameter
    'persist\-id' must be given, and it must match the value of the
    'persist' parameter.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.CancelCommitRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = CancelCommitRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: persist_id
        
        	This parameter is given in order to cancel a persistent confirmed commit.  The value must be equal to the value given in the 'persist' parameter to the <commit> operation. If it does not match, the operation fails with an 'invalid\-value' error
        	**type**\:  str
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.persist_id = None

        @property
        def _common_path(self):

            return '/ietf-netconf:cancel-commit/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.persist_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['CancelCommitRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:cancel-commit'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['CancelCommitRpc']['meta_info']


class ValidateRpc(object):
    """
    Validates the contents of the specified configuration.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ydktest.ietf_netconf.ValidateRpc.Input>`
    
    

    """

    _prefix = 'nc'
    _revision = '2011-06-01'

    def __init__(self):
        self.input = ValidateRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: source
        
        	Particular configuration to validate
        	**type**\:   :py:class:`Source <ydk.models.ydktest.ietf_netconf.ValidateRpc.Input.Source>`
        
        

        """

        _prefix = 'nc'
        _revision = '2011-06-01'

        def __init__(self):
            self.parent = None
            self.source = ValidateRpc.Input.Source()
            self.source.parent = self


        class Source(object):
            """
            Particular configuration to validate.
            
            .. attribute:: candidate
            
            	The candidate configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: config
            
            	Inline Config content\: <config> element.  Represents an entire configuration datastore, not a subset of the running datastore
            	**type**\:  anyxml
            
            .. attribute:: running
            
            	The running configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	The startup configuration is the config source
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: url
            
            	The URL\-based configuration is the config source
            	**type**\:  str
            
            

            """

            _prefix = 'nc'
            _revision = '2011-06-01'

            def __init__(self):
                self.parent = None
                self.candidate = None
                self.config = None
                self.running = None
                self.startup = None
                self.url = None

            @property
            def _common_path(self):

                return '/ietf-netconf:validate/ietf-netconf:input/ietf-netconf:source'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate is not None:
                    return True

                if self.config is not None:
                    return True

                if self.running is not None:
                    return True

                if self.startup is not None:
                    return True

                if self.url is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ydktest._meta import _ietf_netconf as meta
                return meta._meta_table['ValidateRpc.Input.Source']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf:validate/ietf-netconf:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.source is not None and self.source._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ydktest._meta import _ietf_netconf as meta
            return meta._meta_table['ValidateRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf:validate'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ydktest._meta import _ietf_netconf as meta
        return meta._meta_table['ValidateRpc']['meta_info']


